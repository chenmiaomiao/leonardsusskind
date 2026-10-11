#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
session="susskind-polished-translations"
python="${TRANSLATION_PYTHON:-/home/lachlan/miniconda3/bin/python}"
if tmux has-session -t "$session" 2>/dev/null; then
  printf 'Existing session: %s\n' "$session"
  exit 0
fi
mkdir -p "$root/.translation-work"
# tmux uses its server environment. Pass a private file path, never the key in argv.
if [[ -n "${DEEPSEEK_API_KEY:-}" && -z "${DEEPSEEK_API_KEY_FILE:-}" ]]; then
  export DEEPSEEK_API_KEY_FILE="$root/.translation-work/provider.key"
  "$python" -c 'import os; from pathlib import Path; p=Path(os.environ["DEEPSEEK_API_KEY_FILE"]); fd=os.open(p, os.O_WRONLY|os.O_CREAT|os.O_TRUNC, 0o600); os.fchmod(fd,0o600); os.write(fd,os.environ["DEEPSEEK_API_KEY"].encode()); os.close(fd)'
fi
tmux new-session -d -s "$session" -c "$root" 'sleep 3600'
if [[ -n "${DEEPSEEK_API_KEY_FILE:-}" ]]; then
  tmux set-environment -t "$session" DEEPSEEK_API_KEY ''
  tmux set-environment -t "$session" DEEPSEEK_API_KEY_FILE "$DEEPSEEK_API_KEY_FILE"
else
  tmux kill-session -t "$session"
  printf 'Set DEEPSEEK_API_KEY or DEEPSEEK_API_KEY_FILE first.\n' >&2
  exit 1
fi
printf -v command '%q scripts/polished_translation.py run --workers 5 ' "$python"
for arg in "$@"; do printf -v quoted '%q ' "$arg"; command+="$quoted"; done
command+='>>.translation-work/queue.log 2>&1'
tmux respawn-pane -k -t "$session":0 "$command"
printf 'Started %s; log: %s/.translation-work/queue.log\n' "$session" "$root"
