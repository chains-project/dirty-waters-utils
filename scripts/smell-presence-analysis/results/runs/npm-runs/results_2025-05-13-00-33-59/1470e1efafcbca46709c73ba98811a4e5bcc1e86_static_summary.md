
# Software Supply Chain Report of lydell/js-tokens - 1470e1efafcbca46709c73ba98811a4e5bcc1e86

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
        

 ### Total packages in the supply chain: 331


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 10

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 0

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 5

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 312

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 0

:alien: Packages that are aliased (⚠️⚠️): 3


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(10)</summary>
    


| package_name                          | sha_exists   | tag_version   | is_sha   | sha                                      | tag_url   | message                          |   status_code_for_sha | parent              |
|:--------------------------------------|:-------------|:--------------|:---------|:-----------------------------------------|:----------|:---------------------------------|----------------------:|:--------------------|
| `@bcoe/v8-coverage@0.2.3`             | False        | `0.2.3`       | False    |                                          |           | No tags found in the repo        |                   200 | `[]`                |
| `@types/eslint@7.29.0`                | False        | `7.29.0`      | False    |                                          |           | Tag 7.29.0 not found in the repo |                   404 | `[]`                |
| `@types/estree@1.0.5`                 | False        | `1.0.5`       | False    |                                          |           | Tag 1.0.5 not found in the repo  |                   404 | `['rollup@4.22.4']` |
| `@types/json-schema@7.0.15`           | False        | `7.0.15`      | False    |                                          |           | Tag 7.0.15 not found in the repo |                   404 | `[]`                |
| `@types/minimist@1.2.5`               | False        | `1.2.5`       | False    |                                          |           | Tag 1.2.5 not found in the repo  |                   404 | `[]`                |
| `@types/normalize-package-data@2.4.4` | False        | `2.4.4`       | False    |                                          |           | Tag 2.4.4 not found in the repo  |                   404 | `[]`                |
| `decamelize-keys@1.1.1`               | False        | `1.1.1`       | True     | 73b6454e8d0137175c3a0195bc3a35e6194fe538 |           | Tag 1.1.1 not found in the repo  |                   404 | `[]`                |
| `keyv@4.5.4`                          | False        | `4.5.4`       | False    |                                          |           | Tag 4.5.4 not found in the repo  |                   404 | `[]`                |
| `lines-and-columns@1.2.4`             | False        | `1.2.4`       | True     | 3389156275890966091dec7611105fa5d47eb964 |           | Tag 1.2.4 not found in the repo  |                   404 | `[]`                |
| `lodash.merge@4.6.2`                  | False        | `4.6.2`       | False    |                                          |           | Tag 4.6.2 not found in the repo  |                   404 | `[]`                |
</details>

<details>
<summary>Source code links that could not be found(5)</summary>
    


|   index | package_name                 | github_url                                    | github_exists   | parent                       |
|--------:|:-----------------------------|:----------------------------------------------|:----------------|:-----------------------------|
|       1 | `@humanwhocodes/retry@0.3.0` | https://github.com/humanwhocodes/retrier      | False           | `[]`                         |
|       2 | `concat-map@0.0.1`           | https://github.com/substack/node-concat-map   | False           | `['brace-expansion@1.1.11']` |
|       3 | `file-entry-cache@8.0.0`     | https://github.com/jaredwray/file-entry-cache | False           | `[]`                         |
|       4 | `flat-cache@4.0.1`           | https://github.com/jaredwray/flat-cache       | False           | `[]`                         |
|       5 | `text-table@0.2.0`           | https://github.com/substack/text-table        | False           | `[]`                         |
</details>

<details>
<summary>List of packages without provenance(312)</summary>
    


| package_name                                  | provenance_in_version   | parent                                                                                                                                                                |
|:----------------------------------------------|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@ampproject/remapping@2.3.0`                 | False                   | `[]`                                                                                                                                                                  |
| `@babel/code-frame@7.24.7`                    | False                   | `[]`                                                                                                                                                                  |
| `@babel/helper-string-parser@7.24.8`          | False                   | `[]`                                                                                                                                                                  |
| `@babel/helper-validator-identifier@7.24.7`   | False                   | `[]`                                                                                                                                                                  |
| `@babel/highlight@7.24.7`                     | False                   | `[]`                                                                                                                                                                  |
| `@babel/parser@7.25.3`                        | False                   | `[]`                                                                                                                                                                  |
| `@babel/types@7.25.2`                         | False                   | `[]`                                                                                                                                                                  |
| `@bcoe/v8-coverage@0.2.3`                     | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/aix-ppc64@0.21.5`                   | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/android-arm64@0.21.5`               | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/android-arm@0.21.5`                 | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/android-x64@0.21.5`                 | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/darwin-arm64@0.21.5`                | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/darwin-x64@0.21.5`                  | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/freebsd-arm64@0.21.5`               | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/freebsd-x64@0.21.5`                 | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/linux-arm64@0.21.5`                 | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/linux-arm@0.21.5`                   | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/linux-ia32@0.21.5`                  | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/linux-loong64@0.21.5`               | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/linux-mips64el@0.21.5`              | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/linux-ppc64@0.21.5`                 | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/linux-riscv64@0.21.5`               | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/linux-s390x@0.21.5`                 | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/linux-x64@0.21.5`                   | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/netbsd-x64@0.21.5`                  | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/openbsd-x64@0.21.5`                 | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/sunos-x64@0.21.5`                   | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/win32-arm64@0.21.5`                 | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/win32-ia32@0.21.5`                  | False                   | `[]`                                                                                                                                                                  |
| `@esbuild/win32-x64@0.21.5`                   | False                   | `[]`                                                                                                                                                                  |
| `@eslint-community/eslint-utils@4.4.0`        | False                   | `[]`                                                                                                                                                                  |
| `@eslint-community/regexpp@4.11.0`            | False                   | `[]`                                                                                                                                                                  |
| `@eslint/js@9.9.0`                            | False                   | `['eslint@9.9.0']`                                                                                                                                                    |
| `@eslint/object-schema@2.1.4`                 | False                   | `[]`                                                                                                                                                                  |
| `@humanwhocodes/module-importer@1.0.1`        | False                   | `[]`                                                                                                                                                                  |
| `@humanwhocodes/retry@0.3.0`                  | False                   | `[]`                                                                                                                                                                  |
| `@isaacs/cliui@8.0.2`                         | False                   | `[]`                                                                                                                                                                  |
| `@istanbuljs/schema@0.1.3`                    | False                   | `[]`                                                                                                                                                                  |
| `@jest/schemas@29.6.3`                        | False                   | `[]`                                                                                                                                                                  |
| `@jridgewell/gen-mapping@0.3.5`               | False                   | `[]`                                                                                                                                                                  |
| `@jridgewell/resolve-uri@3.1.2`               | False                   | `[]`                                                                                                                                                                  |
| `@jridgewell/set-array@1.2.1`                 | False                   | `[]`                                                                                                                                                                  |
| `@jridgewell/sourcemap-codec@1.5.0`           | False                   | `[]`                                                                                                                                                                  |
| `@jridgewell/trace-mapping@0.3.25`            | False                   | `[]`                                                                                                                                                                  |
| `@nodelib/fs.scandir@2.1.5`                   | False                   | `['@nodelib/fs.walk@1.2.8']`                                                                                                                                          |
| `@nodelib/fs.stat@2.0.5`                      | False                   | `['@nodelib/fs.scandir@2.1.5']`                                                                                                                                       |
| `@nodelib/fs.walk@1.2.8`                      | False                   | `[]`                                                                                                                                                                  |
| `@pkgjs/parseargs@0.11.0`                     | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-android-arm-eabi@4.22.4`      | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-android-arm64@4.22.4`         | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-darwin-arm64@4.22.4`          | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-darwin-x64@4.22.4`            | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-linux-arm-gnueabihf@4.22.4`   | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-linux-arm-musleabihf@4.22.4`  | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-linux-arm64-gnu@4.22.4`       | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-linux-arm64-musl@4.22.4`      | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-linux-powerpc64le-gnu@4.22.4` | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-linux-riscv64-gnu@4.22.4`     | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-linux-s390x-gnu@4.22.4`       | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-linux-x64-gnu@4.22.4`         | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-linux-x64-musl@4.22.4`        | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-win32-arm64-msvc@4.22.4`      | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-win32-ia32-msvc@4.22.4`       | False                   | `[]`                                                                                                                                                                  |
| `@rollup/rollup-win32-x64-msvc@4.22.4`        | False                   | `[]`                                                                                                                                                                  |
| `@sinclair/typebox@0.27.8`                    | False                   | `[]`                                                                                                                                                                  |
| `@tsd/typescript@5.4.5`                       | False                   | `[]`                                                                                                                                                                  |
| `@types/eslint@7.29.0`                        | False                   | `[]`                                                                                                                                                                  |
| `@types/estree@1.0.5`                         | False                   | `['rollup@4.22.4']`                                                                                                                                                   |
| `@types/json-schema@7.0.15`                   | False                   | `[]`                                                                                                                                                                  |
| `@types/minimist@1.2.5`                       | False                   | `[]`                                                                                                                                                                  |
| `@types/normalize-package-data@2.4.4`         | False                   | `[]`                                                                                                                                                                  |
| `@typescript-eslint/scope-manager@8.1.0`      | False                   | `['@typescript-eslint/utils@8.1.0']`                                                                                                                                  |
| `@typescript-eslint/types@8.1.0`              | False                   | `['@typescript-eslint/visitor-keys@8.1.0', '@typescript-eslint/scope-manager@8.1.0', '@typescript-eslint/utils@8.1.0', '@typescript-eslint/typescript-estree@8.1.0']` |
| `@typescript-eslint/typescript-estree@8.1.0`  | False                   | `['@typescript-eslint/utils@8.1.0']`                                                                                                                                  |
| `@typescript-eslint/utils@8.1.0`              | False                   | `[]`                                                                                                                                                                  |
| `@typescript-eslint/visitor-keys@8.1.0`       | False                   | `['@typescript-eslint/scope-manager@8.1.0', '@typescript-eslint/typescript-estree@8.1.0']`                                                                            |
| `@vitest/eslint-plugin@1.0.3`                 | False                   | `[]`                                                                                                                                                                  |
| `acorn-jsx@5.3.2`                             | False                   | `[]`                                                                                                                                                                  |
| `acorn@8.12.1`                                | False                   | `[]`                                                                                                                                                                  |
| `ajv@6.12.6`                                  | False                   | `[]`                                                                                                                                                                  |
| `ansi-escapes@4.3.2`                          | False                   | `[]`                                                                                                                                                                  |
| `ansi-regex@5.0.1`                            | False                   | `[]`                                                                                                                                                                  |
| `ansi-regex@6.0.1`                            | False                   | `[]`                                                                                                                                                                  |
| `ansi-styles@3.2.1`                           | False                   | `[]`                                                                                                                                                                  |
| `ansi-styles@4.3.0`                           | False                   | `[]`                                                                                                                                                                  |
| `ansi-styles@5.2.0`                           | False                   | `[]`                                                                                                                                                                  |
| `ansi-styles@6.2.1`                           | False                   | `[]`                                                                                                                                                                  |
| `argparse@2.0.1`                              | False                   | `[]`                                                                                                                                                                  |
| `array-union@2.1.0`                           | False                   | `[]`                                                                                                                                                                  |
| `arrify@1.0.1`                                | False                   | `[]`                                                                                                                                                                  |
| `assertion-error@2.0.1`                       | False                   | `[]`                                                                                                                                                                  |
| `balanced-match@1.0.2`                        | False                   | `[]`                                                                                                                                                                  |
| `brace-expansion@1.1.11`                      | False                   | `[]`                                                                                                                                                                  |
| `brace-expansion@2.0.1`                       | False                   | `[]`                                                                                                                                                                  |
| `braces@3.0.3`                                | False                   | `[]`                                                                                                                                                                  |
| `cac@6.7.14`                                  | False                   | `[]`                                                                                                                                                                  |
| `callsites@3.1.0`                             | False                   | `[]`                                                                                                                                                                  |
| `camelcase-keys@6.2.2`                        | False                   | `[]`                                                                                                                                                                  |
| `camelcase@5.3.1`                             | False                   | `[]`                                                                                                                                                                  |
| `chai@5.1.1`                                  | False                   | `[]`                                                                                                                                                                  |
| `chalk@2.4.2`                                 | False                   | `[]`                                                                                                                                                                  |
| `chalk@4.1.2`                                 | False                   | `[]`                                                                                                                                                                  |
| `check-error@2.1.1`                           | False                   | `[]`                                                                                                                                                                  |
| `coffeescript@2.7.0`                          | False                   | `[]`                                                                                                                                                                  |
| `color-convert@1.9.3`                         | False                   | `[]`                                                                                                                                                                  |
| `color-convert@2.0.1`                         | False                   | `[]`                                                                                                                                                                  |
| `color-name@1.1.3`                            | False                   | `['color-convert@1.9.3']`                                                                                                                                             |
| `color-name@1.1.4`                            | False                   | `[]`                                                                                                                                                                  |
| `concat-map@0.0.1`                            | False                   | `['brace-expansion@1.1.11']`                                                                                                                                          |
| `cross-spawn@7.0.3`                           | False                   | `[]`                                                                                                                                                                  |
| `debug@4.3.6`                                 | False                   | `[]`                                                                                                                                                                  |
| `decamelize-keys@1.1.1`                       | False                   | `[]`                                                                                                                                                                  |
| `decamelize@1.2.0`                            | False                   | `[]`                                                                                                                                                                  |
| `deep-eql@5.0.2`                              | False                   | `[]`                                                                                                                                                                  |
| `deep-is@0.1.4`                               | False                   | `[]`                                                                                                                                                                  |
| `diff-sequences@29.6.3`                       | False                   | `[]`                                                                                                                                                                  |
| `dir-glob@3.0.1`                              | False                   | `[]`                                                                                                                                                                  |
| `eastasianwidth@0.2.0`                        | False                   | `[]`                                                                                                                                                                  |
| `emoji-regex@8.0.0`                           | False                   | `[]`                                                                                                                                                                  |
| `emoji-regex@9.2.2`                           | False                   | `[]`                                                                                                                                                                  |
| `error-ex@1.3.2`                              | False                   | `[]`                                                                                                                                                                  |
| `esbuild@0.21.5`                              | False                   | `[]`                                                                                                                                                                  |
| `escape-string-regexp@1.0.5`                  | False                   | `[]`                                                                                                                                                                  |
| `escape-string-regexp@4.0.0`                  | False                   | `[]`                                                                                                                                                                  |
| `eslint-formatter-pretty@4.1.0`               | False                   | `[]`                                                                                                                                                                  |
| `eslint-rule-docs@1.1.235`                    | False                   | `[]`                                                                                                                                                                  |
| `eslint@9.9.0`                                | False                   | `[]`                                                                                                                                                                  |
| `esquery@1.6.0`                               | False                   | `[]`                                                                                                                                                                  |
| `esrecurse@4.3.0`                             | False                   | `[]`                                                                                                                                                                  |
| `estraverse@5.3.0`                            | False                   | `[]`                                                                                                                                                                  |
| `estree-walker@3.0.3`                         | False                   | `[]`                                                                                                                                                                  |
| `esutils@2.0.3`                               | False                   | `[]`                                                                                                                                                                  |
| `everything.js@1.0.3`                         | False                   | `[]`                                                                                                                                                                  |
| `execa@8.0.1`                                 | False                   | `[]`                                                                                                                                                                  |
| `fast-deep-equal@3.1.3`                       | False                   | `[]`                                                                                                                                                                  |
| `fast-glob@3.3.2`                             | False                   | `[]`                                                                                                                                                                  |
| `fast-json-stable-stringify@2.1.0`            | False                   | `[]`                                                                                                                                                                  |
| `fast-levenshtein@2.0.6`                      | False                   | `[]`                                                                                                                                                                  |
| `fastq@1.17.1`                                | False                   | `[]`                                                                                                                                                                  |
| `file-entry-cache@8.0.0`                      | False                   | `[]`                                                                                                                                                                  |
| `fill-range@7.1.1`                            | False                   | `[]`                                                                                                                                                                  |
| `find-up@4.1.0`                               | False                   | `[]`                                                                                                                                                                  |
| `find-up@5.0.0`                               | False                   | `[]`                                                                                                                                                                  |
| `flat-cache@4.0.1`                            | False                   | `[]`                                                                                                                                                                  |
| `flatted@3.3.1`                               | False                   | `[]`                                                                                                                                                                  |
| `foreground-child@3.3.0`                      | False                   | `[]`                                                                                                                                                                  |
| `fsevents@2.3.3`                              | False                   | `[]`                                                                                                                                                                  |
| `function-bind@1.1.2`                         | False                   | `[]`                                                                                                                                                                  |
| `get-func-name@2.0.2`                         | False                   | `[]`                                                                                                                                                                  |
| `get-stream@8.0.1`                            | False                   | `[]`                                                                                                                                                                  |
| `glob-parent@5.1.2`                           | False                   | `[]`                                                                                                                                                                  |
| `glob-parent@6.0.2`                           | False                   | `[]`                                                                                                                                                                  |
| `glob@10.4.5`                                 | False                   | `[]`                                                                                                                                                                  |
| `globals@14.0.0`                              | False                   | `[]`                                                                                                                                                                  |
| `globby@11.1.0`                               | False                   | `[]`                                                                                                                                                                  |
| `hard-rejection@2.1.0`                        | False                   | `[]`                                                                                                                                                                  |
| `has-flag@3.0.0`                              | False                   | `[]`                                                                                                                                                                  |
| `has-flag@4.0.0`                              | False                   | `[]`                                                                                                                                                                  |
| `hasown@2.0.2`                                | False                   | `[]`                                                                                                                                                                  |
| `hosted-git-info@2.8.9`                       | False                   | `[]`                                                                                                                                                                  |
| `hosted-git-info@4.1.0`                       | False                   | `[]`                                                                                                                                                                  |
| `html-escaper@2.0.2`                          | False                   | `[]`                                                                                                                                                                  |
| `human-signals@5.0.0`                         | False                   | `[]`                                                                                                                                                                  |
| `ignore@5.3.2`                                | False                   | `[]`                                                                                                                                                                  |
| `import-fresh@3.3.0`                          | False                   | `[]`                                                                                                                                                                  |
| `imurmurhash@0.1.4`                           | False                   | `[]`                                                                                                                                                                  |
| `indent-string@4.0.0`                         | False                   | `[]`                                                                                                                                                                  |
| `irregular-plurals@3.5.0`                     | False                   | `[]`                                                                                                                                                                  |
| `is-arrayish@0.2.1`                           | False                   | `[]`                                                                                                                                                                  |
| `is-core-module@2.15.0`                       | False                   | `[]`                                                                                                                                                                  |
| `is-extglob@2.1.1`                            | False                   | `[]`                                                                                                                                                                  |
| `is-fullwidth-code-point@3.0.0`               | False                   | `[]`                                                                                                                                                                  |
| `is-glob@4.0.3`                               | False                   | `[]`                                                                                                                                                                  |
| `is-number@7.0.0`                             | False                   | `[]`                                                                                                                                                                  |
| `is-path-inside@3.0.3`                        | False                   | `[]`                                                                                                                                                                  |
| `is-plain-obj@1.1.0`                          | False                   | `[]`                                                                                                                                                                  |
| `is-stream@3.0.0`                             | False                   | `[]`                                                                                                                                                                  |
| `is-unicode-supported@0.1.0`                  | False                   | `[]`                                                                                                                                                                  |
| `isexe@2.0.0`                                 | False                   | `[]`                                                                                                                                                                  |
| `istanbul-lib-coverage@3.2.2`                 | False                   | `[]`                                                                                                                                                                  |
| `istanbul-lib-report@3.0.1`                   | False                   | `[]`                                                                                                                                                                  |
| `istanbul-lib-source-maps@5.0.6`              | False                   | `[]`                                                                                                                                                                  |
| `istanbul-reports@3.1.7`                      | False                   | `[]`                                                                                                                                                                  |
| `jackspeak@3.4.3`                             | False                   | `[]`                                                                                                                                                                  |
| `jest-diff@29.7.0`                            | False                   | `[]`                                                                                                                                                                  |
| `jest-get-type@29.6.3`                        | False                   | `[]`                                                                                                                                                                  |
| `js-tokens@4.0.0`                             | False                   | `[]`                                                                                                                                                                  |
| `js-yaml@4.1.0`                               | False                   | `[]`                                                                                                                                                                  |
| `json-buffer@3.0.1`                           | False                   | `['keyv@4.5.4']`                                                                                                                                                      |
| `json-parse-even-better-errors@2.3.1`         | False                   | `[]`                                                                                                                                                                  |
| `json-schema-traverse@0.4.1`                  | False                   | `[]`                                                                                                                                                                  |
| `json-stable-stringify-without-jsonify@1.0.1` | False                   | `[]`                                                                                                                                                                  |
| `keyv@4.5.4`                                  | False                   | `[]`                                                                                                                                                                  |
| `kind-of@6.0.3`                               | False                   | `[]`                                                                                                                                                                  |
| `levn@0.4.1`                                  | False                   | `[]`                                                                                                                                                                  |
| `lines-and-columns@1.2.4`                     | False                   | `[]`                                                                                                                                                                  |
| `locate-path@5.0.0`                           | False                   | `[]`                                                                                                                                                                  |
| `locate-path@6.0.0`                           | False                   | `[]`                                                                                                                                                                  |
| `lodash.merge@4.6.2`                          | False                   | `[]`                                                                                                                                                                  |
| `log-symbols@4.1.0`                           | False                   | `[]`                                                                                                                                                                  |
| `lru-cache@10.4.3`                            | False                   | `[]`                                                                                                                                                                  |
| `lru-cache@6.0.0`                             | False                   | `[]`                                                                                                                                                                  |
| `magic-string@0.30.11`                        | False                   | `[]`                                                                                                                                                                  |
| `magicast@0.3.4`                              | False                   | `[]`                                                                                                                                                                  |
| `make-dir@4.0.0`                              | False                   | `[]`                                                                                                                                                                  |
| `map-obj@1.0.1`                               | False                   | `[]`                                                                                                                                                                  |
| `map-obj@4.3.0`                               | False                   | `[]`                                                                                                                                                                  |
| `meow@9.0.0`                                  | False                   | `[]`                                                                                                                                                                  |
| `merge-stream@2.0.0`                          | False                   | `[]`                                                                                                                                                                  |
| `merge2@1.4.1`                                | False                   | `[]`                                                                                                                                                                  |
| `micromatch@4.0.7`                            | False                   | `[]`                                                                                                                                                                  |
| `mimic-fn@4.0.0`                              | False                   | `[]`                                                                                                                                                                  |
| `min-indent@1.0.1`                            | False                   | `[]`                                                                                                                                                                  |
| `minimatch@3.1.2`                             | False                   | `[]`                                                                                                                                                                  |
| `minimatch@9.0.5`                             | False                   | `[]`                                                                                                                                                                  |
| `minimist-options@4.1.0`                      | False                   | `['meow@9.0.0']`                                                                                                                                                      |
| `minipass@7.1.2`                              | False                   | `[]`                                                                                                                                                                  |
| `ms@2.1.2`                                    | False                   | `['debug@4.3.6']`                                                                                                                                                     |
| `nanoid@3.3.7`                                | False                   | `[]`                                                                                                                                                                  |
| `natural-compare@1.4.0`                       | False                   | `[]`                                                                                                                                                                  |
| `normalize-package-data@2.5.0`                | False                   | `[]`                                                                                                                                                                  |
| `normalize-package-data@3.0.3`                | False                   | `[]`                                                                                                                                                                  |
| `npm-run-path@5.3.0`                          | False                   | `[]`                                                                                                                                                                  |
| `onetime@6.0.0`                               | False                   | `[]`                                                                                                                                                                  |
| `optionator@0.9.4`                            | False                   | `[]`                                                                                                                                                                  |
| `p-limit@2.3.0`                               | False                   | `[]`                                                                                                                                                                  |
| `p-limit@3.1.0`                               | False                   | `[]`                                                                                                                                                                  |
| `p-locate@4.1.0`                              | False                   | `[]`                                                                                                                                                                  |
| `p-locate@5.0.0`                              | False                   | `[]`                                                                                                                                                                  |
| `p-try@2.2.0`                                 | False                   | `[]`                                                                                                                                                                  |
| `package-json-from-dist@1.0.0`                | False                   | `[]`                                                                                                                                                                  |
| `parent-module@1.0.1`                         | False                   | `[]`                                                                                                                                                                  |
| `parse-json@5.2.0`                            | False                   | `[]`                                                                                                                                                                  |
| `path-exists@4.0.0`                           | False                   | `[]`                                                                                                                                                                  |
| `path-key@3.1.1`                              | False                   | `[]`                                                                                                                                                                  |
| `path-key@4.0.0`                              | False                   | `[]`                                                                                                                                                                  |
| `path-parse@1.0.7`                            | False                   | `[]`                                                                                                                                                                  |
| `path-scurry@1.11.1`                          | False                   | `[]`                                                                                                                                                                  |
| `path-type@4.0.0`                             | False                   | `[]`                                                                                                                                                                  |
| `pathe@1.1.2`                                 | False                   | `[]`                                                                                                                                                                  |
| `pathval@2.0.0`                               | False                   | `[]`                                                                                                                                                                  |
| `picocolors@1.1.0`                            | False                   | `[]`                                                                                                                                                                  |
| `picomatch@2.3.1`                             | False                   | `[]`                                                                                                                                                                  |
| `plur@4.0.0`                                  | False                   | `[]`                                                                                                                                                                  |
| `postcss@8.4.47`                              | False                   | `[]`                                                                                                                                                                  |
| `prelude-ls@1.2.1`                            | False                   | `[]`                                                                                                                                                                  |
| `prettier@3.3.3`                              | False                   | `[]`                                                                                                                                                                  |
| `pretty-format@29.7.0`                        | False                   | `[]`                                                                                                                                                                  |
| `punycode@2.3.1`                              | False                   | `[]`                                                                                                                                                                  |
| `queue-microtask@1.2.3`                       | False                   | `[]`                                                                                                                                                                  |
| `quick-lru@4.0.1`                             | False                   | `[]`                                                                                                                                                                  |
| `react-is@18.3.1`                             | False                   | `[]`                                                                                                                                                                  |
| `read-pkg-up@7.0.1`                           | False                   | `[]`                                                                                                                                                                  |
| `read-pkg@5.2.0`                              | False                   | `[]`                                                                                                                                                                  |
| `redent@3.0.0`                                | False                   | `[]`                                                                                                                                                                  |
| `resolve-from@4.0.0`                          | False                   | `[]`                                                                                                                                                                  |
| `resolve@1.22.8`                              | False                   | `[]`                                                                                                                                                                  |
| `reusify@1.0.4`                               | False                   | `[]`                                                                                                                                                                  |
| `rollup@4.22.4`                               | False                   | `[]`                                                                                                                                                                  |
| `run-parallel@1.2.0`                          | False                   | `[]`                                                                                                                                                                  |
| `semver@5.7.2`                                | False                   | `[]`                                                                                                                                                                  |
| `shebang-command@2.0.0`                       | False                   | `[]`                                                                                                                                                                  |
| `shebang-regex@3.0.0`                         | False                   | `[]`                                                                                                                                                                  |
| `siginfo@2.0.0`                               | False                   | `[]`                                                                                                                                                                  |
| `signal-exit@4.1.0`                           | False                   | `[]`                                                                                                                                                                  |
| `slash@3.0.0`                                 | False                   | `[]`                                                                                                                                                                  |
| `source-map-js@1.2.1`                         | False                   | `[]`                                                                                                                                                                  |
| `spdx-correct@3.2.0`                          | False                   | `[]`                                                                                                                                                                  |
| `spdx-exceptions@2.5.0`                       | False                   | `[]`                                                                                                                                                                  |
| `spdx-expression-parse@3.0.1`                 | False                   | `[]`                                                                                                                                                                  |
| `spdx-license-ids@3.0.18`                     | False                   | `[]`                                                                                                                                                                  |
| `stackback@0.0.2`                             | False                   | `['why-is-node-running@2.3.0']`                                                                                                                                       |
| `std-env@3.7.0`                               | False                   | `[]`                                                                                                                                                                  |
| `string-width@4.2.3`                          | False                   | `[]`                                                                                                                                                                  |
| `string-width@5.1.2`                          | False                   | `[]`                                                                                                                                                                  |
| `strip-ansi@6.0.1`                            | False                   | `[]`                                                                                                                                                                  |
| `strip-ansi@7.1.0`                            | False                   | `[]`                                                                                                                                                                  |
| `strip-final-newline@3.0.0`                   | False                   | `[]`                                                                                                                                                                  |
| `strip-indent@3.0.0`                          | False                   | `[]`                                                                                                                                                                  |
| `strip-json-comments@3.1.1`                   | False                   | `[]`                                                                                                                                                                  |
| `supports-color@5.5.0`                        | False                   | `[]`                                                                                                                                                                  |
| `supports-color@7.2.0`                        | False                   | `[]`                                                                                                                                                                  |
| `supports-hyperlinks@2.3.0`                   | False                   | `[]`                                                                                                                                                                  |
| `supports-preserve-symlinks-flag@1.0.0`       | False                   | `[]`                                                                                                                                                                  |
| `test-exclude@7.0.1`                          | False                   | `[]`                                                                                                                                                                  |
| `test262-parser-tests@0.0.5`                  | False                   | `[]`                                                                                                                                                                  |
| `text-table@0.2.0`                            | False                   | `[]`                                                                                                                                                                  |
| `tinybench@2.9.0`                             | False                   | `[]`                                                                                                                                                                  |
| `tinypool@1.0.0`                              | False                   | `[]`                                                                                                                                                                  |
| `tinyrainbow@1.2.0`                           | False                   | `[]`                                                                                                                                                                  |
| `tinyspy@3.0.0`                               | False                   | `[]`                                                                                                                                                                  |
| `to-fast-properties@2.0.0`                    | False                   | `[]`                                                                                                                                                                  |
| `to-regex-range@5.0.1`                        | False                   | `[]`                                                                                                                                                                  |
| `trim-newlines@3.0.1`                         | False                   | `[]`                                                                                                                                                                  |
| `tsd@0.31.1`                                  | False                   | `[]`                                                                                                                                                                  |
| `type-check@0.4.0`                            | False                   | `[]`                                                                                                                                                                  |
| `type-fest@0.18.1`                            | False                   | `[]`                                                                                                                                                                  |
| `type-fest@0.21.3`                            | False                   | `[]`                                                                                                                                                                  |
| `type-fest@0.6.0`                             | False                   | `[]`                                                                                                                                                                  |
| `type-fest@0.8.1`                             | False                   | `[]`                                                                                                                                                                  |
| `typescript@5.5.4`                            | False                   | `[]`                                                                                                                                                                  |
| `uri-js@4.4.1`                                | False                   | `[]`                                                                                                                                                                  |
| `validate-npm-package-license@3.0.4`          | False                   | `[]`                                                                                                                                                                  |
| `which@2.0.2`                                 | False                   | `[]`                                                                                                                                                                  |
| `why-is-node-running@2.3.0`                   | False                   | `[]`                                                                                                                                                                  |
| `word-wrap@1.2.5`                             | False                   | `[]`                                                                                                                                                                  |
| `wrap-ansi@7.0.0`                             | False                   | `[]`                                                                                                                                                                  |
| `wrap-ansi@8.1.0`                             | False                   | `[]`                                                                                                                                                                  |
| `yallist@4.0.0`                               | False                   | `[]`                                                                                                                                                                  |
| `yargs-parser@20.2.9`                         | False                   | `[]`                                                                                                                                                                  |
| `yocto-queue@0.1.0`                           | False                   | `[]`                                                                                                                                                                  |
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

Report created on 2025-05-13 00:34:26
- Tool version: 1dfb5543
- Project Name: lydell/js-tokens
- Project Version: 1470e1efafcbca46709c73ba98811a4e5bcc1e86
- Package Manager: npm
