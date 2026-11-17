# Appendix C - Final Security Assessment: /home/kali/workspace/abb-hackathon/copilot-engineering-secure-software-lab-angular

Generated (UTC): 2026-11-17T17:39:30.909872+00:00

## 1. Executive summary

Automated analysis produced **102 scanner findings** for **/home/kali/workspace/abb-hackathon/copilot-engineering-secure-software-lab-angular**.

These are automated detections requiring review, not independently confirmed vulnerabilities.

### Severity distribution

| Severity | Count |
| --- | --- |
| CRITICAL | 4 |
| HIGH | 17 |
| MEDIUM | 26 |
| LOW | 0 |
| INFO | 47 |
| UNKNOWN | 8 |

### Top five risks

1. **CRITICAL** - Stripe Secret Key (Trivy, src/app/vulnerable/components/data-exposure/data-exposure.component.ts:20)
2. **CRITICAL** - Stripe Secret Key (Trivy, src/app/vulnerable/components/data-exposure/data-exposure.component.ts:232)
3. **CRITICAL** - Stripe Secret Key (Trivy, src/app/vulnerable/components/data-exposure/data-exposure.component.ts:254)
4. **CRITICAL** - Stripe Secret Key (Trivy, src/environments/environment.ts:18)
5. **HIGH** - User controlled data in methods like 'innerHTML', 'outerHTML' or 'document.write' is an anti-pattern that can lead to XSS vulnerabilities (Semgrep, src/app/secure/components/xss-innerhtml/xss-innerhtml.component.ts:325)

### Main limitations

Automated findings have not been independently verified. Reachability, runtime exploitability and business impact are not assessed. Offline vulnerability database freshness cannot be established without database timestamps.

## 2. Scope

| Field | Value |
| --- | --- |
| Repository | /home/kali/workspace/abb-hackathon/copilot-engineering-secure-software-lab-angular |
| Repository URL | https://github.com/ArulaAI/copilot-engineering-secure-software-lab-angular.git |
| Commit | c6ec732798180a797ee9783cf002aefdfccd5039 |
| Branch | main |
| Folders scanned | /home/kali/workspace/abb-hackathon/copilot-engineering-secure-software-lab-angular |
| Known exclusions | node_modules |
| Scanner output directory | /home/kali/workspace/abb-hackathon/scanner_output |

Exclusions listed here are only those recorded in the available reports or metadata. Different scanners may have different exclusions.

## 3. Environment

| Field | Recorded value |
| --- | --- |
| OS / VM | Linux-5.15.0-203-generic-x86_64-with-glibc2.35 |
| CPU architecture | 64 |
| Python version | 3.12.16 (main, Oct 26 2026, 15:28:01) [GCC 11.4.0] |
| Rule-set hashes | Not supplied |
| Vulnerability database timestamps | Not supplied |
| Trivy report timestamp | 2026-11-17T17:28:14.435744214Z |
| ScanCode scan start | 2026-11-17T172827.762977 |

### Scanner versions

| Scanner | Version |
| --- | --- |
| Semgrep | 1.185.0 |
| Trivy | 0.76.2 |
| ScanCode | 32.5.0 |
| Syft | 1.57.1 |

### Scanner input status

| Scanner | Input file | Status |
| --- | --- | --- |
| semgrep | semgrep_output.json | Present |
| trivy | trivy_output_offline.json | Present |
| bandit | bandit_output.json | Present |
| eslint | eslint_output.json | Present |
| gitleaks | gitleaks_output.json | Present |
| scancode | scancode_output.json | Present |
| cyclonedx | sbom_cyclonedx.json | Present |
| spdx | sbom_spdx.json | Present |
| dotnet | dotnet_output.txt | Present |

## 4. Method

| Scanner / format | Purpose | Availability |
| --- | --- | --- |
| semgrep | Rule-based static application security testing | Input present |
| bandit | Python static security analysis | Input present |
| eslint | JavaScript lint and security rules | Input present |
| trivy | Dependency and configuration security checks | Input present |
| gitleaks | Potential secret detection | Input present |
| scancode | License, copyright and package analysis | Input present |
| cyclonedx | CycloneDX software bill of materials | Input present |
| spdx | SPDX software bill of materials | Input present |
| dotnet | NuGet dependency vulnerability analysis | Input present |

Exact execution commands, scan options, offline cache configuration and rule provenance may require execution logs or additional metadata.

## 5. Results by repository

| Repository | Critical | High | Medium | Low | Info | Unknown | Confirmed | Unverified |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /home/kali/workspace/abb-hackathon/copilot-engineering-secure-software-lab-angular | 4 | 17 | 26 | 0 | 47 | 8 | 0 | 102 |

All findings are classified as **unverified** until a human reviewer confirms their disposition. Scanner confidence does not establish exploitability.

### Findings by category

| Category | Count |
| --- | --- |
| correctness | 46 |
| Dependency vulnerability | 21 |
| security | 14 |
| Potential secret | 10 |
| best-practice | 9 |
| Code quality | 2 |

### Findings by scanner

| Scanner | Count |
| --- | --- |
| ESLint | 2 |
| Gitleaks | 6 |
| Semgrep | 69 |
| Trivy | 25 |

## 6. Top findings

### 1. Stripe Secret Key

| Field | Value |
| --- | --- |
| Finding ID | 28c6d83e1fda21ca |
| Scanner | Trivy |
| Severity | CRITICAL |
| Evidence location | src/app/vulnerable/components/data-exposure/data-exposure.component.ts:20 |
| Rule | stripe-secret-token |
| CWE | Not supplied |
| CVE / advisory | Not supplied |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Manual remediation decision required |
| Source | trivy_output_offline.json |
| Reference | Not supplied |

Evidence summary: Potential secret detected; value withheld.

### 2. Stripe Secret Key

| Field | Value |
| --- | --- |
| Finding ID | 9d4db1749eab1f3a |
| Scanner | Trivy |
| Severity | CRITICAL |
| Evidence location | src/app/vulnerable/components/data-exposure/data-exposure.component.ts:232 |
| Rule | stripe-secret-token |
| CWE | Not supplied |
| CVE / advisory | Not supplied |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Manual remediation decision required |
| Source | trivy_output_offline.json |
| Reference | Not supplied |

Evidence summary: Potential secret detected; value withheld.

### 3. Stripe Secret Key

| Field | Value |
| --- | --- |
| Finding ID | 8e6c590f09b2c2fc |
| Scanner | Trivy |
| Severity | CRITICAL |
| Evidence location | src/app/vulnerable/components/data-exposure/data-exposure.component.ts:254 |
| Rule | stripe-secret-token |
| CWE | Not supplied |
| CVE / advisory | Not supplied |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Manual remediation decision required |
| Source | trivy_output_offline.json |
| Reference | Not supplied |

Evidence summary: Potential secret detected; value withheld.

### 4. Stripe Secret Key

| Field | Value |
| --- | --- |
| Finding ID | ef9afcf895b6b311 |
| Scanner | Trivy |
| Severity | CRITICAL |
| Evidence location | src/environments/environment.ts:18 |
| Rule | stripe-secret-token |
| CWE | Not supplied |
| CVE / advisory | Not supplied |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Manual remediation decision required |
| Source | trivy_output_offline.json |
| Reference | Not supplied |

Evidence summary: Potential secret detected; value withheld.

### 5. User controlled data in methods like 'innerHTML', 'outerHTML' or 'document.write' is an anti-pattern that can lead to XSS vulnerabilities

| Field | Value |
| --- | --- |
| Finding ID | 76659cf9d9010277 |
| Scanner | Semgrep |
| Severity | HIGH |
| Evidence location | src/app/secure/components/xss-innerhtml/xss-innerhtml.component.ts:325 |
| Rule | scanner_output.semgrep-configs.javascript.browser.security.insecure-document-method |
| CWE | CWE-79 |
| CVE / advisory | Not supplied |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Manual remediation decision required |
| Source | semgrep_output.json |
| Reference | https://owasp.org/Top10/A03_2021-Injection |

Evidence summary: User controlled data in methods like 'innerHTML', 'outerHTML' or 'document.write' is an anti-pattern that can lead to XSS vulnerabilities

### 6. User controlled data in a 'textarea.innerHTML' is an anti-pattern that can lead to XSS vulnerabilities

| Field | Value |
| --- | --- |
| Finding ID | 81d7485718cbbfd8 |
| Scanner | Semgrep |
| Severity | HIGH |
| Evidence location | src/app/secure/components/xss-innerhtml/xss-innerhtml.component.ts:325 |
| Rule | scanner_output.semgrep-configs.javascript.browser.security.insecure-innerhtml |
| CWE | CWE-79 |
| CVE / advisory | Not supplied |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Manual remediation decision required |
| Source | semgrep_output.json |
| Reference | https://owasp.org/Top10/A03_2021-Injection |

Evidence summary: User controlled data in a 'textarea.innerHTML' is an anti-pattern that can lead to XSS vulnerabilities

### 7. User controlled data in methods like 'innerHTML', 'outerHTML' or 'document.write' is an anti-pattern that can lead to XSS vulnerabilities

| Field | Value |
| --- | --- |
| Finding ID | 44d37fa70817f75a |
| Scanner | Semgrep |
| Severity | HIGH |
| Evidence location | src/app/vulnerable/components/xss-interpolation/xss-interpolation.component.ts:241 |
| Rule | scanner_output.semgrep-configs.javascript.browser.security.insecure-document-method |
| CWE | CWE-79 |
| CVE / advisory | Not supplied |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Manual remediation decision required |
| Source | semgrep_output.json |
| Reference | https://owasp.org/Top10/A03_2021-Injection |

Evidence summary: User controlled data in methods like 'innerHTML', 'outerHTML' or 'document.write' is an anti-pattern that can lead to XSS vulnerabilities

### 8. User controlled data in a 'this.welcomeContainer.nativeElement.innerHTML' is an anti-pattern that can lead to XSS vulnerabilities

| Field | Value |
| --- | --- |
| Finding ID | 1caaed45f152cd82 |
| Scanner | Semgrep |
| Severity | HIGH |
| Evidence location | src/app/vulnerable/components/xss-interpolation/xss-interpolation.component.ts:241 |
| Rule | scanner_output.semgrep-configs.javascript.browser.security.insecure-innerhtml |
| CWE | CWE-79 |
| CVE / advisory | Not supplied |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Manual remediation decision required |
| Source | semgrep_output.json |
| Reference | https://owasp.org/Top10/A03_2021-Injection |

Evidence summary: User controlled data in a 'this.welcomeContainer.nativeElement.innerHTML' is an anti-pattern that can lead to XSS vulnerabilities

### 9. @angular/common: Information Leak via Default Caching of Credentialed Requests in HttpTransferCache

| Field | Value |
| --- | --- |
| Finding ID | e0dc901000368b1b |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-50170 |
| CWE | CWE-524 |
| CVE / advisory | CVE-2026-50170 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.0-rc.2, 20.3.22, 19.2.23, 21.2.15 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-50170 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 22.0.0-rc.2, 21.2.15, 20.3.22, and 19.2.23, a vulnerability was discovered in @angular/common when Server-Side Rendering (SSR) and hydration are enabled. The HttpTransferCache utility optimizes hydration by caching outgoing HTTP requests performed during SSR and transferring the cached state to the client-side application via TransferState. However, the cac

### 10. @angular/common: Angular @angular/common: Denial of Service via malformed digitsInfo parameter

| Field | Value |
| --- | --- |
| Finding ID | b9b3d9075f6afd4e |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-50171 |
| CWE | CWE-400, CWE-834 |
| CVE / advisory | CVE-2026-50171 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.0-rc.2, 20.3.22, 19.2.23, 21.2.15 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-50171 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 22.0.0-rc.2, 21.2.15, 20.3.22, and 19.2.23, a Denial of Service (DoS) vulnerability exists in the @angular/common package of Angular. The formatNumber function, which is also utilized by DecimalPipe, PercentPipe, and CurrencyPipe, does not properly validate the upper bounds of the digitsInfo parameter. Specifically, the minimum and maximum fraction digits p

### 11. @angular/common: Weak 32-Bit Cache Key Hashing in 'HttpTransferCache' Leading to Cross-Request Data Leakage and State Poisoning

| Field | Value |
| --- | --- |
| Finding ID | 278c20169a385e20 |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-54266 |
| CWE | CWE-328, CWE-345 |
| CVE / advisory | CVE-2026-54266 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.1, 21.2.17, 20.3.25 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-54266 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 22.0.1, 21.2.17, and 20.3.25, Angular's HttpTransferCache caches HTTP requests made during Server-Side Rendering (SSR) so that they can be reused during client-side hydration. This avoids repeating the same HTTP requests on the client. The cached responses are stored in TransferState using a cache key generated by hashing request properties (method, respons

### 12. @angular/common: Angular @angular/common: Denial of Service via crafted date format string

| Field | Value |
| --- | --- |
| Finding ID | be4529adfb88c83c |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-54268 |
| CWE | CWE-1333, CWE-400 |
| CVE / advisory | CVE-2026-54268 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.1, 21.2.17, 20.3.25 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-54268 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 22.0.1, 21.2.17, and 20.3.25, a Denial of Service (DoS) vulnerability exists in the @angular/common package of the Angular framework. The formatDate function, which is also utilized by the standard Angular DatePipe, does not properly limit or validate the length of the format parameter. When parsing a maliciously crafted, excessively long date format string

### 13. @angular/common: Angular: Cross-Request Response Reuse and State Poisoning in HttpTransferCache

| Field | Value |
| --- | --- |
| Finding ID | 4d903fc835774f42 |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-68945 |
| CWE | CWE-345 |
| CVE / advisory | CVE-2026-68945 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.2, 21.2.19, 20.3.27 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-68945 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.27, 21.2.19, and 22.0.2, HttpTransferCache comma-joins repeated request parameters, allowing semantically distinct HttpClient requests to use the same transfer-cache key and reuse a wrong backend response. This issue is fixed in versions 20.3.27, 21.2.19, and 22.0.2.

### 14. @angular/core: @angular/compiler: Angular has XSS in i18n attribute bindings

| Field | Value |
| --- | --- |
| Finding ID | 071077b76b821a39 |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-32635 |
| CWE | CWE-79 |
| CVE / advisory | CVE-2026-32635 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.0-next.3, 21.2.4, 20.3.18, 19.2.20 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-32635 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 22.0.0-next.3, 21.2.4, 20.3.18, and 19.2.20, a Cross-Site Scripting (XSS) vulnerability has been identified in the Angular runtime and compiler. It occurs when the application uses a security-sensitive attribute (for example href on an anchor tag) together with Angular's ability to internationalize attributes. Enabling internationalization for the sensitive

### 15. @angular/compiler: @angular/core: Angular: Cross-Site Scripting via internationalization event handlers

| Field | Value |
| --- | --- |
| Finding ID | f2f9f713fad65c5a |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-69151 |
| CWE | CWE-79 |
| CVE / advisory | CVE-2026-69151 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.1, 21.2.19, 20.3.27 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-69151 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.27, 21.2.19, and 22.0.1, the Angular compiler i18n pipeline permits i18n-onerror and other i18n-on event-handler attributes, allowing a lower-trust translation file to replace a static handler with executable JavaScript. This issue is fixed in versions 20.3.27, 21.2.19, and 22.0.1.

### 16. @angular/core: Angular: Cross-site scripting via compromised translation files

| Field | Value |
| --- | --- |
| Finding ID | ec5eacb0d04ee952 |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-27970 |
| CWE | CWE-79 |
| CVE / advisory | CVE-2026-27970 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 21.2.0, 21.1.6, 20.3.17, 19.2.19 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-27970 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Versions prior to 21.2.0, 21.1.16, 20.3.17, and 19.2.19 have a cross-Site scripting vulnerability in the Angular internationalization (i18n) pipeline. In ICU messages (International Components for Unicode), HTML from translated content was not properly sanitized and could execute arbitrary JavaScript. Angular i18n typically involves three steps, extracting all messa

### 17. @angular/core: @angular/compiler: Angular has XSS in i18n attribute bindings

| Field | Value |
| --- | --- |
| Finding ID | e029533f9df878f3 |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-32635 |
| CWE | CWE-79 |
| CVE / advisory | CVE-2026-32635 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.0-next.3, 21.2.4, 20.3.18, 19.2.20 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-32635 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 22.0.0-next.3, 21.2.4, 20.3.18, and 19.2.20, a Cross-Site Scripting (XSS) vulnerability has been identified in the Angular runtime and compiler. It occurs when the application uses a security-sensitive attribute (for example href on an anchor tag) together with Angular's ability to internationalize attributes. Enabling internationalization for the sensitive

### 18. @angular/core: Angular Client Hydration DOM Clobbering & Response-Cache Poisoning

| Field | Value |
| --- | --- |
| Finding ID | dcfd8bef007f8614 |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-54267 |
| CWE | CWE-471, CWE-79 |
| CVE / advisory | CVE-2026-54267 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.1, 21.2.17, 20.3.25 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-54267 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 22.0.1, 21.2.17, and 20.3.25, to optimize client-side bootstrap in Server-Side Rendered (SSR) environments, Angular supports Hydration via provideClientHydration(). During SSR, Angular serializes the application's runtime state (such as cached HttpClient responses) and outputs it into the HTML stream as a <script> tag with a predictable identifier. During c

### 19. @angular/compiler: @angular/core: Angular: Cross-Site Scripting via internationalization event handlers

| Field | Value |
| --- | --- |
| Finding ID | 17a8e474afa80bff |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-69151 |
| CWE | CWE-79 |
| CVE / advisory | CVE-2026-69151 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.0.1, 21.2.19, 20.3.27 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-69151 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.27, 21.2.19, and 22.0.1, the Angular compiler i18n pipeline permits i18n-onerror and other i18n-on event-handler attributes, allowing a lower-trust translation file to replace a static handler with executable JavaScript. This issue is fixed in versions 20.3.27, 21.2.19, and 22.0.1.

### 20. @angular/router: @angular/router: Denial of Service via numeric matrix parameters during Server-Side Rendering

| Field | Value |
| --- | --- |
| Finding ID | f3154c1aef9ab50e |
| Scanner | Trivy |
| Severity | HIGH |
| Evidence location | package-lock.json |
| Rule | CVE-2026-101896 |
| CWE | CWE-400, CWE-770 |
| CVE / advisory | CVE-2026-101896 |
| Reachability | Not assessed |
| Impact | Requires review |
| Disposition | Unverified |
| Suggested fix | Review affected package and update to a compatible fixed version: 22.2.0, 21.2.24, 20.3.32 |
| Source | trivy_output_offline.json |
| Reference | https://avd.aquasec.com/nvd/cve-2026-101896 |

Evidence summary: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.32, 21.2.24, and 22.2.0, the @angular/router URL parser stores numeric matrix parameter names and numeric outlet names as properties on initially empty JavaScript objects during Node.js server-side rendering. V8 can interpret these URL-derived keys as array indices and allocate dense backing stores sized to high numeric values, so repeated small path s

Only the first 20 of 102 findings are expanded here. Complete records are available in consolidated_findings.json.

## 7. Supply chain view

Package scanners identified **1165 distinct package/version entries** after consolidation.

An SBOM package entry does not itself represent a vulnerability.

### Vulnerable packages and advisories

| Package | Installed | Advisory | Severity | Fixed version | Source |
| --- | --- | --- | --- | --- | --- |
| @angular/common | 19.2.18 | CVE-2026-50170 | HIGH | 22.0.0-rc.2, 20.3.22, 19.2.23, 21.2.15 | Trivy |
| @angular/common | 19.2.18 | CVE-2026-50171 | HIGH | 22.0.0-rc.2, 20.3.22, 19.2.23, 21.2.15 | Trivy |
| @angular/common | 19.2.18 | CVE-2026-54266 | HIGH | 22.0.1, 21.2.17, 20.3.25 | Trivy |
| @angular/common | 19.2.18 | CVE-2026-54268 | HIGH | 22.0.1, 21.2.17, 20.3.25 | Trivy |
| @angular/common | 19.2.18 | CVE-2026-68945 | HIGH | 22.0.2, 21.2.19, 20.3.27 | Trivy |
| @angular/compiler | 19.2.18 | CVE-2026-32635 | HIGH | 22.0.0-next.3, 21.2.4, 20.3.18, 19.2.20 | Trivy |
| @angular/compiler | 19.2.18 | CVE-2026-69151 | HIGH | 22.0.1, 21.2.19, 20.3.27 | Trivy |
| @angular/core | 19.2.18 | CVE-2026-27970 | HIGH | 21.2.0, 21.1.6, 20.3.17, 19.2.19 | Trivy |
| @angular/core | 19.2.18 | CVE-2026-32635 | HIGH | 22.0.0-next.3, 21.2.4, 20.3.18, 19.2.20 | Trivy |
| @angular/core | 19.2.18 | CVE-2026-54267 | HIGH | 22.0.1, 21.2.17, 20.3.25 | Trivy |
| @angular/core | 19.2.18 | CVE-2026-69151 | HIGH | 22.0.1, 21.2.19, 20.3.27 | Trivy |
| @angular/router | 19.2.18 | CVE-2026-101896 | HIGH | 22.2.0, 21.2.24, 20.3.32 | Trivy |
| @angular/router | 19.2.18 | CVE-2026-111752 | HIGH | 22.2.1, 21.2.25, 20.3.33 | Trivy |
| @angular/common | 19.2.18 | CVE-2026-111753 | MEDIUM | 21.0.3, 20.3.34 | Trivy |
| @angular/common | 19.2.18 | CVE-2026-88059 | MEDIUM | 22.1.1, 21.2.20, 20.3.28 | Trivy |
| @angular/compiler | 19.2.18 | CVE-2026-50557 | MEDIUM | 21.2.15, 22.0.0-rc.2, 20.3.22, 19.2.22 | Trivy |
| @angular/compiler | 19.2.18 | CVE-2026-54265 | MEDIUM | 22.0.1, 21.2.17, 20.3.25 | Trivy |
| @angular/compiler | 19.2.18 | CVE-2026-88057 | MEDIUM | 22.1.0, 21.2.20, 20.3.28 | Trivy |
| @angular/core | 19.2.18 | CVE-2026-50557 | MEDIUM | 21.2.15, 22.0.0-rc.2, 20.3.22, 19.2.22 | Trivy |
| @angular/core | 19.2.18 | CVE-2026-52725 | MEDIUM | 21.2.15, 22.0.0-rc.2, 19.2.23, 20.3.22 | Trivy |
| @angular/core | 19.2.18 | CVE-2026-88057 | MEDIUM | 22.1.0, 21.2.20, 20.3.28 | Trivy |

### Package inventory

| Package | Version / constraint | Direct / transitive | License | Source |
| --- | --- | --- | --- | --- |
| /home/kali/workspace/abb-hackathon/copilot-engineering-secure-software-lab-angular |  | Unknown | Not identified | Syft SPDX |
| @angular/common | 19.2.18 | Transitive | MIT | Trivy, ScanCode dependency, Syft CycloneDX, Syft SPDX |
| @angular/compiler | 19.2.18 | Transitive | MIT | Trivy, ScanCode dependency, Syft CycloneDX, Syft SPDX |
| @angular/core | 19.2.18 | Transitive | MIT | Trivy, ScanCode dependency, Syft CycloneDX, Syft SPDX |
| @angular/forms | 19.2.18 | Transitive | MIT | Trivy, ScanCode dependency, Syft CycloneDX, Syft SPDX |
| @angular/platform-browser | 19.2.18 | Transitive | MIT | Trivy, ScanCode dependency, Syft CycloneDX, Syft SPDX |
| @angular/platform-browser-dynamic | 19.2.18 | Transitive | MIT | Trivy, ScanCode dependency, Syft CycloneDX, Syft SPDX |
| @angular/router | 19.2.18 | Transitive | MIT | Trivy, ScanCode dependency, Syft CycloneDX, Syft SPDX |
| copilot-secure-angular-lab | 1.0.0 | Unknown | ISC | ScanCode, Syft CycloneDX, Syft SPDX |
| pkg:npm/%40ampproject/remapping@2.3.0 | 2.3.0 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40angular-devkit/architect@0.1902.19 | 0.1902.19 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40angular-devkit/build-angular | ^19.2.19 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40angular-devkit/build-angular@19.2.19 | 19.2.19 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40angular-devkit/build-webpack@0.1902.19 | 0.1902.19 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40angular-devkit/core@19.2.19 | 19.2.19 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40angular-devkit/schematics@19.2.19 | 19.2.19 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/build@19.2.19 | 19.2.19 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/cli | ^19.2.19 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/cli@19.2.19 | 19.2.19 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/common | ^19.2.0 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/compiler | ^19.2.0 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/compiler-cli | ^19.2.0 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/compiler-cli@19.2.18 | 19.2.18 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/core | ^19.2.0 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/forms | ^19.2.0 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/platform-browser | ^19.2.0 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/platform-browser-dynamic | ^19.2.0 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40angular/router | ^19.2.0 | Direct | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/code-frame@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/compat-data@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/core@7.26.10 | 7.26.10 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/core@7.26.9 | 7.26.9 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/core@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/generator@7.26.10 | 7.26.10 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/generator@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-annotate-as-pure@7.25.9 | 7.25.9 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-annotate-as-pure@7.27.3 | 7.27.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-compilation-targets@7.27.2 | 7.27.2 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-create-class-features-plugin@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-create-regexp-features-plugin@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-define-polyfill-provider@0.6.5 | 0.6.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-globals@7.28.0 | 7.28.0 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-member-expression-to-functions@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-module-imports@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-module-transforms@7.28.3 | 7.28.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-optimise-call-expression@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-plugin-utils@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-remap-async-to-generator@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-replace-supers@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-skip-transparent-expression-wrappers@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-split-export-declaration@7.24.7 | 7.24.7 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-string-parser@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-validator-identifier@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-validator-option@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helper-wrap-function@7.28.3 | 7.28.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/helpers@7.28.4 | 7.28.4 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/parser@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-bugfix-firefox-class-in-computed-class-key@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-bugfix-safari-class-field-initializer-scope@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-bugfix-safari-id-destructuring-collision-in-function-expression@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-bugfix-v8-spread-parameters-in-optional-chaining@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-bugfix-v8-static-class-fields-redefine-readonly@7.28.3 | 7.28.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-proposal-private-property-in-object@7.21.0-placeholder-for-preset-env.2 | 7.21.0-placeholder-for-preset-env.2 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-async-generators@7.8.4 | 7.8.4 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-bigint@7.8.3 | 7.8.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-class-properties@7.12.13 | 7.12.13 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-class-static-block@7.14.5 | 7.14.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-import-assertions@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-import-attributes@7.26.0 | 7.26.0 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-import-attributes@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-import-meta@7.10.4 | 7.10.4 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-json-strings@7.8.3 | 7.8.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-jsx@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-logical-assignment-operators@7.10.4 | 7.10.4 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-nullish-coalescing-operator@7.8.3 | 7.8.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-numeric-separator@7.10.4 | 7.10.4 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-object-rest-spread@7.8.3 | 7.8.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-optional-catch-binding@7.8.3 | 7.8.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-optional-chaining@7.8.3 | 7.8.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-private-property-in-object@7.14.5 | 7.14.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-top-level-await@7.14.5 | 7.14.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-typescript@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-syntax-unicode-sets-regex@7.18.6 | 7.18.6 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-arrow-functions@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-async-generator-functions@7.26.8 | 7.26.8 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-async-to-generator@7.25.9 | 7.25.9 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-block-scoped-functions@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-block-scoping@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-class-properties@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-class-static-block@7.28.3 | 7.28.3 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-classes@7.28.4 | 7.28.4 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-computed-properties@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-destructuring@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-dotall-regex@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-duplicate-keys@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-duplicate-named-capturing-groups-regex@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-dynamic-import@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-exponentiation-operator@7.28.5 | 7.28.5 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-export-namespace-from@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |
| pkg:npm/%40babel/plugin-transform-for-of@7.27.1 | 7.27.1 | Transitive | Not assessed | ScanCode dependency |

Additional package entries are available in consolidated_findings.json.

### Repository license

isc

Detected licenses are not a legal compliance determination. Unknown dependency relationships are not inferred.

## 8. Remediation outcomes

No baseline/post-remediation comparison, patch evidence or test results were supplied.

Before-and-after counts, verified fixes and closure status are **not assessed**.

## 9. Limitations

- Static analysis and dependency scanners can produce false positives and false negatives.
- Reachability, exploitability, runtime controls and business impact have not been validated.
- Offline vulnerability databases and rules may be stale. Report timestamps do not prove database freshness.
- A missing or failed scanner must not be interpreted as reporting zero vulnerabilities.
- Source coverage, excluded files and unsupported language features may not be fully established by scanner reports alone.
- Potential secret findings require validation. Matched secret values are withheld.

## 10. Recommendations

1. **Triage ownership:** Assign each finding to a responsible repository or component owner.
2. **Validate findings:** Confirm whether flagged code and dependencies are deployed and reachable. Record false positives.
3. **Fix timelines:** Establish severity-based remediation SLAs using an approved policy.
4. **CI integration:** Integrate scanners into CI and define policy gates with an exception process.
5. **Supply chain:** Update vulnerable dependencies to compatible patched versions and review license obligations.
6. **Offline maintenance:** Periodically refresh scanner rules and vulnerability databases through an approved process.
7. **Remediation verification:** Rerun scans and tests after fixes. Preserve baseline and follow-up reports.

