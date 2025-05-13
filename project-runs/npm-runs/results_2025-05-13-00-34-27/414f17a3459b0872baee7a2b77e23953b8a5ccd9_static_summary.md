
# Software Supply Chain Report of jsdom/whatwg-url - 414f17a3459b0872baee7a2b77e23953b8a5ccd9

## Enabled Checks
The following checks were specifically requested:

- Source Code: `source_code`
- Source Code Sha: `source_code_sha`
- Deprecated: `deprecated`
- Provenance: `provenance`
- Code Signature: `code_signature`
- Aliased Packages: `aliased_packages`

---


<details>
    <summary>How to read the results :book: </summary>
    
 Dirty-waters has analyzed your project dependencies and found different categories for each of them:

    
 - ⚠️⚠️⚠️⚠️ : critical severity 

    
 - ⚠️⚠️⚠️ : high severity 

    
 - ⚠️⚠️: medium severity 

    
 - ⚠️: low severity 

</details>
        

 ### Total packages in the supply chain: 170


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 5

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 0

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 3

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 157

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 0

:alien: Packages that are aliased (⚠️⚠️): 3


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(5)</summary>
    


| package_name                         | sha_exists   | tag_version   | is_sha   | sha   | tag_url   | message                          |   status_code_for_sha | parent   |
|:-------------------------------------|:-------------|:--------------|:---------|:------|:----------|:---------------------------------|----------------------:|:---------|
| `@types/estree@1.0.6`                | False        | `1.0.6`       | False    |       |           | Tag 1.0.6 not found in the repo  |                   404 | `[]`     |
| `@types/istanbul-lib-coverage@2.0.6` | False        | `2.0.6`       | False    |       |           | Tag 2.0.6 not found in the repo  |                   404 | `[]`     |
| `@types/json-schema@7.0.15`          | False        | `7.0.15`      | False    |       |           | Tag 7.0.15 not found in the repo |                   404 | `[]`     |
| `keyv@4.5.4`                         | False        | `4.5.4`       | False    |       |           | Tag 4.5.4 not found in the repo  |                   404 | `[]`     |
| `lodash.merge@4.6.2`                 | False        | `4.6.2`       | False    |       |           | Tag 4.6.2 not found in the repo  |                   404 | `[]`     |
</details>

<details>
<summary>Source code links that could not be found(3)</summary>
    


|   index | package_name             | github_url                                    | github_exists   | parent                       |
|--------:|:-------------------------|:----------------------------------------------|:----------------|:-----------------------------|
|       1 | `concat-map@0.0.1`       | https://github.com/substack/node-concat-map   | False           | `['brace-expansion@1.1.11']` |
|       2 | `file-entry-cache@8.0.0` | https://github.com/jaredwray/file-entry-cache | False           | `[]`                         |
|       3 | `flat-cache@4.0.1`       | https://github.com/jaredwray/flat-cache       | False           | `[]`                         |
</details>

<details>
<summary>List of packages without provenance(157)</summary>
    


| package_name                                  | provenance_in_version   | parent                       |
|:----------------------------------------------|:------------------------|:-----------------------------|
| `@bcoe/v8-coverage@1.0.2`                     | False                   | `[]`                         |
| `@domenic/eslint-config@4.0.1`                | False                   | `[]`                         |
| `@esbuild/aix-ppc64@0.25.1`                   | False                   | `[]`                         |
| `@esbuild/android-arm64@0.25.1`               | False                   | `[]`                         |
| `@esbuild/android-arm@0.25.1`                 | False                   | `[]`                         |
| `@esbuild/android-x64@0.25.1`                 | False                   | `[]`                         |
| `@esbuild/darwin-arm64@0.25.1`                | False                   | `[]`                         |
| `@esbuild/darwin-x64@0.25.1`                  | False                   | `[]`                         |
| `@esbuild/freebsd-arm64@0.25.1`               | False                   | `[]`                         |
| `@esbuild/freebsd-x64@0.25.1`                 | False                   | `[]`                         |
| `@esbuild/linux-arm64@0.25.1`                 | False                   | `[]`                         |
| `@esbuild/linux-arm@0.25.1`                   | False                   | `[]`                         |
| `@esbuild/linux-ia32@0.25.1`                  | False                   | `[]`                         |
| `@esbuild/linux-loong64@0.25.1`               | False                   | `[]`                         |
| `@esbuild/linux-mips64el@0.25.1`              | False                   | `[]`                         |
| `@esbuild/linux-ppc64@0.25.1`                 | False                   | `[]`                         |
| `@esbuild/linux-riscv64@0.25.1`               | False                   | `[]`                         |
| `@esbuild/linux-s390x@0.25.1`                 | False                   | `[]`                         |
| `@esbuild/linux-x64@0.25.1`                   | False                   | `[]`                         |
| `@esbuild/netbsd-arm64@0.25.1`                | False                   | `[]`                         |
| `@esbuild/netbsd-x64@0.25.1`                  | False                   | `[]`                         |
| `@esbuild/openbsd-arm64@0.25.1`               | False                   | `[]`                         |
| `@esbuild/openbsd-x64@0.25.1`                 | False                   | `[]`                         |
| `@esbuild/sunos-x64@0.25.1`                   | False                   | `[]`                         |
| `@esbuild/win32-arm64@0.25.1`                 | False                   | `[]`                         |
| `@esbuild/win32-ia32@0.25.1`                  | False                   | `[]`                         |
| `@esbuild/win32-x64@0.25.1`                   | False                   | `[]`                         |
| `@eslint/js@9.22.0`                           | False                   | `['eslint@9.22.0']`          |
| `@humanfs/core@0.19.1`                        | False                   | `[]`                         |
| `@humanfs/node@0.16.6`                        | False                   | `[]`                         |
| `@humanwhocodes/module-importer@1.0.1`        | False                   | `[]`                         |
| `@humanwhocodes/retry@0.3.1`                  | False                   | `[]`                         |
| `@humanwhocodes/retry@0.4.2`                  | False                   | `[]`                         |
| `@isaacs/cliui@8.0.2`                         | False                   | `[]`                         |
| `@istanbuljs/schema@0.1.3`                    | False                   | `[]`                         |
| `@jridgewell/resolve-uri@3.1.2`               | False                   | `[]`                         |
| `@jridgewell/sourcemap-codec@1.5.0`           | False                   | `[]`                         |
| `@jridgewell/trace-mapping@0.3.25`            | False                   | `[]`                         |
| `@pkgjs/parseargs@0.11.0`                     | False                   | `[]`                         |
| `@types/estree@1.0.6`                         | False                   | `[]`                         |
| `@types/istanbul-lib-coverage@2.0.6`          | False                   | `[]`                         |
| `@types/json-schema@7.0.15`                   | False                   | `[]`                         |
| `acorn-jsx@5.3.2`                             | False                   | `[]`                         |
| `acorn@8.14.1`                                | False                   | `[]`                         |
| `ajv@6.12.6`                                  | False                   | `[]`                         |
| `ansi-regex@5.0.1`                            | False                   | `[]`                         |
| `ansi-regex@6.1.0`                            | False                   | `[]`                         |
| `ansi-styles@4.3.0`                           | False                   | `[]`                         |
| `ansi-styles@6.2.1`                           | False                   | `[]`                         |
| `argparse@2.0.1`                              | False                   | `[]`                         |
| `balanced-match@1.0.2`                        | False                   | `[]`                         |
| `benchmark@2.1.4`                             | False                   | `[]`                         |
| `brace-expansion@1.1.11`                      | False                   | `[]`                         |
| `brace-expansion@2.0.1`                       | False                   | `[]`                         |
| `c8@10.1.3`                                   | False                   | `[]`                         |
| `callsites@3.1.0`                             | False                   | `[]`                         |
| `chalk@4.1.2`                                 | False                   | `[]`                         |
| `cliui@8.0.1`                                 | False                   | `[]`                         |
| `color-convert@2.0.1`                         | False                   | `[]`                         |
| `color-name@1.1.4`                            | False                   | `[]`                         |
| `concat-map@0.0.1`                            | False                   | `['brace-expansion@1.1.11']` |
| `convert-source-map@2.0.0`                    | False                   | `[]`                         |
| `cross-spawn@7.0.6`                           | False                   | `[]`                         |
| `debug@4.4.0`                                 | False                   | `[]`                         |
| `deep-is@0.1.4`                               | False                   | `[]`                         |
| `eastasianwidth@0.2.0`                        | False                   | `[]`                         |
| `emoji-regex@8.0.0`                           | False                   | `[]`                         |
| `emoji-regex@9.2.2`                           | False                   | `[]`                         |
| `esbuild@0.25.1`                              | False                   | `[]`                         |
| `escalade@3.2.0`                              | False                   | `[]`                         |
| `escape-string-regexp@4.0.0`                  | False                   | `[]`                         |
| `eslint@9.22.0`                               | False                   | `[]`                         |
| `esquery@1.6.0`                               | False                   | `[]`                         |
| `esrecurse@4.3.0`                             | False                   | `[]`                         |
| `estraverse@5.3.0`                            | False                   | `[]`                         |
| `esutils@2.0.3`                               | False                   | `[]`                         |
| `fast-deep-equal@3.1.3`                       | False                   | `[]`                         |
| `fast-json-stable-stringify@2.1.0`            | False                   | `[]`                         |
| `fast-levenshtein@2.0.6`                      | False                   | `[]`                         |
| `file-entry-cache@8.0.0`                      | False                   | `[]`                         |
| `find-up@5.0.0`                               | False                   | `[]`                         |
| `flat-cache@4.0.1`                            | False                   | `[]`                         |
| `flatted@3.3.3`                               | False                   | `[]`                         |
| `foreground-child@3.3.1`                      | False                   | `[]`                         |
| `get-caller-file@2.0.5`                       | False                   | `[]`                         |
| `glob-parent@6.0.2`                           | False                   | `[]`                         |
| `glob@10.4.5`                                 | False                   | `[]`                         |
| `globals@14.0.0`                              | False                   | `[]`                         |
| `globals@16.0.0`                              | False                   | `[]`                         |
| `has-flag@4.0.0`                              | False                   | `[]`                         |
| `html-escaper@2.0.2`                          | False                   | `[]`                         |
| `ignore@5.3.2`                                | False                   | `[]`                         |
| `import-fresh@3.3.1`                          | False                   | `[]`                         |
| `imurmurhash@0.1.4`                           | False                   | `[]`                         |
| `is-extglob@2.1.1`                            | False                   | `[]`                         |
| `is-fullwidth-code-point@3.0.0`               | False                   | `[]`                         |
| `is-glob@4.0.3`                               | False                   | `[]`                         |
| `isexe@2.0.0`                                 | False                   | `[]`                         |
| `istanbul-lib-coverage@3.2.2`                 | False                   | `[]`                         |
| `istanbul-lib-report@3.0.1`                   | False                   | `[]`                         |
| `istanbul-reports@3.1.7`                      | False                   | `[]`                         |
| `jackspeak@3.4.3`                             | False                   | `[]`                         |
| `js-yaml@4.1.0`                               | False                   | `[]`                         |
| `json-buffer@3.0.1`                           | False                   | `['keyv@4.5.4']`             |
| `json-schema-traverse@0.4.1`                  | False                   | `[]`                         |
| `json-stable-stringify-without-jsonify@1.0.1` | False                   | `[]`                         |
| `keyv@4.5.4`                                  | False                   | `[]`                         |
| `levn@0.4.1`                                  | False                   | `[]`                         |
| `locate-path@6.0.0`                           | False                   | `[]`                         |
| `lodash.merge@4.6.2`                          | False                   | `[]`                         |
| `lodash@4.17.21`                              | False                   | `[]`                         |
| `lru-cache@10.4.3`                            | False                   | `[]`                         |
| `make-dir@4.0.0`                              | False                   | `[]`                         |
| `minimatch@3.1.2`                             | False                   | `[]`                         |
| `minimatch@9.0.5`                             | False                   | `[]`                         |
| `minipass@7.1.2`                              | False                   | `[]`                         |
| `ms@2.1.3`                                    | False                   | `[]`                         |
| `natural-compare@1.4.0`                       | False                   | `[]`                         |
| `optionator@0.9.4`                            | False                   | `[]`                         |
| `p-limit@3.1.0`                               | False                   | `[]`                         |
| `p-locate@5.0.0`                              | False                   | `[]`                         |
| `package-json-from-dist@1.0.1`                | False                   | `[]`                         |
| `parent-module@1.0.1`                         | False                   | `[]`                         |
| `path-exists@4.0.0`                           | False                   | `[]`                         |
| `path-key@3.1.1`                              | False                   | `[]`                         |
| `path-scurry@1.11.1`                          | False                   | `[]`                         |
| `platform@1.3.6`                              | False                   | `[]`                         |
| `prelude-ls@1.2.1`                            | False                   | `[]`                         |
| `prettier@2.8.8`                              | False                   | `[]`                         |
| `punycode@2.3.1`                              | False                   | `[]`                         |
| `require-directory@2.1.1`                     | False                   | `[]`                         |
| `resolve-from@4.0.0`                          | False                   | `[]`                         |
| `shebang-command@2.0.0`                       | False                   | `[]`                         |
| `shebang-regex@3.0.0`                         | False                   | `[]`                         |
| `signal-exit@4.1.0`                           | False                   | `[]`                         |
| `string-width@4.2.3`                          | False                   | `[]`                         |
| `string-width@5.1.2`                          | False                   | `[]`                         |
| `strip-ansi@6.0.1`                            | False                   | `[]`                         |
| `strip-ansi@7.1.0`                            | False                   | `[]`                         |
| `strip-json-comments@3.1.1`                   | False                   | `[]`                         |
| `supports-color@7.2.0`                        | False                   | `[]`                         |
| `test-exclude@7.0.1`                          | False                   | `[]`                         |
| `tr46@5.1.0`                                  | False                   | `[]`                         |
| `type-check@0.4.0`                            | False                   | `[]`                         |
| `uri-js@4.4.1`                                | False                   | `[]`                         |
| `v8-to-istanbul@9.3.0`                        | False                   | `[]`                         |
| `webidl-conversions@7.0.0`                    | False                   | `[]`                         |
| `webidl2@24.4.1`                              | False                   | `[]`                         |
| `webidl2js@18.0.0`                            | False                   | `[]`                         |
| `which@2.0.2`                                 | False                   | `[]`                         |
| `word-wrap@1.2.5`                             | False                   | `[]`                         |
| `wrap-ansi@7.0.0`                             | False                   | `[]`                         |
| `wrap-ansi@8.1.0`                             | False                   | `[]`                         |
| `y18n@5.0.8`                                  | False                   | `[]`                         |
| `yargs-parser@21.1.1`                         | False                   | `[]`                         |
| `yargs@17.7.2`                                | False                   | `[]`                         |
| `yocto-queue@0.1.0`                           | False                   | `[]`                         |
</details>

All packages have valid code signature.

All packages have code signature.

No deprecated package found.

<details>
<summary>List of aliased packages(3)</summary>
    


| package_name         | aliased_package_name   | parent   |
|:---------------------|:-----------------------|:---------|
| `string-width@4.2.3` | `string-width-cjs`     | `[]`     |
| `strip-ansi@6.0.1`   | `strip-ansi-cjs`       | `[]`     |
| `wrap-ansi@7.0.0`    | `wrap-ansi-cjs`        | `[]`     |
</details>

### Call to Action:

<details>
<summary>👻What do I do now? </summary>


For packages **without source code & accessible SHA/release tags**:

- **Why?** Missing or inaccessible source code makes it impossible to audit the package for security vulnerabilities or malicious code.

1. Pull Request to the maintainer of dependency, requesting correct repository metadata and proper versioning/tagging. 


For **deprecated** packages:

- **Why?** Deprecated packages may contain known security issues and are no longer maintained, putting your project at risk.

1. Confirm the maintainer's deprecation intention 
2. Check for not deprecated versions

For packages **without code signature**:

- **Why?** Code signatures help verify the authenticity and integrity of the package, ensuring it hasn't been tampered with.

1. Open an issue in the dependency's repository to request the inclusion of code signature in the CI/CD pipeline. 


For packages **with invalid code signature**:

- **Why?** Invalid signatures could indicate tampering or compromised build processes.

1. It's recommended to verify the code signature and contact the maintainer to fix the issue.

For packages **without provenance**:

- **Why?** Without provenance, there's no way to verify that the package was built from the claimed source code, making supply chain attacks possible.

1. Open an issue in the dependency's repository to request the inclusion of provenance and build attestation in the CI/CD pipeline.

For packages that are **aliased**:

- **Why?** Aliased packages may hide malicious dependencies under seemingly legitimate names.

1. Check the aliased package and its repository to verify the alias is not malicious.
</details>
---

Report created by [dirty-waters](https://github.com/chains-project/dirty-waters/).

Report created on 2025-05-13 00:34:38
- Tool version: 1dfb5543
- Project Name: jsdom/whatwg-url
- Project Version: 414f17a3459b0872baee7a2b77e23953b8a5ccd9
- Package Manager: npm
