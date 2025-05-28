
# Software Supply Chain Report of isaacs/minimatch - 0569cd3373408f9d701d3aab187b3f43a24a0db7

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
        

 ### Total packages in the supply chain: 301


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 9

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 3

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 1

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 261

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 0

:alien: Packages that are aliased (⚠️⚠️): 3


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(9)</summary>
    


| package_name                                   | sha_exists   | tag_version   | is_sha   | sha                                      | tag_url   | message                            |   status_code_for_sha | parent                                                                                                           |
|:-----------------------------------------------|:-------------|:--------------|:---------|:-----------------------------------------|:----------|:-----------------------------------|----------------------:|:-----------------------------------------------------------------------------------------------------------------|
| `@bcoe/v8-coverage@0.2.3`                      | False        | `0.2.3`       | False    |                                          |           | No tags found in the repo          |                   200 | `[]`                                                                                                             |
| `@isaacs/ts-node-temp-fork-for-pr-2009@10.9.7` | False        | `10.9.7`      | True     | b94410f249225de05d877d75f8b1839417cbdad3 |           | Tag 10.9.7 not found in the repo   |                   404 | `[]`                                                                                                             |
| `@tsconfig/node14@1.0.3`                       | False        | `1.0.3`       | False    |                                          |           | No tags found in the repo          |                   200 | `[]`                                                                                                             |
| `@types/brace-expansion@1.1.2`                 | False        | `1.1.2`       | False    |                                          |           | Tag 1.1.2 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/hast@3.0.4`                            | False        | `3.0.4`       | False    |                                          |           | Tag 3.0.4 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/istanbul-lib-coverage@2.0.6`           | False        | `2.0.6`       | False    |                                          |           | Tag 2.0.6 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/node@20.14.10`                         | False        | `20.14.10`    | False    |                                          |           | Tag 20.14.10 not found in the repo |                   404 | `[]`                                                                                                             |
| `@types/unist@3.0.2`                           | False        | `3.0.2`       | False    |                                          |           | Tag 3.0.2 not found in the repo    |                   404 | `[]`                                                                                                             |
| `tap-yaml@3.0.0`                               | False        | `3.0.0`       | True     | 7c022d052fef858727bb58dc37f508a76a6e062b |           | Tag 3.0.0 not found in the repo    |                   404 | `['@tapjs/config@4.0.3', '@tapjs/core@3.0.3', '@tapjs/run@3.0.3', 'tap-parser@17.0.0', '@tapjs/reporter@3.0.3']` |
</details>

<details>
<summary>Source code links that could not be found(4)</summary>
    


|   index | package_name                     | github_url                                  | github_exists   | parent   |
|--------:|:---------------------------------|:--------------------------------------------|:----------------|:---------|
|       1 | `@alcalzone/ansi-tokenize@0.1.3` | No_repo_info_found                          |                 | `[]`     |
|       2 | `minipass-pipeline@1.2.4`        | No_repo_info_found                          |                 | `[]`     |
|       3 | `yoga-wasm-web@0.3.3`            | No_repo_info_found                          |                 | `[]`     |
|       4 | `prismjs-terminal@1.2.3`         | https://github.com/isaacs/prismajs-terminal | False           | `[]`     |
</details>

<details>
<summary>List of packages without provenance(261)</summary>
    


| package_name                                   | provenance_in_version   | parent                                                                                                                                                 |
|:-----------------------------------------------|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@alcalzone/ansi-tokenize@0.1.3`               | False                   | `[]`                                                                                                                                                   |
| `@base2/pretty-print-object@1.0.1`             | False                   | `['react-element-to-jsx-string@15.0.0']`                                                                                                               |
| `@bcoe/v8-coverage@0.2.3`                      | False                   | `[]`                                                                                                                                                   |
| `@cspotcode/source-map-support@0.8.1`          | False                   | `[]`                                                                                                                                                   |
| `@isaacs/cliui@8.0.2`                          | False                   | `[]`                                                                                                                                                   |
| `@isaacs/ts-node-temp-fork-for-pr-2009@10.9.7` | False                   | `[]`                                                                                                                                                   |
| `@istanbuljs/schema@0.1.3`                     | False                   | `[]`                                                                                                                                                   |
| `@jridgewell/resolve-uri@3.1.0`                | False                   | `[]`                                                                                                                                                   |
| `@jridgewell/sourcemap-codec@1.4.15`           | False                   | `[]`                                                                                                                                                   |
| `@jridgewell/trace-mapping@0.3.25`             | False                   | `[]`                                                                                                                                                   |
| `@jridgewell/trace-mapping@0.3.9`              | False                   | `['@cspotcode/source-map-support@0.8.1']`                                                                                                              |
| `@npmcli/fs@3.1.1`                             | False                   | `[]`                                                                                                                                                   |
| `@npmcli/node-gyp@3.0.0`                       | False                   | `[]`                                                                                                                                                   |
| `@pkgjs/parseargs@0.11.0`                      | False                   | `[]`                                                                                                                                                   |
| `@shikijs/core@1.10.3`                         | False                   | `['shiki@1.10.3']`                                                                                                                                     |
| `@tapjs/after-each@3.0.3`                      | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/after@2.0.3`                           | False                   | `['@tapjs/mock@3.0.3', 'tap@20.0.3', '@tapjs/run@3.0.3', '@tapjs/test@3.0.3', '@tapjs/intercept@3.0.3']`                                               |
| `@tapjs/asserts@3.0.3`                         | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/before-each@3.0.3`                     | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/before@3.0.3`                          | False                   | `['tap@20.0.3', '@tapjs/run@3.0.3', '@tapjs/test@3.0.3']`                                                                                              |
| `@tapjs/chdir@2.0.3`                           | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/config@4.0.3`                          | False                   | `['@tapjs/run@3.0.3', '@tapjs/reporter@3.0.3']`                                                                                                        |
| `@tapjs/core@3.0.3`                            | False                   | `['@tapjs/config@4.0.3', 'tap@20.0.3']`                                                                                                                |
| `@tapjs/error-serdes@3.0.0`                    | False                   | `['@tapjs/node-serialize@3.0.3']`                                                                                                                      |
| `@tapjs/filter@3.0.3`                          | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/fixture@3.0.3`                         | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/intercept@3.0.3`                       | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/mock@3.0.3`                            | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/node-serialize@3.0.3`                  | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/processinfo@3.1.8`                     | False                   | `[]`                                                                                                                                                   |
| `@tapjs/reporter@3.0.3`                        | False                   | `['@tapjs/run@3.0.3']`                                                                                                                                 |
| `@tapjs/run@3.0.3`                             | False                   | `['tap@20.0.3']`                                                                                                                                       |
| `@tapjs/snapshot@3.0.3`                        | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/spawn@3.0.3`                           | False                   | `['tap@20.0.3', '@tapjs/run@3.0.3', '@tapjs/test@3.0.3']`                                                                                              |
| `@tapjs/stack@3.0.0`                           | False                   | `['@tapjs/node-serialize@3.0.3', '@tapjs/mock@3.0.3', '@tapjs/core@3.0.3', '@tapjs/asserts@3.0.3', '@tapjs/reporter@3.0.3', '@tapjs/intercept@3.0.3']` |
| `@tapjs/stdin@3.0.3`                           | False                   | `['tap@20.0.3', '@tapjs/run@3.0.3', '@tapjs/test@3.0.3']`                                                                                              |
| `@tapjs/test@3.0.3`                            | False                   | `['@tapjs/config@4.0.3', 'tap@20.0.3', '@tapjs/core@3.0.3', '@tapjs/run@3.0.3']`                                                                       |
| `@tapjs/typescript@2.0.3`                      | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tapjs/worker@3.0.3`                          | False                   | `['tap@20.0.3', '@tapjs/test@3.0.3']`                                                                                                                  |
| `@tsconfig/node14@1.0.3`                       | False                   | `[]`                                                                                                                                                   |
| `@tsconfig/node16@1.0.4`                       | False                   | `[]`                                                                                                                                                   |
| `@tsconfig/node18@18.2.4`                      | False                   | `[]`                                                                                                                                                   |
| `@tsconfig/node20@20.1.4`                      | False                   | `[]`                                                                                                                                                   |
| `@types/brace-expansion@1.1.2`                 | False                   | `[]`                                                                                                                                                   |
| `@types/hast@3.0.4`                            | False                   | `[]`                                                                                                                                                   |
| `@types/istanbul-lib-coverage@2.0.6`           | False                   | `[]`                                                                                                                                                   |
| `@types/node@20.14.10`                         | False                   | `[]`                                                                                                                                                   |
| `@types/unist@3.0.2`                           | False                   | `[]`                                                                                                                                                   |
| `abbrev@2.0.0`                                 | False                   | `[]`                                                                                                                                                   |
| `acorn-walk@8.2.0`                             | False                   | `[]`                                                                                                                                                   |
| `acorn@8.10.0`                                 | False                   | `[]`                                                                                                                                                   |
| `agent-base@7.1.1`                             | False                   | `[]`                                                                                                                                                   |
| `aggregate-error@3.1.0`                        | False                   | `[]`                                                                                                                                                   |
| `ansi-escapes@7.0.0`                           | False                   | `[]`                                                                                                                                                   |
| `ansi-regex@5.0.1`                             | False                   | `[]`                                                                                                                                                   |
| `ansi-regex@6.0.1`                             | False                   | `[]`                                                                                                                                                   |
| `ansi-styles@4.3.0`                            | False                   | `[]`                                                                                                                                                   |
| `ansi-styles@6.2.1`                            | False                   | `[]`                                                                                                                                                   |
| `anymatch@3.1.3`                               | False                   | `[]`                                                                                                                                                   |
| `arg@4.1.3`                                    | False                   | `[]`                                                                                                                                                   |
| `argparse@2.0.1`                               | False                   | `[]`                                                                                                                                                   |
| `async-hook-domain@4.0.1`                      | False                   | `[]`                                                                                                                                                   |
| `auto-bind@5.0.1`                              | False                   | `[]`                                                                                                                                                   |
| `balanced-match@1.0.2`                         | False                   | `[]`                                                                                                                                                   |
| `binary-extensions@2.3.0`                      | False                   | `[]`                                                                                                                                                   |
| `brace-expansion@2.0.1`                        | False                   | `[]`                                                                                                                                                   |
| `braces@3.0.3`                                 | False                   | `[]`                                                                                                                                                   |
| `c8@10.1.2`                                    | False                   | `[]`                                                                                                                                                   |
| `chalk@5.3.0`                                  | False                   | `[]`                                                                                                                                                   |
| `chownr@2.0.0`                                 | False                   | `[]`                                                                                                                                                   |
| `clean-stack@2.2.0`                            | False                   | `[]`                                                                                                                                                   |
| `cli-boxes@3.0.0`                              | False                   | `[]`                                                                                                                                                   |
| `cli-cursor@4.0.0`                             | False                   | `[]`                                                                                                                                                   |
| `cli-truncate@4.0.0`                           | False                   | `[]`                                                                                                                                                   |
| `cliui@8.0.1`                                  | False                   | `[]`                                                                                                                                                   |
| `code-excerpt@4.0.0`                           | False                   | `[]`                                                                                                                                                   |
| `color-convert@2.0.1`                          | False                   | `[]`                                                                                                                                                   |
| `color-name@1.1.4`                             | False                   | `[]`                                                                                                                                                   |
| `convert-source-map@2.0.0`                     | False                   | `[]`                                                                                                                                                   |
| `convert-to-spaces@2.0.1`                      | False                   | `[]`                                                                                                                                                   |
| `cross-spawn@7.0.3`                            | False                   | `[]`                                                                                                                                                   |
| `debug@4.3.4`                                  | False                   | `[]`                                                                                                                                                   |
| `diff@4.0.2`                                   | False                   | `[]`                                                                                                                                                   |
| `diff@5.2.0`                                   | False                   | `[]`                                                                                                                                                   |
| `eastasianwidth@0.2.0`                         | False                   | `[]`                                                                                                                                                   |
| `emoji-regex@10.3.0`                           | False                   | `[]`                                                                                                                                                   |
| `emoji-regex@8.0.0`                            | False                   | `[]`                                                                                                                                                   |
| `emoji-regex@9.2.2`                            | False                   | `[]`                                                                                                                                                   |
| `encoding@0.1.13`                              | False                   | `[]`                                                                                                                                                   |
| `entities@4.5.0`                               | False                   | `[]`                                                                                                                                                   |
| `env-paths@2.2.1`                              | False                   | `[]`                                                                                                                                                   |
| `environment@1.1.0`                            | False                   | `[]`                                                                                                                                                   |
| `err-code@2.0.3`                               | False                   | `[]`                                                                                                                                                   |
| `escalade@3.1.2`                               | False                   | `[]`                                                                                                                                                   |
| `escape-string-regexp@2.0.0`                   | False                   | `[]`                                                                                                                                                   |
| `events-to-array@2.0.3`                        | False                   | `[]`                                                                                                                                                   |
| `exponential-backoff@3.1.1`                    | False                   | `[]`                                                                                                                                                   |
| `fill-range@7.1.1`                             | False                   | `[]`                                                                                                                                                   |
| `find-up@5.0.0`                                | False                   | `[]`                                                                                                                                                   |
| `foreground-child@3.2.1`                       | False                   | `[]`                                                                                                                                                   |
| `fromentries@1.3.2`                            | False                   | `[]`                                                                                                                                                   |
| `fs-minipass@2.1.0`                            | False                   | `[]`                                                                                                                                                   |
| `fsevents@2.3.3`                               | False                   | `[]`                                                                                                                                                   |
| `function-loop@4.0.0`                          | False                   | `[]`                                                                                                                                                   |
| `get-caller-file@2.0.5`                        | False                   | `[]`                                                                                                                                                   |
| `get-east-asian-width@1.2.0`                   | False                   | `[]`                                                                                                                                                   |
| `glob-parent@5.1.2`                            | False                   | `[]`                                                                                                                                                   |
| `glob@10.4.3`                                  | False                   | `[]`                                                                                                                                                   |
| `graceful-fs@4.2.11`                           | False                   | `[]`                                                                                                                                                   |
| `has-flag@4.0.0`                               | False                   | `[]`                                                                                                                                                   |
| `html-escaper@2.0.2`                           | False                   | `[]`                                                                                                                                                   |
| `http-cache-semantics@4.1.1`                   | False                   | `[]`                                                                                                                                                   |
| `http-proxy-agent@7.0.2`                       | False                   | `[]`                                                                                                                                                   |
| `https-proxy-agent@7.0.5`                      | False                   | `[]`                                                                                                                                                   |
| `iconv-lite@0.6.3`                             | False                   | `[]`                                                                                                                                                   |
| `imurmurhash@0.1.4`                            | False                   | `[]`                                                                                                                                                   |
| `indent-string@4.0.0`                          | False                   | `[]`                                                                                                                                                   |
| `indent-string@5.0.0`                          | False                   | `[]`                                                                                                                                                   |
| `ink@5.0.1`                                    | False                   | `[]`                                                                                                                                                   |
| `ip-address@9.0.5`                             | False                   | `[]`                                                                                                                                                   |
| `is-actual-promise@1.0.2`                      | False                   | `[]`                                                                                                                                                   |
| `is-binary-path@2.1.0`                         | False                   | `[]`                                                                                                                                                   |
| `is-extglob@2.1.1`                             | False                   | `[]`                                                                                                                                                   |
| `is-fullwidth-code-point@3.0.0`                | False                   | `[]`                                                                                                                                                   |
| `is-fullwidth-code-point@4.0.0`                | False                   | `[]`                                                                                                                                                   |
| `is-fullwidth-code-point@5.0.0`                | False                   | `[]`                                                                                                                                                   |
| `is-glob@4.0.3`                                | False                   | `[]`                                                                                                                                                   |
| `is-in-ci@0.1.0`                               | False                   | `[]`                                                                                                                                                   |
| `is-lambda@1.0.1`                              | False                   | `[]`                                                                                                                                                   |
| `is-number@7.0.0`                              | False                   | `[]`                                                                                                                                                   |
| `is-plain-object@5.0.0`                        | False                   | `['react-element-to-jsx-string@15.0.0']`                                                                                                               |
| `isexe@2.0.0`                                  | False                   | `[]`                                                                                                                                                   |
| `isexe@3.1.1`                                  | False                   | `[]`                                                                                                                                                   |
| `istanbul-lib-coverage@3.2.2`                  | False                   | `[]`                                                                                                                                                   |
| `istanbul-lib-report@3.0.1`                    | False                   | `[]`                                                                                                                                                   |
| `istanbul-reports@3.1.7`                       | False                   | `[]`                                                                                                                                                   |
| `jackspeak@3.4.2`                              | False                   | `[]`                                                                                                                                                   |
| `js-tokens@4.0.0`                              | False                   | `[]`                                                                                                                                                   |
| `jsbn@1.1.0`                                   | False                   | `['ip-address@9.0.5']`                                                                                                                                 |
| `jsonparse@1.3.1`                              | False                   | `[]`                                                                                                                                                   |
| `linkify-it@5.0.0`                             | False                   | `[]`                                                                                                                                                   |
| `locate-path@6.0.0`                            | False                   | `[]`                                                                                                                                                   |
| `lodash@4.17.21`                               | False                   | `[]`                                                                                                                                                   |
| `loose-envify@1.4.0`                           | False                   | `[]`                                                                                                                                                   |
| `lru-cache@10.4.0`                             | False                   | `[]`                                                                                                                                                   |
| `lunr@2.3.9`                                   | False                   | `[]`                                                                                                                                                   |
| `make-dir@4.0.0`                               | False                   | `[]`                                                                                                                                                   |
| `make-error@1.3.6`                             | False                   | `[]`                                                                                                                                                   |
| `markdown-it@14.1.0`                           | False                   | `[]`                                                                                                                                                   |
| `mdurl@2.0.0`                                  | False                   | `[]`                                                                                                                                                   |
| `mimic-fn@2.1.0`                               | False                   | `[]`                                                                                                                                                   |
| `minimatch@9.0.5`                              | False                   | `[]`                                                                                                                                                   |
| `minipass-collect@2.0.1`                       | False                   | `[]`                                                                                                                                                   |
| `minipass-flush@1.0.5`                         | False                   | `[]`                                                                                                                                                   |
| `minipass-pipeline@1.2.4`                      | False                   | `[]`                                                                                                                                                   |
| `minipass-sized@1.0.3`                         | False                   | `[]`                                                                                                                                                   |
| `minipass@3.3.6`                               | False                   | `[]`                                                                                                                                                   |
| `minipass@5.0.0`                               | False                   | `[]`                                                                                                                                                   |
| `minipass@7.1.2`                               | False                   | `[]`                                                                                                                                                   |
| `minizlib@2.1.2`                               | False                   | `[]`                                                                                                                                                   |
| `mkdirp@1.0.4`                                 | False                   | `[]`                                                                                                                                                   |
| `mkdirp@3.0.1`                                 | False                   | `[]`                                                                                                                                                   |
| `ms@2.1.2`                                     | False                   | `['debug@4.3.4']`                                                                                                                                      |
| `ms@2.1.3`                                     | False                   | `[]`                                                                                                                                                   |
| `negotiator@0.6.3`                             | False                   | `[]`                                                                                                                                                   |
| `node-gyp@10.1.0`                              | False                   | `[]`                                                                                                                                                   |
| `normalize-path@3.0.0`                         | False                   | `[]`                                                                                                                                                   |
| `onetime@5.1.2`                                | False                   | `[]`                                                                                                                                                   |
| `opener@1.5.2`                                 | False                   | `[]`                                                                                                                                                   |
| `p-limit@3.1.0`                                | False                   | `[]`                                                                                                                                                   |
| `p-locate@5.0.0`                               | False                   | `[]`                                                                                                                                                   |
| `p-map@4.0.0`                                  | False                   | `[]`                                                                                                                                                   |
| `package-json-from-dist@1.0.0`                 | False                   | `[]`                                                                                                                                                   |
| `patch-console@2.0.0`                          | False                   | `[]`                                                                                                                                                   |
| `path-exists@4.0.0`                            | False                   | `[]`                                                                                                                                                   |
| `path-key@3.1.1`                               | False                   | `[]`                                                                                                                                                   |
| `path-scurry@1.11.1`                           | False                   | `[]`                                                                                                                                                   |
| `picomatch@2.3.1`                              | False                   | `[]`                                                                                                                                                   |
| `pirates@4.0.6`                                | False                   | `[]`                                                                                                                                                   |
| `polite-json@5.0.0`                            | False                   | `[]`                                                                                                                                                   |
| `prettier@3.3.2`                               | False                   | `[]`                                                                                                                                                   |
| `prismjs-terminal@1.2.3`                       | False                   | `[]`                                                                                                                                                   |
| `prismjs@1.29.0`                               | False                   | `[]`                                                                                                                                                   |
| `proc-log@3.0.0`                               | False                   | `[]`                                                                                                                                                   |
| `process-on-spawn@1.0.0`                       | False                   | `[]`                                                                                                                                                   |
| `promise-inflight@1.0.1`                       | False                   | `[]`                                                                                                                                                   |
| `promise-retry@2.0.1`                          | False                   | `[]`                                                                                                                                                   |
| `punycode.js@2.3.1`                            | False                   | `[]`                                                                                                                                                   |
| `react-dom@18.3.1`                             | False                   | `[]`                                                                                                                                                   |
| `react-element-to-jsx-string@15.0.0`           | False                   | `[]`                                                                                                                                                   |
| `react-is@18.1.0`                              | False                   | `['react-element-to-jsx-string@15.0.0']`                                                                                                               |
| `react-reconciler@0.29.2`                      | False                   | `[]`                                                                                                                                                   |
| `react@18.3.1`                                 | False                   | `[]`                                                                                                                                                   |
| `readdirp@3.6.0`                               | False                   | `[]`                                                                                                                                                   |
| `require-directory@2.1.1`                      | False                   | `[]`                                                                                                                                                   |
| `resolve-import@1.4.5`                         | False                   | `[]`                                                                                                                                                   |
| `restore-cursor@4.0.0`                         | False                   | `[]`                                                                                                                                                   |
| `retry@0.12.0`                                 | False                   | `[]`                                                                                                                                                   |
| `rimraf@5.0.8`                                 | False                   | `[]`                                                                                                                                                   |
| `safer-buffer@2.1.2`                           | False                   | `[]`                                                                                                                                                   |
| `scheduler@0.23.2`                             | False                   | `[]`                                                                                                                                                   |
| `shebang-command@2.0.0`                        | False                   | `[]`                                                                                                                                                   |
| `shebang-regex@3.0.0`                          | False                   | `[]`                                                                                                                                                   |
| `shiki@1.10.3`                                 | False                   | `[]`                                                                                                                                                   |
| `signal-exit@3.0.7`                            | False                   | `[]`                                                                                                                                                   |
| `signal-exit@4.1.0`                            | False                   | `[]`                                                                                                                                                   |
| `slice-ansi@5.0.0`                             | False                   | `[]`                                                                                                                                                   |
| `slice-ansi@7.1.0`                             | False                   | `[]`                                                                                                                                                   |
| `smart-buffer@4.2.0`                           | False                   | `[]`                                                                                                                                                   |
| `socks-proxy-agent@8.0.4`                      | False                   | `[]`                                                                                                                                                   |
| `socks@2.8.3`                                  | False                   | `[]`                                                                                                                                                   |
| `spdx-correct@3.2.0`                           | False                   | `[]`                                                                                                                                                   |
| `spdx-exceptions@2.5.0`                        | False                   | `[]`                                                                                                                                                   |
| `spdx-expression-parse@3.0.1`                  | False                   | `[]`                                                                                                                                                   |
| `spdx-license-ids@3.0.18`                      | False                   | `[]`                                                                                                                                                   |
| `sprintf-js@1.1.3`                             | False                   | `[]`                                                                                                                                                   |
| `stack-utils@2.0.6`                            | False                   | `[]`                                                                                                                                                   |
| `string-length@6.0.0`                          | False                   | `[]`                                                                                                                                                   |
| `string-width@4.2.3`                           | False                   | `[]`                                                                                                                                                   |
| `string-width@5.1.2`                           | False                   | `[]`                                                                                                                                                   |
| `string-width@7.2.0`                           | False                   | `[]`                                                                                                                                                   |
| `strip-ansi@6.0.1`                             | False                   | `[]`                                                                                                                                                   |
| `strip-ansi@7.1.0`                             | False                   | `[]`                                                                                                                                                   |
| `supports-color@7.2.0`                         | False                   | `[]`                                                                                                                                                   |
| `sync-content@1.0.2`                           | False                   | `[]`                                                                                                                                                   |
| `tap-parser@17.0.0`                            | False                   | `['@tapjs/node-serialize@3.0.3', '@tapjs/core@3.0.3', '@tapjs/run@3.0.3', '@tapjs/test@3.0.3', '@tapjs/reporter@3.0.3']`                               |
| `tap-yaml@3.0.0`                               | False                   | `['@tapjs/config@4.0.3', '@tapjs/core@3.0.3', '@tapjs/run@3.0.3', 'tap-parser@17.0.0', '@tapjs/reporter@3.0.3']`                                       |
| `tap@20.0.3`                                   | False                   | `[]`                                                                                                                                                   |
| `tar@6.2.1`                                    | False                   | `[]`                                                                                                                                                   |
| `tcompare@8.0.0`                               | False                   | `['@tapjs/snapshot@3.0.3', '@tapjs/core@3.0.3', '@tapjs/run@3.0.3', '@tapjs/asserts@3.0.3', '@tapjs/reporter@3.0.3']`                                  |
| `test-exclude@7.0.1`                           | False                   | `[]`                                                                                                                                                   |
| `to-regex-range@5.0.1`                         | False                   | `[]`                                                                                                                                                   |
| `trivial-deferred@2.0.0`                       | False                   | `[]`                                                                                                                                                   |
| `tshy@1.18.0`                                  | False                   | `[]`                                                                                                                                                   |
| `tshy@2.0.1`                                   | False                   | `[]`                                                                                                                                                   |
| `type-fest@4.21.0`                             | False                   | `[]`                                                                                                                                                   |
| `typedoc@0.26.3`                               | False                   | `[]`                                                                                                                                                   |
| `typescript@5.5.3`                             | False                   | `[]`                                                                                                                                                   |
| `uc.micro@2.1.0`                               | False                   | `[]`                                                                                                                                                   |
| `undici-types@5.26.5`                          | False                   | `[]`                                                                                                                                                   |
| `unique-filename@3.0.0`                        | False                   | `[]`                                                                                                                                                   |
| `unique-slug@4.0.0`                            | False                   | `[]`                                                                                                                                                   |
| `uuid@8.3.2`                                   | False                   | `[]`                                                                                                                                                   |
| `v8-compile-cache-lib@3.0.1`                   | False                   | `[]`                                                                                                                                                   |
| `v8-to-istanbul@9.3.0`                         | False                   | `[]`                                                                                                                                                   |
| `validate-npm-package-license@3.0.4`           | False                   | `[]`                                                                                                                                                   |
| `walk-up-path@3.0.1`                           | False                   | `[]`                                                                                                                                                   |
| `which@2.0.2`                                  | False                   | `[]`                                                                                                                                                   |
| `widest-line@5.0.0`                            | False                   | `[]`                                                                                                                                                   |
| `wrap-ansi@7.0.0`                              | False                   | `[]`                                                                                                                                                   |
| `wrap-ansi@8.1.0`                              | False                   | `[]`                                                                                                                                                   |
| `wrap-ansi@9.0.0`                              | False                   | `[]`                                                                                                                                                   |
| `ws@8.18.0`                                    | False                   | `[]`                                                                                                                                                   |
| `y18n@5.0.8`                                   | False                   | `[]`                                                                                                                                                   |
| `yallist@4.0.0`                                | False                   | `[]`                                                                                                                                                   |
| `yaml-types@0.3.0`                             | False                   | `[]`                                                                                                                                                   |
| `yaml@2.4.5`                                   | False                   | `[]`                                                                                                                                                   |
| `yargs-parser@21.1.1`                          | False                   | `[]`                                                                                                                                                   |
| `yargs@17.7.2`                                 | False                   | `[]`                                                                                                                                                   |
| `yocto-queue@0.1.0`                            | False                   | `[]`                                                                                                                                                   |
| `yoga-wasm-web@0.3.3`                          | False                   | `[]`                                                                                                                                                   |
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

Report created on 2025-05-13 00:32:00
- Tool version: 1dfb5543
- Project Name: isaacs/minimatch
- Project Version: 0569cd3373408f9d701d3aab187b3f43a24a0db7
- Package Manager: npm
