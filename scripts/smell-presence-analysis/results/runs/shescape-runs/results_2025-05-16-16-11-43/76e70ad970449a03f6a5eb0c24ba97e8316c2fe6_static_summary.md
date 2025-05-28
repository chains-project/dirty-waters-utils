
# Software Supply Chain Report of ericcornelissen/shescape - 76e70ad970449a03f6a5eb0c24ba97e8316c2fe6

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
        

 ### Total packages in the supply chain: 1044


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 29

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 4

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 3

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 937

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 13

:alien: Packages that are aliased (⚠️⚠️): 4


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(29)</summary>
    


| package_name                          | sha_exists   | tag_version   | is_sha   | sha                                      | tag_url   | message                           |   status_code_for_sha | parent                  |
|:--------------------------------------|:-------------|:--------------|:---------|:-----------------------------------------|:----------|:----------------------------------|----------------------:|:------------------------|
| `@fast-check/ava@2.0.1`               | False        | `2.0.1`       | False    |                                          |           | Tag 2.0.1 not found in the repo   |                   404 | `[]`                    |
| `@jridgewell/gen-mapping@0.3.8`       | False        | `0.3.8`       | True     | 0719ff4756b9f1c6c66c244a2ef29e0229e8dcd9 |           | Tag 0.3.8 not found in the repo   |                   404 | `[]`                    |
| `@pnpm/config.env-replace@1.1.0`      | False        | `1.1.0`       | False    |                                          |           | No tags found in the repo         |                   200 | `[]`                    |
| `@pnpm/network.ca-file@1.0.2`         | False        | `1.0.2`       | False    |                                          |           | No tags found in the repo         |                   200 | `[]`                    |
| `@pnpm/npm-conf@2.3.1`                | False        | `2.3.1`       | False    |                                          |           | Tag 2.3.1 not found in the repo   |                   404 | `[]`                    |
| `@types/debug@4.1.12`                 | False        | `4.1.12`      | False    |                                          |           | Tag 4.1.12 not found in the repo  |                   404 | `[]`                    |
| `@types/estree@1.0.6`                 | False        | `1.0.6`       | False    |                                          |           | Tag 1.0.6 not found in the repo   |                   404 | `['rollup@4.34.6']`     |
| `@types/http-cache-semantics@4.0.4`   | False        | `4.0.4`       | False    |                                          |           | Tag 4.0.4 not found in the repo   |                   404 | `[]`                    |
| `@types/istanbul-lib-coverage@2.0.6`  | False        | `2.0.6`       | False    |                                          |           | Tag 2.0.6 not found in the repo   |                   404 | `[]`                    |
| `@types/json-schema@7.0.15`           | False        | `7.0.15`      | False    |                                          |           | Tag 7.0.15 not found in the repo  |                   404 | `[]`                    |
| `@types/katex@0.16.7`                 | False        | `0.16.7`      | False    |                                          |           | Tag 0.16.7 not found in the repo  |                   404 | `[]`                    |
| `@types/mdast@4.0.4`                  | False        | `4.0.4`       | False    |                                          |           | Tag 4.0.4 not found in the repo   |                   404 | `[]`                    |
| `@types/ms@0.7.34`                    | False        | `0.7.34`      | False    |                                          |           | Tag 0.7.34 not found in the repo  |                   404 | `[]`                    |
| `@types/mute-stream@0.0.4`            | False        | `0.0.4`       | False    |                                          |           | Tag 0.0.4 not found in the repo   |                   404 | `[]`                    |
| `@types/node@22.7.4`                  | False        | `22.7.4`      | False    |                                          |           | Tag 22.7.4 not found in the repo  |                   404 | `[]`                    |
| `@types/normalize-package-data@2.4.4` | False        | `2.4.4`       | False    |                                          |           | Tag 2.4.4 not found in the repo   |                   404 | `[]`                    |
| `@types/unist@2.0.11`                 | False        | `2.0.11`      | False    |                                          |           | Tag 2.0.11 not found in the repo  |                   404 | `[]`                    |
| `@types/unist@3.0.3`                  | False        | `3.0.3`       | False    |                                          |           | Tag 3.0.3 not found in the repo   |                   404 | `[]`                    |
| `@types/wrap-ansi@3.0.0`              | False        | `3.0.0`       | False    |                                          |           | Tag 3.0.0 not found in the repo   |                   404 | `[]`                    |
| `acorn-import-attributes@1.9.5`       | False        | `1.9.5`       | False    |                                          |           | Tag 1.9.5 not found in the repo   |                   404 | `[]`                    |
| `cacheable-request@10.2.14`           | False        | `10.2.14`     | False    |                                          |           | Tag 10.2.14 not found in the repo |                   404 | `[]`                    |
| `cli-progress@3.12.0`                 | False        | `3.12.0`      | False    |                                          |           | Tag 3.12.0 not found in the repo  |                   404 | `[]`                    |
| `keyv@4.5.4`                          | False        | `4.5.4`       | False    |                                          |           | Tag 4.5.4 not found in the repo   |                   404 | `[]`                    |
| `lines-and-columns@1.2.4`             | False        | `1.2.4`       | True     | 3389156275890966091dec7611105fa5d47eb964 |           | Tag 1.2.4 not found in the repo   |                   404 | `[]`                    |
| `lodash.get@4.4.2`                    | False        | `4.4.2`       | False    |                                          |           | Tag 4.4.2 not found in the repo   |                   404 | `[]`                    |
| `lodash.merge@4.6.2`                  | False        | `4.6.2`       | False    |                                          |           | Tag 4.6.2 not found in the repo   |                   404 | `[]`                    |
| `lodash.truncate@4.4.2`               | False        | `4.4.2`       | False    |                                          |           | Tag 4.4.2 not found in the repo   |                   404 | `[]`                    |
| `slashes@3.0.12`                      | False        | `3.0.12`      | False    |                                          |           | Tag 3.0.12 not found in the repo  |                   404 | `[]`                    |
| `tap-yaml@3.0.0`                      | False        | `3.0.0`       | True     | 7c022d052fef858727bb58dc37f508a76a6e062b |           | Tag 3.0.0 not found in the repo   |                   404 | `['tap-parser@17.0.0']` |
</details>

<details>
<summary>Source code links that could not be found(7)</summary>
    


|   index | package_name                     | github_url                                    | github_exists   | parent                       |
|--------:|:---------------------------------|:----------------------------------------------|:----------------|:-----------------------------|
|       1 | `@andrewbranch/untar.js@1.0.3`   | No_repo_info_found                            |                 | `[]`                         |
|       2 | `micro-spelling-correcter@1.1.1` | No_repo_info_found                            |                 | `[]`                         |
|       3 | `minipass-pipeline@1.2.4`        | No_repo_info_found                            |                 | `[]`                         |
|       4 | `promise-all-reject-late@1.0.1`  | No_repo_info_found                            |                 | `[]`                         |
|       5 | `concat-map@0.0.1`               | https://github.com/substack/node-concat-map   | False           | `['brace-expansion@1.1.11']` |
|       6 | `file-entry-cache@8.0.0`         | https://github.com/jaredwray/file-entry-cache | False           | `[]`                         |
|       7 | `flat-cache@4.0.1`               | https://github.com/jaredwray/flat-cache       | False           | `[]`                         |
</details>

<details>
<summary>List of packages without provenance(937)</summary>
    


| package_name                                                 | provenance_in_version   | parent                                                          |
|:-------------------------------------------------------------|:------------------------|:----------------------------------------------------------------|
| `@ampproject/remapping@2.3.0`                                | False                   | `[]`                                                            |
| `@andrewbranch/untar.js@1.0.3`                               | False                   | `[]`                                                            |
| `@arethetypeswrong/cli@0.17.2`                               | False                   | `[]`                                                            |
| `@arethetypeswrong/core@0.17.2`                              | False                   | `['@arethetypeswrong/cli@0.17.2']`                              |
| `@babel/code-frame@7.26.2`                                   | False                   | `[]`                                                            |
| `@babel/compat-data@7.26.3`                                  | False                   | `[]`                                                            |
| `@babel/core@7.25.9`                                         | False                   | `[]`                                                            |
| `@babel/generator@7.25.9`                                    | False                   | `[]`                                                            |
| `@babel/generator@7.26.3`                                    | False                   | `[]`                                                            |
| `@babel/helper-annotate-as-pure@7.25.9`                      | False                   | `[]`                                                            |
| `@babel/helper-compilation-targets@7.25.9`                   | False                   | `[]`                                                            |
| `@babel/helper-create-class-features-plugin@7.25.9`          | False                   | `[]`                                                            |
| `@babel/helper-member-expression-to-functions@7.25.9`        | False                   | `[]`                                                            |
| `@babel/helper-module-imports@7.25.9`                        | False                   | `[]`                                                            |
| `@babel/helper-module-transforms@7.26.0`                     | False                   | `[]`                                                            |
| `@babel/helper-optimise-call-expression@7.25.9`              | False                   | `[]`                                                            |
| `@babel/helper-plugin-utils@7.25.9`                          | False                   | `[]`                                                            |
| `@babel/helper-replace-supers@7.25.9`                        | False                   | `[]`                                                            |
| `@babel/helper-skip-transparent-expression-wrappers@7.25.9`  | False                   | `[]`                                                            |
| `@babel/helper-string-parser@7.25.9`                         | False                   | `[]`                                                            |
| `@babel/helper-validator-identifier@7.25.9`                  | False                   | `[]`                                                            |
| `@babel/helper-validator-option@7.25.9`                      | False                   | `[]`                                                            |
| `@babel/helpers@7.26.0`                                      | False                   | `[]`                                                            |
| `@babel/parser@7.25.9`                                       | False                   | `[]`                                                            |
| `@babel/parser@7.26.3`                                       | False                   | `[]`                                                            |
| `@babel/plugin-proposal-decorators@7.24.7`                   | False                   | `[]`                                                            |
| `@babel/plugin-proposal-explicit-resource-management@7.25.9` | False                   | `[]`                                                            |
| `@babel/plugin-syntax-decorators@7.25.9`                     | False                   | `[]`                                                            |
| `@babel/plugin-syntax-jsx@7.25.9`                            | False                   | `[]`                                                            |
| `@babel/plugin-syntax-typescript@7.25.9`                     | False                   | `[]`                                                            |
| `@babel/plugin-transform-modules-commonjs@7.26.3`            | False                   | `[]`                                                            |
| `@babel/plugin-transform-typescript@7.26.3`                  | False                   | `[]`                                                            |
| `@babel/preset-typescript@7.24.7`                            | False                   | `[]`                                                            |
| `@babel/template@7.25.9`                                     | False                   | `[]`                                                            |
| `@babel/traverse@7.26.4`                                     | False                   | `[]`                                                            |
| `@babel/types@7.26.3`                                        | False                   | `[]`                                                            |
| `@bcoe/v8-coverage@1.0.1`                                    | False                   | `[]`                                                            |
| `@blueoak/list@15.0.0`                                       | False                   | `[]`                                                            |
| `@colors/colors@1.5.0`                                       | False                   | `[]`                                                            |
| `@es-joy/jsdoccomment@0.49.0`                                | False                   | `[]`                                                            |
| `@eslint-community/eslint-utils@4.4.0`                       | False                   | `[]`                                                            |
| `@eslint/core@0.10.0`                                        | False                   | `[]`                                                            |
| `@eslint/js@9.19.0`                                          | False                   | `['eslint@9.19.0']`                                             |
| `@eslint/plugin-kit@0.2.5`                                   | False                   | `[]`                                                            |
| `@gar/promisify@1.1.3`                                       | False                   | `[]`                                                            |
| `@humanfs/core@0.19.1`                                       | False                   | `[]`                                                            |
| `@humanfs/node@0.16.6`                                       | False                   | `[]`                                                            |
| `@humanwhocodes/module-importer@1.0.1`                       | False                   | `[]`                                                            |
| `@humanwhocodes/momoa@3.3.5`                                 | False                   | `[]`                                                            |
| `@humanwhocodes/retry@0.3.1`                                 | False                   | `[]`                                                            |
| `@humanwhocodes/retry@0.4.1`                                 | False                   | `[]`                                                            |
| `@inquirer/checkbox@3.0.1`                                   | False                   | `[]`                                                            |
| `@inquirer/confirm@4.0.1`                                    | False                   | `[]`                                                            |
| `@inquirer/core@9.2.1`                                       | False                   | `[]`                                                            |
| `@inquirer/editor@3.0.1`                                     | False                   | `[]`                                                            |
| `@inquirer/expand@3.0.1`                                     | False                   | `[]`                                                            |
| `@inquirer/figures@1.0.6`                                    | False                   | `[]`                                                            |
| `@inquirer/input@3.0.1`                                      | False                   | `[]`                                                            |
| `@inquirer/number@2.0.1`                                     | False                   | `[]`                                                            |
| `@inquirer/password@3.0.1`                                   | False                   | `[]`                                                            |
| `@inquirer/prompts@6.0.1`                                    | False                   | `[]`                                                            |
| `@inquirer/rawlist@3.0.1`                                    | False                   | `[]`                                                            |
| `@inquirer/search@2.0.1`                                     | False                   | `[]`                                                            |
| `@inquirer/select@3.0.1`                                     | False                   | `[]`                                                            |
| `@inquirer/type@2.0.0`                                       | False                   | `[]`                                                            |
| `@isaacs/cliui@8.0.2`                                        | False                   | `[]`                                                            |
| `@isaacs/fs-minipass@4.0.1`                                  | False                   | `[]`                                                            |
| `@isaacs/string-locale-compare@1.1.0`                        | False                   | `[]`                                                            |
| `@istanbuljs/schema@0.1.3`                                   | False                   | `[]`                                                            |
| `@jridgewell/gen-mapping@0.3.8`                              | False                   | `[]`                                                            |
| `@jridgewell/resolve-uri@3.1.2`                              | False                   | `[]`                                                            |
| `@jridgewell/set-array@1.2.1`                                | False                   | `[]`                                                            |
| `@jridgewell/sourcemap-codec@1.5.0`                          | False                   | `[]`                                                            |
| `@jridgewell/trace-mapping@0.3.25`                           | False                   | `[]`                                                            |
| `@mapbox/node-pre-gyp@2.0.0-rc.0`                            | False                   | `[]`                                                            |
| `@nodelib/fs.scandir@2.1.5`                                  | False                   | `['@nodelib/fs.walk@1.2.8']`                                    |
| `@nodelib/fs.stat@2.0.5`                                     | False                   | `['@nodelib/fs.scandir@2.1.5']`                                 |
| `@nodelib/fs.walk@1.2.8`                                     | False                   | `[]`                                                            |
| `@npmcli/arborist@6.5.1`                                     | False                   | `[]`                                                            |
| `@npmcli/arborist@7.5.4`                                     | False                   | `[]`                                                            |
| `@npmcli/fs@2.1.2`                                           | False                   | `[]`                                                            |
| `@npmcli/fs@3.1.1`                                           | False                   | `[]`                                                            |
| `@npmcli/metavuln-calculator@5.0.1`                          | False                   | `[]`                                                            |
| `@npmcli/move-file@2.0.1`                                    | False                   | `[]`                                                            |
| `@npmcli/name-from-folder@2.0.0`                             | False                   | `[]`                                                            |
| `@npmcli/node-gyp@3.0.0`                                     | False                   | `[]`                                                            |
| `@npmcli/promise-spawn@6.0.2`                                | False                   | `[]`                                                            |
| `@pkgjs/parseargs@0.11.0`                                    | False                   | `[]`                                                            |
| `@pkgr/core@0.1.1`                                           | False                   | `[]`                                                            |
| `@pnpm/config.env-replace@1.1.0`                             | False                   | `[]`                                                            |
| `@pnpm/network.ca-file@1.0.2`                                | False                   | `[]`                                                            |
| `@pnpm/npm-conf@2.3.1`                                       | False                   | `[]`                                                            |
| `@rollup/pluginutils@5.1.3`                                  | False                   | `[]`                                                            |
| `@rollup/rollup-android-arm-eabi@4.34.6`                     | False                   | `[]`                                                            |
| `@rollup/rollup-android-arm64@4.34.6`                        | False                   | `[]`                                                            |
| `@rollup/rollup-darwin-arm64@4.34.6`                         | False                   | `[]`                                                            |
| `@rollup/rollup-darwin-x64@4.34.6`                           | False                   | `[]`                                                            |
| `@rollup/rollup-freebsd-arm64@4.34.6`                        | False                   | `[]`                                                            |
| `@rollup/rollup-freebsd-x64@4.34.6`                          | False                   | `[]`                                                            |
| `@rollup/rollup-linux-arm-gnueabihf@4.34.6`                  | False                   | `[]`                                                            |
| `@rollup/rollup-linux-arm-musleabihf@4.34.6`                 | False                   | `[]`                                                            |
| `@rollup/rollup-linux-arm64-gnu@4.34.6`                      | False                   | `[]`                                                            |
| `@rollup/rollup-linux-arm64-musl@4.34.6`                     | False                   | `[]`                                                            |
| `@rollup/rollup-linux-loongarch64-gnu@4.34.6`                | False                   | `[]`                                                            |
| `@rollup/rollup-linux-powerpc64le-gnu@4.34.6`                | False                   | `[]`                                                            |
| `@rollup/rollup-linux-riscv64-gnu@4.34.6`                    | False                   | `[]`                                                            |
| `@rollup/rollup-linux-s390x-gnu@4.34.6`                      | False                   | `[]`                                                            |
| `@rollup/rollup-linux-x64-gnu@4.34.6`                        | False                   | `[]`                                                            |
| `@rollup/rollup-linux-x64-musl@4.34.6`                       | False                   | `[]`                                                            |
| `@rollup/rollup-win32-arm64-msvc@4.34.6`                     | False                   | `[]`                                                            |
| `@rollup/rollup-win32-ia32-msvc@4.34.6`                      | False                   | `[]`                                                            |
| `@rollup/rollup-win32-x64-msvc@4.34.6`                       | False                   | `[]`                                                            |
| `@sindresorhus/is@4.6.0`                                     | False                   | `[]`                                                            |
| `@sindresorhus/is@5.6.0`                                     | False                   | `[]`                                                            |
| `@sindresorhus/merge-streams@2.3.0`                          | False                   | `[]`                                                            |
| `@sindresorhus/merge-streams@4.0.0`                          | False                   | `[]`                                                            |
| `@sinonjs/commons@3.0.1`                                     | False                   | `[]`                                                            |
| `@sinonjs/fake-timers@13.0.2`                                | False                   | `[]`                                                            |
| `@sinonjs/samsam@8.0.2`                                      | False                   | `[]`                                                            |
| `@sinonjs/text-encoding@0.7.3`                               | False                   | `[]`                                                            |
| `@szmarczak/http-timer@5.0.1`                                | False                   | `[]`                                                            |
| `@tootallnate/once@2.0.0`                                    | False                   | `[]`                                                            |
| `@types/debug@4.1.12`                                        | False                   | `[]`                                                            |
| `@types/estree@1.0.6`                                        | False                   | `['rollup@4.34.6']`                                             |
| `@types/http-cache-semantics@4.0.4`                          | False                   | `[]`                                                            |
| `@types/istanbul-lib-coverage@2.0.6`                         | False                   | `[]`                                                            |
| `@types/json-schema@7.0.15`                                  | False                   | `[]`                                                            |
| `@types/katex@0.16.7`                                        | False                   | `[]`                                                            |
| `@types/mdast@4.0.4`                                         | False                   | `[]`                                                            |
| `@types/ms@0.7.34`                                           | False                   | `[]`                                                            |
| `@types/mute-stream@0.0.4`                                   | False                   | `[]`                                                            |
| `@types/node@22.7.4`                                         | False                   | `[]`                                                            |
| `@types/normalize-package-data@2.4.4`                        | False                   | `[]`                                                            |
| `@types/unist@2.0.11`                                        | False                   | `[]`                                                            |
| `@types/unist@3.0.3`                                         | False                   | `[]`                                                            |
| `@types/wrap-ansi@3.0.0`                                     | False                   | `[]`                                                            |
| `@vercel/nft@0.27.9`                                         | False                   | `[]`                                                            |
| `@yarnpkg/parsers@3.0.2`                                     | False                   | `[]`                                                            |
| `abbrev@1.1.1`                                               | False                   | `[]`                                                            |
| `abbrev@2.0.0`                                               | False                   | `[]`                                                            |
| `acorn-import-attributes@1.9.5`                              | False                   | `[]`                                                            |
| `acorn-jsx@5.3.2`                                            | False                   | `[]`                                                            |
| `acorn-walk@8.3.4`                                           | False                   | `[]`                                                            |
| `acorn@8.14.0`                                               | False                   | `[]`                                                            |
| `agent-base@6.0.2`                                           | False                   | `[]`                                                            |
| `agent-base@7.1.1`                                           | False                   | `[]`                                                            |
| `agent-base@7.1.3`                                           | False                   | `[]`                                                            |
| `agentkeepalive@4.5.0`                                       | False                   | `[]`                                                            |
| `aggregate-error@3.1.0`                                      | False                   | `[]`                                                            |
| `ajv@6.12.6`                                                 | False                   | `[]`                                                            |
| `ajv@8.17.1`                                                 | False                   | `[]`                                                            |
| `all-node-versions@13.0.0`                                   | False                   | `[]`                                                            |
| `angular-html-parser@6.0.2`                                  | False                   | `[]`                                                            |
| `ansi-align@3.0.1`                                           | False                   | `[]`                                                            |
| `ansi-escapes@4.3.2`                                         | False                   | `[]`                                                            |
| `ansi-escapes@7.0.0`                                         | False                   | `[]`                                                            |
| `ansi-regex@5.0.1`                                           | False                   | `[]`                                                            |
| `ansi-regex@6.1.0`                                           | False                   | `[]`                                                            |
| `ansi-styles@4.3.0`                                          | False                   | `[]`                                                            |
| `ansi-styles@6.2.1`                                          | False                   | `[]`                                                            |
| `any-promise@1.3.0`                                          | False                   | `[]`                                                            |
| `aproba@2.0.0`                                               | False                   | `[]`                                                            |
| `are-docs-informative@0.0.2`                                 | False                   | `[]`                                                            |
| `are-we-there-yet@3.0.1`                                     | False                   | `[]`                                                            |
| `argparse@1.0.10`                                            | False                   | `[]`                                                            |
| `argparse@2.0.1`                                             | False                   | `[]`                                                            |
| `array-buffer-byte-length@1.0.1`                             | False                   | `[]`                                                            |
| `array-find-index@1.0.2`                                     | False                   | `[]`                                                            |
| `array.prototype.flat@1.3.2`                                 | False                   | `[]`                                                            |
| `array.prototype.map@1.0.7`                                  | False                   | `[]`                                                            |
| `array.prototype.some@1.1.6`                                 | False                   | `[]`                                                            |
| `array.prototype.tosorted@1.1.4`                             | False                   | `[]`                                                            |
| `arraybuffer.prototype.slice@1.0.3`                          | False                   | `[]`                                                            |
| `arrgv@1.0.2`                                                | False                   | `[]`                                                            |
| `arrify@3.0.0`                                               | False                   | `[]`                                                            |
| `asap@2.0.6`                                                 | False                   | `[]`                                                            |
| `astral-regex@2.0.0`                                         | False                   | `[]`                                                            |
| `async-sema@3.1.1`                                           | False                   | `[]`                                                            |
| `atomically@2.0.3`                                           | False                   | `[]`                                                            |
| `ava@6.2.0`                                                  | False                   | `[]`                                                            |
| `available-typed-arrays@1.0.7`                               | False                   | `[]`                                                            |
| `b4a@1.6.7`                                                  | False                   | `[]`                                                            |
| `balanced-match@1.0.2`                                       | False                   | `[]`                                                            |
| `bare-events@2.5.0`                                          | False                   | `[]`                                                            |
| `bare-fs@2.3.5`                                              | False                   | `[]`                                                            |
| `bare-os@2.4.4`                                              | False                   | `[]`                                                            |
| `bare-path@2.1.3`                                            | False                   | `[]`                                                            |
| `bare-stream@2.3.0`                                          | False                   | `[]`                                                            |
| `better-npm-audit@3.9.0`                                     | False                   | `[]`                                                            |
| `bindings@1.5.0`                                             | False                   | `[]`                                                            |
| `blueimp-md5@2.19.0`                                         | False                   | `[]`                                                            |
| `boxen@8.0.1`                                                | False                   | `[]`                                                            |
| `brace-expansion@1.1.11`                                     | False                   | `[]`                                                            |
| `brace-expansion@2.0.1`                                      | False                   | `[]`                                                            |
| `braces@3.0.3`                                               | False                   | `[]`                                                            |
| `browserslist@4.24.2`                                        | False                   | `[]`                                                            |
| `builtin-modules@3.3.0`                                      | False                   | `[]`                                                            |
| `c8@10.1.3`                                                  | False                   | `[]`                                                            |
| `cacache@16.1.3`                                             | False                   | `[]`                                                            |
| `cacheable-lookup@7.0.0`                                     | False                   | `[]`                                                            |
| `cacheable-request@10.2.14`                                  | False                   | `[]`                                                            |
| `cachedir@2.4.0`                                             | False                   | `[]`                                                            |
| `call-bind@1.0.7`                                            | False                   | `[]`                                                            |
| `callsites@3.1.0`                                            | False                   | `[]`                                                            |
| `callsites@4.2.0`                                            | False                   | `[]`                                                            |
| `camelcase@8.0.0`                                            | False                   | `[]`                                                            |
| `caniuse-lite@1.0.30001688`                                  | False                   | `[]`                                                            |
| `cbor@9.0.2`                                                 | False                   | `[]`                                                            |
| `ccount@2.0.1`                                               | False                   | `[]`                                                            |
| `chalk-string@3.0.0`                                         | False                   | `[]`                                                            |
| `chalk@4.1.2`                                                | False                   | `[]`                                                            |
| `chalk@5.3.0`                                                | False                   | `[]`                                                            |
| `char-regex@1.0.2`                                           | False                   | `[]`                                                            |
| `character-entities-legacy@3.0.0`                            | False                   | `[]`                                                            |
| `character-entities@2.0.2`                                   | False                   | `[]`                                                            |
| `character-reference-invalid@2.0.1`                          | False                   | `[]`                                                            |
| `chardet@0.7.0`                                              | False                   | `[]`                                                            |
| `chownr@2.0.0`                                               | False                   | `[]`                                                            |
| `chownr@3.0.0`                                               | False                   | `[]`                                                            |
| `chunkd@2.0.1`                                               | False                   | `[]`                                                            |
| `ci-info@4.1.0`                                              | False                   | `[]`                                                            |
| `ci-parallel-vars@1.0.1`                                     | False                   | `[]`                                                            |
| `cjs-module-lexer@1.4.1`                                     | False                   | `[]`                                                            |
| `clean-regexp@1.0.0`                                         | False                   | `[]`                                                            |
| `clean-stack@2.2.0`                                          | False                   | `[]`                                                            |
| `cli-boxes@3.0.0`                                            | False                   | `[]`                                                            |
| `cli-highlight@2.1.11`                                       | False                   | `[]`                                                            |
| `cli-progress@3.12.0`                                        | False                   | `[]`                                                            |
| `cli-table3@0.6.5`                                           | False                   | `[]`                                                            |
| `cli-truncate@4.0.0`                                         | False                   | `[]`                                                            |
| `cli-width@4.1.0`                                            | False                   | `[]`                                                            |
| `cliui@7.0.4`                                                | False                   | `[]`                                                            |
| `cliui@8.0.1`                                                | False                   | `[]`                                                            |
| `code-excerpt@4.0.0`                                         | False                   | `[]`                                                            |
| `color-convert@2.0.1`                                        | False                   | `[]`                                                            |
| `color-name@1.1.4`                                           | False                   | `[]`                                                            |
| `color-support@1.1.3`                                        | False                   | `[]`                                                            |
| `colors-option@6.0.0`                                        | False                   | `[]`                                                            |
| `colors@1.4.0`                                               | False                   | `[]`                                                            |
| `commander@10.0.1`                                           | False                   | `[]`                                                            |
| `commander@12.1.0`                                           | False                   | `[]`                                                            |
| `commander@13.1.0`                                           | False                   | `[]`                                                            |
| `commander@8.3.0`                                            | False                   | `[]`                                                            |
| `comment-parser@1.4.1`                                       | False                   | `['eslint-plugin-jsdoc@50.4.1', '@es-joy/jsdoccomment@0.49.0']` |
| `common-ancestor-path@1.0.1`                                 | False                   | `[]`                                                            |
| `common-path-prefix@3.0.0`                                   | False                   | `[]`                                                            |
| `concat-map@0.0.1`                                           | False                   | `['brace-expansion@1.1.11']`                                    |
| `concordance@5.0.4`                                          | False                   | `[]`                                                            |
| `config-chain@1.1.13`                                        | False                   | `[]`                                                            |
| `configstore@7.0.0`                                          | False                   | `[]`                                                            |
| `consola@3.2.3`                                              | False                   | `[]`                                                            |
| `console-control-strings@1.1.0`                              | False                   | `[]`                                                            |
| `convert-source-map@2.0.0`                                   | False                   | `[]`                                                            |
| `convert-to-spaces@2.0.1`                                    | False                   | `[]`                                                            |
| `core-js-compat@3.39.0`                                      | False                   | `[]`                                                            |
| `core-util-is@1.0.3`                                         | False                   | `[]`                                                            |
| `correct-license-metadata@1.4.0`                             | False                   | `[]`                                                            |
| `cosmiconfig@8.3.6`                                          | False                   | `[]`                                                            |
| `cross-spawn@7.0.6`                                          | False                   | `[]`                                                            |
| `cssesc@3.0.0`                                               | False                   | `[]`                                                            |
| `currently-unhandled@0.4.1`                                  | False                   | `[]`                                                            |
| `data-view-buffer@1.0.1`                                     | False                   | `[]`                                                            |
| `data-view-byte-length@1.0.1`                                | False                   | `[]`                                                            |
| `data-view-byte-offset@1.0.0`                                | False                   | `[]`                                                            |
| `date-time@3.1.0`                                            | False                   | `[]`                                                            |
| `dayjs@1.11.13`                                              | False                   | `[]`                                                            |
| `debug@2.6.9`                                                | False                   | `[]`                                                            |
| `debug@4.3.7`                                                | False                   | `[]`                                                            |
| `decode-named-character-reference@1.0.2`                     | False                   | `[]`                                                            |
| `decompress-response@6.0.0`                                  | False                   | `[]`                                                            |
| `deep-extend@0.6.0`                                          | False                   | `[]`                                                            |
| `deep-is@0.1.4`                                              | False                   | `[]`                                                            |
| `defer-to-connect@2.0.1`                                     | False                   | `[]`                                                            |
| `define-data-property@1.1.4`                                 | False                   | `[]`                                                            |
| `define-properties@1.2.1`                                    | False                   | `[]`                                                            |
| `delegates@1.0.0`                                            | False                   | `[]`                                                            |
| `dequal@2.0.3`                                               | False                   | `[]`                                                            |
| `des.js@1.1.0`                                               | False                   | `[]`                                                            |
| `detect-libc@2.0.3`                                          | False                   | `[]`                                                            |
| `devlop@1.1.0`                                               | False                   | `[]`                                                            |
| `diff-match-patch@1.0.5`                                     | False                   | `['@stryker-mutator/core@8.7.1']`                               |
| `diff@7.0.0`                                                 | False                   | `[]`                                                            |
| `docopt@0.6.2`                                               | False                   | `[]`                                                            |
| `dot-prop@9.0.0`                                             | False                   | `[]`                                                            |
| `dotenv@16.3.1`                                              | False                   | `[]`                                                            |
| `eastasianwidth@0.2.0`                                       | False                   | `[]`                                                            |
| `electron-to-chromium@1.5.73`                                | False                   | `[]`                                                            |
| `emittery@1.0.3`                                             | False                   | `[]`                                                            |
| `emoji-regex@10.4.0`                                         | False                   | `[]`                                                            |
| `emoji-regex@8.0.0`                                          | False                   | `[]`                                                            |
| `emoji-regex@9.2.2`                                          | False                   | `[]`                                                            |
| `emojilib@2.4.0`                                             | False                   | `[]`                                                            |
| `encoding@0.1.13`                                            | False                   | `[]`                                                            |
| `end-of-stream@1.4.4`                                        | False                   | `[]`                                                            |
| `enhance-visitors@1.0.0`                                     | False                   | `[]`                                                            |
| `entities@4.5.0`                                             | False                   | `[]`                                                            |
| `env-paths@2.2.1`                                            | False                   | `[]`                                                            |
| `environment@1.1.0`                                          | False                   | `[]`                                                            |
| `err-code@2.0.3`                                             | False                   | `[]`                                                            |
| `error-ex@1.3.2`                                             | False                   | `[]`                                                            |
| `es-abstract@1.23.3`                                         | False                   | `[]`                                                            |
| `es-array-method-boxes-properly@1.0.0`                       | False                   | `[]`                                                            |
| `es-define-property@1.0.0`                                   | False                   | `[]`                                                            |
| `es-errors@1.3.0`                                            | False                   | `[]`                                                            |
| `es-get-iterator@1.1.3`                                      | False                   | `[]`                                                            |
| `es-module-lexer@1.5.4`                                      | False                   | `[]`                                                            |
| `es-object-atoms@1.0.0`                                      | False                   | `[]`                                                            |
| `es-set-tostringtag@2.0.3`                                   | False                   | `[]`                                                            |
| `es-shim-unscopables@1.0.2`                                  | False                   | `[]`                                                            |
| `es-to-primitive@1.2.1`                                      | False                   | `[]`                                                            |
| `escalade@3.2.0`                                             | False                   | `[]`                                                            |
| `escape-goat@4.0.0`                                          | False                   | `[]`                                                            |
| `escape-string-regexp@1.0.5`                                 | False                   | `[]`                                                            |
| `escape-string-regexp@2.0.0`                                 | False                   | `[]`                                                            |
| `escape-string-regexp@4.0.0`                                 | False                   | `[]`                                                            |
| `escape-string-regexp@5.0.0`                                 | False                   | `[]`                                                            |
| `eslint-compat-utils@0.5.1`                                  | False                   | `[]`                                                            |
| `eslint-plugin-ava@15.0.1`                                   | False                   | `[]`                                                            |
| `eslint-plugin-jsdoc@50.4.1`                                 | False                   | `[]`                                                            |
| `eslint-plugin-regexp@2.6.0`                                 | False                   | `[]`                                                            |
| `eslint-plugin-unicorn@56.0.1`                               | False                   | `[]`                                                            |
| `eslint-plugin-yml@1.14.0`                                   | False                   | `[]`                                                            |
| `eslint-utils@3.0.0`                                         | False                   | `[]`                                                            |
| `eslint-visitor-keys@2.1.0`                                  | False                   | `[]`                                                            |
| `eslint@9.19.0`                                              | False                   | `[]`                                                            |
| `esprima@4.0.1`                                              | False                   | `[]`                                                            |
| `espurify@2.1.1`                                             | False                   | `[]`                                                            |
| `esquery@1.6.0`                                              | False                   | `[]`                                                            |
| `esrecurse@4.3.0`                                            | False                   | `[]`                                                            |
| `estraverse@5.3.0`                                           | False                   | `[]`                                                            |
| `estree-walker@2.0.2`                                        | False                   | `['@vercel/nft@0.27.9']`                                        |
| `esutils@2.0.3`                                              | False                   | `[]`                                                            |
| `events-to-array@2.0.3`                                      | False                   | `[]`                                                            |
| `execa@9.4.0`                                                | False                   | `[]`                                                            |
| `exponential-backoff@3.1.1`                                  | False                   | `[]`                                                            |
| `external-editor@3.1.0`                                      | False                   | `[]`                                                            |
| `fast-deep-equal@3.1.3`                                      | False                   | `[]`                                                            |
| `fast-diff@1.3.0`                                            | False                   | `[]`                                                            |
| `fast-fifo@1.3.2`                                            | False                   | `[]`                                                            |
| `fast-glob@3.3.2`                                            | False                   | `[]`                                                            |
| `fast-json-stable-stringify@2.1.0`                           | False                   | `[]`                                                            |
| `fast-levenshtein@2.0.6`                                     | False                   | `[]`                                                            |
| `fast-uri@3.0.2`                                             | False                   | `[]`                                                            |
| `fast_array_intersect@1.1.0`                                 | False                   | `[]`                                                            |
| `fastq@1.17.1`                                               | False                   | `[]`                                                            |
| `fd-package-json@1.2.0`                                      | False                   | `[]`                                                            |
| `fetch-node-website@9.0.0`                                   | False                   | `[]`                                                            |
| `fflate@0.8.2`                                               | False                   | `[]`                                                            |
| `figures@5.0.0`                                              | False                   | `[]`                                                            |
| `figures@6.1.0`                                              | False                   | `[]`                                                            |
| `file-entry-cache@8.0.0`                                     | False                   | `[]`                                                            |
| `file-uri-to-path@1.0.0`                                     | False                   | `['bindings@1.5.0']`                                            |
| `file-url@4.0.0`                                             | False                   | `[]`                                                            |
| `fill-range@7.1.1`                                           | False                   | `[]`                                                            |
| `filter-obj@5.1.0`                                           | False                   | `[]`                                                            |
| `find-up-simple@1.0.0`                                       | False                   | `[]`                                                            |
| `find-up@4.1.0`                                              | False                   | `[]`                                                            |
| `find-up@5.0.0`                                              | False                   | `[]`                                                            |
| `find-up@6.3.0`                                              | False                   | `[]`                                                            |
| `flat-cache@4.0.1`                                           | False                   | `[]`                                                            |
| `flatted@3.3.1`                                              | False                   | `[]`                                                            |
| `for-each@0.3.3`                                             | False                   | `[]`                                                            |
| `foreground-child@3.3.0`                                     | False                   | `[]`                                                            |
| `form-data-encoder@2.1.4`                                    | False                   | `[]`                                                            |
| `fs-minipass@2.1.0`                                          | False                   | `[]`                                                            |
| `fs.realpath@1.0.0`                                          | False                   | `[]`                                                            |
| `fsevents@2.3.3`                                             | False                   | `[]`                                                            |
| `function-bind@1.1.2`                                        | False                   | `[]`                                                            |
| `function.prototype.name@1.1.6`                              | False                   | `[]`                                                            |
| `functions-have-names@1.2.3`                                 | False                   | `[]`                                                            |
| `gauge@4.0.4`                                                | False                   | `[]`                                                            |
| `gensync@1.0.0-beta.2`                                       | False                   | `[]`                                                            |
| `get-caller-file@2.0.5`                                      | False                   | `[]`                                                            |
| `get-dep-tree@2.0.0`                                         | False                   | `[]`                                                            |
| `get-east-asian-width@1.2.0`                                 | False                   | `[]`                                                            |
| `get-intrinsic@1.2.4`                                        | False                   | `[]`                                                            |
| `get-json@1.1.0`                                             | False                   | `[]`                                                            |
| `get-node@15.0.1`                                            | False                   | `[]`                                                            |
| `get-stdin@9.0.0`                                            | False                   | `[]`                                                            |
| `get-stream@6.0.1`                                           | False                   | `[]`                                                            |
| `get-stream@9.0.1`                                           | False                   | `[]`                                                            |
| `get-symbol-description@1.0.2`                               | False                   | `[]`                                                            |
| `glob-parent@5.1.2`                                          | False                   | `[]`                                                            |
| `glob-parent@6.0.2`                                          | False                   | `[]`                                                            |
| `glob@10.4.5`                                                | False                   | `[]`                                                            |
| `glob@7.2.3`                                                 | False                   | `[]`                                                            |
| `glob@8.1.0`                                                 | False                   | `[]`                                                            |
| `global-cache-dir@6.0.0`                                     | False                   | `[]`                                                            |
| `global-directory@4.0.1`                                     | False                   | `[]`                                                            |
| `globals@11.12.0`                                            | False                   | `[]`                                                            |
| `globals@14.0.0`                                             | False                   | `[]`                                                            |
| `globals@15.13.0`                                            | False                   | `[]`                                                            |
| `globalthis@1.0.4`                                           | False                   | `[]`                                                            |
| `globby@14.0.2`                                              | False                   | `[]`                                                            |
| `gopd@1.0.1`                                                 | False                   | `[]`                                                            |
| `got@13.0.0`                                                 | False                   | `[]`                                                            |
| `graceful-fs@4.2.10`                                         | False                   | `['@pnpm/network.ca-file@1.0.2']`                               |
| `graceful-fs@4.2.11`                                         | False                   | `[]`                                                            |
| `handle-cli-error@5.0.0`                                     | False                   | `[]`                                                            |
| `has-bigints@1.0.2`                                          | False                   | `[]`                                                            |
| `has-flag@4.0.0`                                             | False                   | `[]`                                                            |
| `has-property-descriptors@1.0.2`                             | False                   | `[]`                                                            |
| `has-proto@1.0.3`                                            | False                   | `[]`                                                            |
| `has-symbols@1.0.3`                                          | False                   | `[]`                                                            |
| `has-tostringtag@1.0.2`                                      | False                   | `[]`                                                            |
| `has-unicode@2.0.1`                                          | False                   | `[]`                                                            |
| `hasown@2.0.2`                                               | False                   | `[]`                                                            |
| `highlight.js@10.7.3`                                        | False                   | `[]`                                                            |
| `hosted-git-info@2.8.9`                                      | False                   | `[]`                                                            |
| `hosted-git-info@6.1.1`                                      | False                   | `[]`                                                            |
| `html-escaper@2.0.2`                                         | False                   | `[]`                                                            |
| `http-cache-semantics@4.1.1`                                 | False                   | `[]`                                                            |
| `http-proxy-agent@5.0.0`                                     | False                   | `[]`                                                            |
| `http-proxy-agent@7.0.2`                                     | False                   | `[]`                                                            |
| `http2-wrapper@2.2.1`                                        | False                   | `[]`                                                            |
| `https-proxy-agent@5.0.1`                                    | False                   | `[]`                                                            |
| `https-proxy-agent@7.0.5`                                    | False                   | `[]`                                                            |
| `https-proxy-agent@7.0.6`                                    | False                   | `[]`                                                            |
| `human-signals@8.0.0`                                        | False                   | `[]`                                                            |
| `humanize-ms@1.2.1`                                          | False                   | `[]`                                                            |
| `iconv-lite@0.4.24`                                          | False                   | `[]`                                                            |
| `iconv-lite@0.6.3`                                           | False                   | `[]`                                                            |
| `ignore-by-default@2.1.0`                                    | False                   | `[]`                                                            |
| `ignore@5.3.2`                                               | False                   | `[]`                                                            |
| `ignore@7.0.3`                                               | False                   | `[]`                                                            |
| `immediate@3.0.6`                                            | False                   | `[]`                                                            |
| `import-fresh@3.3.0`                                         | False                   | `[]`                                                            |
| `import-modules@2.1.0`                                       | False                   | `[]`                                                            |
| `imurmurhash@0.1.4`                                          | False                   | `[]`                                                            |
| `indent-string@4.0.0`                                        | False                   | `[]`                                                            |
| `indent-string@5.0.0`                                        | False                   | `[]`                                                            |
| `infer-owner@1.0.4`                                          | False                   | `[]`                                                            |
| `inflight@1.0.6`                                             | False                   | `[]`                                                            |
| `inherits@2.0.4`                                             | False                   | `[]`                                                            |
| `ini@1.3.8`                                                  | False                   | `[]`                                                            |
| `internal-slot@1.0.7`                                        | False                   | `[]`                                                            |
| `ip-address@9.0.5`                                           | False                   | `[]`                                                            |
| `irregular-plurals@3.5.0`                                    | False                   | `[]`                                                            |
| `is-alphabetical@2.0.1`                                      | False                   | `[]`                                                            |
| `is-alphanumerical@2.0.1`                                    | False                   | `[]`                                                            |
| `is-arguments@1.1.1`                                         | False                   | `[]`                                                            |
| `is-array-buffer@3.0.4`                                      | False                   | `[]`                                                            |
| `is-arrayish@0.2.1`                                          | False                   | `[]`                                                            |
| `is-bigint@1.0.4`                                            | False                   | `[]`                                                            |
| `is-boolean-object@1.1.2`                                    | False                   | `[]`                                                            |
| `is-builtin-module@3.2.1`                                    | False                   | `[]`                                                            |
| `is-callable@1.2.7`                                          | False                   | `[]`                                                            |
| `is-ci@4.1.0`                                                | False                   | `[]`                                                            |
| `is-core-module@2.16.0`                                      | False                   | `[]`                                                            |
| `is-data-view@1.0.1`                                         | False                   | `[]`                                                            |
| `is-date-object@1.0.5`                                       | False                   | `[]`                                                            |
| `is-decimal@2.0.1`                                           | False                   | `[]`                                                            |
| `is-error-instance@2.0.0`                                    | False                   | `[]`                                                            |
| `is-error-instance@3.0.0`                                    | False                   | `[]`                                                            |
| `is-extglob@2.1.1`                                           | False                   | `[]`                                                            |
| `is-fullwidth-code-point@3.0.0`                              | False                   | `[]`                                                            |
| `is-fullwidth-code-point@4.0.0`                              | False                   | `[]`                                                            |
| `is-glob@4.0.3`                                              | False                   | `[]`                                                            |
| `is-hexadecimal@2.0.1`                                       | False                   | `[]`                                                            |
| `is-in-ci@1.0.0`                                             | False                   | `[]`                                                            |
| `is-installed-globally@1.0.0`                                | False                   | `[]`                                                            |
| `is-lambda@1.0.1`                                            | False                   | `[]`                                                            |
| `is-map@2.0.3`                                               | False                   | `[]`                                                            |
| `is-negative-zero@2.0.3`                                     | False                   | `[]`                                                            |
| `is-npm@6.0.0`                                               | False                   | `[]`                                                            |
| `is-number-object@1.0.7`                                     | False                   | `[]`                                                            |
| `is-number@7.0.0`                                            | False                   | `[]`                                                            |
| `is-path-inside@4.0.0`                                       | False                   | `[]`                                                            |
| `is-plain-obj@4.1.0`                                         | False                   | `[]`                                                            |
| `is-plain-object@5.0.0`                                      | False                   | `[]`                                                            |
| `is-promise@4.0.0`                                           | False                   | `[]`                                                            |
| `is-regex@1.1.4`                                             | False                   | `[]`                                                            |
| `is-set@2.0.3`                                               | False                   | `[]`                                                            |
| `is-shared-array-buffer@1.0.3`                               | False                   | `[]`                                                            |
| `is-stream@4.0.1`                                            | False                   | `[]`                                                            |
| `is-string@1.0.7`                                            | False                   | `[]`                                                            |
| `is-symbol@1.0.4`                                            | False                   | `[]`                                                            |
| `is-typed-array@1.1.13`                                      | False                   | `[]`                                                            |
| `is-unicode-supported@1.3.0`                                 | False                   | `[]`                                                            |
| `is-unicode-supported@2.1.0`                                 | False                   | `[]`                                                            |
| `is-weakref@1.0.2`                                           | False                   | `[]`                                                            |
| `is@3.3.0`                                                   | False                   | `[]`                                                            |
| `isarray@1.0.0`                                              | False                   | `[]`                                                            |
| `isarray@2.0.5`                                              | False                   | `[]`                                                            |
| `isexe@2.0.0`                                                | False                   | `[]`                                                            |
| `isexe@3.1.1`                                                | False                   | `[]`                                                            |
| `istanbul-lib-coverage@3.2.2`                                | False                   | `[]`                                                            |
| `istanbul-lib-report@3.0.1`                                  | False                   | `[]`                                                            |
| `istanbul-reports@3.1.7`                                     | False                   | `[]`                                                            |
| `iterate-iterator@1.0.2`                                     | False                   | `[]`                                                            |
| `iterate-value@1.0.2`                                        | False                   | `[]`                                                            |
| `jackspeak@3.4.3`                                            | False                   | `[]`                                                            |
| `jiti@2.4.0`                                                 | False                   | `[]`                                                            |
| `js-md4@0.3.2`                                               | False                   | `[]`                                                            |
| `js-string-escape@1.0.1`                                     | False                   | `[]`                                                            |
| `js-tokens@4.0.0`                                            | False                   | `[]`                                                            |
| `js-yaml@3.14.1`                                             | False                   | `[]`                                                            |
| `js-yaml@4.1.0`                                              | False                   | `[]`                                                            |
| `jsbn@1.1.0`                                                 | False                   | `['ip-address@9.0.5']`                                          |
| `jsdoc-type-pratt-parser@4.1.0`                              | False                   | `[]`                                                            |
| `jsesc@0.5.0`                                                | False                   | `[]`                                                            |
| `jsesc@3.1.0`                                                | False                   | `[]`                                                            |
| `json-buffer@3.0.1`                                          | False                   | `['keyv@4.5.4']`                                                |
| `json-file-plus@3.3.1`                                       | False                   | `[]`                                                            |
| `json-parse-even-better-errors@2.3.1`                        | False                   | `[]`                                                            |
| `json-schema-traverse@0.4.1`                                 | False                   | `[]`                                                            |
| `json-schema-traverse@1.0.0`                                 | False                   | `[]`                                                            |
| `json-stable-stringify-without-jsonify@1.0.1`                | False                   | `[]`                                                            |
| `json-stringify-nice@1.1.4`                                  | False                   | `[]`                                                            |
| `json5@2.2.3`                                                | False                   | `[]`                                                            |
| `jsonc-parser@3.3.1`                                         | False                   | `[]`                                                            |
| `jsonp@0.2.1`                                                | False                   | `[]`                                                            |
| `jsonparse@1.3.1`                                            | False                   | `[]`                                                            |
| `jsonpointer@5.0.1`                                          | False                   | `[]`                                                            |
| `jszip@3.10.1`                                               | False                   | `[]`                                                            |
| `just-diff-apply@5.5.0`                                      | False                   | `[]`                                                            |
| `just-diff@6.0.2`                                            | False                   | `[]`                                                            |
| `just-extend@6.2.0`                                          | False                   | `[]`                                                            |
| `katex@0.16.21`                                              | False                   | `[]`                                                            |
| `keyv@4.5.4`                                                 | False                   | `[]`                                                            |
| `ky@1.7.2`                                                   | False                   | `[]`                                                            |
| `latest-version@9.0.0`                                       | False                   | `[]`                                                            |
| `levn@0.4.1`                                                 | False                   | `[]`                                                            |
| `licensee@11.1.1`                                            | False                   | `[]`                                                            |
| `lie@3.3.0`                                                  | False                   | `[]`                                                            |
| `lines-and-columns@1.2.4`                                    | False                   | `[]`                                                            |
| `lines-and-columns@2.0.4`                                    | False                   | `[]`                                                            |
| `linkify-it@5.0.0`                                           | False                   | `[]`                                                            |
| `load-json-file@7.0.1`                                       | False                   | `[]`                                                            |
| `locate-path@5.0.0`                                          | False                   | `[]`                                                            |
| `locate-path@6.0.0`                                          | False                   | `[]`                                                            |
| `locate-path@7.2.0`                                          | False                   | `[]`                                                            |
| `lockfile-info@1.0.0`                                        | False                   | `[]`                                                            |
| `lockfile-lint-api@5.9.1`                                    | False                   | `[]`                                                            |
| `lockfile-lint@4.13.1`                                       | False                   | `[]`                                                            |
| `lodash.get@4.4.2`                                           | False                   | `[]`                                                            |
| `lodash.groupby@4.6.0`                                       | False                   | `[]`                                                            |
| `lodash.merge@4.6.2`                                         | False                   | `[]`                                                            |
| `lodash.truncate@4.4.2`                                      | False                   | `[]`                                                            |
| `lodash@4.17.21`                                             | False                   | `[]`                                                            |
| `longest-streak@3.1.0`                                       | False                   | `[]`                                                            |
| `lowercase-keys@3.0.0`                                       | False                   | `[]`                                                            |
| `lru-cache@10.4.3`                                           | False                   | `[]`                                                            |
| `lru-cache@5.1.1`                                            | False                   | `[]`                                                            |
| `lru-cache@7.18.3`                                           | False                   | `[]`                                                            |
| `ls-engines@0.9.3`                                           | False                   | `[]`                                                            |
| `make-dir@4.0.0`                                             | False                   | `[]`                                                            |
| `make-fetch-happen@10.2.1`                                   | False                   | `[]`                                                            |
| `map-age-cleaner@0.1.3`                                      | False                   | `[]`                                                            |
| `markdown-it@14.1.0`                                         | False                   | `['markdownlint@0.37.4']`                                       |
| `markdown-table@3.0.4`                                       | False                   | `[]`                                                            |
| `markdownlint-cli@0.44.0`                                    | False                   | `[]`                                                            |
| `markdownlint@0.37.4`                                        | False                   | `[]`                                                            |
| `marked-terminal@7.1.0`                                      | False                   | `[]`                                                            |
| `marked@9.1.6`                                               | False                   | `[]`                                                            |
| `matcher@5.0.0`                                              | False                   | `[]`                                                            |
| `md5-hex@3.0.1`                                              | False                   | `[]`                                                            |
| `mdast-util-find-and-replace@3.0.1`                          | False                   | `[]`                                                            |
| `mdast-util-from-markdown@2.0.2`                             | False                   | `[]`                                                            |
| `mdast-util-gfm-autolink-literal@2.0.1`                      | False                   | `[]`                                                            |
| `mdast-util-gfm-footnote@2.0.0`                              | False                   | `[]`                                                            |
| `mdast-util-gfm-strikethrough@2.0.0`                         | False                   | `[]`                                                            |
| `mdast-util-gfm-table@2.0.0`                                 | False                   | `[]`                                                            |
| `mdast-util-gfm-task-list-item@2.0.0`                        | False                   | `[]`                                                            |
| `mdast-util-gfm@3.0.0`                                       | False                   | `[]`                                                            |
| `mdast-util-phrasing@4.1.0`                                  | False                   | `[]`                                                            |
| `mdast-util-to-markdown@2.1.2`                               | False                   | `[]`                                                            |
| `mdast-util-to-string@4.0.0`                                 | False                   | `[]`                                                            |
| `mdurl@2.0.0`                                                | False                   | `[]`                                                            |
| `mem@9.0.2`                                                  | False                   | `[]`                                                            |
| `memoize@10.0.0`                                             | False                   | `[]`                                                            |
| `memorystream@0.3.1`                                         | False                   | `[]`                                                            |
| `merge2@1.4.1`                                               | False                   | `[]`                                                            |
| `micro-spelling-correcter@1.1.1`                             | False                   | `[]`                                                            |
| `micromark-core-commonmark@2.0.2`                            | False                   | `['markdownlint@0.37.4']`                                       |
| `micromark-extension-directive@3.0.2`                        | False                   | `['markdownlint@0.37.4']`                                       |
| `micromark-extension-gfm-autolink-literal@2.1.0`             | False                   | `['markdownlint@0.37.4']`                                       |
| `micromark-extension-gfm-footnote@2.1.0`                     | False                   | `['markdownlint@0.37.4']`                                       |
| `micromark-extension-gfm-strikethrough@2.1.0`                | False                   | `[]`                                                            |
| `micromark-extension-gfm-table@2.1.0`                        | False                   | `['markdownlint@0.37.4']`                                       |
| `micromark-extension-gfm-tagfilter@2.0.0`                    | False                   | `[]`                                                            |
| `micromark-extension-gfm-task-list-item@2.1.0`               | False                   | `[]`                                                            |
| `micromark-extension-gfm@3.0.0`                              | False                   | `[]`                                                            |
| `micromark-extension-math@3.1.0`                             | False                   | `['markdownlint@0.37.4']`                                       |
| `micromark-factory-destination@2.0.1`                        | False                   | `[]`                                                            |
| `micromark-factory-label@2.0.1`                              | False                   | `[]`                                                            |
| `micromark-factory-space@2.0.1`                              | False                   | `[]`                                                            |
| `micromark-factory-title@2.0.1`                              | False                   | `[]`                                                            |
| `micromark-factory-whitespace@2.0.1`                         | False                   | `[]`                                                            |
| `micromark-util-character@2.1.1`                             | False                   | `[]`                                                            |
| `micromark-util-chunked@2.0.1`                               | False                   | `[]`                                                            |
| `micromark-util-classify-character@2.0.1`                    | False                   | `[]`                                                            |
| `micromark-util-combine-extensions@2.0.1`                    | False                   | `[]`                                                            |
| `micromark-util-decode-numeric-character-reference@2.0.2`    | False                   | `[]`                                                            |
| `micromark-util-decode-string@2.0.1`                         | False                   | `[]`                                                            |
| `micromark-util-encode@2.0.1`                                | False                   | `[]`                                                            |
| `micromark-util-html-tag-name@2.0.1`                         | False                   | `[]`                                                            |
| `micromark-util-normalize-identifier@2.0.1`                  | False                   | `[]`                                                            |
| `micromark-util-resolve-all@2.0.1`                           | False                   | `[]`                                                            |
| `micromark-util-sanitize-uri@2.0.1`                          | False                   | `[]`                                                            |
| `micromark-util-subtokenize@2.0.3`                           | False                   | `[]`                                                            |
| `micromark-util-symbol@2.0.1`                                | False                   | `[]`                                                            |
| `micromark-util-types@2.0.1`                                 | False                   | `['markdownlint@0.37.4']`                                       |
| `micromark@4.0.1`                                            | False                   | `['markdownlint@0.37.4']`                                       |
| `micromatch@4.0.8`                                           | False                   | `[]`                                                            |
| `mimic-fn@4.0.0`                                             | False                   | `[]`                                                            |
| `mimic-function@5.0.1`                                       | False                   | `[]`                                                            |
| `mimic-response@3.1.0`                                       | False                   | `[]`                                                            |
| `mimic-response@4.0.0`                                       | False                   | `[]`                                                            |
| `min-indent@1.0.1`                                           | False                   | `[]`                                                            |
| `minimalistic-assert@1.0.1`                                  | False                   | `[]`                                                            |
| `minimatch@3.1.2`                                            | False                   | `[]`                                                            |
| `minimatch@5.1.6`                                            | False                   | `[]`                                                            |
| `minimatch@9.0.5`                                            | False                   | `[]`                                                            |
| `minimist@1.2.8`                                             | False                   | `[]`                                                            |
| `minipass-collect@1.0.2`                                     | False                   | `[]`                                                            |
| `minipass-collect@2.0.1`                                     | False                   | `[]`                                                            |
| `minipass-fetch@2.1.2`                                       | False                   | `[]`                                                            |
| `minipass-flush@1.0.5`                                       | False                   | `[]`                                                            |
| `minipass-json-stream@1.0.2`                                 | False                   | `[]`                                                            |
| `minipass-pipeline@1.2.4`                                    | False                   | `[]`                                                            |
| `minipass-sized@1.0.3`                                       | False                   | `[]`                                                            |
| `minipass@3.3.6`                                             | False                   | `[]`                                                            |
| `minipass@5.0.0`                                             | False                   | `[]`                                                            |
| `minipass@7.1.2`                                             | False                   | `[]`                                                            |
| `minizlib@2.1.2`                                             | False                   | `[]`                                                            |
| `minizlib@3.0.1`                                             | False                   | `[]`                                                            |
| `mkdirp@1.0.4`                                               | False                   | `[]`                                                            |
| `mkdirp@3.0.1`                                               | False                   | `[]`                                                            |
| `move-file@3.1.0`                                            | False                   | `[]`                                                            |
| `mri@1.2.0`                                                  | False                   | `[]`                                                            |
| `ms@2.0.0`                                                   | False                   | `['debug@2.6.9']`                                               |
| `ms@2.1.3`                                                   | False                   | `[]`                                                            |
| `mute-stream@1.0.0`                                          | False                   | `[]`                                                            |
| `mz@2.7.0`                                                   | False                   | `[]`                                                            |
| `natural-compare@1.4.0`                                      | False                   | `[]`                                                            |
| `negotiator@0.6.3`                                           | False                   | `[]`                                                            |
| `nise@6.1.1`                                                 | False                   | `[]`                                                            |
| `node-fetch@2.7.0`                                           | False                   | `[]`                                                            |
| `node-gyp-build@4.8.2`                                       | False                   | `[]`                                                            |
| `node-gyp@10.2.0`                                            | False                   | `[]`                                                            |
| `node-gyp@9.4.1`                                             | False                   | `[]`                                                            |
| `node-releases@2.0.19`                                       | False                   | `[]`                                                            |
| `node-version-alias@5.0.0`                                   | False                   | `[]`                                                            |
| `node.extend@2.0.3`                                          | False                   | `[]`                                                            |
| `nofilter@3.1.0`                                             | False                   | `[]`                                                            |
| `nopt@6.0.0`                                                 | False                   | `[]`                                                            |
| `normalize-exception@3.0.0`                                  | False                   | `[]`                                                            |
| `normalize-node-version@14.0.0`                              | False                   | `[]`                                                            |
| `normalize-package-data@2.5.0`                               | False                   | `[]`                                                            |
| `normalize-package-data@5.0.0`                               | False                   | `[]`                                                            |
| `normalize-url@8.0.1`                                        | False                   | `[]`                                                            |
| `npm-license-corrections@1.9.0`                              | False                   | `[]`                                                            |
| `npm-package-arg@10.1.0`                                     | False                   | `[]`                                                            |
| `npm-packlist@7.0.4`                                         | False                   | `[]`                                                            |
| `npm-run-all2@7.0.1`                                         | False                   | `[]`                                                            |
| `npm-run-path@5.3.0`                                         | False                   | `[]`                                                            |
| `npm-run-path@6.0.0`                                         | False                   | `[]`                                                            |
| `npmlog@6.0.2`                                               | False                   | `[]`                                                            |
| `npmlog@7.0.1`                                               | False                   | `[]`                                                            |
| `nve@18.0.0`                                                 | False                   | `[]`                                                            |
| `nvexeca@11.0.1`                                             | False                   | `[]`                                                            |
| `object-assign@4.1.1`                                        | False                   | `[]`                                                            |
| `object-hash@3.0.0`                                          | False                   | `[]`                                                            |
| `object-inspect@1.13.2`                                      | False                   | `[]`                                                            |
| `object-keys@1.1.1`                                          | False                   | `[]`                                                            |
| `object.assign@4.1.5`                                        | False                   | `[]`                                                            |
| `object.fromentries@2.0.8`                                   | False                   | `[]`                                                            |
| `object.groupby@1.0.3`                                       | False                   | `[]`                                                            |
| `object.values@1.2.0`                                        | False                   | `[]`                                                            |
| `once@1.4.0`                                                 | False                   | `[]`                                                            |
| `optionator@0.9.4`                                           | False                   | `[]`                                                            |
| `os-tmpdir@1.0.2`                                            | False                   | `[]`                                                            |
| `p-cancelable@3.0.0`                                         | False                   | `[]`                                                            |
| `p-defer@1.0.0`                                              | False                   | `[]`                                                            |
| `p-limit@2.3.0`                                              | False                   | `[]`                                                            |
| `p-limit@3.1.0`                                              | False                   | `[]`                                                            |
| `p-limit@4.0.0`                                              | False                   | `[]`                                                            |
| `p-locate@4.1.0`                                             | False                   | `[]`                                                            |
| `p-locate@5.0.0`                                             | False                   | `[]`                                                            |
| `p-locate@6.0.0`                                             | False                   | `[]`                                                            |
| `p-map@4.0.0`                                                | False                   | `[]`                                                            |
| `p-map@7.0.2`                                                | False                   | `[]`                                                            |
| `p-try@2.2.0`                                                | False                   | `[]`                                                            |
| `package-config@5.0.0`                                       | False                   | `[]`                                                            |
| `package-json-from-dist@1.0.1`                               | False                   | `[]`                                                            |
| `package-json@10.0.1`                                        | False                   | `[]`                                                            |
| `pako@1.0.11`                                                | False                   | `[]`                                                            |
| `parent-module@1.0.1`                                        | False                   | `[]`                                                            |
| `parse-conflict-json@3.0.1`                                  | False                   | `[]`                                                            |
| `parse-entities@4.0.2`                                       | False                   | `[]`                                                            |
| `parse-imports@2.2.1`                                        | False                   | `[]`                                                            |
| `parse-json@5.2.0`                                           | False                   | `[]`                                                            |
| `parse-json@7.1.1`                                           | False                   | `[]`                                                            |
| `parse-ms@4.0.0`                                             | False                   | `[]`                                                            |
| `parse5-htmlparser2-tree-adapter@6.0.1`                      | False                   | `[]`                                                            |
| `parse5@5.1.1`                                               | False                   | `[]`                                                            |
| `parse5@6.0.1`                                               | False                   | `[]`                                                            |
| `path-exists@4.0.0`                                          | False                   | `[]`                                                            |
| `path-exists@5.0.0`                                          | False                   | `[]`                                                            |
| `path-is-absolute@1.0.1`                                     | False                   | `[]`                                                            |
| `path-key@3.1.1`                                             | False                   | `[]`                                                            |
| `path-key@4.0.0`                                             | False                   | `[]`                                                            |
| `path-parse@1.0.7`                                           | False                   | `[]`                                                            |
| `path-scurry@1.11.1`                                         | False                   | `[]`                                                            |
| `path-to-regexp@8.2.0`                                       | False                   | `[]`                                                            |
| `path-type@4.0.0`                                            | False                   | `[]`                                                            |
| `path-type@5.0.0`                                            | False                   | `[]`                                                            |
| `picocolors@1.1.1`                                           | False                   | `[]`                                                            |
| `picomatch@2.3.1`                                            | False                   | `[]`                                                            |
| `picomatch@4.0.2`                                            | False                   | `[]`                                                            |
| `pidtree@0.6.0`                                              | False                   | `[]`                                                            |
| `pkg-dir@5.0.0`                                              | False                   | `[]`                                                            |
| `plur@5.1.0`                                                 | False                   | `[]`                                                            |
| `pluralize@8.0.0`                                            | False                   | `[]`                                                            |
| `possible-typed-array-names@1.0.0`                           | False                   | `[]`                                                            |
| `postcss-selector-parser@6.1.2`                              | False                   | `[]`                                                            |
| `preferred-node-version@5.0.0`                               | False                   | `[]`                                                            |
| `prelude-ls@1.2.1`                                           | False                   | `[]`                                                            |
| `prettier@3.5.1`                                             | False                   | `[]`                                                            |
| `pretty-ms@9.0.0`                                            | False                   | `[]`                                                            |
| `pretty-ms@9.1.0`                                            | False                   | `[]`                                                            |
| `proc-log@3.0.0`                                             | False                   | `[]`                                                            |
| `process-nextick-args@2.0.1`                                 | False                   | `[]`                                                            |
| `proggy@2.0.0`                                               | False                   | `[]`                                                            |
| `progress@2.0.3`                                             | False                   | `[]`                                                            |
| `promise-all-reject-late@1.0.1`                              | False                   | `[]`                                                            |
| `promise-call-limit@1.0.2`                                   | False                   | `[]`                                                            |
| `promise-call-limit@3.0.2`                                   | False                   | `[]`                                                            |
| `promise-deferred@2.0.4`                                     | False                   | `[]`                                                            |
| `promise-inflight@1.0.1`                                     | False                   | `[]`                                                            |
| `promise-retry@2.0.1`                                        | False                   | `[]`                                                            |
| `promise.allsettled@1.0.7`                                   | False                   | `[]`                                                            |
| `promise@8.3.0`                                              | False                   | `[]`                                                            |
| `promiseback@2.0.3`                                          | False                   | `[]`                                                            |
| `proto-list@1.2.4`                                           | False                   | `[]`                                                            |
| `pump@3.0.2`                                                 | False                   | `[]`                                                            |
| `punycode.js@2.3.1`                                          | False                   | `[]`                                                            |
| `punycode@2.3.1`                                             | False                   | `[]`                                                            |
| `pupa@3.1.0`                                                 | False                   | `[]`                                                            |
| `qs@6.13.0`                                                  | False                   | `[]`                                                            |
| `queue-microtask@1.2.3`                                      | False                   | `[]`                                                            |
| `queue-tick@1.0.1`                                           | False                   | `[]`                                                            |
| `quick-lru@5.1.1`                                            | False                   | `[]`                                                            |
| `rc@1.2.8`                                                   | False                   | `['registry-url@6.0.1']`                                        |
| `read-cmd-shim@4.0.0`                                        | False                   | `[]`                                                            |
| `read-package-json-fast@3.0.2`                               | False                   | `[]`                                                            |
| `read-pkg-up@10.1.0`                                         | False                   | `[]`                                                            |
| `read-pkg-up@7.0.1`                                          | False                   | `[]`                                                            |
| `read-pkg@5.2.0`                                             | False                   | `[]`                                                            |
| `read-pkg@8.1.0`                                             | False                   | `[]`                                                            |
| `readable-stream@2.3.8`                                      | False                   | `[]`                                                            |
| `readable-stream@3.6.2`                                      | False                   | `[]`                                                            |
| `refa@0.12.1`                                                | False                   | `[]`                                                            |
| `regexp-ast-analysis@0.7.1`                                  | False                   | `[]`                                                            |
| `regexp-tree@0.1.27`                                         | False                   | `[]`                                                            |
| `regexp.prototype.flags@1.5.3`                               | False                   | `[]`                                                            |
| `registry-auth-token@5.0.2`                                  | False                   | `[]`                                                            |
| `registry-url@6.0.1`                                         | False                   | `[]`                                                            |
| `regjsparser@0.10.0`                                         | False                   | `[]`                                                            |
| `require-directory@2.1.1`                                    | False                   | `[]`                                                            |
| `require-from-string@2.0.2`                                  | False                   | `[]`                                                            |
| `resolve-alpn@1.2.1`                                         | False                   | `[]`                                                            |
| `resolve-cwd@3.0.0`                                          | False                   | `[]`                                                            |
| `resolve-from@4.0.0`                                         | False                   | `[]`                                                            |
| `resolve-from@5.0.0`                                         | False                   | `[]`                                                            |
| `resolve@1.22.9`                                             | False                   | `[]`                                                            |
| `responselike@3.0.0`                                         | False                   | `[]`                                                            |
| `retry@0.12.0`                                               | False                   | `[]`                                                            |
| `reusify@1.0.4`                                              | False                   | `[]`                                                            |
| `rimraf@3.0.2`                                               | False                   | `[]`                                                            |
| `rimraf@5.0.10`                                              | False                   | `[]`                                                            |
| `rollup@4.34.6`                                              | False                   | `[]`                                                            |
| `run-con@1.3.2`                                              | False                   | `[]`                                                            |
| `run-parallel@1.2.0`                                         | False                   | `[]`                                                            |
| `rxjs@7.8.1`                                                 | False                   | `[]`                                                            |
| `sade@1.8.1`                                                 | False                   | `[]`                                                            |
| `safe-array-concat@1.1.2`                                    | False                   | `[]`                                                            |
| `safe-buffer@5.1.2`                                          | False                   | `[]`                                                            |
| `safe-buffer@5.2.1`                                          | False                   | `[]`                                                            |
| `safe-regex-test@1.0.3`                                      | False                   | `[]`                                                            |
| `safer-buffer@2.1.2`                                         | False                   | `[]`                                                            |
| `scslre@0.3.0`                                               | False                   | `[]`                                                            |
| `semver@5.7.2`                                               | False                   | `[]`                                                            |
| `semver@6.3.1`                                               | False                   | `[]`                                                            |
| `serialize-error@7.0.1`                                      | False                   | `[]`                                                            |
| `set-blocking@2.0.0`                                         | False                   | `[]`                                                            |
| `set-function-length@1.2.2`                                  | False                   | `[]`                                                            |
| `set-function-name@2.0.2`                                    | False                   | `[]`                                                            |
| `setimmediate@1.0.5`                                         | False                   | `[]`                                                            |
| `shebang-command@2.0.0`                                      | False                   | `[]`                                                            |
| `shebang-regex@3.0.0`                                        | False                   | `[]`                                                            |
| `shell-quote@1.8.1`                                          | False                   | `[]`                                                            |
| `side-channel@1.0.6`                                         | False                   | `[]`                                                            |
| `signal-exit@3.0.7`                                          | False                   | `[]`                                                            |
| `signal-exit@4.1.0`                                          | False                   | `[]`                                                            |
| `sinon@19.0.2`                                               | False                   | `[]`                                                            |
| `skin-tone@2.0.0`                                            | False                   | `[]`                                                            |
| `slash@5.1.0`                                                | False                   | `[]`                                                            |
| `slashes@3.0.12`                                             | False                   | `[]`                                                            |
| `slice-ansi@4.0.0`                                           | False                   | `[]`                                                            |
| `slice-ansi@5.0.0`                                           | False                   | `[]`                                                            |
| `smart-buffer@4.2.0`                                         | False                   | `[]`                                                            |
| `smol-toml@1.3.1`                                            | False                   | `[]`                                                            |
| `socks-proxy-agent@7.0.0`                                    | False                   | `[]`                                                            |
| `socks-proxy-agent@8.0.4`                                    | False                   | `[]`                                                            |
| `socks@2.8.3`                                                | False                   | `[]`                                                            |
| `source-map@0.7.4`                                           | False                   | `[]`                                                            |
| `spdx-compare@1.0.0`                                         | False                   | `[]`                                                            |
| `spdx-correct@3.2.0`                                         | False                   | `[]`                                                            |
| `spdx-exceptions@2.5.0`                                      | False                   | `[]`                                                            |
| `spdx-expression-parse@3.0.1`                                | False                   | `[]`                                                            |
| `spdx-expression-parse@4.0.0`                                | False                   | `[]`                                                            |
| `spdx-expression-validate@2.0.0`                             | False                   | `[]`                                                            |
| `spdx-license-ids@3.0.20`                                    | False                   | `[]`                                                            |
| `spdx-osi@3.0.0`                                             | False                   | `[]`                                                            |
| `spdx-ranges@2.1.1`                                          | False                   | `[]`                                                            |
| `spdx-whitelisted@1.0.0`                                     | False                   | `[]`                                                            |
| `sprintf-js@1.0.3`                                           | False                   | `[]`                                                            |
| `sprintf-js@1.1.3`                                           | False                   | `[]`                                                            |
| `ssri@9.0.1`                                                 | False                   | `[]`                                                            |
| `stack-utils@2.0.6`                                          | False                   | `[]`                                                            |
| `stop-iteration-iterator@1.0.0`                              | False                   | `[]`                                                            |
| `streamx@2.20.1`                                             | False                   | `[]`                                                            |
| `string-width@4.2.3`                                         | False                   | `[]`                                                            |
| `string-width@5.1.2`                                         | False                   | `[]`                                                            |
| `string-width@7.2.0`                                         | False                   | `[]`                                                            |
| `string.prototype.trim@1.2.9`                                | False                   | `[]`                                                            |
| `string.prototype.trimend@1.0.8`                             | False                   | `[]`                                                            |
| `string.prototype.trimstart@1.0.8`                           | False                   | `[]`                                                            |
| `string_decoder@1.1.1`                                       | False                   | `[]`                                                            |
| `strip-ansi@6.0.1`                                           | False                   | `[]`                                                            |
| `strip-ansi@7.1.0`                                           | False                   | `[]`                                                            |
| `strip-final-newline@4.0.0`                                  | False                   | `[]`                                                            |
| `strip-indent@3.0.0`                                         | False                   | `[]`                                                            |
| `strip-json-comments@2.0.1`                                  | False                   | `[]`                                                            |
| `strip-json-comments@3.1.1`                                  | False                   | `[]`                                                            |
| `stubborn-fs@1.2.5`                                          | False                   | `[]`                                                            |
| `supertap@3.0.1`                                             | False                   | `[]`                                                            |
| `supports-color@7.2.0`                                       | False                   | `[]`                                                            |
| `supports-hyperlinks@3.1.0`                                  | False                   | `[]`                                                            |
| `supports-preserve-symlinks-flag@1.0.0`                      | False                   | `[]`                                                            |
| `synckit@0.9.1`                                              | False                   | `[]`                                                            |
| `table@6.8.2`                                                | False                   | `[]`                                                            |
| `tap-parser@17.0.0`                                          | False                   | `[]`                                                            |
| `tap-yaml@3.0.0`                                             | False                   | `['tap-parser@17.0.0']`                                         |
| `tar-fs@3.0.6`                                               | False                   | `[]`                                                            |
| `tar-stream@3.1.7`                                           | False                   | `[]`                                                            |
| `tar@6.2.1`                                                  | False                   | `[]`                                                            |
| `tar@7.4.3`                                                  | False                   | `[]`                                                            |
| `temp-dir@3.0.0`                                             | False                   | `[]`                                                            |
| `test-exclude@7.0.1`                                         | False                   | `[]`                                                            |
| `text-decoder@1.2.0`                                         | False                   | `[]`                                                            |
| `thenify-all@1.6.0`                                          | False                   | `[]`                                                            |
| `thenify@3.3.1`                                              | False                   | `[]`                                                            |
| `time-zone@1.0.0`                                            | False                   | `[]`                                                            |
| `tmp-promise@3.0.3`                                          | False                   | `[]`                                                            |
| `tmp@0.0.33`                                                 | False                   | `[]`                                                            |
| `tmp@0.2.3`                                                  | False                   | `[]`                                                            |
| `to-regex-range@5.0.1`                                       | False                   | `[]`                                                            |
| `tr46@0.0.3`                                                 | False                   | `[]`                                                            |
| `tree-kill@1.2.2`                                            | False                   | `[]`                                                            |
| `treeverse@3.0.0`                                            | False                   | `[]`                                                            |
| `tslib@2.7.0`                                                | False                   | `['@stryker-mutator/core@8.7.1']`                               |
| `tunnel@0.0.6`                                               | False                   | `['typed-rest-client@2.1.0']`                                   |
| `type-check@0.4.0`                                           | False                   | `[]`                                                            |
| `type-detect@4.0.8`                                          | False                   | `['@sinonjs/commons@3.0.1']`                                    |
| `type-detect@4.1.0`                                          | False                   | `[]`                                                            |
| `type-fest@0.13.1`                                           | False                   | `[]`                                                            |
| `type-fest@0.21.3`                                           | False                   | `[]`                                                            |
| `type-fest@0.6.0`                                            | False                   | `[]`                                                            |
| `type-fest@0.8.1`                                            | False                   | `[]`                                                            |
| `type-fest@3.13.1`                                           | False                   | `[]`                                                            |
| `type-fest@4.26.1`                                           | False                   | `[]`                                                            |
| `typed-array-buffer@1.0.2`                                   | False                   | `[]`                                                            |
| `typed-array-byte-length@1.0.1`                              | False                   | `[]`                                                            |
| `typed-array-byte-offset@1.0.2`                              | False                   | `[]`                                                            |
| `typed-array-length@1.0.6`                                   | False                   | `[]`                                                            |
| `typed-inject@4.0.0`                                         | False                   | `[]`                                                            |
| `typed-rest-client@2.1.0`                                    | False                   | `[]`                                                            |
| `typescript@5.6.1-rc`                                        | False                   | `['@arethetypeswrong/core@0.17.2']`                             |
| `typescript@5.6.2`                                           | False                   | `[]`                                                            |
| `uc.micro@2.1.0`                                             | False                   | `[]`                                                            |
| `unbox-primitive@1.0.2`                                      | False                   | `[]`                                                            |
| `underscore@1.13.7`                                          | False                   | `[]`                                                            |
| `undici-types@6.19.8`                                        | False                   | `[]`                                                            |
| `unicode-emoji-modifier-base@1.0.0`                          | False                   | `[]`                                                            |
| `unicorn-magic@0.1.0`                                        | False                   | `[]`                                                            |
| `unicorn-magic@0.3.0`                                        | False                   | `[]`                                                            |
| `unique-filename@2.0.1`                                      | False                   | `[]`                                                            |
| `unique-filename@3.0.0`                                      | False                   | `[]`                                                            |
| `unique-slug@3.0.0`                                          | False                   | `[]`                                                            |
| `unique-slug@4.0.0`                                          | False                   | `[]`                                                            |
| `unist-util-is@6.0.0`                                        | False                   | `[]`                                                            |
| `unist-util-stringify-position@4.0.0`                        | False                   | `[]`                                                            |
| `unist-util-visit-parents@6.0.1`                             | False                   | `[]`                                                            |
| `unist-util-visit@5.0.0`                                     | False                   | `[]`                                                            |
| `update-browserslist-db@1.1.1`                               | False                   | `[]`                                                            |
| `update-notifier@7.3.1`                                      | False                   | `[]`                                                            |
| `uri-js@4.4.1`                                               | False                   | `[]`                                                            |
| `util-deprecate@1.0.2`                                       | False                   | `[]`                                                            |
| `v8-to-istanbul@9.3.0`                                       | False                   | `[]`                                                            |
| `validate-npm-package-license@3.0.4`                         | False                   | `[]`                                                            |
| `walk-up-path@3.0.1`                                         | False                   | `[]`                                                            |
| `webidl-conversions@3.0.1`                                   | False                   | `[]`                                                            |
| `well-known-symbols@2.0.0`                                   | False                   | `[]`                                                            |
| `whatwg-url@5.0.0`                                           | False                   | `[]`                                                            |
| `when-exit@2.1.3`                                            | False                   | `[]`                                                            |
| `which-boxed-primitive@1.0.2`                                | False                   | `[]`                                                            |
| `which-typed-array@1.1.15`                                   | False                   | `[]`                                                            |
| `which@2.0.2`                                                | False                   | `[]`                                                            |
| `which@3.0.0`                                                | False                   | `[]`                                                            |
| `wide-align@1.1.5`                                           | False                   | `[]`                                                            |
| `widest-line@5.0.0`                                          | False                   | `[]`                                                            |
| `word-wrap@1.2.5`                                            | False                   | `[]`                                                            |
| `wrap-ansi@6.2.0`                                            | False                   | `[]`                                                            |
| `wrap-ansi@7.0.0`                                            | False                   | `[]`                                                            |
| `wrap-ansi@8.1.0`                                            | False                   | `[]`                                                            |
| `wrap-ansi@9.0.0`                                            | False                   | `[]`                                                            |
| `wrappy@1.0.2`                                               | False                   | `[]`                                                            |
| `xdg-basedir@5.1.0`                                          | False                   | `[]`                                                            |
| `y18n@5.0.8`                                                 | False                   | `[]`                                                            |
| `yallist@3.1.1`                                              | False                   | `[]`                                                            |
| `yallist@4.0.0`                                              | False                   | `[]`                                                            |
| `yallist@5.0.0`                                              | False                   | `[]`                                                            |
| `yaml-eslint-parser@1.2.3`                                   | False                   | `[]`                                                            |
| `yaml-types@0.3.0`                                           | False                   | `[]`                                                            |
| `yaml@2.5.1`                                                 | False                   | `[]`                                                            |
| `yargs-parser@20.2.9`                                        | False                   | `[]`                                                            |
| `yargs-parser@21.1.1`                                        | False                   | `[]`                                                            |
| `yargs@16.2.0`                                               | False                   | `[]`                                                            |
| `yargs@17.7.2`                                               | False                   | `[]`                                                            |
| `yocto-queue@0.1.0`                                          | False                   | `[]`                                                            |
| `yocto-queue@1.1.1`                                          | False                   | `[]`                                                            |
| `yoctocolors-cjs@2.1.2`                                      | False                   | `[]`                                                            |
| `yoctocolors@2.1.1`                                          | False                   | `[]`                                                            |
| `zwitch@2.0.4`                                               | False                   | `[]`                                                            |
</details>

All packages have valid code signature.

All packages have code signature.

<details>
<summary>List of deprecated packages(13)</summary>
    


| package_name              | deprecated_in_version   | all_deprecated   | parent   |
|:--------------------------|:------------------------|:-----------------|:---------|
| `@npmcli/move-file@2.0.1` | True                    | True             | `[]`     |
| `are-we-there-yet@3.0.1`  | True                    | True             | `[]`     |
| `are-we-there-yet@4.0.2`  | True                    | True             | `[]`     |
| `gauge@4.0.4`             | True                    | True             | `[]`     |
| `gauge@5.0.2`             | True                    | True             | `[]`     |
| `glob@7.2.3`              | True                    | False            | `[]`     |
| `glob@8.1.0`              | True                    | False            | `[]`     |
| `inflight@1.0.6`          | True                    | True             | `[]`     |
| `lodash.get@4.4.2`        | True                    | True             | `[]`     |
| `npmlog@6.0.2`            | True                    | True             | `[]`     |
| `npmlog@7.0.1`            | True                    | True             | `[]`     |
| `read-package-json@6.0.4` | True                    | True             | `[]`     |
| `rimraf@3.0.2`            | True                    | False            | `[]`     |
</details>

<details>
<summary>List of aliased packages(4)</summary>
    


| package_name         | aliased_package_name   | parent   |
|:---------------------|:-----------------------|:---------|
| `shescape@2.1.1`     | `shescape-previous`    | `[]`     |
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

### Notes

<details>
    <summary>Other info:</summary>
    
- Source code repo is not hosted on GitHub:  1

    This could be due, for example, to the package being hosted on a different platform.

    This does not mean that the source code URL is invalid.

    However, for non-GitHub repositories, not all checks can currently be performed.

|   index | package_name        | github_url                                             | parent   |
|--------:|:--------------------|:-------------------------------------------------------|:---------|
|       1 | `pp-test-kit@0.5.1` | git+https://gitlab.com/ericcornelissen/pp-test-kit.git | `[]`     |
</details>


---

Report created by [dirty-waters](https://github.com/chains-project/dirty-waters/).

Report created on 2025-05-16 16:40:51
- Tool version: 6065c48e
- Project Name: ericcornelissen/shescape
- Project Version: 76e70ad970449a03f6a5eb0c24ba97e8316c2fe6
- Package Manager: npm
