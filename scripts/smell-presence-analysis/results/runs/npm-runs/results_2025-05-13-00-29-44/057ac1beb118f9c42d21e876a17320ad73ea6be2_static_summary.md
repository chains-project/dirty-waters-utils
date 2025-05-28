
# Software Supply Chain Report of TypeStrong/ts-node - 057ac1beb118f9c42d21e876a17320ad73ea6be2

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
        

 ### Total packages in the supply chain: 519


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 37

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 0

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 5

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 509

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 11

:alien: Packages that are aliased (⚠️⚠️): 0


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(37)</summary>
    


| package_name                          | sha_exists   | tag_version   | is_sha   | sha   | tag_url   | message                            |   status_code_for_sha | parent                                                                                                           |
|:--------------------------------------|:-------------|:--------------|:---------|:------|:----------|:-----------------------------------|----------------------:|:-----------------------------------------------------------------------------------------------------------------|
| `@microsoft/tsdoc-config@0.15.2`      | False        | `0.15.2`      | False    |       |           | Tag 0.15.2 not found in the repo   |                   404 | `[]`                                                                                                             |
| `@microsoft/tsdoc@0.13.2`             | False        | `0.13.2`      | False    |       |           | Tag 0.13.2 not found in the repo   |                   404 | `['@microsoft/tsdoc-config@0.15.2', '@microsoft/api-extractor@7.19.4', '@microsoft/api-extractor-model@7.15.3']` |
| `@tsconfig/node10@1.0.7`              | False        | `1.0.7`       | False    |       |           | No tags found in the repo          |                   200 | `[]`                                                                                                             |
| `@tsconfig/node12@1.0.7`              | False        | `1.0.7`       | False    |       |           | No tags found in the repo          |                   200 | `[]`                                                                                                             |
| `@tsconfig/node14@1.0.0`              | False        | `1.0.0`       | False    |       |           | No tags found in the repo          |                   200 | `[]`                                                                                                             |
| `@tsconfig/node16@1.0.2`              | False        | `1.0.2`       | False    |       |           | No tags found in the repo          |                   200 | `[]`                                                                                                             |
| `@types/argparse@1.0.38`              | False        | `1.0.38`      | False    |       |           | Tag 1.0.38 not found in the repo   |                   404 | `['@rushstack/ts-command-line@4.10.6']`                                                                          |
| `@types/color-name@1.1.1`             | False        | `1.1.1`       | False    |       |           | Tag 1.1.1 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/diff@4.0.2`                   | False        | `4.0.2`       | False    |       |           | Tag 4.0.2 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/emscripten@1.39.4`            | False        | `1.39.4`      | False    |       |           | Tag 1.39.4 not found in the repo   |                   404 | `[]`                                                                                                             |
| `@types/events@3.0.0`                 | False        | `3.0.0`       | False    |       |           | Tag 3.0.0 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/glob@7.1.1`                   | False        | `7.1.1`       | False    |       |           | Tag 7.1.1 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/istanbul-lib-coverage@2.0.3`  | False        | `2.0.3`       | False    |       |           | Tag 2.0.3 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/istanbul-lib-report@3.0.0`    | False        | `3.0.0`       | False    |       |           | Tag 3.0.0 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/istanbul-reports@3.0.1`       | False        | `3.0.1`       | False    |       |           | Tag 3.0.1 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/json-schema@7.0.9`            | False        | `7.0.9`       | False    |       |           | Tag 7.0.9 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/lodash@4.14.151`              | False        | `4.14.151`    | False    |       |           | Tag 4.14.151 not found in the repo |                   404 | `[]`                                                                                                             |
| `@types/minimatch@3.0.3`              | False        | `3.0.3`       | False    |       |           | Tag 3.0.3 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/node@12.20.24`                | False        | `12.20.24`    | False    |       |           | Tag 12.20.24 not found in the repo |                   404 | `['@rushstack/node-core-library@3.45.0']`                                                                        |
| `@types/node@13.13.5`                 | False        | `13.13.5`     | False    |       |           | Tag 13.13.5 not found in the repo  |                   404 | `[]`                                                                                                             |
| `@types/node@16.11.25`                | False        | `16.11.25`    | False    |       |           | Tag 16.11.25 not found in the repo |                   404 | `[]`                                                                                                             |
| `@types/normalize-package-data@2.4.0` | False        | `2.4.0`       | False    |       |           | Tag 2.4.0 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/prop-types@15.7.5`            | False        | `15.7.5`      | False    |       |           | Tag 15.7.5 not found in the repo   |                   404 | `[]`                                                                                                             |
| `@types/proper-lockfile@4.1.2`        | False        | `4.1.2`       | False    |       |           | Tag 4.1.2 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/proxyquire@1.3.28`            | False        | `1.3.28`      | False    |       |           | Tag 1.3.28 not found in the repo   |                   404 | `[]`                                                                                                             |
| `@types/react@16.14.26`               | False        | `16.14.26`    | False    |       |           | Tag 16.14.26 not found in the repo |                   404 | `[]`                                                                                                             |
| `@types/retry@0.12.1`                 | False        | `0.12.1`      | False    |       |           | Tag 0.12.1 not found in the repo   |                   404 | `[]`                                                                                                             |
| `@types/rimraf@3.0.0`                 | False        | `3.0.0`       | False    |       |           | Tag 3.0.0 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/scheduler@0.16.2`             | False        | `0.16.2`      | False    |       |           | Tag 0.16.2 not found in the repo   |                   404 | `[]`                                                                                                             |
| `@types/semver@7.1.0`                 | False        | `7.1.0`       | False    |       |           | Tag 7.1.0 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/stack-utils@2.0.0`            | False        | `2.0.0`       | False    |       |           | Tag 2.0.0 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@types/yargs-parser@20.2.0`          | False        | `20.2.0`      | False    |       |           | Tag 20.2.0 not found in the repo   |                   404 | `[]`                                                                                                             |
| `@types/yargs@16.0.3`                 | False        | `16.0.3`      | False    |       |           | Tag 16.0.3 not found in the repo   |                   404 | `[]`                                                                                                             |
| `@yarnpkg/fslib@2.4.0`                | False        | `2.4.0`       | False    |       |           | Tag 2.4.0 not found in the repo    |                   404 | `[]`                                                                                                             |
| `@yarnpkg/libzip@2.2.1`               | False        | `2.2.1`       | False    |       |           | Tag 2.2.1 not found in the repo    |                   404 | `[]`                                                                                                             |
| `lodash.get@4.4.2`                    | False        | `4.4.2`       | False    |       |           | Tag 4.4.2 not found in the repo    |                   404 | `[]`                                                                                                             |
| `shiki@0.9.15`                        | False        | `0.9.15`      | False    |       |           | Tag 0.9.15 not found in the repo   |                   404 | `[]`                                                                                                             |
</details>

<details>
<summary>Source code links that could not be found(5)</summary>
    


|   index | package_name              | github_url                                      | github_exists   | parent                      |
|--------:|:--------------------------|:------------------------------------------------|:----------------|:----------------------------|
|       1 | `archy@1.0.0`             | https://github.com/substack/node-archy          | False           | `[]`                        |
|       2 | `cacheable-request@6.1.0` | https://github.com/lukechilds/cacheable-request | False           | `[]`                        |
|       3 | `commondir@1.0.1`         | https://github.com/substack/node-commondir      | False           | `[]`                        |
|       4 | `concat-map@0.0.1`        | https://github.com/substack/node-concat-map     | False           | `['brace-expansion@1.1.8']` |
|       5 | `minimist@1.2.5`          | https://github.com/substack/minimist            | False           | `[]`                        |
</details>

<details>
<summary>List of packages without provenance(509)</summary>
    


| package_name                                         | provenance_in_version   | parent                                                                                                           |
|:-----------------------------------------------------|:------------------------|:-----------------------------------------------------------------------------------------------------------------|
| `@babel/code-frame@7.12.13`                          | False                   | `[]`                                                                                                             |
| `@babel/core@7.9.6`                                  | False                   | `[]`                                                                                                             |
| `@babel/generator@7.9.6`                             | False                   | `[]`                                                                                                             |
| `@babel/helper-function-name@7.9.5`                  | False                   | `[]`                                                                                                             |
| `@babel/helper-get-function-arity@7.8.3`             | False                   | `[]`                                                                                                             |
| `@babel/helper-member-expression-to-functions@7.8.3` | False                   | `[]`                                                                                                             |
| `@babel/helper-module-imports@7.8.3`                 | False                   | `[]`                                                                                                             |
| `@babel/helper-module-transforms@7.9.0`              | False                   | `[]`                                                                                                             |
| `@babel/helper-optimise-call-expression@7.8.3`       | False                   | `[]`                                                                                                             |
| `@babel/helper-replace-supers@7.9.6`                 | False                   | `[]`                                                                                                             |
| `@babel/helper-simple-access@7.8.3`                  | False                   | `[]`                                                                                                             |
| `@babel/helper-split-export-declaration@7.8.3`       | False                   | `[]`                                                                                                             |
| `@babel/helper-validator-identifier@7.14.0`          | False                   | `[]`                                                                                                             |
| `@babel/helpers@7.9.6`                               | False                   | `[]`                                                                                                             |
| `@babel/highlight@7.14.0`                            | False                   | `[]`                                                                                                             |
| `@babel/parser@7.9.6`                                | False                   | `[]`                                                                                                             |
| `@babel/template@7.8.6`                              | False                   | `[]`                                                                                                             |
| `@babel/traverse@7.9.6`                              | False                   | `[]`                                                                                                             |
| `@babel/types@7.9.6`                                 | False                   | `[]`                                                                                                             |
| `@concordance/react@2.0.0`                           | False                   | `[]`                                                                                                             |
| `@cspotcode/source-map-consumer@0.8.0`               | False                   | `['@cspotcode/source-map-support@0.7.0']`                                                                        |
| `@cspotcode/source-map-support@0.7.0`                | False                   | `['ts-node@10.5.0']`                                                                                             |
| `@cspotcode/source-map-support@0.8.0`                | False                   | `[]`                                                                                                             |
| `@istanbuljs/load-nyc-config@1.0.0`                  | False                   | `[]`                                                                                                             |
| `@istanbuljs/schema@0.1.2`                           | False                   | `[]`                                                                                                             |
| `@jest/types@27.0.2`                                 | False                   | `[]`                                                                                                             |
| `@jridgewell/resolve-uri@3.0.6`                      | False                   | `[]`                                                                                                             |
| `@jridgewell/sourcemap-codec@1.4.11`                 | False                   | `[]`                                                                                                             |
| `@jridgewell/trace-mapping@0.3.9`                    | False                   | `['@cspotcode/source-map-support@0.8.0']`                                                                        |
| `@microsoft/api-extractor-model@7.15.3`              | False                   | `['@microsoft/api-extractor@7.19.4']`                                                                            |
| `@microsoft/api-extractor@7.19.4`                    | False                   | `[]`                                                                                                             |
| `@microsoft/tsdoc-config@0.15.2`                     | False                   | `[]`                                                                                                             |
| `@microsoft/tsdoc@0.13.2`                            | False                   | `['@microsoft/tsdoc-config@0.15.2', '@microsoft/api-extractor@7.19.4', '@microsoft/api-extractor-model@7.15.3']` |
| `@nodelib/fs.scandir@2.1.4`                          | False                   | `['@nodelib/fs.walk@1.2.6']`                                                                                     |
| `@nodelib/fs.stat@2.0.4`                             | False                   | `['@nodelib/fs.scandir@2.1.4']`                                                                                  |
| `@nodelib/fs.walk@1.2.6`                             | False                   | `[]`                                                                                                             |
| `@rushstack/node-core-library@3.45.0`                | False                   | `['@microsoft/api-extractor@7.19.4', '@microsoft/api-extractor-model@7.15.3']`                                   |
| `@rushstack/rig-package@0.3.7`                       | False                   | `['@microsoft/api-extractor@7.19.4']`                                                                            |
| `@rushstack/ts-command-line@4.10.6`                  | False                   | `['@microsoft/api-extractor@7.19.4']`                                                                            |
| `@sindresorhus/is@0.14.0`                            | False                   | `[]`                                                                                                             |
| `@swc/counter@0.1.2`                                 | False                   | `[]`                                                                                                             |
| `@swc/types@0.1.5`                                   | False                   | `[]`                                                                                                             |
| `@swc/wasm@1.3.100`                                  | False                   | `[]`                                                                                                             |
| `@szmarczak/http-timer@1.1.2`                        | False                   | `[]`                                                                                                             |
| `@tsconfig/node10@1.0.7`                             | False                   | `[]`                                                                                                             |
| `@tsconfig/node12@1.0.7`                             | False                   | `[]`                                                                                                             |
| `@tsconfig/node14@1.0.0`                             | False                   | `[]`                                                                                                             |
| `@tsconfig/node16@1.0.2`                             | False                   | `[]`                                                                                                             |
| `@types/argparse@1.0.38`                             | False                   | `['@rushstack/ts-command-line@4.10.6']`                                                                          |
| `@types/color-name@1.1.1`                            | False                   | `[]`                                                                                                             |
| `@types/diff@4.0.2`                                  | False                   | `[]`                                                                                                             |
| `@types/emscripten@1.39.4`                           | False                   | `[]`                                                                                                             |
| `@types/events@3.0.0`                                | False                   | `[]`                                                                                                             |
| `@types/glob@7.1.1`                                  | False                   | `[]`                                                                                                             |
| `@types/istanbul-lib-coverage@2.0.3`                 | False                   | `[]`                                                                                                             |
| `@types/istanbul-lib-report@3.0.0`                   | False                   | `[]`                                                                                                             |
| `@types/istanbul-reports@3.0.1`                      | False                   | `[]`                                                                                                             |
| `@types/json-schema@7.0.9`                           | False                   | `[]`                                                                                                             |
| `@types/lodash@4.14.151`                             | False                   | `[]`                                                                                                             |
| `@types/minimatch@3.0.3`                             | False                   | `[]`                                                                                                             |
| `@types/node@12.20.24`                               | False                   | `['@rushstack/node-core-library@3.45.0']`                                                                        |
| `@types/node@13.13.5`                                | False                   | `[]`                                                                                                             |
| `@types/node@16.11.25`                               | False                   | `[]`                                                                                                             |
| `@types/normalize-package-data@2.4.0`                | False                   | `[]`                                                                                                             |
| `@types/prop-types@15.7.5`                           | False                   | `[]`                                                                                                             |
| `@types/proper-lockfile@4.1.2`                       | False                   | `[]`                                                                                                             |
| `@types/proxyquire@1.3.28`                           | False                   | `[]`                                                                                                             |
| `@types/react@16.14.26`                              | False                   | `[]`                                                                                                             |
| `@types/retry@0.12.1`                                | False                   | `[]`                                                                                                             |
| `@types/rimraf@3.0.0`                                | False                   | `[]`                                                                                                             |
| `@types/scheduler@0.16.2`                            | False                   | `[]`                                                                                                             |
| `@types/semver@7.1.0`                                | False                   | `[]`                                                                                                             |
| `@types/stack-utils@2.0.0`                           | False                   | `[]`                                                                                                             |
| `@types/yargs-parser@20.2.0`                         | False                   | `[]`                                                                                                             |
| `@types/yargs@16.0.3`                                | False                   | `[]`                                                                                                             |
| `@yarnpkg/fslib@2.4.0`                               | False                   | `[]`                                                                                                             |
| `@yarnpkg/libzip@2.2.1`                              | False                   | `[]`                                                                                                             |
| `acorn-walk@8.1.1`                                   | False                   | `[]`                                                                                                             |
| `acorn@8.4.1`                                        | False                   | `[]`                                                                                                             |
| `aggregate-error@3.0.1`                              | False                   | `[]`                                                                                                             |
| `ajv@6.12.6`                                         | False                   | `[]`                                                                                                             |
| `ansi-align@3.0.0`                                   | False                   | `[]`                                                                                                             |
| `ansi-regex@4.1.0`                                   | False                   | `[]`                                                                                                             |
| `ansi-regex@5.0.0`                                   | False                   | `[]`                                                                                                             |
| `ansi-regex@5.0.1`                                   | False                   | `[]`                                                                                                             |
| `ansi-styles@3.2.1`                                  | False                   | `[]`                                                                                                             |
| `ansi-styles@4.2.1`                                  | False                   | `[]`                                                                                                             |
| `ansi-styles@4.3.0`                                  | False                   | `[]`                                                                                                             |
| `ansi-styles@5.1.0`                                  | False                   | `[]`                                                                                                             |
| `ansi-styles@5.2.0`                                  | False                   | `[]`                                                                                                             |
| `anymatch@3.1.1`                                     | False                   | `[]`                                                                                                             |
| `append-transform@2.0.0`                             | False                   | `[]`                                                                                                             |
| `archy@1.0.0`                                        | False                   | `[]`                                                                                                             |
| `arg@4.1.0`                                          | False                   | `[]`                                                                                                             |
| `argparse@1.0.9`                                     | False                   | `[]`                                                                                                             |
| `array-find-index@1.0.2`                             | False                   | `[]`                                                                                                             |
| `array-union@2.1.0`                                  | False                   | `[]`                                                                                                             |
| `arrgv@1.0.2`                                        | False                   | `[]`                                                                                                             |
| `arrify@1.0.1`                                       | False                   | `[]`                                                                                                             |
| `arrify@2.0.1`                                       | False                   | `[]`                                                                                                             |
| `astral-regex@2.0.0`                                 | False                   | `[]`                                                                                                             |
| `ava@3.15.0`                                         | False                   | `[]`                                                                                                             |
| `axios@0.21.1`                                       | False                   | `[]`                                                                                                             |
| `balanced-match@1.0.0`                               | False                   | `[]`                                                                                                             |
| `base64-js@1.5.1`                                    | False                   | `[]`                                                                                                             |
| `binary-extensions@2.2.0`                            | False                   | `[]`                                                                                                             |
| `bl@4.1.0`                                           | False                   | `[]`                                                                                                             |
| `blueimp-md5@2.18.0`                                 | False                   | `[]`                                                                                                             |
| `boxen@5.0.0`                                        | False                   | `[]`                                                                                                             |
| `brace-expansion@1.1.8`                              | False                   | `[]`                                                                                                             |
| `braces@3.0.2`                                       | False                   | `[]`                                                                                                             |
| `buffer-from@1.1.1`                                  | False                   | `[]`                                                                                                             |
| `buffer@5.7.1`                                       | False                   | `[]`                                                                                                             |
| `cacheable-request@6.1.0`                            | False                   | `[]`                                                                                                             |
| `caching-transform@4.0.0`                            | False                   | `[]`                                                                                                             |
| `callsites@3.1.0`                                    | False                   | `[]`                                                                                                             |
| `camelcase@5.3.1`                                    | False                   | `[]`                                                                                                             |
| `camelcase@6.2.0`                                    | False                   | `[]`                                                                                                             |
| `chalk@2.4.2`                                        | False                   | `[]`                                                                                                             |
| `chalk@4.1.1`                                        | False                   | `[]`                                                                                                             |
| `chokidar@3.5.1`                                     | False                   | `[]`                                                                                                             |
| `chunkd@2.0.1`                                       | False                   | `[]`                                                                                                             |
| `ci-info@2.0.0`                                      | False                   | `[]`                                                                                                             |
| `ci-parallel-vars@1.0.1`                             | False                   | `[]`                                                                                                             |
| `clean-stack@2.2.0`                                  | False                   | `[]`                                                                                                             |
| `clean-yaml-object@0.1.0`                            | False                   | `[]`                                                                                                             |
| `cli-boxes@2.2.1`                                    | False                   | `[]`                                                                                                             |
| `cli-cursor@3.1.0`                                   | False                   | `[]`                                                                                                             |
| `cli-spinners@2.5.0`                                 | False                   | `[]`                                                                                                             |
| `cli-truncate@2.1.0`                                 | False                   | `[]`                                                                                                             |
| `cliui@6.0.0`                                        | False                   | `[]`                                                                                                             |
| `cliui@7.0.4`                                        | False                   | `[]`                                                                                                             |
| `clone-response@1.0.2`                               | False                   | `[]`                                                                                                             |
| `clone@1.0.4`                                        | False                   | `[]`                                                                                                             |
| `code-excerpt@3.0.0`                                 | False                   | `[]`                                                                                                             |
| `color-convert@1.9.3`                                | False                   | `[]`                                                                                                             |
| `color-convert@2.0.1`                                | False                   | `[]`                                                                                                             |
| `color-name@1.1.3`                                   | False                   | `['color-convert@1.9.3']`                                                                                        |
| `color-name@1.1.4`                                   | False                   | `[]`                                                                                                             |
| `colors@1.2.5`                                       | False                   | `[]`                                                                                                             |
| `commander@2.20.3`                                   | False                   | `[]`                                                                                                             |
| `common-path-prefix@3.0.0`                           | False                   | `[]`                                                                                                             |
| `commondir@1.0.1`                                    | False                   | `[]`                                                                                                             |
| `concat-map@0.0.1`                                   | False                   | `['brace-expansion@1.1.8']`                                                                                      |
| `concordance@5.0.2`                                  | False                   | `[]`                                                                                                             |
| `configstore@5.0.1`                                  | False                   | `[]`                                                                                                             |
| `convert-source-map@1.7.0`                           | False                   | `[]`                                                                                                             |
| `convert-to-spaces@1.0.2`                            | False                   | `[]`                                                                                                             |
| `create-require@1.1.0`                               | False                   | `[]`                                                                                                             |
| `cross-spawn@7.0.2`                                  | False                   | `[]`                                                                                                             |
| `crypto-random-string@2.0.0`                         | False                   | `[]`                                                                                                             |
| `csstype@3.0.11`                                     | False                   | `[]`                                                                                                             |
| `currently-unhandled@0.4.1`                          | False                   | `[]`                                                                                                             |
| `date-time@3.1.0`                                    | False                   | `[]`                                                                                                             |
| `debug@4.1.1`                                        | False                   | `[]`                                                                                                             |
| `debug@4.3.1`                                        | False                   | `[]`                                                                                                             |
| `decamelize@1.2.0`                                   | False                   | `[]`                                                                                                             |
| `decompress-response@3.3.0`                          | False                   | `[]`                                                                                                             |
| `deep-extend@0.6.0`                                  | False                   | `[]`                                                                                                             |
| `default-require-extensions@3.0.0`                   | False                   | `[]`                                                                                                             |
| `defaults@1.0.3`                                     | False                   | `[]`                                                                                                             |
| `defer-to-connect@1.1.3`                             | False                   | `[]`                                                                                                             |
| `define-properties@1.1.3`                            | False                   | `[]`                                                                                                             |
| `del@6.0.0`                                          | False                   | `[]`                                                                                                             |
| `diff-sequences@27.0.1`                              | False                   | `[]`                                                                                                             |
| `diff@4.0.1`                                         | False                   | `[]`                                                                                                             |
| `dir-glob@3.0.1`                                     | False                   | `[]`                                                                                                             |
| `dot-prop@5.3.0`                                     | False                   | `[]`                                                                                                             |
| `dprint@0.25.0`                                      | False                   | `[]`                                                                                                             |
| `duplexer3@0.1.4`                                    | False                   | `[]`                                                                                                             |
| `emittery@0.8.1`                                     | False                   | `[]`                                                                                                             |
| `emoji-regex@7.0.3`                                  | False                   | `[]`                                                                                                             |
| `emoji-regex@8.0.0`                                  | False                   | `[]`                                                                                                             |
| `end-of-stream@1.4.4`                                | False                   | `[]`                                                                                                             |
| `equal-length@1.0.1`                                 | False                   | `[]`                                                                                                             |
| `error-ex@1.3.2`                                     | False                   | `[]`                                                                                                             |
| `es-abstract@1.17.4`                                 | False                   | `[]`                                                                                                             |
| `es-to-primitive@1.2.1`                              | False                   | `[]`                                                                                                             |
| `es6-error@4.1.1`                                    | False                   | `[]`                                                                                                             |
| `escalade@3.1.1`                                     | False                   | `[]`                                                                                                             |
| `escape-goat@2.1.1`                                  | False                   | `[]`                                                                                                             |
| `escape-string-regexp@1.0.5`                         | False                   | `[]`                                                                                                             |
| `escape-string-regexp@2.0.0`                         | False                   | `[]`                                                                                                             |
| `escape-string-regexp@4.0.0`                         | False                   | `[]`                                                                                                             |
| `esprima@4.0.1`                                      | False                   | `[]`                                                                                                             |
| `esutils@2.0.3`                                      | False                   | `[]`                                                                                                             |
| `expect@27.0.2`                                      | False                   | `[]`                                                                                                             |
| `fast-deep-equal@3.1.3`                              | False                   | `[]`                                                                                                             |
| `fast-diff@1.2.0`                                    | False                   | `[]`                                                                                                             |
| `fast-glob@3.2.5`                                    | False                   | `[]`                                                                                                             |
| `fast-json-stable-stringify@2.1.0`                   | False                   | `[]`                                                                                                             |
| `fastq@1.10.1`                                       | False                   | `[]`                                                                                                             |
| `figures@3.2.0`                                      | False                   | `[]`                                                                                                             |
| `fill-keys@1.0.2`                                    | False                   | `[]`                                                                                                             |
| `fill-range@7.0.1`                                   | False                   | `[]`                                                                                                             |
| `find-cache-dir@3.3.1`                               | False                   | `[]`                                                                                                             |
| `find-up@3.0.0`                                      | False                   | `[]`                                                                                                             |
| `find-up@4.1.0`                                      | False                   | `[]`                                                                                                             |
| `follow-redirects@1.13.1`                            | False                   | `[]`                                                                                                             |
| `foreground-child@2.0.0`                             | False                   | `[]`                                                                                                             |
| `fromentries@1.2.0`                                  | False                   | `[]`                                                                                                             |
| `fs-extra@7.0.1`                                     | False                   | `[]`                                                                                                             |
| `fs.realpath@1.0.0`                                  | False                   | `[]`                                                                                                             |
| `fsevents@2.3.2`                                     | False                   | `[]`                                                                                                             |
| `function-bind@1.1.1`                                | False                   | `[]`                                                                                                             |
| `gensync@1.0.0-beta.1`                               | False                   | `[]`                                                                                                             |
| `get-caller-file@2.0.5`                              | False                   | `[]`                                                                                                             |
| `get-stream@4.1.0`                                   | False                   | `[]`                                                                                                             |
| `get-stream@5.2.0`                                   | False                   | `[]`                                                                                                             |
| `get-stream@6.0.0`                                   | False                   | `[]`                                                                                                             |
| `glob-parent@5.1.1`                                  | False                   | `[]`                                                                                                             |
| `glob@7.1.3`                                         | False                   | `[]`                                                                                                             |
| `glob@7.1.4`                                         | False                   | `[]`                                                                                                             |
| `glob@7.1.6`                                         | False                   | `[]`                                                                                                             |
| `glob@7.2.0`                                         | False                   | `[]`                                                                                                             |
| `global-dirs@3.0.0`                                  | False                   | `[]`                                                                                                             |
| `globals@11.12.0`                                    | False                   | `[]`                                                                                                             |
| `globby@11.0.2`                                      | False                   | `[]`                                                                                                             |
| `got@9.6.0`                                          | False                   | `[]`                                                                                                             |
| `graceful-fs@4.2.4`                                  | False                   | `[]`                                                                                                             |
| `has-flag@3.0.0`                                     | False                   | `[]`                                                                                                             |
| `has-flag@4.0.0`                                     | False                   | `[]`                                                                                                             |
| `has-symbols@1.0.1`                                  | False                   | `[]`                                                                                                             |
| `has-yarn@2.1.0`                                     | False                   | `[]`                                                                                                             |
| `has@1.0.3`                                          | False                   | `[]`                                                                                                             |
| `hasha@5.2.0`                                        | False                   | `[]`                                                                                                             |
| `hosted-git-info@2.8.8`                              | False                   | `[]`                                                                                                             |
| `html-escaper@2.0.2`                                 | False                   | `[]`                                                                                                             |
| `http-cache-semantics@4.1.0`                         | False                   | `[]`                                                                                                             |
| `ieee754@1.2.1`                                      | False                   | `[]`                                                                                                             |
| `ignore-by-default@2.0.0`                            | False                   | `[]`                                                                                                             |
| `ignore@5.1.8`                                       | False                   | `[]`                                                                                                             |
| `import-lazy@2.1.0`                                  | False                   | `[]`                                                                                                             |
| `import-lazy@4.0.0`                                  | False                   | `[]`                                                                                                             |
| `import-local@3.0.2`                                 | False                   | `[]`                                                                                                             |
| `imurmurhash@0.1.4`                                  | False                   | `[]`                                                                                                             |
| `indent-string@4.0.0`                                | False                   | `[]`                                                                                                             |
| `inflight@1.0.6`                                     | False                   | `[]`                                                                                                             |
| `inherits@2.0.3`                                     | False                   | `[]`                                                                                                             |
| `inherits@2.0.4`                                     | False                   | `[]`                                                                                                             |
| `ini@1.3.8`                                          | False                   | `[]`                                                                                                             |
| `ini@2.0.0`                                          | False                   | `['global-dirs@3.0.0']`                                                                                          |
| `irregular-plurals@3.2.0`                            | False                   | `[]`                                                                                                             |
| `is-arrayish@0.2.1`                                  | False                   | `[]`                                                                                                             |
| `is-binary-path@2.1.0`                               | False                   | `[]`                                                                                                             |
| `is-callable@1.1.5`                                  | False                   | `[]`                                                                                                             |
| `is-ci@2.0.0`                                        | False                   | `[]`                                                                                                             |
| `is-core-module@2.2.0`                               | False                   | `[]`                                                                                                             |
| `is-date-object@1.0.2`                               | False                   | `[]`                                                                                                             |
| `is-error@2.2.2`                                     | False                   | `[]`                                                                                                             |
| `is-extglob@2.1.1`                                   | False                   | `[]`                                                                                                             |
| `is-fullwidth-code-point@2.0.0`                      | False                   | `[]`                                                                                                             |
| `is-fullwidth-code-point@3.0.0`                      | False                   | `[]`                                                                                                             |
| `is-glob@4.0.1`                                      | False                   | `[]`                                                                                                             |
| `is-installed-globally@0.4.0`                        | False                   | `[]`                                                                                                             |
| `is-interactive@1.0.0`                               | False                   | `[]`                                                                                                             |
| `is-npm@5.0.0`                                       | False                   | `[]`                                                                                                             |
| `is-number@7.0.0`                                    | False                   | `[]`                                                                                                             |
| `is-obj@2.0.0`                                       | False                   | `[]`                                                                                                             |
| `is-object@1.0.1`                                    | False                   | `[]`                                                                                                             |
| `is-path-cwd@2.2.0`                                  | False                   | `[]`                                                                                                             |
| `is-path-inside@3.0.2`                               | False                   | `[]`                                                                                                             |
| `is-plain-object@5.0.0`                              | False                   | `[]`                                                                                                             |
| `is-promise@4.0.0`                                   | False                   | `[]`                                                                                                             |
| `is-regex@1.0.5`                                     | False                   | `[]`                                                                                                             |
| `is-stream@2.0.0`                                    | False                   | `[]`                                                                                                             |
| `is-symbol@1.0.3`                                    | False                   | `[]`                                                                                                             |
| `is-typedarray@1.0.0`                                | False                   | `[]`                                                                                                             |
| `is-windows@1.0.2`                                   | False                   | `[]`                                                                                                             |
| `is-yarn-global@0.3.0`                               | False                   | `[]`                                                                                                             |
| `isexe@2.0.0`                                        | False                   | `[]`                                                                                                             |
| `istanbul-lib-coverage@3.0.0`                        | False                   | `[]`                                                                                                             |
| `istanbul-lib-hook@3.0.0`                            | False                   | `[]`                                                                                                             |
| `istanbul-lib-instrument@4.0.3`                      | False                   | `[]`                                                                                                             |
| `istanbul-lib-processinfo@2.0.2`                     | False                   | `[]`                                                                                                             |
| `istanbul-lib-report@3.0.0`                          | False                   | `[]`                                                                                                             |
| `istanbul-lib-source-maps@4.0.0`                     | False                   | `[]`                                                                                                             |
| `istanbul-reports@3.0.2`                             | False                   | `[]`                                                                                                             |
| `jest-diff@27.0.2`                                   | False                   | `[]`                                                                                                             |
| `jest-get-type@27.0.1`                               | False                   | `[]`                                                                                                             |
| `jest-matcher-utils@27.0.2`                          | False                   | `[]`                                                                                                             |
| `jest-message-util@27.0.2`                           | False                   | `[]`                                                                                                             |
| `jest-regex-util@27.0.1`                             | False                   | `[]`                                                                                                             |
| `jju@1.4.0`                                          | False                   | `[]`                                                                                                             |
| `js-string-escape@1.0.1`                             | False                   | `[]`                                                                                                             |
| `js-tokens@4.0.0`                                    | False                   | `[]`                                                                                                             |
| `js-yaml@3.14.1`                                     | False                   | `[]`                                                                                                             |
| `jsesc@2.5.2`                                        | False                   | `[]`                                                                                                             |
| `json-buffer@3.0.0`                                  | False                   | `['keyv@3.1.0']`                                                                                                 |
| `json-parse-better-errors@1.0.2`                     | False                   | `[]`                                                                                                             |
| `json-parse-even-better-errors@2.3.1`                | False                   | `[]`                                                                                                             |
| `json-schema-traverse@0.4.1`                         | False                   | `[]`                                                                                                             |
| `json5@2.1.3`                                        | False                   | `[]`                                                                                                             |
| `jsonc-parser@3.0.0`                                 | False                   | `[]`                                                                                                             |
| `jsonfile@4.0.0`                                     | False                   | `[]`                                                                                                             |
| `keyv@3.1.0`                                         | False                   | `[]`                                                                                                             |
| `latest-version@5.1.0`                               | False                   | `[]`                                                                                                             |
| `lines-and-columns@1.1.6`                            | False                   | `[]`                                                                                                             |
| `load-json-file@5.3.0`                               | False                   | `[]`                                                                                                             |
| `locate-path@3.0.0`                                  | False                   | `[]`                                                                                                             |
| `locate-path@5.0.0`                                  | False                   | `[]`                                                                                                             |
| `lodash.flattendeep@4.4.0`                           | False                   | `[]`                                                                                                             |
| `lodash.get@4.4.2`                                   | False                   | `[]`                                                                                                             |
| `lodash.isequal@4.5.0`                               | False                   | `[]`                                                                                                             |
| `lodash@4.17.19`                                     | False                   | `[]`                                                                                                             |
| `lodash@4.17.20`                                     | False                   | `[]`                                                                                                             |
| `log-symbols@4.0.0`                                  | False                   | `[]`                                                                                                             |
| `loose-envify@1.4.0`                                 | False                   | `[]`                                                                                                             |
| `lowercase-keys@1.0.1`                               | False                   | `[]`                                                                                                             |
| `lowercase-keys@2.0.0`                               | False                   | `[]`                                                                                                             |
| `lru-cache@6.0.0`                                    | False                   | `[]`                                                                                                             |
| `lunr@2.3.9`                                         | False                   | `[]`                                                                                                             |
| `make-dir@3.1.0`                                     | False                   | `[]`                                                                                                             |
| `make-error@1.3.0`                                   | False                   | `[]`                                                                                                             |
| `map-age-cleaner@0.1.3`                              | False                   | `[]`                                                                                                             |
| `marked@3.0.8`                                       | False                   | `[]`                                                                                                             |
| `matcher@3.0.0`                                      | False                   | `[]`                                                                                                             |
| `md5-hex@3.0.1`                                      | False                   | `[]`                                                                                                             |
| `mem@8.0.0`                                          | False                   | `[]`                                                                                                             |
| `merge-descriptors@1.0.1`                            | False                   | `[]`                                                                                                             |
| `merge2@1.4.1`                                       | False                   | `[]`                                                                                                             |
| `micromatch@4.0.4`                                   | False                   | `[]`                                                                                                             |
| `mimic-fn@2.1.0`                                     | False                   | `[]`                                                                                                             |
| `mimic-fn@3.1.0`                                     | False                   | `[]`                                                                                                             |
| `mimic-response@1.0.1`                               | False                   | `[]`                                                                                                             |
| `minimatch@3.0.4`                                    | False                   | `[]`                                                                                                             |
| `minimist@1.2.5`                                     | False                   | `[]`                                                                                                             |
| `module-not-found-error@1.0.1`                       | False                   | `[]`                                                                                                             |
| `ms@2.1.1`                                           | False                   | `[]`                                                                                                             |
| `ms@2.1.2`                                           | False                   | `['debug@4.3.1']`                                                                                                |
| `ms@2.1.3`                                           | False                   | `[]`                                                                                                             |
| `node-preload@0.2.1`                                 | False                   | `[]`                                                                                                             |
| `normalize-package-data@2.5.0`                       | False                   | `[]`                                                                                                             |
| `normalize-path@3.0.0`                               | False                   | `[]`                                                                                                             |
| `normalize-url@4.5.0`                                | False                   | `[]`                                                                                                             |
| `ntypescript@1.201706190042.1`                       | False                   | `[]`                                                                                                             |
| `nyc@15.0.1`                                         | False                   | `[]`                                                                                                             |
| `object-assign@4.1.1`                                | False                   | `[]`                                                                                                             |
| `object-inspect@1.7.0`                               | False                   | `[]`                                                                                                             |
| `object-keys@1.1.1`                                  | False                   | `[]`                                                                                                             |
| `object.assign@4.1.0`                                | False                   | `[]`                                                                                                             |
| `object.getownpropertydescriptors@2.1.0`             | False                   | `[]`                                                                                                             |
| `once@1.4.0`                                         | False                   | `[]`                                                                                                             |
| `onetime@5.1.2`                                      | False                   | `[]`                                                                                                             |
| `ora@5.3.0`                                          | False                   | `[]`                                                                                                             |
| `outdent@0.8.0`                                      | False                   | `[]`                                                                                                             |
| `p-cancelable@1.1.0`                                 | False                   | `[]`                                                                                                             |
| `p-defer@1.0.0`                                      | False                   | `[]`                                                                                                             |
| `p-event@4.2.0`                                      | False                   | `[]`                                                                                                             |
| `p-finally@1.0.0`                                    | False                   | `[]`                                                                                                             |
| `p-limit@2.2.2`                                      | False                   | `[]`                                                                                                             |
| `p-locate@3.0.0`                                     | False                   | `[]`                                                                                                             |
| `p-locate@4.1.0`                                     | False                   | `[]`                                                                                                             |
| `p-map@3.0.0`                                        | False                   | `[]`                                                                                                             |
| `p-map@4.0.0`                                        | False                   | `[]`                                                                                                             |
| `p-timeout@3.2.0`                                    | False                   | `[]`                                                                                                             |
| `p-try@2.2.0`                                        | False                   | `[]`                                                                                                             |
| `package-hash@4.0.0`                                 | False                   | `[]`                                                                                                             |
| `package-json@6.5.0`                                 | False                   | `[]`                                                                                                             |
| `parse-json@4.0.0`                                   | False                   | `[]`                                                                                                             |
| `parse-json@5.2.0`                                   | False                   | `[]`                                                                                                             |
| `parse-ms@2.1.0`                                     | False                   | `[]`                                                                                                             |
| `path-exists@3.0.0`                                  | False                   | `[]`                                                                                                             |
| `path-exists@4.0.0`                                  | False                   | `[]`                                                                                                             |
| `path-is-absolute@1.0.1`                             | False                   | `[]`                                                                                                             |
| `path-key@3.1.1`                                     | False                   | `[]`                                                                                                             |
| `path-parse@1.0.6`                                   | False                   | `[]`                                                                                                             |
| `path-type@4.0.0`                                    | False                   | `[]`                                                                                                             |
| `picomatch@2.3.0`                                    | False                   | `[]`                                                                                                             |
| `pify@4.0.1`                                         | False                   | `[]`                                                                                                             |
| `pkg-conf@3.1.0`                                     | False                   | `[]`                                                                                                             |
| `pkg-dir@4.2.0`                                      | False                   | `[]`                                                                                                             |
| `plur@4.0.0`                                         | False                   | `[]`                                                                                                             |
| `prepend-http@2.0.0`                                 | False                   | `[]`                                                                                                             |
| `pretty-format@27.0.2`                               | False                   | `[]`                                                                                                             |
| `pretty-ms@7.0.1`                                    | False                   | `[]`                                                                                                             |
| `process-on-spawn@1.0.0`                             | False                   | `[]`                                                                                                             |
| `prop-types@15.7.2`                                  | False                   | `[]`                                                                                                             |
| `proper-lockfile@4.1.2`                              | False                   | `[]`                                                                                                             |
| `proxyquire@2.0.0`                                   | False                   | `[]`                                                                                                             |
| `pump@3.0.0`                                         | False                   | `[]`                                                                                                             |
| `punycode@2.1.1`                                     | False                   | `[]`                                                                                                             |
| `pupa@2.1.1`                                         | False                   | `[]`                                                                                                             |
| `queue-microtask@1.2.2`                              | False                   | `[]`                                                                                                             |
| `rc@1.2.8`                                           | False                   | `[]`                                                                                                             |
| `react-is@16.13.1`                                   | False                   | `[]`                                                                                                             |
| `react-is@17.0.2`                                    | False                   | `[]`                                                                                                             |
| `react@16.14.0`                                      | False                   | `[]`                                                                                                             |
| `read-pkg@5.2.0`                                     | False                   | `[]`                                                                                                             |
| `readable-stream@3.6.0`                              | False                   | `[]`                                                                                                             |
| `readdirp@3.5.0`                                     | False                   | `[]`                                                                                                             |
| `registry-auth-token@4.2.1`                          | False                   | `[]`                                                                                                             |
| `registry-url@5.1.0`                                 | False                   | `[]`                                                                                                             |
| `release-zalgo@1.0.0`                                | False                   | `[]`                                                                                                             |
| `require-directory@2.1.1`                            | False                   | `[]`                                                                                                             |
| `require-main-filename@2.0.0`                        | False                   | `[]`                                                                                                             |
| `resolve-cwd@3.0.0`                                  | False                   | `[]`                                                                                                             |
| `resolve-from@5.0.0`                                 | False                   | `[]`                                                                                                             |
| `resolve@1.1.7`                                      | False                   | `[]`                                                                                                             |
| `resolve@1.17.0`                                     | False                   | `[]`                                                                                                             |
| `resolve@1.19.0`                                     | False                   | `[]`                                                                                                             |
| `resolve@1.20.0`                                     | False                   | `[]`                                                                                                             |
| `responselike@1.0.2`                                 | False                   | `[]`                                                                                                             |
| `restore-cursor@3.1.0`                               | False                   | `[]`                                                                                                             |
| `retry@0.12.0`                                       | False                   | `[]`                                                                                                             |
| `reusify@1.0.4`                                      | False                   | `[]`                                                                                                             |
| `rimraf@3.0.0`                                       | False                   | `[]`                                                                                                             |
| `rimraf@3.0.2`                                       | False                   | `[]`                                                                                                             |
| `run-parallel@1.2.0`                                 | False                   | `[]`                                                                                                             |
| `safe-buffer@5.1.2`                                  | False                   | `[]`                                                                                                             |
| `safe-buffer@5.2.1`                                  | False                   | `[]`                                                                                                             |
| `safe-stable-stringify@2.3.1`                        | False                   | `[]`                                                                                                             |
| `semver-diff@3.1.1`                                  | False                   | `[]`                                                                                                             |
| `semver@5.7.1`                                       | False                   | `[]`                                                                                                             |
| `semver@6.3.0`                                       | False                   | `[]`                                                                                                             |
| `semver@7.1.3`                                       | False                   | `[]`                                                                                                             |
| `semver@7.3.4`                                       | False                   | `[]`                                                                                                             |
| `semver@7.3.5`                                       | False                   | `[]`                                                                                                             |
| `serialize-error@7.0.1`                              | False                   | `[]`                                                                                                             |
| `set-blocking@2.0.0`                                 | False                   | `[]`                                                                                                             |
| `shebang-command@2.0.0`                              | False                   | `[]`                                                                                                             |
| `shebang-regex@3.0.0`                                | False                   | `[]`                                                                                                             |
| `shiki@0.9.15`                                       | False                   | `[]`                                                                                                             |
| `signal-exit@3.0.3`                                  | False                   | `[]`                                                                                                             |
| `slash@3.0.0`                                        | False                   | `[]`                                                                                                             |
| `slice-ansi@3.0.0`                                   | False                   | `[]`                                                                                                             |
| `source-map-support@0.5.19`                          | False                   | `[]`                                                                                                             |
| `source-map@0.5.7`                                   | False                   | `[]`                                                                                                             |
| `source-map@0.6.1`                                   | False                   | `[]`                                                                                                             |
| `spawn-wrap@2.0.0`                                   | False                   | `[]`                                                                                                             |
| `spdx-correct@3.1.1`                                 | False                   | `[]`                                                                                                             |
| `spdx-exceptions@2.3.0`                              | False                   | `[]`                                                                                                             |
| `spdx-expression-parse@3.0.1`                        | False                   | `[]`                                                                                                             |
| `spdx-license-ids@3.0.7`                             | False                   | `[]`                                                                                                             |
| `sprintf-js@1.0.3`                                   | False                   | `[]`                                                                                                             |
| `stack-utils@2.0.3`                                  | False                   | `[]`                                                                                                             |
| `string-argv@0.3.1`                                  | False                   | `[]`                                                                                                             |
| `string-width@3.1.0`                                 | False                   | `[]`                                                                                                             |
| `string-width@4.2.0`                                 | False                   | `[]`                                                                                                             |
| `string-width@4.2.3`                                 | False                   | `[]`                                                                                                             |
| `string.prototype.trimleft@2.1.1`                    | False                   | `[]`                                                                                                             |
| `string.prototype.trimright@2.1.1`                   | False                   | `[]`                                                                                                             |
| `string_decoder@1.3.0`                               | False                   | `[]`                                                                                                             |
| `strip-ansi@5.2.0`                                   | False                   | `[]`                                                                                                             |
| `strip-ansi@6.0.0`                                   | False                   | `[]`                                                                                                             |
| `strip-ansi@6.0.1`                                   | False                   | `[]`                                                                                                             |
| `strip-bom@3.0.0`                                    | False                   | `[]`                                                                                                             |
| `strip-bom@4.0.0`                                    | False                   | `[]`                                                                                                             |
| `strip-json-comments@2.0.1`                          | False                   | `[]`                                                                                                             |
| `strip-json-comments@3.1.1`                          | False                   | `[]`                                                                                                             |
| `supertap@2.0.0`                                     | False                   | `[]`                                                                                                             |
| `supports-color@5.5.0`                               | False                   | `[]`                                                                                                             |
| `supports-color@7.2.0`                               | False                   | `[]`                                                                                                             |
| `temp-dir@2.0.0`                                     | False                   | `[]`                                                                                                             |
| `test-exclude@6.0.0`                                 | False                   | `[]`                                                                                                             |
| `throat@6.0.1`                                       | False                   | `[]`                                                                                                             |
| `time-zone@1.0.0`                                    | False                   | `[]`                                                                                                             |
| `timsort@0.3.0`                                      | False                   | `[]`                                                                                                             |
| `to-fast-properties@2.0.0`                           | False                   | `[]`                                                                                                             |
| `to-readable-stream@1.0.0`                           | False                   | `[]`                                                                                                             |
| `to-regex-range@5.0.1`                               | False                   | `[]`                                                                                                             |
| `trim-off-newlines@1.0.1`                            | False                   | `[]`                                                                                                             |
| `ts-node@10.5.0`                                     | False                   | `[]`                                                                                                             |
| `tslib@1.14.1`                                       | False                   | `[]`                                                                                                             |
| `type-fest@0.13.1`                                   | False                   | `[]`                                                                                                             |
| `type-fest@0.20.2`                                   | False                   | `[]`                                                                                                             |
| `type-fest@0.3.1`                                    | False                   | `[]`                                                                                                             |
| `type-fest@0.6.0`                                    | False                   | `[]`                                                                                                             |
| `type-fest@0.8.1`                                    | False                   | `[]`                                                                                                             |
| `typedarray-to-buffer@3.1.5`                         | False                   | `[]`                                                                                                             |
| `typedoc@0.22.10`                                    | False                   | `[]`                                                                                                             |
| `typescript-json-schema@0.53.0`                      | False                   | `[]`                                                                                                             |
| `typescript@4.5.5`                                   | False                   | `[]`                                                                                                             |
| `typescript@4.7.4`                                   | False                   | `[]`                                                                                                             |
| `unique-string@2.0.0`                                | False                   | `[]`                                                                                                             |
| `universalify@0.1.2`                                 | False                   | `[]`                                                                                                             |
| `update-notifier@5.1.0`                              | False                   | `[]`                                                                                                             |
| `uri-js@4.4.1`                                       | False                   | `[]`                                                                                                             |
| `url-parse-lax@3.0.0`                                | False                   | `[]`                                                                                                             |
| `util-deprecate@1.0.2`                               | False                   | `[]`                                                                                                             |
| `util.promisify@1.0.1`                               | False                   | `[]`                                                                                                             |
| `uuid@3.4.0`                                         | False                   | `[]`                                                                                                             |
| `v8-compile-cache-lib@3.0.1`                         | False                   | `[]`                                                                                                             |
| `validate-npm-package-license@3.0.4`                 | False                   | `[]`                                                                                                             |
| `validator@13.7.0`                                   | False                   | `[]`                                                                                                             |
| `vscode-oniguruma@1.6.1`                             | False                   | `[]`                                                                                                             |
| `vscode-textmate@5.2.0`                              | False                   | `['shiki@0.9.15']`                                                                                               |
| `wcwidth@1.0.1`                                      | False                   | `[]`                                                                                                             |
| `well-known-symbols@2.0.0`                           | False                   | `[]`                                                                                                             |
| `which-module@2.0.0`                                 | False                   | `[]`                                                                                                             |
| `which@2.0.2`                                        | False                   | `[]`                                                                                                             |
| `widest-line@3.1.0`                                  | False                   | `[]`                                                                                                             |
| `wrap-ansi@6.2.0`                                    | False                   | `[]`                                                                                                             |
| `wrap-ansi@7.0.0`                                    | False                   | `[]`                                                                                                             |
| `wrappy@1.0.2`                                       | False                   | `[]`                                                                                                             |
| `write-file-atomic@3.0.3`                            | False                   | `[]`                                                                                                             |
| `xdg-basedir@4.0.0`                                  | False                   | `[]`                                                                                                             |
| `y18n@4.0.0`                                         | False                   | `[]`                                                                                                             |
| `y18n@5.0.5`                                         | False                   | `[]`                                                                                                             |
| `y18n@5.0.8`                                         | False                   | `[]`                                                                                                             |
| `yallist@4.0.0`                                      | False                   | `[]`                                                                                                             |
| `yargs-parser@18.1.3`                                | False                   | `[]`                                                                                                             |
| `yargs-parser@20.2.5`                                | False                   | `[]`                                                                                                             |
| `yargs-parser@21.0.0`                                | False                   | `[]`                                                                                                             |
| `yargs@15.3.1`                                       | False                   | `[]`                                                                                                             |
| `yargs@16.2.0`                                       | False                   | `[]`                                                                                                             |
| `yargs@17.3.1`                                       | False                   | `[]`                                                                                                             |
| `yn@3.1.1`                                           | False                   | `['ts-node@10.5.0']`                                                                                             |
| `z-schema@5.0.2`                                     | False                   | `[]`                                                                                                             |
</details>

All packages have valid code signature.

All packages have code signature.

<details>
<summary>List of deprecated packages(11)</summary>
    


| package_name           | deprecated_in_version   | all_deprecated   | parent   |
|:-----------------------|:------------------------|:-----------------|:---------|
| `debug@4.1.1`          | True                    | False            | `[]`     |
| `glob@7.1.3`           | True                    | False            | `[]`     |
| `glob@7.1.4`           | True                    | False            | `[]`     |
| `glob@7.1.6`           | True                    | False            | `[]`     |
| `glob@7.2.0`           | True                    | False            | `[]`     |
| `inflight@1.0.6`       | True                    | True             | `[]`     |
| `lodash.get@4.4.2`     | True                    | True             | `[]`     |
| `lodash.isequal@4.5.0` | True                    | True             | `[]`     |
| `rimraf@3.0.0`         | True                    | False            | `[]`     |
| `rimraf@3.0.2`         | True                    | False            | `[]`     |
| `uuid@3.4.0`           | True                    | False            | `[]`     |
</details>

No aliased package found.

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

Report created on 2025-05-13 00:30:04
- Tool version: 1dfb5543
- Project Name: TypeStrong/ts-node
- Project Version: 057ac1beb118f9c42d21e876a17320ad73ea6be2
- Package Manager: npm
