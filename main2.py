
from datetime import datetime

from scan_config import TARGET_DIR

print("=" * 60)
print("OFFLINE SECURITY SCANNER - WITHOUT SEMGREP")
print("=" * 60)
print(f"Target Repository: {TARGET_DIR}")
print(f"Started at: {datetime.now()}")
print("=" * 60)

# 1. Dependency, Configuration and Secret Scanning
from scanners import trivy_scanner
trivy_scanner.main()
print("\n[1/7] Trivy scanning completed!")

# 2. Software Bill of Materials Generation
from scanners import syft_scanner
syft_scanner.main()
print("\n[2/7] SBOM generation completed!")

# 3. Secret Detection
from scanners import gitleaks_scanner
gitleaks_scanner.main()
print("\n[3/7] Gitleaks scanning completed!")

# 4. License, Copyright and Package Inventory
from scanners import scancode_scanner
scancode_scanner.main()
print("\n[4/7] ScanCode scanning completed!")

# 5. Python-Specific Security
from scanners import bandit_scanner
bandit_scanner.main()
print("\n[5/7] Bandit scanning completed!")

# 6. .NET NuGet Vulnerability Scanning
from scanners import dotnet_scanner
dotnet_scanner.main()
print("\n[6/7] .NET vulnerability scanning completed!")

# 7. JavaScript Security and Code Quality
from scanners import eslint_scanner
eslint_scanner.main()
print("\n[7/7] ESLint scanning completed!")

print("\n" + "=" * 60)
print("ALL 7 SCANNERS COMPLETED")
print(f"Finished at: {datetime.now()}")
print("=" * 60)
