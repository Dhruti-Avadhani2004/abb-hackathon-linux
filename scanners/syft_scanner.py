
# import os
# import shutil
# import subprocess
# from pathlib import Path

# # Project paths
# BASE_DIR = Path(__file__).resolve().parent.parent

# from scan_config import TARGET_DIR
# OUTPUT_DIR = BASE_DIR / "scanner_output"

# CYCLONEDX_FILE = OUTPUT_DIR / "sbom_cyclonedx.json"
# SPDX_FILE = OUTPUT_DIR / "sbom_spdx.json"
# LOG_FILE = OUTPUT_DIR / "syft_output.txt"

# # Locate Syft
# SYFT_PATH = shutil.which("syft")

# if not SYFT_PATH:
#     possible_path = (
#         Path(os.environ["LOCALAPPDATA"])
#         / "Microsoft"
#         / "WinGet"
#         / "Packages"
#         / "Anchore.Syft_Microsoft.Winget.Source_8wekyb3d8bbwe"
#         / "syft.exe"
#     )

#     if possible_path.exists():
#         SYFT_PATH = str(possible_path)


# def main():

#     if not TARGET_DIR.is_dir():
#         print(f"Target directory not found: {TARGET_DIR}")
#         return

#     if not SYFT_PATH:
#         print("Syft executable not found.")
#         return

#     OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

#     commands = [
#         (
#             "CycloneDX",
#             CYCLONEDX_FILE,
#             "cyclonedx-json"
#         ),
#         (
#             "SPDX",
#             SPDX_FILE,
#             "spdx-json"
#         )
#     ]

#     log_lines = []
#     results = {}

#     for name, output_file, format_name in commands:

#         print(f"\nGenerating {name} SBOM...")

#         # Remove previous output so stale files cannot appear successful
#         if output_file.exists():
#             output_file.unlink()

#         command = [
#             SYFT_PATH,
#             f"dir:{TARGET_DIR}",
#             "-o",
#             f"{format_name}={output_file}"
#         ]

#         result = subprocess.run(
#             command,
#             capture_output=True,
#             text=True,
#             encoding="utf-8",
#             errors="replace"
#         )

#         output = result.stdout + result.stderr
#         log_lines.append(f"\n===== {name} SBOM =====\n{output}")

#         success = (
#             result.returncode == 0
#             and output_file.exists()
#             and output_file.stat().st_size > 0
#         )

#         results[name] = success

#         if success:
#             print(f"{name} SBOM generated successfully.")
#         else:
#             print(f"{name} generation failed.")
#             print(output)

#     LOG_FILE.write_text(
#         "\n".join(log_lines),
#         encoding="utf-8"
#     )

#     print("\n===== Syft Scan Summary =====")
#     print(f"CycloneDX: {'SUCCESS' if results.get('CycloneDX') else 'FAILED'}")
#     print(f"SPDX:      {'SUCCESS' if results.get('SPDX') else 'FAILED'}")
#     print(f"Log:       {LOG_FILE}")


# if __name__ == "__main__":
#     main()



import os
import shutil
import subprocess
from pathlib import Path

from scan_config import TARGET_DIR, OUTPUT_DIR

CYCLONEDX_FILE = OUTPUT_DIR / "sbom_cyclonedx.json"
SPDX_FILE = OUTPUT_DIR / "sbom_spdx.json"
LOG_FILE = OUTPUT_DIR / "syft_output.txt"


def main():
    if not TARGET_DIR.is_dir():
        raise FileNotFoundError(
            f"Target directory not found: {TARGET_DIR}"
        )

    syft_path = shutil.which("syft")

    if not syft_path:
        raise FileNotFoundError(
            "Syft executable not found in PATH"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    commands = [
        ("CycloneDX", CYCLONEDX_FILE, "cyclonedx-json"),
        ("SPDX", SPDX_FILE, "spdx-json")
    ]

    # Disable Syft's automatic update checks.
    # Scan only the local directory.
    env = os.environ.copy()
    env["SYFT_CHECK_FOR_APP_UPDATE"] = "false"

    log_lines = []
    results = {}

    for name, output_file, format_name in commands:
        print(f"\nGenerating {name} SBOM...")

        if output_file.exists():
            output_file.unlink()

        command = [
            syft_path,
            f"dir:{TARGET_DIR}",
            "-o",
            f"{format_name}={output_file}"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env
        )

        output = result.stdout + result.stderr
        log_lines.append(
            f"\n===== {name} SBOM =====\n{output}"
        )

        success = (
            result.returncode == 0
            and output_file.is_file()
            and output_file.stat().st_size > 0
        )

        results[name] = success

        if success:
            print(f"{name} SBOM generated successfully.")
        else:
            print(f"{name} SBOM generation failed.")
            print(output)

    LOG_FILE.write_text(
        "\n".join(log_lines),
        encoding="utf-8"
    )

    print("\n===== Syft Scan Summary =====")
    print(
        f"CycloneDX: "
        f"{'SUCCESS' if results['CycloneDX'] else 'FAILED'}"
    )
    print(
        f"SPDX:      "
        f"{'SUCCESS' if results['SPDX'] else 'FAILED'}"
    )
    print(f"Log:       {LOG_FILE}")
    print("=============================")

    if not all(results.values()):
        raise RuntimeError(
            "One or more Syft SBOM generations failed"
        )


if __name__ == "__main__":
    main()
