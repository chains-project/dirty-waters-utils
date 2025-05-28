
# Software Supply Chain Report of paulmillr/readdirp - a124cce86eff988cec15215994b33bb79b5e7443

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
        

 ### Total packages in the supply chain: 80


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 2

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 0

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 0

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 77

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 0

:alien: Packages that are aliased (⚠️⚠️): 3


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(2)</summary>
    


| package_name                         | sha_exists   | tag_version   | is_sha   | sha   | tag_url   | message                           |   status_code_for_sha | parent   |
|:-------------------------------------|:-------------|:--------------|:---------|:------|:----------|:----------------------------------|----------------------:|:---------|
| `@types/istanbul-lib-coverage@2.0.6` | False        | `2.0.6`       | False    |       |           | Tag 2.0.6 not found in the repo   |                   404 | `[]`     |
| `@types/node@20.14.8`                | False        | `20.14.8`     | False    |       |           | Tag 20.14.8 not found in the repo |                   404 | `[]`     |
</details>
All analyzed packages have a source code repo.

<details>
<summary>List of packages without provenance(77)</summary>
    


| package_name                         | provenance_in_version   | parent   |
|:-------------------------------------|:------------------------|:---------|
| `@bcoe/v8-coverage@1.0.1`            | False                   | `[]`     |
| `@isaacs/cliui@8.0.2`                | False                   | `[]`     |
| `@istanbuljs/schema@0.1.3`           | False                   | `[]`     |
| `@jridgewell/resolve-uri@3.1.2`      | False                   | `[]`     |
| `@jridgewell/sourcemap-codec@1.5.0`  | False                   | `[]`     |
| `@jridgewell/trace-mapping@0.3.25`   | False                   | `[]`     |
| `@pkgjs/parseargs@0.11.0`            | False                   | `[]`     |
| `@types/istanbul-lib-coverage@2.0.6` | False                   | `[]`     |
| `@types/node@20.14.8`                | False                   | `[]`     |
| `ansi-regex@5.0.1`                   | False                   | `[]`     |
| `ansi-regex@6.1.0`                   | False                   | `[]`     |
| `ansi-styles@4.3.0`                  | False                   | `[]`     |
| `ansi-styles@6.2.1`                  | False                   | `[]`     |
| `assertion-error@1.1.0`              | False                   | `[]`     |
| `balanced-match@1.0.2`               | False                   | `[]`     |
| `brace-expansion@2.0.1`              | False                   | `[]`     |
| `c8@10.1.3`                          | False                   | `[]`     |
| `chai-subset@1.6.0`                  | False                   | `[]`     |
| `chai@4.3.4`                         | False                   | `[]`     |
| `check-error@1.0.3`                  | False                   | `[]`     |
| `cliui@8.0.1`                        | False                   | `[]`     |
| `color-convert@2.0.1`                | False                   | `[]`     |
| `color-name@1.1.4`                   | False                   | `[]`     |
| `convert-source-map@2.0.0`           | False                   | `[]`     |
| `cross-spawn@7.0.6`                  | False                   | `[]`     |
| `deep-eql@3.0.1`                     | False                   | `[]`     |
| `eastasianwidth@0.2.0`               | False                   | `[]`     |
| `emoji-regex@8.0.0`                  | False                   | `[]`     |
| `emoji-regex@9.2.2`                  | False                   | `[]`     |
| `escalade@3.2.0`                     | False                   | `[]`     |
| `find-up@5.0.0`                      | False                   | `[]`     |
| `foreground-child@3.3.0`             | False                   | `[]`     |
| `get-caller-file@2.0.5`              | False                   | `[]`     |
| `get-func-name@2.0.2`                | False                   | `[]`     |
| `glob@10.4.5`                        | False                   | `[]`     |
| `has-flag@4.0.0`                     | False                   | `[]`     |
| `html-escaper@2.0.2`                 | False                   | `[]`     |
| `is-fullwidth-code-point@3.0.0`      | False                   | `[]`     |
| `isexe@2.0.0`                        | False                   | `[]`     |
| `istanbul-lib-coverage@3.2.2`        | False                   | `[]`     |
| `istanbul-lib-report@3.0.1`          | False                   | `[]`     |
| `istanbul-reports@3.1.7`             | False                   | `[]`     |
| `jackspeak@3.4.3`                    | False                   | `[]`     |
| `locate-path@6.0.0`                  | False                   | `[]`     |
| `lru-cache@10.4.3`                   | False                   | `[]`     |
| `make-dir@4.0.0`                     | False                   | `[]`     |
| `minimatch@9.0.5`                    | False                   | `[]`     |
| `minipass@7.1.2`                     | False                   | `[]`     |
| `p-limit@3.1.0`                      | False                   | `[]`     |
| `p-locate@5.0.0`                     | False                   | `[]`     |
| `package-json-from-dist@1.0.1`       | False                   | `[]`     |
| `path-exists@4.0.0`                  | False                   | `[]`     |
| `path-key@3.1.1`                     | False                   | `[]`     |
| `path-scurry@1.11.1`                 | False                   | `[]`     |
| `pathval@1.1.1`                      | False                   | `[]`     |
| `prettier@3.1.1`                     | False                   | `[]`     |
| `require-directory@2.1.1`            | False                   | `[]`     |
| `shebang-command@2.0.0`              | False                   | `[]`     |
| `shebang-regex@3.0.0`                | False                   | `[]`     |
| `signal-exit@4.1.0`                  | False                   | `[]`     |
| `string-width@4.2.3`                 | False                   | `[]`     |
| `string-width@5.1.2`                 | False                   | `[]`     |
| `strip-ansi@6.0.1`                   | False                   | `[]`     |
| `strip-ansi@7.1.0`                   | False                   | `[]`     |
| `supports-color@7.2.0`               | False                   | `[]`     |
| `test-exclude@7.0.1`                 | False                   | `[]`     |
| `type-detect@4.1.0`                  | False                   | `[]`     |
| `typescript@5.5.2`                   | False                   | `[]`     |
| `undici-types@5.26.5`                | False                   | `[]`     |
| `v8-to-istanbul@9.3.0`               | False                   | `[]`     |
| `which@2.0.2`                        | False                   | `[]`     |
| `wrap-ansi@7.0.0`                    | False                   | `[]`     |
| `wrap-ansi@8.1.0`                    | False                   | `[]`     |
| `y18n@5.0.8`                         | False                   | `[]`     |
| `yargs-parser@21.1.1`                | False                   | `[]`     |
| `yargs@17.7.2`                       | False                   | `[]`     |
| `yocto-queue@0.1.0`                  | False                   | `[]`     |
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

Report created on 2025-05-13 00:50:32
- Tool version: 1dfb5543
- Project Name: paulmillr/readdirp
- Project Version: a124cce86eff988cec15215994b33bb79b5e7443
- Package Manager: npm
