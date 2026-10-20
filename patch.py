#!/usr/bin/env python3
"""Apply the verified IntelliJ 2026.2 metadata patch to Color Brackets."""

import argparse
import hashlib
from pathlib import Path
import tempfile
import zipfile


VERSION = "2024.6.1.8-local-262"
OUTPUT_NAME = f"ColorBrackets-{VERSION}.jar"
EXPECTED_INPUT_SHA256 = "07cf127bfa6643bfd8d083eb04992f1f989af7cd2c9b2f0ea343ec5450510d62"
EXPECTED_OUTPUT_SHA256 = "fec2fcc001237dda96e20596154e71066593bc2bdfdcf265c417262deb909ee8"


def patch(source: Path, destination: Path) -> None:
    if destination.exists():
        raise ValueError(f"Output already exists: {destination}")
    if hashlib.sha256(source.read_bytes()).hexdigest() != EXPECTED_INPUT_SHA256:
        raise ValueError("Expected the unmodified Color Brackets 2024.6.1.8 JAR.")

    with tempfile.TemporaryDirectory(dir=destination.parent) as tmp:
        candidate = Path(tmp) / OUTPUT_NAME
        with zipfile.ZipFile(source) as original, zipfile.ZipFile(candidate, "w") as updated:
            for entry in original.infolist():
                data = original.read(entry.filename)
                if entry.filename == "META-INF/plugin.xml":
                    data = data.replace(b'until-build="261.*"', b'until-build="262.*"')
                    data = data.replace(
                        b"<version>2024.6.1.8</version>",
                        f"<version>{VERSION}</version>".encode(),
                    )
                updated.writestr(entry, data)

        if hashlib.sha256(candidate.read_bytes()).hexdigest() != EXPECTED_OUTPUT_SHA256:
            raise ValueError("Generated JAR differs from the verified patch.")
        # Exclusive creation keeps an existing output safe even if it appeared meanwhile.
        with destination.open("xb") as output:
            output.write(candidate.read_bytes())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jar", type=Path, help="Original ColorBrackets-2024.6.1.8.jar")
    parser.add_argument("--output", type=Path, help="Output JAR path; must not exist")
    args = parser.parse_args()
    destination = args.output or args.jar.with_name(OUTPUT_NAME)
    try:
        patch(args.jar, destination)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        parser.exit(1, f"Error: {error}\n")
    print(f"Created {destination}\nSHA256: {EXPECTED_OUTPUT_SHA256}")


if __name__ == "__main__":
    main()
