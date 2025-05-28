
# Software Supply Chain Report of microsoft/TypeScript - 68cead182cc24afdc3f1ce7c8ff5853aba14b65a

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
        

 ### Total packages in the supply chain: 365


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 13

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 2

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 3

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 333

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 2

:alien: Packages that are aliased (⚠️⚠️): 3


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(13)</summary>
    


| package_name                         | sha_exists   | tag_version   | is_sha   | sha   | tag_url   | message                           |   status_code_for_sha | parent                                      |
|:-------------------------------------|:-------------|:--------------|:---------|:------|:----------|:----------------------------------|----------------------:|:--------------------------------------------|
| `@types/chai@4.3.20`                 | False        | `4.3.20`      | False    |       |           | Tag 4.3.20 not found in the repo  |                   404 | `[]`                                        |
| `@types/diff@5.2.3`                  | False        | `5.2.3`       | False    |       |           | Tag 5.2.3 not found in the repo   |                   404 | `[]`                                        |
| `@types/estree@1.0.6`                | False        | `1.0.6`       | False    |       |           | Tag 1.0.6 not found in the repo   |                   404 | `[]`                                        |
| `@types/istanbul-lib-coverage@2.0.6` | False        | `2.0.6`       | False    |       |           | Tag 2.0.6 not found in the repo   |                   404 | `[]`                                        |
| `@types/json-schema@7.0.15`          | False        | `7.0.15`      | False    |       |           | Tag 7.0.15 not found in the repo  |                   404 | `[]`                                        |
| `@types/minimist@1.2.5`              | False        | `1.2.5`       | False    |       |           | Tag 1.2.5 not found in the repo   |                   404 | `[]`                                        |
| `@types/mocha@10.0.10`               | False        | `10.0.10`     | False    |       |           | Tag 10.0.10 not found in the repo |                   404 | `[]`                                        |
| `@types/ms@0.7.34`                   | False        | `0.7.34`      | False    |       |           | Tag 0.7.34 not found in the repo  |                   404 | `[]`                                        |
| `@types/node@22.10.2`                | False        | `22.10.2`     | False    |       |           | Tag 22.10.2 not found in the repo |                   404 | `[]`                                        |
| `@types/source-map-support@0.5.10`   | False        | `0.5.10`      | False    |       |           | Tag 0.5.10 not found in the repo  |                   404 | `[]`                                        |
| `@types/which@3.0.4`                 | False        | `3.0.4`       | False    |       |           | Tag 3.0.4 not found in the repo   |                   404 | `[]`                                        |
| `keyv@4.5.4`                         | False        | `4.5.4`       | False    |       |           | Tag 4.5.4 not found in the repo   |                   404 | `[]`                                        |
| `lodash.merge@4.6.2`                 | False        | `4.6.2`       | False    |       |           | Tag 4.6.2 not found in the repo   |                   404 | `['@typescript-eslint/rule-tester@8.18.1']` |
</details>

<details>
<summary>Source code links that could not be found(5)</summary>
    


|   index | package_name             | github_url                                    | github_exists   | parent                       |
|--------:|:-------------------------|:----------------------------------------------|:----------------|:-----------------------------|
|       1 | `lz-utils@2.1.0`         | No_repo_info_found                            |                 | `[]`                         |
|       2 | `monocart-locator@1.0.2` | No_repo_info_found                            |                 | `[]`                         |
|       3 | `concat-map@0.0.1`       | https://github.com/substack/node-concat-map   | False           | `['brace-expansion@1.1.11']` |
|       4 | `file-entry-cache@8.0.0` | https://github.com/jaredwray/file-entry-cache | False           | `[]`                         |
|       5 | `flat-cache@4.0.1`       | https://github.com/jaredwray/flat-cache       | False           | `[]`                         |
</details>

<details>
<summary>List of packages without provenance(333)</summary>
    


| package_name                                  | provenance_in_version   | parent                                                                                                                                                                                                        |
|:----------------------------------------------|:------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@bcoe/v8-coverage@1.0.1`                     | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/darwin-arm64@0.47.6`                 | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/darwin-x64@0.47.6`                   | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/formatter@0.4.1`                     | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/linux-arm64-glibc@0.47.6`            | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/linux-arm64-musl@0.47.6`             | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/linux-riscv64-glibc@0.47.6`          | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/linux-x64-glibc@0.47.6`              | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/linux-x64-musl@0.47.6`               | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/typescript@0.93.3`                   | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/win32-arm64@0.47.6`                  | False                   | `[]`                                                                                                                                                                                                          |
| `@dprint/win32-x64@0.47.6`                    | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/aix-ppc64@0.24.0`                   | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/android-arm64@0.24.0`               | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/android-arm@0.24.0`                 | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/android-x64@0.24.0`                 | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/darwin-arm64@0.24.0`                | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/darwin-x64@0.24.0`                  | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/freebsd-arm64@0.24.0`               | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/freebsd-x64@0.24.0`                 | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/linux-arm64@0.24.0`                 | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/linux-arm@0.24.0`                   | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/linux-ia32@0.24.0`                  | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/linux-loong64@0.24.0`               | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/linux-mips64el@0.24.0`              | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/linux-ppc64@0.24.0`                 | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/linux-riscv64@0.24.0`               | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/linux-s390x@0.24.0`                 | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/linux-x64@0.24.0`                   | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/netbsd-x64@0.24.0`                  | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/openbsd-arm64@0.24.0`               | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/openbsd-x64@0.24.0`                 | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/sunos-x64@0.24.0`                   | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/win32-arm64@0.24.0`                 | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/win32-ia32@0.24.0`                  | False                   | `[]`                                                                                                                                                                                                          |
| `@esbuild/win32-x64@0.24.0`                   | False                   | `[]`                                                                                                                                                                                                          |
| `@esfx/cancelable@1.0.0`                      | False                   | `[]`                                                                                                                                                                                                          |
| `@esfx/canceltoken@1.0.0`                     | False                   | `[]`                                                                                                                                                                                                          |
| `@esfx/disposable@1.0.0`                      | False                   | `[]`                                                                                                                                                                                                          |
| `@eslint/js@9.17.0`                           | False                   | `['eslint@9.17.0']`                                                                                                                                                                                           |
| `@humanfs/core@0.19.1`                        | False                   | `[]`                                                                                                                                                                                                          |
| `@humanfs/node@0.16.6`                        | False                   | `[]`                                                                                                                                                                                                          |
| `@humanwhocodes/module-importer@1.0.1`        | False                   | `[]`                                                                                                                                                                                                          |
| `@humanwhocodes/retry@0.3.1`                  | False                   | `[]`                                                                                                                                                                                                          |
| `@humanwhocodes/retry@0.4.1`                  | False                   | `[]`                                                                                                                                                                                                          |
| `@isaacs/cliui@8.0.2`                         | False                   | `[]`                                                                                                                                                                                                          |
| `@istanbuljs/schema@0.1.3`                    | False                   | `[]`                                                                                                                                                                                                          |
| `@jridgewell/resolve-uri@3.1.2`               | False                   | `[]`                                                                                                                                                                                                          |
| `@jridgewell/sourcemap-codec@1.5.0`           | False                   | `[]`                                                                                                                                                                                                          |
| `@jridgewell/trace-mapping@0.3.25`            | False                   | `[]`                                                                                                                                                                                                          |
| `@nodelib/fs.scandir@2.1.5`                   | False                   | `['@nodelib/fs.walk@1.2.8']`                                                                                                                                                                                  |
| `@nodelib/fs.stat@2.0.5`                      | False                   | `['@nodelib/fs.scandir@2.1.5']`                                                                                                                                                                               |
| `@nodelib/fs.walk@1.2.8`                      | False                   | `['knip@5.41.0']`                                                                                                                                                                                             |
| `@pkgjs/parseargs@0.11.0`                     | False                   | `[]`                                                                                                                                                                                                          |
| `@snyk/github-codeowners@1.1.0`               | False                   | `['knip@5.41.0']`                                                                                                                                                                                             |
| `@types/chai@4.3.20`                          | False                   | `[]`                                                                                                                                                                                                          |
| `@types/diff@5.2.3`                           | False                   | `[]`                                                                                                                                                                                                          |
| `@types/estree@1.0.6`                         | False                   | `[]`                                                                                                                                                                                                          |
| `@types/istanbul-lib-coverage@2.0.6`          | False                   | `[]`                                                                                                                                                                                                          |
| `@types/json-schema@7.0.15`                   | False                   | `[]`                                                                                                                                                                                                          |
| `@types/minimist@1.2.5`                       | False                   | `[]`                                                                                                                                                                                                          |
| `@types/mocha@10.0.10`                        | False                   | `[]`                                                                                                                                                                                                          |
| `@types/ms@0.7.34`                            | False                   | `[]`                                                                                                                                                                                                          |
| `@types/node@22.10.2`                         | False                   | `[]`                                                                                                                                                                                                          |
| `@types/source-map-support@0.5.10`            | False                   | `[]`                                                                                                                                                                                                          |
| `@types/which@3.0.4`                          | False                   | `[]`                                                                                                                                                                                                          |
| `@typescript-eslint/eslint-plugin@8.18.1`     | False                   | `['typescript-eslint@8.18.1']`                                                                                                                                                                                |
| `@typescript-eslint/parser@8.18.1`            | False                   | `['typescript-eslint@8.18.1']`                                                                                                                                                                                |
| `@typescript-eslint/rule-tester@8.18.1`       | False                   | `[]`                                                                                                                                                                                                          |
| `@typescript-eslint/scope-manager@8.18.1`     | False                   | `['@typescript-eslint/parser@8.18.1', '@typescript-eslint/utils@8.18.1', '@typescript-eslint/eslint-plugin@8.18.1']`                                                                                          |
| `@typescript-eslint/type-utils@8.18.1`        | False                   | `['@typescript-eslint/eslint-plugin@8.18.1']`                                                                                                                                                                 |
| `@typescript-eslint/types@8.18.1`             | False                   | `['@typescript-eslint/parser@8.18.1', '@typescript-eslint/scope-manager@8.18.1', '@typescript-eslint/typescript-estree@8.18.1', '@typescript-eslint/visitor-keys@8.18.1', '@typescript-eslint/utils@8.18.1']` |
| `@typescript-eslint/typescript-estree@8.18.1` | False                   | `['@typescript-eslint/rule-tester@8.18.1', '@typescript-eslint/parser@8.18.1', '@typescript-eslint/type-utils@8.18.1', '@typescript-eslint/utils@8.18.1']`                                                    |
| `@typescript-eslint/utils@8.18.1`             | False                   | `['@typescript-eslint/rule-tester@8.18.1', '@typescript-eslint/type-utils@8.18.1', 'typescript-eslint@8.18.1', '@typescript-eslint/eslint-plugin@8.18.1']`                                                    |
| `@typescript-eslint/visitor-keys@8.18.1`      | False                   | `['@typescript-eslint/parser@8.18.1', '@typescript-eslint/scope-manager@8.18.1', '@typescript-eslint/typescript-estree@8.18.1', '@typescript-eslint/eslint-plugin@8.18.1']`                                   |
| `acorn-jsx@5.3.2`                             | False                   | `[]`                                                                                                                                                                                                          |
| `acorn-loose@8.4.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `acorn-walk@8.3.4`                            | False                   | `[]`                                                                                                                                                                                                          |
| `acorn@8.14.0`                                | False                   | `[]`                                                                                                                                                                                                          |
| `aggregate-error@3.1.0`                       | False                   | `[]`                                                                                                                                                                                                          |
| `ajv@6.12.6`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `ansi-colors@4.1.3`                           | False                   | `[]`                                                                                                                                                                                                          |
| `ansi-regex@5.0.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `ansi-regex@6.1.0`                            | False                   | `[]`                                                                                                                                                                                                          |
| `ansi-styles@3.2.1`                           | False                   | `[]`                                                                                                                                                                                                          |
| `ansi-styles@4.3.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `ansi-styles@6.2.1`                           | False                   | `[]`                                                                                                                                                                                                          |
| `anymatch@3.1.3`                              | False                   | `[]`                                                                                                                                                                                                          |
| `argparse@2.0.1`                              | False                   | `[]`                                                                                                                                                                                                          |
| `array-back@4.0.2`                            | False                   | `[]`                                                                                                                                                                                                          |
| `assertion-error@1.1.0`                       | False                   | `[]`                                                                                                                                                                                                          |
| `azure-devops-node-api@14.1.0`                | False                   | `[]`                                                                                                                                                                                                          |
| `balanced-match@1.0.2`                        | False                   | `[]`                                                                                                                                                                                                          |
| `before-after-hook@3.0.2`                     | False                   | `[]`                                                                                                                                                                                                          |
| `binary-extensions@2.3.0`                     | False                   | `[]`                                                                                                                                                                                                          |
| `brace-expansion@1.1.11`                      | False                   | `[]`                                                                                                                                                                                                          |
| `brace-expansion@2.0.1`                       | False                   | `[]`                                                                                                                                                                                                          |
| `braces@3.0.3`                                | False                   | `[]`                                                                                                                                                                                                          |
| `browser-stdout@1.3.1`                        | False                   | `[]`                                                                                                                                                                                                          |
| `buffer-from@1.1.2`                           | False                   | `[]`                                                                                                                                                                                                          |
| `c8@10.1.3`                                   | False                   | `[]`                                                                                                                                                                                                          |
| `call-bind-apply-helpers@1.0.1`               | False                   | `[]`                                                                                                                                                                                                          |
| `call-bound@1.0.3`                            | False                   | `[]`                                                                                                                                                                                                          |
| `callsites@3.1.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `camelcase@6.3.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `chai@4.5.0`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `chalk@2.4.2`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `chalk@4.1.2`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `check-error@1.0.3`                           | False                   | `[]`                                                                                                                                                                                                          |
| `clean-stack@2.2.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `cliui@7.0.4`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `cliui@8.0.1`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `clone@1.0.4`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `color-convert@1.9.3`                         | False                   | `[]`                                                                                                                                                                                                          |
| `color-convert@2.0.1`                         | False                   | `[]`                                                                                                                                                                                                          |
| `color-name@1.1.3`                            | False                   | `['color-convert@1.9.3']`                                                                                                                                                                                     |
| `color-name@1.1.4`                            | False                   | `[]`                                                                                                                                                                                                          |
| `command-line-usage@6.1.3`                    | False                   | `[]`                                                                                                                                                                                                          |
| `commander@12.1.0`                            | False                   | `[]`                                                                                                                                                                                                          |
| `commander@4.1.1`                             | False                   | `[]`                                                                                                                                                                                                          |
| `comment-parser@1.4.1`                        | False                   | `[]`                                                                                                                                                                                                          |
| `concat-map@0.0.1`                            | False                   | `['brace-expansion@1.1.11']`                                                                                                                                                                                  |
| `console-grid@2.2.2`                          | False                   | `[]`                                                                                                                                                                                                          |
| `convert-source-map@2.0.0`                    | False                   | `[]`                                                                                                                                                                                                          |
| `cross-spawn@7.0.6`                           | False                   | `[]`                                                                                                                                                                                                          |
| `debug@4.4.0`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `decamelize@4.0.0`                            | False                   | `[]`                                                                                                                                                                                                          |
| `deep-eql@4.1.4`                              | False                   | `[]`                                                                                                                                                                                                          |
| `deep-extend@0.6.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `deep-is@0.1.4`                               | False                   | `[]`                                                                                                                                                                                                          |
| `defaults@1.0.4`                              | False                   | `[]`                                                                                                                                                                                                          |
| `des.js@1.1.0`                                | False                   | `[]`                                                                                                                                                                                                          |
| `diff@5.2.0`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `dprint@0.47.6`                               | False                   | `[]`                                                                                                                                                                                                          |
| `dunder-proto@1.0.1`                          | False                   | `[]`                                                                                                                                                                                                          |
| `eastasianwidth@0.2.0`                        | False                   | `[]`                                                                                                                                                                                                          |
| `easy-table@1.2.0`                            | False                   | `['knip@5.41.0']`                                                                                                                                                                                             |
| `eight-colors@1.3.1`                          | False                   | `[]`                                                                                                                                                                                                          |
| `emoji-regex@8.0.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `emoji-regex@9.2.2`                           | False                   | `[]`                                                                                                                                                                                                          |
| `enhanced-resolve@5.17.1`                     | False                   | `[]`                                                                                                                                                                                                          |
| `es-define-property@1.0.1`                    | False                   | `[]`                                                                                                                                                                                                          |
| `es-errors@1.3.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `es-object-atoms@1.0.0`                       | False                   | `[]`                                                                                                                                                                                                          |
| `esbuild@0.24.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `escalade@3.2.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `escape-string-regexp@1.0.5`                  | False                   | `[]`                                                                                                                                                                                                          |
| `escape-string-regexp@4.0.0`                  | False                   | `[]`                                                                                                                                                                                                          |
| `eslint-formatter-autolinkable-stylish@1.4.0` | False                   | `[]`                                                                                                                                                                                                          |
| `eslint-plugin-regexp@2.7.0`                  | False                   | `[]`                                                                                                                                                                                                          |
| `eslint@9.17.0`                               | False                   | `[]`                                                                                                                                                                                                          |
| `esquery@1.6.0`                               | False                   | `[]`                                                                                                                                                                                                          |
| `esrecurse@4.3.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `estraverse@5.3.0`                            | False                   | `[]`                                                                                                                                                                                                          |
| `esutils@2.0.3`                               | False                   | `[]`                                                                                                                                                                                                          |
| `fast-deep-equal@3.1.3`                       | False                   | `[]`                                                                                                                                                                                                          |
| `fast-glob@3.3.2`                             | False                   | `[]`                                                                                                                                                                                                          |
| `fast-json-stable-stringify@2.1.0`            | False                   | `[]`                                                                                                                                                                                                          |
| `fast-levenshtein@2.0.6`                      | False                   | `[]`                                                                                                                                                                                                          |
| `fast-xml-parser@4.5.1`                       | False                   | `[]`                                                                                                                                                                                                          |
| `fastest-levenshtein@1.0.16`                  | False                   | `[]`                                                                                                                                                                                                          |
| `fastq@1.17.1`                                | False                   | `[]`                                                                                                                                                                                                          |
| `file-entry-cache@8.0.0`                      | False                   | `[]`                                                                                                                                                                                                          |
| `fill-range@7.1.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `find-up@5.0.0`                               | False                   | `[]`                                                                                                                                                                                                          |
| `flat-cache@4.0.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `flat@5.0.2`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `flatted@3.3.2`                               | False                   | `[]`                                                                                                                                                                                                          |
| `foreground-child@3.3.0`                      | False                   | `[]`                                                                                                                                                                                                          |
| `fs.realpath@1.0.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `fsevents@2.3.2`                              | False                   | `[]`                                                                                                                                                                                                          |
| `fsevents@2.3.3`                              | False                   | `[]`                                                                                                                                                                                                          |
| `function-bind@1.1.2`                         | False                   | `[]`                                                                                                                                                                                                          |
| `get-caller-file@2.0.5`                       | False                   | `[]`                                                                                                                                                                                                          |
| `get-func-name@2.0.2`                         | False                   | `[]`                                                                                                                                                                                                          |
| `get-intrinsic@1.2.6`                         | False                   | `[]`                                                                                                                                                                                                          |
| `glob-parent@5.1.2`                           | False                   | `[]`                                                                                                                                                                                                          |
| `glob-parent@6.0.2`                           | False                   | `[]`                                                                                                                                                                                                          |
| `glob@10.4.5`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `glob@8.1.0`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `globals@14.0.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `globals@15.13.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `gopd@1.2.0`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `graceful-fs@4.2.11`                          | False                   | `[]`                                                                                                                                                                                                          |
| `graphemer@1.4.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `has-flag@3.0.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `has-flag@4.0.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `has-symbols@1.1.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `hasown@2.0.2`                                | False                   | `[]`                                                                                                                                                                                                          |
| `he@1.2.0`                                    | False                   | `[]`                                                                                                                                                                                                          |
| `html-escaper@2.0.2`                          | False                   | `[]`                                                                                                                                                                                                          |
| `ignore@5.3.2`                                | False                   | `[]`                                                                                                                                                                                                          |
| `import-fresh@3.3.0`                          | False                   | `[]`                                                                                                                                                                                                          |
| `imurmurhash@0.1.4`                           | False                   | `[]`                                                                                                                                                                                                          |
| `indent-string@4.0.0`                         | False                   | `[]`                                                                                                                                                                                                          |
| `inflight@1.0.6`                              | False                   | `[]`                                                                                                                                                                                                          |
| `inherits@2.0.4`                              | False                   | `[]`                                                                                                                                                                                                          |
| `irregular-plurals@3.5.0`                     | False                   | `[]`                                                                                                                                                                                                          |
| `is-binary-path@2.1.0`                        | False                   | `[]`                                                                                                                                                                                                          |
| `is-extglob@2.1.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `is-fullwidth-code-point@3.0.0`               | False                   | `[]`                                                                                                                                                                                                          |
| `is-glob@4.0.3`                               | False                   | `[]`                                                                                                                                                                                                          |
| `is-number@7.0.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `is-plain-obj@2.1.0`                          | False                   | `[]`                                                                                                                                                                                                          |
| `is-unicode-supported@0.1.0`                  | False                   | `[]`                                                                                                                                                                                                          |
| `isexe@2.0.0`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `istanbul-lib-coverage@3.2.2`                 | False                   | `[]`                                                                                                                                                                                                          |
| `istanbul-lib-report@3.0.1`                   | False                   | `[]`                                                                                                                                                                                                          |
| `istanbul-reports@3.1.7`                      | False                   | `[]`                                                                                                                                                                                                          |
| `jackspeak@3.4.3`                             | False                   | `[]`                                                                                                                                                                                                          |
| `jiti@2.4.2`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `js-md4@0.3.2`                                | False                   | `[]`                                                                                                                                                                                                          |
| `js-yaml@4.1.0`                               | False                   | `[]`                                                                                                                                                                                                          |
| `jsdoc-type-pratt-parser@4.1.0`               | False                   | `[]`                                                                                                                                                                                                          |
| `json-buffer@3.0.1`                           | False                   | `['keyv@4.5.4']`                                                                                                                                                                                              |
| `json-schema-traverse@0.4.1`                  | False                   | `[]`                                                                                                                                                                                                          |
| `json-stable-stringify-without-jsonify@1.0.1` | False                   | `[]`                                                                                                                                                                                                          |
| `jsonc-parser@3.3.1`                          | False                   | `[]`                                                                                                                                                                                                          |
| `keyv@4.5.4`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `knip@5.41.0`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `levn@0.4.1`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `locate-path@6.0.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `lodash.merge@4.6.2`                          | False                   | `['@typescript-eslint/rule-tester@8.18.1']`                                                                                                                                                                   |
| `log-symbols@4.1.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `loupe@2.3.7`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `lru-cache@10.4.3`                            | False                   | `[]`                                                                                                                                                                                                          |
| `lz-utils@2.1.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `make-dir@4.0.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `math-intrinsics@1.0.0`                       | False                   | `[]`                                                                                                                                                                                                          |
| `merge2@1.4.1`                                | False                   | `[]`                                                                                                                                                                                                          |
| `micromatch@4.0.8`                            | False                   | `[]`                                                                                                                                                                                                          |
| `minimalistic-assert@1.0.1`                   | False                   | `[]`                                                                                                                                                                                                          |
| `minimatch@3.1.2`                             | False                   | `[]`                                                                                                                                                                                                          |
| `minimatch@5.1.6`                             | False                   | `[]`                                                                                                                                                                                                          |
| `minimatch@9.0.5`                             | False                   | `[]`                                                                                                                                                                                                          |
| `minimist@1.2.8`                              | False                   | `[]`                                                                                                                                                                                                          |
| `minipass@7.1.2`                              | False                   | `[]`                                                                                                                                                                                                          |
| `mocha-fivemat-progress-reporter@0.1.0`       | False                   | `[]`                                                                                                                                                                                                          |
| `monocart-coverage-reports@2.11.4`            | False                   | `[]`                                                                                                                                                                                                          |
| `monocart-locator@1.0.2`                      | False                   | `[]`                                                                                                                                                                                                          |
| `ms@2.1.3`                                    | False                   | `[]`                                                                                                                                                                                                          |
| `natural-compare@1.4.0`                       | False                   | `[]`                                                                                                                                                                                                          |
| `normalize-path@3.0.0`                        | False                   | `[]`                                                                                                                                                                                                          |
| `object-inspect@1.13.3`                       | False                   | `[]`                                                                                                                                                                                                          |
| `once@1.4.0`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `optionator@0.9.4`                            | False                   | `[]`                                                                                                                                                                                                          |
| `p-limit@3.1.0`                               | False                   | `[]`                                                                                                                                                                                                          |
| `p-locate@5.0.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `p-map@4.0.0`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `package-json-from-dist@1.0.1`                | False                   | `[]`                                                                                                                                                                                                          |
| `parent-module@1.0.1`                         | False                   | `[]`                                                                                                                                                                                                          |
| `parse-ms@3.0.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `parse-ms@4.0.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `path-exists@4.0.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `path-key@3.1.1`                              | False                   | `[]`                                                                                                                                                                                                          |
| `path-scurry@1.11.1`                          | False                   | `[]`                                                                                                                                                                                                          |
| `pathval@1.1.1`                               | False                   | `[]`                                                                                                                                                                                                          |
| `picocolors@1.1.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `picomatch@2.3.1`                             | False                   | `[]`                                                                                                                                                                                                          |
| `picomatch@4.0.2`                             | False                   | `[]`                                                                                                                                                                                                          |
| `plur@4.0.0`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `prelude-ls@1.2.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `pretty-ms@8.0.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `pretty-ms@9.2.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `punycode@2.3.1`                              | False                   | `[]`                                                                                                                                                                                                          |
| `qs@6.13.1`                                   | False                   | `[]`                                                                                                                                                                                                          |
| `queue-microtask@1.2.3`                       | False                   | `[]`                                                                                                                                                                                                          |
| `randombytes@2.1.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `readdirp@3.6.0`                              | False                   | `[]`                                                                                                                                                                                                          |
| `reduce-flatten@2.0.0`                        | False                   | `[]`                                                                                                                                                                                                          |
| `refa@0.12.1`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `regexp-ast-analysis@0.7.1`                   | False                   | `[]`                                                                                                                                                                                                          |
| `require-directory@2.1.1`                     | False                   | `[]`                                                                                                                                                                                                          |
| `resolve-from@4.0.0`                          | False                   | `[]`                                                                                                                                                                                                          |
| `reusify@1.0.4`                               | False                   | `[]`                                                                                                                                                                                                          |
| `run-parallel@1.2.0`                          | False                   | `[]`                                                                                                                                                                                                          |
| `safe-buffer@5.2.1`                           | False                   | `[]`                                                                                                                                                                                                          |
| `scslre@0.3.0`                                | False                   | `[]`                                                                                                                                                                                                          |
| `serialize-javascript@6.0.2`                  | False                   | `[]`                                                                                                                                                                                                          |
| `shebang-command@2.0.0`                       | False                   | `[]`                                                                                                                                                                                                          |
| `shebang-regex@3.0.0`                         | False                   | `[]`                                                                                                                                                                                                          |
| `side-channel-list@1.0.0`                     | False                   | `[]`                                                                                                                                                                                                          |
| `side-channel-map@1.0.1`                      | False                   | `[]`                                                                                                                                                                                                          |
| `side-channel-weakmap@1.0.2`                  | False                   | `[]`                                                                                                                                                                                                          |
| `side-channel@1.1.0`                          | False                   | `[]`                                                                                                                                                                                                          |
| `signal-exit@4.1.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `smol-toml@1.3.1`                             | False                   | `[]`                                                                                                                                                                                                          |
| `source-map-support@0.5.21`                   | False                   | `[]`                                                                                                                                                                                                          |
| `source-map@0.6.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `string-width@4.2.3`                          | False                   | `[]`                                                                                                                                                                                                          |
| `string-width@5.1.2`                          | False                   | `[]`                                                                                                                                                                                                          |
| `strip-ansi@6.0.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `strip-ansi@7.1.0`                            | False                   | `[]`                                                                                                                                                                                                          |
| `strip-json-comments@3.1.1`                   | False                   | `[]`                                                                                                                                                                                                          |
| `strip-json-comments@5.0.1`                   | False                   | `['knip@5.41.0']`                                                                                                                                                                                             |
| `strnum@1.0.5`                                | False                   | `[]`                                                                                                                                                                                                          |
| `summary@2.1.0`                               | False                   | `['knip@5.41.0']`                                                                                                                                                                                             |
| `supports-color@5.5.0`                        | False                   | `[]`                                                                                                                                                                                                          |
| `supports-color@7.2.0`                        | False                   | `[]`                                                                                                                                                                                                          |
| `supports-color@8.1.1`                        | False                   | `[]`                                                                                                                                                                                                          |
| `table-layout@1.0.2`                          | False                   | `[]`                                                                                                                                                                                                          |
| `tapable@2.2.1`                               | False                   | `[]`                                                                                                                                                                                                          |
| `test-exclude@7.0.1`                          | False                   | `[]`                                                                                                                                                                                                          |
| `to-regex-range@5.0.1`                        | False                   | `[]`                                                                                                                                                                                                          |
| `tslib@2.8.1`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `tunnel@0.0.6`                                | False                   | `['typed-rest-client@2.1.0', 'azure-devops-node-api@14.1.0']`                                                                                                                                                 |
| `type-check@0.4.0`                            | False                   | `[]`                                                                                                                                                                                                          |
| `type-detect@4.1.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `typed-rest-client@2.1.0`                     | False                   | `['azure-devops-node-api@14.1.0']`                                                                                                                                                                            |
| `typescript-eslint@8.18.1`                    | False                   | `[]`                                                                                                                                                                                                          |
| `typescript@5.7.2`                            | False                   | `[]`                                                                                                                                                                                                          |
| `typical@5.2.0`                               | False                   | `[]`                                                                                                                                                                                                          |
| `underscore@1.13.7`                           | False                   | `[]`                                                                                                                                                                                                          |
| `undici-types@6.20.0`                         | False                   | `[]`                                                                                                                                                                                                          |
| `universal-user-agent@7.0.2`                  | False                   | `[]`                                                                                                                                                                                                          |
| `uri-js@4.4.1`                                | False                   | `[]`                                                                                                                                                                                                          |
| `v8-to-istanbul@9.3.0`                        | False                   | `[]`                                                                                                                                                                                                          |
| `wcwidth@1.0.1`                               | False                   | `[]`                                                                                                                                                                                                          |
| `which@2.0.2`                                 | False                   | `[]`                                                                                                                                                                                                          |
| `word-wrap@1.2.5`                             | False                   | `[]`                                                                                                                                                                                                          |
| `wordwrapjs@4.0.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `workerpool@6.5.1`                            | False                   | `[]`                                                                                                                                                                                                          |
| `wrap-ansi@7.0.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `wrap-ansi@8.1.0`                             | False                   | `[]`                                                                                                                                                                                                          |
| `wrappy@1.0.2`                                | False                   | `[]`                                                                                                                                                                                                          |
| `y18n@5.0.8`                                  | False                   | `[]`                                                                                                                                                                                                          |
| `yargs-parser@20.2.9`                         | False                   | `[]`                                                                                                                                                                                                          |
| `yargs-parser@21.1.1`                         | False                   | `[]`                                                                                                                                                                                                          |
| `yargs-unparser@2.0.0`                        | False                   | `[]`                                                                                                                                                                                                          |
| `yargs@16.2.0`                                | False                   | `[]`                                                                                                                                                                                                          |
| `yargs@17.7.2`                                | False                   | `[]`                                                                                                                                                                                                          |
| `yocto-queue@0.1.0`                           | False                   | `[]`                                                                                                                                                                                                          |
| `zod-validation-error@3.4.0`                  | False                   | `[]`                                                                                                                                                                                                          |
</details>

All packages have valid code signature.

All packages have code signature.

<details>
<summary>List of deprecated packages(2)</summary>
    


| package_name     | deprecated_in_version   | all_deprecated   | parent   |
|:-----------------|:------------------------|:-----------------|:---------|
| `glob@8.1.0`     | True                    | False            | `[]`     |
| `inflight@1.0.6` | True                    | True             | `[]`     |
</details>

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

Report created on 2025-05-13 00:37:14
- Tool version: 1dfb5543
- Project Name: microsoft/TypeScript
- Project Version: 68cead182cc24afdc3f1ce7c8ff5853aba14b65a
- Package Manager: npm
