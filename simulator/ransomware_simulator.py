"""
SAFE RANSOMWARE-BEHAVIOR SIMULATOR
==================================

Portfolio lab component.

IMPORTANT:
- Only operates inside the configured test directory.
- Creates/renames synthetic files only.
- Does NOT encrypt data.
- Does NOT delete files.
- Does NOT spread, persist, evade, or contact remote systems.

Run only in an isolated lab VM after reviewing the code.
"""

from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path

DEFAULT_CONFIG = Path(__file__).with_name("config.json")


def load_config() -> dict:
    with DEFAULT_CONFIG.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_target(target: Path, allowed_root: Path) -> None:
    target = target.resolve()
    allowed_root = allowed_root.resolve()

    if target == allowed_root or allowed_root not in target.parents:
        raise RuntimeError(
            f"Safety check failed. Target must be below {allowed_root}"
        )


def create_synthetic_files(target: Path, count: int) -> list[Path]:
    files = []
    for i in range(1, count + 1):
        p = target / f"synthetic_document_{i:03d}.txt"
        p.write_text(
            f"SYNTHETIC SOC LAB FILE {i}\n"
            "This file contains no real user data.\n",
            encoding="utf-8",
        )
        files.append(p)
    return files


def simulate_file_activity(target: Path, extension: str, delay: float) -> list[Path]:
    changed = []
    for p in sorted(target.glob("synthetic_document_*.txt")):
        new_path = p.with_suffix(extension)
        p.rename(new_path)
        changed.append(new_path)
        logging.info("SIMULATED_FILE_RENAME source=%s target=%s", p, new_path)
        time.sleep(delay)

    note = target / "SIMULATED_RANSOM_NOTE.txt"
    note.write_text(
        "SAFE TRAINING SIMULATION\n\n"
        "No encryption occurred. This is a synthetic ransomware-behavior test.\n",
        encoding="utf-8",
    )
    logging.info("SIMULATED_RANSOM_NOTE path=%s", note)
    return changed


def main() -> None:
    config = load_config()
    allowed_root = Path(config["allowed_root"])
    target = Path(config["target_directory"])
    count = int(config.get("synthetic_file_count", 30))
    extension = config.get("simulated_extension", ".locked")
    delay = float(config.get("delay_seconds", 0.05))
    log_file = Path(config.get("log_file", "simulation.log"))

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    validate_target(target, allowed_root)
    target.mkdir(parents=True, exist_ok=True)

    logging.info("SIMULATION_START target=%s", target)
    logging.info("SAFETY_MODE synthetic_only=true destructive_actions=false")

    create_synthetic_files(target, count)
    simulate_file_activity(target, extension, delay)

    logging.info("SIMULATION_COMPLETE target=%s", target)
    print("Safe ransomware-behavior simulation completed.")
    print(f"Target: {target}")
    print("No encryption or destructive actions were performed.")


if __name__ == "__main__":
    main()
