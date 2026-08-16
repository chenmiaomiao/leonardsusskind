#!/usr/bin/env python3
"""Publish merged 1.2x pocket books to the human-facing Nutstore share."""

from __future__ import annotations

import argparse
import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path


DEFAULT_TARGET_ROOT = Path("/home/lachlan/Nutstore Files/Share/Leonard Susskind")


@dataclass(frozen=True)
class Book:
    course: str
    category: str
    source_name: str
    display_name: str


BOOKS = (
    Book(
        "core/classical_mechanics/2011_fall_modern_physics_stanford_partial",
        "core",
        "classical_mechanics_stanford_partial_pocket_1_2x.pdf",
        "Classical Mechanics - Modern Physics Stanford (2011 Fall, Partial) - Pocket 1.2x.pdf",
    ),
    Book(
        "core/classical_mechanics/2011_fall_theoretical_minimum",
        "core",
        "classical_mechanics_theoretical_minimum_pocket_1_2x.pdf",
        "Classical Mechanics - The Theoretical Minimum (2011 Fall) - Pocket 1.2x.pdf",
    ),
    Book(
        "core/cosmology/2009_winter_legacy_cosmology",
        "core",
        "cosmology_legacy_pocket_1_2x.pdf",
        "Cosmology - Legacy Course (2009 Winter) - Pocket 1.2x.pdf",
    ),
    Book(
        "core/cosmology/2013_winter_theoretical_minimum",
        "core",
        "cosmology_theoretical_minimum_pocket_1_2x.pdf",
        "Cosmology - The Theoretical Minimum (2013 Winter) - Pocket 1.2x.pdf",
    ),
    Book(
        "core/general_relativity/2008_fall_einsteins_general_theory_of_relativity",
        "core",
        "general_relativity_2008_fall_einsteins_general_theory_of_relativity_pocket_1_2x.pdf",
        "Einstein's General Theory of Relativity (2008 Fall) - Pocket 1.2x.pdf",
    ),
    Book(
        "core/general_relativity/2012_fall_theoretical_minimum",
        "core",
        "general_relativity_theoretical_minimum_pocket_1_2x.pdf",
        "General Relativity - The Theoretical Minimum (2012 Fall) - Pocket 1.2x.pdf",
    ),
    Book(
        "core/quantum_mechanics/2012_winter_modern_physics_stanford",
        "core",
        "quantum_mechanics_2012_winter_modern_physics_stanford_pocket_1_2x.pdf",
        "Quantum Mechanics - Modern Physics Stanford (2012 Winter) - Pocket 1.2x.pdf",
    ),
    Book(
        "core/quantum_mechanics/2012_winter_theoretical_minimum_alt_title",
        "core",
        "quantum_mechanics_theoretical_minimum_pocket_1_2x.pdf",
        "Quantum Mechanics - The Theoretical Minimum (2012 Winter) - Pocket 1.2x.pdf",
    ),
    Book(
        "core/special_relativity/2012_spring_theoretical_minimum",
        "core",
        "special_relativity_theoretical_minimum_pocket_1_2x.pdf",
        "Special Relativity - The Theoretical Minimum (2012 Spring) - Pocket 1.2x.pdf",
    ),
    Book(
        "core/statistical_mechanics/2013_spring_theoretical_minimum",
        "core",
        "statistical_mechanics_theoretical_minimum_pocket_1_2x.pdf",
        "Statistical Mechanics - The Theoretical Minimum (2013 Spring) - Pocket 1.2x.pdf",
    ),
    Book(
        "supplementary/advanced_quantum_mechanics/2013_fall",
        "supplemental",
        "advanced_quantum_mechanics_pocket_1_2x.pdf",
        "Advanced Quantum Mechanics (2013 Fall) - Pocket 1.2x.pdf",
    ),
    Book(
        "supplementary/cosmology_and_black_holes/2011_winter_topics_in_string_theory",
        "supplemental",
        "topics_in_string_theory_pocket_1_2x.pdf",
        "Topics in String Theory (2011 Winter) - Pocket 1.2x.pdf",
    ),
    Book(
        "supplementary/higgs_boson/2012_summer",
        "supplemental",
        "demystifying_the_higgs_boson_pocket_1_2x.pdf",
        "Demystifying the Higgs Boson (2012 Summer) - Pocket 1.2x.pdf",
    ),
    Book(
        "supplementary/particle_physics_1_basic_concepts/2009_fall",
        "supplemental",
        "particle_physics_1_basic_concepts_pocket_1_2x.pdf",
        "Particle Physics 1 - Basic Concepts (2009 Fall) - Pocket 1.2x.pdf",
    ),
    Book(
        "supplementary/particle_physics_2_standard_model/2010_winter",
        "supplemental",
        "particle_physics_2_standard_model_pocket_1_2x.pdf",
        "Particle Physics 2 - The Standard Model (2010 Winter) - Pocket 1.2x.pdf",
    ),
    Book(
        "supplementary/particle_physics_3_supersymmetry_and_grand_unification/2010_spring",
        "supplemental",
        "particle_physics_3_supersymmetry_and_grand_unification_pocket_1_2x.pdf",
        "Particle Physics 3 - Supersymmetry and Grand Unification (2010 Spring) - Pocket 1.2x.pdf",
    ),
    Book(
        "supplementary/quantum_entanglement/2006_fall_part_1",
        "supplemental",
        "quantum_entanglement_part_1_pocket_1_2x.pdf",
        "Quantum Entanglement, Part 1 (2006 Fall) - Pocket 1.2x.pdf",
    ),
    Book(
        "supplementary/quantum_entanglement/2006_fall_part_3",
        "supplemental",
        "quantum_entanglement_part_3_pocket_1_2x.pdf",
        "Quantum Entanglement, Part 3 (2006 Fall) - Pocket 1.2x.pdf",
    ),
    Book(
        "supplementary/string_theory/2010_fall_string_theory_and_m_theory",
        "supplemental",
        "string_theory_and_m_theory_pocket_1_2x.pdf",
        "String Theory and M-Theory (2010 Fall) - Pocket 1.2x.pdf",
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync merged 1.2x pocket books to flat, human-named Nutstore folders."
    )
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--target-root", type=Path, default=DEFAULT_TARGET_ROOT)
    parser.add_argument(
        "--course",
        action="append",
        help="Sync only this generated_course_notes course path; repeat as needed.",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def select_books(courses: list[str] | None) -> tuple[Book, ...]:
    if not courses:
        return BOOKS

    requested = set(courses)
    known = {book.course for book in BOOKS}
    unknown = sorted(requested - known)
    if unknown:
        raise SystemExit(f"unknown course(s): {', '.join(unknown)}")
    return tuple(book for book in BOOKS if book.course in requested)


def validate_catalog(source_dir: Path) -> None:
    expected = {book.source_name for book in BOOKS}
    present = {path.name for path in source_dir.glob("*.pdf")}
    unknown = sorted(present - expected)
    if unknown:
        raise SystemExit(
            "unmapped 1.2x pocket PDF(s); add human titles to BOOKS first: "
            + ", ".join(unknown)
        )


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    source_dir = (args.source_dir or repo_root / "all_notes" / "pocket_books_1_2x").resolve()
    target_root = args.target_root.expanduser().resolve()

    if not source_dir.is_dir():
        raise SystemExit(f"missing 1.2x pocket source directory: {source_dir}")

    validate_catalog(source_dir)
    books = select_books(args.course)
    missing = [book.source_name for book in books if not (source_dir / book.source_name).is_file()]
    if missing:
        raise SystemExit(f"missing merged 1.2x pocket PDF(s): {', '.join(missing)}")

    for category in ("core", "supplemental"):
        if not args.dry_run:
            (target_root / category).mkdir(parents=True, exist_ok=True)

    for book in books:
        source = source_dir / book.source_name
        target = target_root / book.category / book.display_name
        legacy_target = target_root / book.category / book.source_name
        print(f"{book.course} -> {target}")

        if args.dry_run:
            continue

        if not target.exists() or sha256(source) != sha256(target):
            shutil.copy2(source, target)
        if sha256(source) != sha256(target):
            raise SystemExit(f"copy verification failed: {target}")

        if legacy_target != target and legacy_target.exists():
            legacy_target.unlink()

    print(f"verified {len(books)} merged 1.2x pocket book(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
