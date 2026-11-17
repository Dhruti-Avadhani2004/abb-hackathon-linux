
# 1. Static Application Security Testing
from scanners import semgrep_scanner
print("\nStatic Analysis completed!")

# 2. Dependency, Configuration and License Scanning
from scanners import trivy_scanner
trivy_scanner.main()
print("\nDependencies, configuration and licenses scan completed!")

# 3. Software Bill of Materials Generation
from scanners import syft_scanner
syft_scanner.main()
print("\nSoftware Bill of Materials (SBOM) generation completed!")

# 4. Secret Detection
from scanners import gitleaks_scanner
gitleaks_scanner.main()
print("\nSecrets scanning completed!")

# 5. License, copyright and package inventory
from scanners import scancode_scanner
scancode_scanner.main()
print("\nLicense, copyright and package inventory scan completed!")

# 6. Python-specific security
from scanners import bandit_scanner
bandit_scanner.main()
print("\nPython-specific security scanning completed!")

# 7. .NET NuGet vulnerability
from scanners import dotnet_scanner
dotnet_scanner.main()
print("\n.NET NuGet vulnerability scanning completed!")

# 8. JavaScript security and code-quality
from scanners import eslint_scanner
eslint_scanner.main()
print("\nJavaScript security and code-quality scanning completed!")