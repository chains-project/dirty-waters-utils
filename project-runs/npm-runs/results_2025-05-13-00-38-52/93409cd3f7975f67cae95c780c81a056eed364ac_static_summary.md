
# Software Supply Chain Report of chaijs/chai - 93409cd3f7975f67cae95c780c81a056eed364ac

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
        

 ### Total packages in the supply chain: 526


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 34

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 1

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 6

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 515

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 8

:alien: Packages that are aliased (⚠️⚠️): 3


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(34)</summary>
    


| package_name                               | sha_exists   | tag_version   | is_sha   | sha                                      | tag_url   | message                           |   status_code_for_sha | parent                                   |
|:-------------------------------------------|:-------------|:--------------|:---------|:-----------------------------------------|:----------|:----------------------------------|----------------------:|:-----------------------------------------|
| `@types/accepts@1.3.7`                     | False        | `1.3.7`       | False    |                                          |           | Tag 1.3.7 not found in the repo   |                   404 | `[]`                                     |
| `@types/babel__code-frame@7.0.6`           | False        | `7.0.6`       | False    |                                          |           | Tag 7.0.6 not found in the repo   |                   404 | `[]`                                     |
| `@types/body-parser@1.19.5`                | False        | `1.19.5`      | False    |                                          |           | Tag 1.19.5 not found in the repo  |                   404 | `[]`                                     |
| `@types/co-body@6.1.3`                     | False        | `6.1.3`       | False    |                                          |           | Tag 6.1.3 not found in the repo   |                   404 | `[]`                                     |
| `@types/command-line-args@5.2.3`           | False        | `5.2.3`       | False    |                                          |           | Tag 5.2.3 not found in the repo   |                   404 | `[]`                                     |
| `@types/connect@3.4.38`                    | False        | `3.4.38`      | False    |                                          |           | Tag 3.4.38 not found in the repo  |                   404 | `[]`                                     |
| `@types/content-disposition@0.5.8`         | False        | `0.5.8`       | False    |                                          |           | Tag 0.5.8 not found in the repo   |                   404 | `[]`                                     |
| `@types/convert-source-map@2.0.3`          | False        | `2.0.3`       | False    |                                          |           | Tag 2.0.3 not found in the repo   |                   404 | `[]`                                     |
| `@types/cookies@0.7.10`                    | False        | `0.7.10`      | False    |                                          |           | Tag 0.7.10 not found in the repo  |                   404 | `[]`                                     |
| `@types/debounce@1.2.4`                    | False        | `1.2.4`       | False    |                                          |           | Tag 1.2.4 not found in the repo   |                   404 | `[]`                                     |
| `@types/estree@1.0.5`                      | False        | `1.0.5`       | False    |                                          |           | Tag 1.0.5 not found in the repo   |                   404 | `['rollup@4.22.4']`                      |
| `@types/express-serve-static-core@4.17.41` | False        | `4.17.41`     | False    |                                          |           | Tag 4.17.41 not found in the repo |                   404 | `[]`                                     |
| `@types/express@4.17.21`                   | False        | `4.17.21`     | False    |                                          |           | Tag 4.17.21 not found in the repo |                   404 | `[]`                                     |
| `@types/http-assert@1.5.5`                 | False        | `1.5.5`       | False    |                                          |           | Tag 1.5.5 not found in the repo   |                   404 | `[]`                                     |
| `@types/http-errors@2.0.4`                 | False        | `2.0.4`       | False    |                                          |           | Tag 2.0.4 not found in the repo   |                   404 | `[]`                                     |
| `@types/istanbul-lib-coverage@2.0.6`       | False        | `2.0.6`       | False    |                                          |           | Tag 2.0.6 not found in the repo   |                   404 | `[]`                                     |
| `@types/istanbul-lib-report@3.0.3`         | False        | `3.0.3`       | False    |                                          |           | Tag 3.0.3 not found in the repo   |                   404 | `[]`                                     |
| `@types/istanbul-reports@3.0.4`            | False        | `3.0.4`       | False    |                                          |           | Tag 3.0.4 not found in the repo   |                   404 | `[]`                                     |
| `@types/keygrip@1.0.6`                     | False        | `1.0.6`       | False    |                                          |           | Tag 1.0.6 not found in the repo   |                   404 | `[]`                                     |
| `@types/koa-compose@3.2.8`                 | False        | `3.2.8`       | False    |                                          |           | Tag 3.2.8 not found in the repo   |                   404 | `[]`                                     |
| `@types/koa@2.13.12`                       | False        | `2.13.12`     | False    |                                          |           | Tag 2.13.12 not found in the repo |                   404 | `[]`                                     |
| `@types/mime@1.3.5`                        | False        | `1.3.5`       | False    |                                          |           | Tag 1.3.5 not found in the repo   |                   404 | `[]`                                     |
| `@types/node@20.10.5`                      | False        | `20.10.5`     | False    |                                          |           | Tag 20.10.5 not found in the repo |                   404 | `[]`                                     |
| `@types/parse5@6.0.3`                      | False        | `6.0.3`       | False    |                                          |           | Tag 6.0.3 not found in the repo   |                   404 | `[]`                                     |
| `@types/qs@6.9.11`                         | False        | `6.9.11`      | False    |                                          |           | Tag 6.9.11 not found in the repo  |                   404 | `[]`                                     |
| `@types/range-parser@1.2.7`                | False        | `1.2.7`       | False    |                                          |           | Tag 1.2.7 not found in the repo   |                   404 | `[]`                                     |
| `@types/resolve@1.20.2`                    | False        | `1.20.2`      | False    |                                          |           | Tag 1.20.2 not found in the repo  |                   404 | `['@rollup/plugin-node-resolve@15.2.3']` |
| `@types/send@0.17.4`                       | False        | `0.17.4`      | False    |                                          |           | Tag 0.17.4 not found in the repo  |                   404 | `[]`                                     |
| `@types/serve-static@1.15.5`               | False        | `1.15.5`      | False    |                                          |           | Tag 1.15.5 not found in the repo  |                   404 | `[]`                                     |
| `@types/ws@7.4.7`                          | False        | `7.4.7`       | False    |                                          |           | Tag 7.4.7 not found in the repo   |                   404 | `[]`                                     |
| `@types/yauzl@2.10.3`                      | False        | `2.10.3`      | False    |                                          |           | Tag 2.10.3 not found in the repo  |                   404 | `[]`                                     |
| `keyv@4.5.4`                               | False        | `4.5.4`       | False    |                                          |           | Tag 4.5.4 not found in the repo   |                   404 | `[]`                                     |
| `lodash.merge@4.6.2`                       | False        | `4.6.2`       | False    |                                          |           | Tag 4.6.2 not found in the repo   |                   404 | `[]`                                     |
| `unbzip2-stream@1.4.3`                     | False        | `1.4.3`       | True     | 78be9344d6969b355bbed3deeb9e0bde14b550b2 |           | Tag 1.4.3 not found in the repo   |                   404 | `[]`                                     |
</details>

<details>
<summary>Source code links that could not be found(7)</summary>
    


|   index | package_name              | github_url                                    | github_exists   | parent                       |
|--------:|:--------------------------|:----------------------------------------------|:----------------|:-----------------------------|
|       1 | `lighthouse-logger@1.4.2` | No_repo_info_found                            |                 | `[]`                         |
|       2 | `commondir@1.0.1`         | https://github.com/substack/node-commondir    | False           | `[]`                         |
|       3 | `concat-map@0.0.1`        | https://github.com/substack/node-concat-map   | False           | `['brace-expansion@1.1.11']` |
|       4 | `file-entry-cache@6.0.1`  | https://github.com/royriojas/file-entry-cache | False           | `[]`                         |
|       5 | `flat-cache@3.2.0`        | https://github.com/jaredwray/flat-cache       | False           | `[]`                         |
|       6 | `mkdirp@0.5.6`            | https://github.com/substack/node-mkdirp       | False           | `[]`                         |
|       7 | `text-table@0.2.0`        | https://github.com/substack/text-table        | False           | `[]`                         |
</details>

<details>
<summary>List of packages without provenance(515)</summary>
    


| package_name                                  | provenance_in_version   | parent                                                          |
|:----------------------------------------------|:------------------------|:----------------------------------------------------------------|
| `@75lb/deep-merge@1.1.2`                      | False                   | `[]`                                                            |
| `@aashutoshrathi/word-wrap@1.2.6`             | False                   | `[]`                                                            |
| `@babel/code-frame@7.23.5`                    | False                   | `[]`                                                            |
| `@babel/helper-validator-identifier@7.22.20`  | False                   | `[]`                                                            |
| `@babel/highlight@7.23.4`                     | False                   | `[]`                                                            |
| `@bcoe/v8-coverage@1.0.2`                     | False                   | `[]`                                                            |
| `@es-joy/jsdoccomment@0.41.0`                 | False                   | `[]`                                                            |
| `@esbuild/aix-ppc64@0.19.10`                  | False                   | `[]`                                                            |
| `@esbuild/android-arm64@0.19.10`              | False                   | `[]`                                                            |
| `@esbuild/android-arm@0.19.10`                | False                   | `[]`                                                            |
| `@esbuild/android-x64@0.19.10`                | False                   | `[]`                                                            |
| `@esbuild/darwin-arm64@0.19.10`               | False                   | `[]`                                                            |
| `@esbuild/darwin-x64@0.19.10`                 | False                   | `[]`                                                            |
| `@esbuild/freebsd-arm64@0.19.10`              | False                   | `[]`                                                            |
| `@esbuild/freebsd-x64@0.19.10`                | False                   | `[]`                                                            |
| `@esbuild/linux-arm64@0.19.10`                | False                   | `[]`                                                            |
| `@esbuild/linux-arm@0.19.10`                  | False                   | `[]`                                                            |
| `@esbuild/linux-ia32@0.19.10`                 | False                   | `[]`                                                            |
| `@esbuild/linux-loong64@0.19.10`              | False                   | `[]`                                                            |
| `@esbuild/linux-mips64el@0.19.10`             | False                   | `[]`                                                            |
| `@esbuild/linux-ppc64@0.19.10`                | False                   | `[]`                                                            |
| `@esbuild/linux-riscv64@0.19.10`              | False                   | `[]`                                                            |
| `@esbuild/linux-s390x@0.19.10`                | False                   | `[]`                                                            |
| `@esbuild/linux-x64@0.19.10`                  | False                   | `[]`                                                            |
| `@esbuild/netbsd-x64@0.19.10`                 | False                   | `[]`                                                            |
| `@esbuild/openbsd-x64@0.19.10`                | False                   | `[]`                                                            |
| `@esbuild/sunos-x64@0.19.10`                  | False                   | `[]`                                                            |
| `@esbuild/win32-arm64@0.19.10`                | False                   | `[]`                                                            |
| `@esbuild/win32-ia32@0.19.10`                 | False                   | `[]`                                                            |
| `@esbuild/win32-x64@0.19.10`                  | False                   | `[]`                                                            |
| `@eslint-community/eslint-utils@4.4.0`        | False                   | `[]`                                                            |
| `@eslint-community/regexpp@4.10.0`            | False                   | `[]`                                                            |
| `@eslint/js@8.56.0`                           | False                   | `['eslint@8.56.0']`                                             |
| `@eslint/js@9.17.0`                           | False                   | `[]`                                                            |
| `@humanwhocodes/config-array@0.11.14`         | False                   | `[]`                                                            |
| `@humanwhocodes/module-importer@1.0.1`        | False                   | `[]`                                                            |
| `@humanwhocodes/object-schema@2.0.2`          | False                   | `[]`                                                            |
| `@isaacs/cliui@8.0.2`                         | False                   | `[]`                                                            |
| `@istanbuljs/schema@0.1.3`                    | False                   | `[]`                                                            |
| `@jridgewell/resolve-uri@3.1.1`               | False                   | `[]`                                                            |
| `@jridgewell/sourcemap-codec@1.4.15`          | False                   | `[]`                                                            |
| `@jridgewell/trace-mapping@0.3.20`            | False                   | `[]`                                                            |
| `@nodelib/fs.scandir@2.1.5`                   | False                   | `['@nodelib/fs.walk@1.2.8']`                                    |
| `@nodelib/fs.stat@2.0.5`                      | False                   | `['@nodelib/fs.scandir@2.1.5']`                                 |
| `@nodelib/fs.walk@1.2.8`                      | False                   | `[]`                                                            |
| `@pkgjs/parseargs@0.11.0`                     | False                   | `[]`                                                            |
| `@puppeteer/browsers@2.3.0`                   | False                   | `['puppeteer-core@22.15.0']`                                    |
| `@rollup/plugin-commonjs@25.0.7`              | False                   | `[]`                                                            |
| `@rollup/plugin-node-resolve@15.2.3`          | False                   | `[]`                                                            |
| `@rollup/pluginutils@5.1.0`                   | False                   | `[]`                                                            |
| `@rollup/rollup-android-arm-eabi@4.22.4`      | False                   | `[]`                                                            |
| `@rollup/rollup-android-arm64@4.22.4`         | False                   | `[]`                                                            |
| `@rollup/rollup-darwin-arm64@4.22.4`          | False                   | `[]`                                                            |
| `@rollup/rollup-darwin-x64@4.22.4`            | False                   | `[]`                                                            |
| `@rollup/rollup-linux-arm-gnueabihf@4.22.4`   | False                   | `[]`                                                            |
| `@rollup/rollup-linux-arm-musleabihf@4.22.4`  | False                   | `[]`                                                            |
| `@rollup/rollup-linux-arm64-gnu@4.22.4`       | False                   | `[]`                                                            |
| `@rollup/rollup-linux-arm64-musl@4.22.4`      | False                   | `[]`                                                            |
| `@rollup/rollup-linux-powerpc64le-gnu@4.22.4` | False                   | `[]`                                                            |
| `@rollup/rollup-linux-riscv64-gnu@4.22.4`     | False                   | `[]`                                                            |
| `@rollup/rollup-linux-s390x-gnu@4.22.4`       | False                   | `[]`                                                            |
| `@rollup/rollup-linux-x64-gnu@4.22.4`         | False                   | `[]`                                                            |
| `@rollup/rollup-linux-x64-musl@4.22.4`        | False                   | `[]`                                                            |
| `@rollup/rollup-win32-arm64-msvc@4.22.4`      | False                   | `[]`                                                            |
| `@rollup/rollup-win32-ia32-msvc@4.22.4`       | False                   | `[]`                                                            |
| `@rollup/rollup-win32-x64-msvc@4.22.4`        | False                   | `[]`                                                            |
| `@tootallnate/quickjs-emscripten@0.23.0`      | False                   | `[]`                                                            |
| `@types/accepts@1.3.7`                        | False                   | `[]`                                                            |
| `@types/babel__code-frame@7.0.6`              | False                   | `[]`                                                            |
| `@types/body-parser@1.19.5`                   | False                   | `[]`                                                            |
| `@types/co-body@6.1.3`                        | False                   | `[]`                                                            |
| `@types/command-line-args@5.2.3`              | False                   | `[]`                                                            |
| `@types/connect@3.4.38`                       | False                   | `[]`                                                            |
| `@types/content-disposition@0.5.8`            | False                   | `[]`                                                            |
| `@types/convert-source-map@2.0.3`             | False                   | `[]`                                                            |
| `@types/cookies@0.7.10`                       | False                   | `[]`                                                            |
| `@types/debounce@1.2.4`                       | False                   | `[]`                                                            |
| `@types/estree@1.0.5`                         | False                   | `['rollup@4.22.4']`                                             |
| `@types/express-serve-static-core@4.17.41`    | False                   | `[]`                                                            |
| `@types/express@4.17.21`                      | False                   | `[]`                                                            |
| `@types/http-assert@1.5.5`                    | False                   | `[]`                                                            |
| `@types/http-errors@2.0.4`                    | False                   | `[]`                                                            |
| `@types/istanbul-lib-coverage@2.0.6`          | False                   | `[]`                                                            |
| `@types/istanbul-lib-report@3.0.3`            | False                   | `[]`                                                            |
| `@types/istanbul-reports@3.0.4`               | False                   | `[]`                                                            |
| `@types/keygrip@1.0.6`                        | False                   | `[]`                                                            |
| `@types/koa-compose@3.2.8`                    | False                   | `[]`                                                            |
| `@types/koa@2.13.12`                          | False                   | `[]`                                                            |
| `@types/mime@1.3.5`                           | False                   | `[]`                                                            |
| `@types/node@20.10.5`                         | False                   | `[]`                                                            |
| `@types/parse5@6.0.3`                         | False                   | `[]`                                                            |
| `@types/qs@6.9.11`                            | False                   | `[]`                                                            |
| `@types/range-parser@1.2.7`                   | False                   | `[]`                                                            |
| `@types/resolve@1.20.2`                       | False                   | `['@rollup/plugin-node-resolve@15.2.3']`                        |
| `@types/send@0.17.4`                          | False                   | `[]`                                                            |
| `@types/serve-static@1.15.5`                  | False                   | `[]`                                                            |
| `@types/ws@7.4.7`                             | False                   | `[]`                                                            |
| `@types/yauzl@2.10.3`                         | False                   | `[]`                                                            |
| `@ungap/structured-clone@1.2.0`               | False                   | `[]`                                                            |
| `@web/browser-logs@0.4.0`                     | False                   | `[]`                                                            |
| `@web/config-loader@0.3.1`                    | False                   | `[]`                                                            |
| `@web/dev-server-core@0.7.3`                  | False                   | `[]`                                                            |
| `@web/dev-server-rollup@0.6.1`                | False                   | `[]`                                                            |
| `@web/dev-server@0.4.6`                       | False                   | `[]`                                                            |
| `@web/parse5-utils@2.1.0`                     | False                   | `[]`                                                            |
| `@web/test-runner-chrome@0.16.0`              | False                   | `[]`                                                            |
| `@web/test-runner-commands@0.9.0`             | False                   | `[]`                                                            |
| `@web/test-runner-core@0.13.4`                | False                   | `[]`                                                            |
| `@web/test-runner-coverage-v8@0.8.0`          | False                   | `[]`                                                            |
| `@web/test-runner-mocha@0.9.0`                | False                   | `[]`                                                            |
| `@web/test-runner-playwright@0.11.0`          | False                   | `[]`                                                            |
| `@web/test-runner@0.18.3`                     | False                   | `[]`                                                            |
| `accepts@1.3.8`                               | False                   | `[]`                                                            |
| `acorn-jsx@5.3.2`                             | False                   | `[]`                                                            |
| `acorn@8.11.3`                                | False                   | `[]`                                                            |
| `agent-base@7.1.1`                            | False                   | `[]`                                                            |
| `ajv@6.12.6`                                  | False                   | `[]`                                                            |
| `ansi-colors@4.1.1`                           | False                   | `['mocha@10.2.0']`                                              |
| `ansi-escapes@4.3.2`                          | False                   | `[]`                                                            |
| `ansi-regex@5.0.1`                            | False                   | `[]`                                                            |
| `ansi-regex@6.1.0`                            | False                   | `[]`                                                            |
| `ansi-styles@3.2.1`                           | False                   | `[]`                                                            |
| `ansi-styles@4.3.0`                           | False                   | `[]`                                                            |
| `ansi-styles@6.2.1`                           | False                   | `[]`                                                            |
| `anymatch@3.1.3`                              | False                   | `[]`                                                            |
| `are-docs-informative@0.0.2`                  | False                   | `[]`                                                            |
| `argparse@2.0.1`                              | False                   | `[]`                                                            |
| `array-back@3.1.0`                            | False                   | `[]`                                                            |
| `array-back@6.2.2`                            | False                   | `[]`                                                            |
| `array-union@2.1.0`                           | False                   | `[]`                                                            |
| `assertion-error@2.0.1`                       | False                   | `[]`                                                            |
| `ast-types@0.13.4`                            | False                   | `[]`                                                            |
| `astral-regex@2.0.0`                          | False                   | `[]`                                                            |
| `async-mutex@0.4.0`                           | False                   | `['@web/test-runner-chrome@0.16.0']`                            |
| `async@2.6.4`                                 | False                   | `[]`                                                            |
| `b4a@1.6.7`                                   | False                   | `[]`                                                            |
| `balanced-match@1.0.2`                        | False                   | `[]`                                                            |
| `bare-events@2.5.0`                           | False                   | `[]`                                                            |
| `bare-fs@2.3.5`                               | False                   | `[]`                                                            |
| `bare-os@2.4.4`                               | False                   | `[]`                                                            |
| `bare-path@2.1.3`                             | False                   | `[]`                                                            |
| `bare-stream@2.3.0`                           | False                   | `[]`                                                            |
| `base64-js@1.5.1`                             | False                   | `[]`                                                            |
| `basic-ftp@5.0.5`                             | False                   | `[]`                                                            |
| `binary-extensions@2.2.0`                     | False                   | `[]`                                                            |
| `brace-expansion@1.1.11`                      | False                   | `[]`                                                            |
| `brace-expansion@2.0.1`                       | False                   | `[]`                                                            |
| `braces@3.0.3`                                | False                   | `[]`                                                            |
| `browser-stdout@1.3.1`                        | False                   | `['mocha@10.2.0']`                                              |
| `buffer-crc32@0.2.13`                         | False                   | `[]`                                                            |
| `buffer@5.7.1`                                | False                   | `[]`                                                            |
| `builtin-modules@3.3.0`                       | False                   | `[]`                                                            |
| `bytes@3.1.2`                                 | False                   | `['raw-body@2.5.2']`                                            |
| `c8@10.1.3`                                   | False                   | `[]`                                                            |
| `cache-content-type@1.0.1`                    | False                   | `[]`                                                            |
| `call-bind@1.0.5`                             | False                   | `[]`                                                            |
| `callsites@3.1.0`                             | False                   | `[]`                                                            |
| `camelcase@6.3.0`                             | False                   | `[]`                                                            |
| `chalk-template@0.4.0`                        | False                   | `[]`                                                            |
| `chalk@2.4.2`                                 | False                   | `[]`                                                            |
| `chalk@4.1.2`                                 | False                   | `[]`                                                            |
| `check-error@2.1.1`                           | False                   | `[]`                                                            |
| `chokidar@3.5.3`                              | False                   | `['mocha@10.2.0']`                                              |
| `chrome-launcher@0.15.2`                      | False                   | `[]`                                                            |
| `chromium-bidi@0.6.3`                         | False                   | `['puppeteer-core@22.15.0']`                                    |
| `cli-cursor@3.1.0`                            | False                   | `[]`                                                            |
| `cliui@7.0.4`                                 | False                   | `[]`                                                            |
| `cliui@8.0.1`                                 | False                   | `[]`                                                            |
| `clone@2.1.2`                                 | False                   | `[]`                                                            |
| `co-body@6.1.0`                               | False                   | `[]`                                                            |
| `co@4.6.0`                                    | False                   | `[]`                                                            |
| `color-convert@1.9.3`                         | False                   | `[]`                                                            |
| `color-convert@2.0.1`                         | False                   | `[]`                                                            |
| `color-name@1.1.3`                            | False                   | `['color-convert@1.9.3']`                                       |
| `color-name@1.1.4`                            | False                   | `[]`                                                            |
| `command-line-args@5.2.1`                     | False                   | `[]`                                                            |
| `command-line-usage@7.0.1`                    | False                   | `[]`                                                            |
| `comment-parser@1.4.1`                        | False                   | `['eslint-plugin-jsdoc@48.0.4', '@es-joy/jsdoccomment@0.41.0']` |
| `commondir@1.0.1`                             | False                   | `[]`                                                            |
| `concat-map@0.0.1`                            | False                   | `['brace-expansion@1.1.11']`                                    |
| `content-disposition@0.5.4`                   | False                   | `[]`                                                            |
| `content-type@1.0.5`                          | False                   | `[]`                                                            |
| `convert-source-map@2.0.0`                    | False                   | `[]`                                                            |
| `cookies@0.8.0`                               | False                   | `[]`                                                            |
| `cross-spawn@7.0.3`                           | False                   | `[]`                                                            |
| `data-uri-to-buffer@6.0.2`                    | False                   | `[]`                                                            |
| `debounce@1.2.1`                              | False                   | `[]`                                                            |
| `debug@2.6.9`                                 | False                   | `[]`                                                            |
| `debug@3.2.7`                                 | False                   | `[]`                                                            |
| `debug@4.3.4`                                 | False                   | `['mocha@10.2.0']`                                              |
| `debug@4.3.7`                                 | False                   | `[]`                                                            |
| `decamelize@4.0.0`                            | False                   | `[]`                                                            |
| `deep-eql@5.0.2`                              | False                   | `[]`                                                            |
| `deep-equal@1.0.1`                            | False                   | `[]`                                                            |
| `deep-is@0.1.4`                               | False                   | `[]`                                                            |
| `deepmerge@4.3.1`                             | False                   | `[]`                                                            |
| `default-gateway@6.0.3`                       | False                   | `[]`                                                            |
| `define-data-property@1.1.1`                  | False                   | `[]`                                                            |
| `define-lazy-prop@2.0.0`                      | False                   | `[]`                                                            |
| `degenerator@5.0.1`                           | False                   | `[]`                                                            |
| `delegates@1.0.0`                             | False                   | `[]`                                                            |
| `depd@1.1.2`                                  | False                   | `[]`                                                            |
| `depd@2.0.0`                                  | False                   | `['http-errors@2.0.0']`                                         |
| `dependency-graph@0.11.0`                     | False                   | `[]`                                                            |
| `destroy@1.2.0`                               | False                   | `[]`                                                            |
| `devtools-protocol@0.0.1312386`               | False                   | `['puppeteer-core@22.15.0']`                                    |
| `diff@5.0.0`                                  | False                   | `['mocha@10.2.0']`                                              |
| `diff@5.1.0`                                  | False                   | `[]`                                                            |
| `dir-glob@3.0.1`                              | False                   | `[]`                                                            |
| `doctrine@3.0.0`                              | False                   | `[]`                                                            |
| `eastasianwidth@0.2.0`                        | False                   | `[]`                                                            |
| `ee-first@1.1.1`                              | False                   | `['on-finished@2.4.1']`                                         |
| `emoji-regex@8.0.0`                           | False                   | `[]`                                                            |
| `emoji-regex@9.2.2`                           | False                   | `[]`                                                            |
| `encodeurl@1.0.2`                             | False                   | `[]`                                                            |
| `end-of-stream@1.4.4`                         | False                   | `[]`                                                            |
| `errorstacks@2.4.1`                           | False                   | `[]`                                                            |
| `es-module-lexer@1.4.1`                       | False                   | `[]`                                                            |
| `esbuild@0.19.10`                             | False                   | `[]`                                                            |
| `escalade@3.1.1`                              | False                   | `[]`                                                            |
| `escape-html@1.0.3`                           | False                   | `[]`                                                            |
| `escape-string-regexp@1.0.5`                  | False                   | `[]`                                                            |
| `escape-string-regexp@4.0.0`                  | False                   | `['mocha@10.2.0']`                                              |
| `escodegen@2.1.0`                             | False                   | `[]`                                                            |
| `eslint-plugin-jsdoc@48.0.4`                  | False                   | `[]`                                                            |
| `eslint@8.56.0`                               | False                   | `[]`                                                            |
| `esprima@4.0.1`                               | False                   | `[]`                                                            |
| `esquery@1.5.0`                               | False                   | `[]`                                                            |
| `esrecurse@4.3.0`                             | False                   | `[]`                                                            |
| `estraverse@5.3.0`                            | False                   | `[]`                                                            |
| `estree-walker@2.0.2`                         | False                   | `[]`                                                            |
| `esutils@2.0.3`                               | False                   | `[]`                                                            |
| `etag@1.8.1`                                  | False                   | `[]`                                                            |
| `execa@5.1.1`                                 | False                   | `[]`                                                            |
| `extract-zip@2.0.1`                           | False                   | `[]`                                                            |
| `fast-deep-equal@3.1.3`                       | False                   | `[]`                                                            |
| `fast-fifo@1.3.2`                             | False                   | `[]`                                                            |
| `fast-glob@3.3.2`                             | False                   | `[]`                                                            |
| `fast-json-stable-stringify@2.1.0`            | False                   | `[]`                                                            |
| `fast-levenshtein@2.0.6`                      | False                   | `[]`                                                            |
| `fastq@1.16.0`                                | False                   | `[]`                                                            |
| `fd-slicer@1.1.0`                             | False                   | `[]`                                                            |
| `file-entry-cache@6.0.1`                      | False                   | `[]`                                                            |
| `fill-range@7.1.1`                            | False                   | `[]`                                                            |
| `find-replace@3.0.0`                          | False                   | `[]`                                                            |
| `find-up@5.0.0`                               | False                   | `['mocha@10.2.0']`                                              |
| `flat-cache@3.2.0`                            | False                   | `[]`                                                            |
| `flat@5.0.2`                                  | False                   | `[]`                                                            |
| `flatted@3.2.9`                               | False                   | `[]`                                                            |
| `foreground-child@3.3.0`                      | False                   | `[]`                                                            |
| `fresh@0.5.2`                                 | False                   | `[]`                                                            |
| `fs-extra@11.2.0`                             | False                   | `[]`                                                            |
| `fs.realpath@1.0.0`                           | False                   | `[]`                                                            |
| `fsevents@2.3.2`                              | False                   | `[]`                                                            |
| `fsevents@2.3.3`                              | False                   | `[]`                                                            |
| `function-bind@1.1.2`                         | False                   | `[]`                                                            |
| `get-caller-file@2.0.5`                       | False                   | `[]`                                                            |
| `get-intrinsic@1.2.2`                         | False                   | `[]`                                                            |
| `get-stream@5.2.0`                            | False                   | `[]`                                                            |
| `get-stream@6.0.1`                            | False                   | `[]`                                                            |
| `get-uri@6.0.3`                               | False                   | `[]`                                                            |
| `glob-parent@5.1.2`                           | False                   | `[]`                                                            |
| `glob-parent@6.0.2`                           | False                   | `[]`                                                            |
| `glob@10.4.5`                                 | False                   | `[]`                                                            |
| `glob@7.2.0`                                  | False                   | `['mocha@10.2.0']`                                              |
| `glob@7.2.3`                                  | False                   | `[]`                                                            |
| `glob@8.1.0`                                  | False                   | `[]`                                                            |
| `globals@13.24.0`                             | False                   | `[]`                                                            |
| `globby@11.1.0`                               | False                   | `[]`                                                            |
| `gopd@1.0.1`                                  | False                   | `[]`                                                            |
| `graceful-fs@4.2.11`                          | False                   | `[]`                                                            |
| `graphemer@1.4.0`                             | False                   | `[]`                                                            |
| `has-flag@3.0.0`                              | False                   | `[]`                                                            |
| `has-flag@4.0.0`                              | False                   | `[]`                                                            |
| `has-property-descriptors@1.0.1`              | False                   | `[]`                                                            |
| `has-proto@1.0.1`                             | False                   | `[]`                                                            |
| `has-symbols@1.0.3`                           | False                   | `[]`                                                            |
| `has-tostringtag@1.0.0`                       | False                   | `[]`                                                            |
| `hasown@2.0.0`                                | False                   | `[]`                                                            |
| `he@1.2.0`                                    | False                   | `['mocha@10.2.0']`                                              |
| `html-escaper@2.0.2`                          | False                   | `[]`                                                            |
| `http-assert@1.5.0`                           | False                   | `[]`                                                            |
| `http-errors@1.6.3`                           | False                   | `[]`                                                            |
| `http-errors@1.8.1`                           | False                   | `[]`                                                            |
| `http-errors@2.0.0`                           | False                   | `['raw-body@2.5.2']`                                            |
| `http-proxy-agent@7.0.2`                      | False                   | `[]`                                                            |
| `https-proxy-agent@7.0.5`                     | False                   | `[]`                                                            |
| `human-signals@2.1.0`                         | False                   | `[]`                                                            |
| `iconv-lite@0.4.24`                           | False                   | `['raw-body@2.5.2']`                                            |
| `ieee754@1.2.1`                               | False                   | `[]`                                                            |
| `ignore@5.3.0`                                | False                   | `[]`                                                            |
| `import-fresh@3.3.0`                          | False                   | `[]`                                                            |
| `imurmurhash@0.1.4`                           | False                   | `[]`                                                            |
| `inflation@2.1.0`                             | False                   | `[]`                                                            |
| `inflight@1.0.6`                              | False                   | `[]`                                                            |
| `inherits@2.0.3`                              | False                   | `['http-errors@1.6.3']`                                         |
| `inherits@2.0.4`                              | False                   | `['http-errors@2.0.0', 'http-errors@1.8.1']`                    |
| `internal-ip@6.2.0`                           | False                   | `[]`                                                            |
| `ip-address@9.0.5`                            | False                   | `[]`                                                            |
| `ip-regex@4.3.0`                              | False                   | `[]`                                                            |
| `ipaddr.js@1.9.1`                             | False                   | `[]`                                                            |
| `is-binary-path@2.1.0`                        | False                   | `[]`                                                            |
| `is-builtin-module@3.2.1`                     | False                   | `[]`                                                            |
| `is-core-module@2.13.1`                       | False                   | `[]`                                                            |
| `is-docker@2.2.1`                             | False                   | `[]`                                                            |
| `is-extglob@2.1.1`                            | False                   | `[]`                                                            |
| `is-fullwidth-code-point@3.0.0`               | False                   | `[]`                                                            |
| `is-generator-function@1.0.10`                | False                   | `[]`                                                            |
| `is-glob@4.0.3`                               | False                   | `[]`                                                            |
| `is-ip@3.1.0`                                 | False                   | `[]`                                                            |
| `is-module@1.0.0`                             | False                   | `[]`                                                            |
| `is-number@7.0.0`                             | False                   | `[]`                                                            |
| `is-path-inside@3.0.3`                        | False                   | `[]`                                                            |
| `is-plain-obj@2.1.0`                          | False                   | `[]`                                                            |
| `is-reference@1.2.1`                          | False                   | `['@rollup/plugin-commonjs@25.0.7']`                            |
| `is-stream@2.0.1`                             | False                   | `[]`                                                            |
| `is-unicode-supported@0.1.0`                  | False                   | `[]`                                                            |
| `is-wsl@2.2.0`                                | False                   | `[]`                                                            |
| `isbinaryfile@5.0.0`                          | False                   | `[]`                                                            |
| `isexe@2.0.0`                                 | False                   | `[]`                                                            |
| `istanbul-lib-coverage@3.2.2`                 | False                   | `[]`                                                            |
| `istanbul-lib-report@3.0.1`                   | False                   | `[]`                                                            |
| `istanbul-reports@3.1.6`                      | False                   | `[]`                                                            |
| `jackspeak@3.4.3`                             | False                   | `[]`                                                            |
| `js-tokens@4.0.0`                             | False                   | `[]`                                                            |
| `js-yaml@4.1.0`                               | False                   | `['mocha@10.2.0']`                                              |
| `jsbn@1.1.0`                                  | False                   | `['ip-address@9.0.5']`                                          |
| `jsdoc-type-pratt-parser@4.0.0`               | False                   | `[]`                                                            |
| `json-buffer@3.0.1`                           | False                   | `['keyv@4.5.4']`                                                |
| `json-schema-traverse@0.4.1`                  | False                   | `[]`                                                            |
| `json-stable-stringify-without-jsonify@1.0.1` | False                   | `[]`                                                            |
| `jsonfile@6.1.0`                              | False                   | `[]`                                                            |
| `keygrip@1.1.0`                               | False                   | `[]`                                                            |
| `keyv@4.5.4`                                  | False                   | `[]`                                                            |
| `koa-compose@4.1.0`                           | False                   | `[]`                                                            |
| `koa-convert@2.0.0`                           | False                   | `[]`                                                            |
| `koa-etag@4.0.0`                              | False                   | `[]`                                                            |
| `koa-send@5.0.1`                              | False                   | `[]`                                                            |
| `koa-static@5.0.0`                            | False                   | `[]`                                                            |
| `koa@2.14.2`                                  | False                   | `[]`                                                            |
| `levn@0.4.1`                                  | False                   | `[]`                                                            |
| `lighthouse-logger@1.4.2`                     | False                   | `[]`                                                            |
| `locate-path@6.0.0`                           | False                   | `[]`                                                            |
| `lodash.camelcase@4.3.0`                      | False                   | `[]`                                                            |
| `lodash.merge@4.6.2`                          | False                   | `[]`                                                            |
| `lodash@4.17.21`                              | False                   | `[]`                                                            |
| `log-symbols@4.1.0`                           | False                   | `['mocha@10.2.0']`                                              |
| `log-update@4.0.0`                            | False                   | `[]`                                                            |
| `lru-cache@10.4.3`                            | False                   | `[]`                                                            |
| `lru-cache@7.18.3`                            | False                   | `[]`                                                            |
| `lru-cache@8.0.5`                             | False                   | `[]`                                                            |
| `magic-string@0.30.5`                         | False                   | `[]`                                                            |
| `make-dir@4.0.0`                              | False                   | `[]`                                                            |
| `marky@1.2.5`                                 | False                   | `[]`                                                            |
| `media-typer@0.3.0`                           | False                   | `['type-is@1.6.18']`                                            |
| `merge-stream@2.0.0`                          | False                   | `[]`                                                            |
| `merge2@1.4.1`                                | False                   | `[]`                                                            |
| `micromatch@4.0.8`                            | False                   | `[]`                                                            |
| `mime-db@1.52.0`                              | False                   | `['mime-types@2.1.35']`                                         |
| `mime-types@2.1.35`                           | False                   | `[]`                                                            |
| `mimic-fn@2.1.0`                              | False                   | `[]`                                                            |
| `minimatch@3.1.2`                             | False                   | `[]`                                                            |
| `minimatch@5.0.1`                             | False                   | `['mocha@10.2.0']`                                              |
| `minimatch@5.1.6`                             | False                   | `[]`                                                            |
| `minimatch@9.0.5`                             | False                   | `[]`                                                            |
| `minimist@1.2.8`                              | False                   | `[]`                                                            |
| `minipass@7.1.2`                              | False                   | `[]`                                                            |
| `mitt@3.0.1`                                  | False                   | `['chromium-bidi@0.6.3']`                                       |
| `mkdirp@0.5.6`                                | False                   | `[]`                                                            |
| `mkdirp@1.0.4`                                | False                   | `[]`                                                            |
| `mocha@10.2.0`                                | False                   | `[]`                                                            |
| `ms@2.0.0`                                    | False                   | `['debug@2.6.9']`                                               |
| `ms@2.1.2`                                    | False                   | `['debug@4.3.4']`                                               |
| `ms@2.1.3`                                    | False                   | `['mocha@10.2.0']`                                              |
| `nanocolors@0.2.13`                           | False                   | `[]`                                                            |
| `nanoid@3.3.3`                                | False                   | `['mocha@10.2.0']`                                              |
| `nanoid@3.3.7`                                | False                   | `[]`                                                            |
| `natural-compare@1.4.0`                       | False                   | `[]`                                                            |
| `negotiator@0.6.3`                            | False                   | `['accepts@1.3.8']`                                             |
| `netmask@2.0.2`                               | False                   | `[]`                                                            |
| `normalize-path@3.0.0`                        | False                   | `[]`                                                            |
| `npm-run-path@4.0.1`                          | False                   | `[]`                                                            |
| `object-inspect@1.13.1`                       | False                   | `[]`                                                            |
| `on-finished@2.4.1`                           | False                   | `[]`                                                            |
| `once@1.4.0`                                  | False                   | `[]`                                                            |
| `onetime@5.1.2`                               | False                   | `[]`                                                            |
| `only@0.0.2`                                  | False                   | `[]`                                                            |
| `open@8.4.2`                                  | False                   | `[]`                                                            |
| `optionator@0.9.3`                            | False                   | `[]`                                                            |
| `p-event@4.2.0`                               | False                   | `[]`                                                            |
| `p-finally@1.0.0`                             | False                   | `[]`                                                            |
| `p-limit@3.1.0`                               | False                   | `[]`                                                            |
| `p-locate@5.0.0`                              | False                   | `[]`                                                            |
| `p-timeout@3.2.0`                             | False                   | `[]`                                                            |
| `pac-proxy-agent@7.0.2`                       | False                   | `[]`                                                            |
| `pac-resolver@7.0.1`                          | False                   | `[]`                                                            |
| `package-json-from-dist@1.0.1`                | False                   | `[]`                                                            |
| `parent-module@1.0.1`                         | False                   | `[]`                                                            |
| `parse5@6.0.1`                                | False                   | `[]`                                                            |
| `parseurl@1.3.3`                              | False                   | `[]`                                                            |
| `path-exists@4.0.0`                           | False                   | `[]`                                                            |
| `path-is-absolute@1.0.1`                      | False                   | `['resolve-path@1.4.0']`                                        |
| `path-key@3.1.1`                              | False                   | `[]`                                                            |
| `path-parse@1.0.7`                            | False                   | `[]`                                                            |
| `path-scurry@1.11.1`                          | False                   | `[]`                                                            |
| `path-type@4.0.0`                             | False                   | `[]`                                                            |
| `pathval@2.0.0`                               | False                   | `[]`                                                            |
| `pend@1.2.0`                                  | False                   | `[]`                                                            |
| `picomatch@2.3.1`                             | False                   | `[]`                                                            |
| `portfinder@1.0.32`                           | False                   | `[]`                                                            |
| `prelude-ls@1.2.1`                            | False                   | `[]`                                                            |
| `prettier@3.4.2`                              | False                   | `[]`                                                            |
| `progress@2.0.3`                              | False                   | `[]`                                                            |
| `proxy-agent@6.4.0`                           | False                   | `[]`                                                            |
| `proxy-from-env@1.1.0`                        | False                   | `[]`                                                            |
| `pump@3.0.2`                                  | False                   | `[]`                                                            |
| `punycode@2.3.1`                              | False                   | `[]`                                                            |
| `puppeteer-core@22.15.0`                      | False                   | `[]`                                                            |
| `qs@6.11.2`                                   | False                   | `[]`                                                            |
| `queue-microtask@1.2.3`                       | False                   | `[]`                                                            |
| `queue-tick@1.0.1`                            | False                   | `[]`                                                            |
| `randombytes@2.1.0`                           | False                   | `[]`                                                            |
| `raw-body@2.5.2`                              | False                   | `[]`                                                            |
| `readdirp@3.6.0`                              | False                   | `[]`                                                            |
| `require-directory@2.1.1`                     | False                   | `[]`                                                            |
| `resolve-from@4.0.0`                          | False                   | `[]`                                                            |
| `resolve-path@1.4.0`                          | False                   | `[]`                                                            |
| `resolve@1.22.8`                              | False                   | `[]`                                                            |
| `restore-cursor@3.1.0`                        | False                   | `[]`                                                            |
| `reusify@1.0.4`                               | False                   | `[]`                                                            |
| `rimraf@3.0.2`                                | False                   | `[]`                                                            |
| `rollup@4.22.4`                               | False                   | `[]`                                                            |
| `run-parallel@1.2.0`                          | False                   | `[]`                                                            |
| `safe-buffer@5.2.1`                           | False                   | `['content-disposition@0.5.4']`                                 |
| `safer-buffer@2.1.2`                          | False                   | `[]`                                                            |
| `serialize-javascript@6.0.0`                  | False                   | `['mocha@10.2.0']`                                              |
| `set-function-length@1.1.1`                   | False                   | `[]`                                                            |
| `setprototypeof@1.1.0`                        | False                   | `['http-errors@1.6.3']`                                         |
| `setprototypeof@1.2.0`                        | False                   | `['http-errors@2.0.0', 'http-errors@1.8.1']`                    |
| `shebang-command@2.0.0`                       | False                   | `[]`                                                            |
| `shebang-regex@3.0.0`                         | False                   | `[]`                                                            |
| `side-channel@1.0.4`                          | False                   | `[]`                                                            |
| `signal-exit@3.0.7`                           | False                   | `[]`                                                            |
| `signal-exit@4.1.0`                           | False                   | `[]`                                                            |
| `slash@3.0.0`                                 | False                   | `[]`                                                            |
| `slice-ansi@4.0.0`                            | False                   | `[]`                                                            |
| `smart-buffer@4.2.0`                          | False                   | `[]`                                                            |
| `socks-proxy-agent@8.0.4`                     | False                   | `[]`                                                            |
| `socks@2.8.3`                                 | False                   | `[]`                                                            |
| `source-map@0.6.1`                            | False                   | `[]`                                                            |
| `source-map@0.7.4`                            | False                   | `[]`                                                            |
| `spdx-exceptions@2.4.0`                       | False                   | `[]`                                                            |
| `spdx-expression-parse@4.0.0`                 | False                   | `[]`                                                            |
| `spdx-license-ids@3.0.16`                     | False                   | `[]`                                                            |
| `sprintf-js@1.1.3`                            | False                   | `[]`                                                            |
| `statuses@1.5.0`                              | False                   | `[]`                                                            |
| `statuses@2.0.1`                              | False                   | `['http-errors@2.0.0']`                                         |
| `stream-read-all@3.0.1`                       | False                   | `[]`                                                            |
| `streamx@2.20.1`                              | False                   | `[]`                                                            |
| `string-width@4.2.3`                          | False                   | `[]`                                                            |
| `string-width@5.1.2`                          | False                   | `[]`                                                            |
| `strip-ansi@6.0.1`                            | False                   | `[]`                                                            |
| `strip-ansi@7.1.0`                            | False                   | `[]`                                                            |
| `strip-final-newline@2.0.0`                   | False                   | `[]`                                                            |
| `strip-json-comments@3.1.1`                   | False                   | `['mocha@10.2.0']`                                              |
| `supports-color@5.5.0`                        | False                   | `[]`                                                            |
| `supports-color@7.2.0`                        | False                   | `[]`                                                            |
| `supports-color@8.1.1`                        | False                   | `['mocha@10.2.0']`                                              |
| `supports-preserve-symlinks-flag@1.0.0`       | False                   | `[]`                                                            |
| `table-layout@3.0.2`                          | False                   | `[]`                                                            |
| `tar-fs@3.0.6`                                | False                   | `[]`                                                            |
| `tar-stream@3.1.7`                            | False                   | `[]`                                                            |
| `test-exclude@7.0.1`                          | False                   | `[]`                                                            |
| `text-decoder@1.2.0`                          | False                   | `[]`                                                            |
| `text-table@0.2.0`                            | False                   | `[]`                                                            |
| `through@2.3.8`                               | False                   | `[]`                                                            |
| `to-regex-range@5.0.1`                        | False                   | `[]`                                                            |
| `toidentifier@1.0.1`                          | False                   | `['http-errors@2.0.0', 'http-errors@1.8.1']`                    |
| `tr46@3.0.0`                                  | False                   | `[]`                                                            |
| `tslib@2.7.0`                                 | False                   | `[]`                                                            |
| `tsscmp@1.0.6`                                | False                   | `['keygrip@1.1.0']`                                             |
| `type-check@0.4.0`                            | False                   | `[]`                                                            |
| `type-fest@0.20.2`                            | False                   | `[]`                                                            |
| `type-fest@0.21.3`                            | False                   | `[]`                                                            |
| `type-is@1.6.18`                              | False                   | `[]`                                                            |
| `typical@4.0.0`                               | False                   | `[]`                                                            |
| `typical@7.1.1`                               | False                   | `[]`                                                            |
| `unbzip2-stream@1.4.3`                        | False                   | `[]`                                                            |
| `undici-types@5.26.5`                         | False                   | `[]`                                                            |
| `universalify@2.0.1`                          | False                   | `[]`                                                            |
| `unpipe@1.0.0`                                | False                   | `['raw-body@2.5.2']`                                            |
| `uri-js@4.4.1`                                | False                   | `[]`                                                            |
| `urlpattern-polyfill@10.0.0`                  | False                   | `['chromium-bidi@0.6.3']`                                       |
| `v8-to-istanbul@9.2.0`                        | False                   | `[]`                                                            |
| `vary@1.1.2`                                  | False                   | `[]`                                                            |
| `webidl-conversions@7.0.0`                    | False                   | `[]`                                                            |
| `whatwg-url@11.0.0`                           | False                   | `[]`                                                            |
| `which@2.0.2`                                 | False                   | `[]`                                                            |
| `wordwrapjs@5.1.0`                            | False                   | `[]`                                                            |
| `workerpool@6.2.1`                            | False                   | `['mocha@10.2.0']`                                              |
| `wrap-ansi@6.2.0`                             | False                   | `[]`                                                            |
| `wrap-ansi@7.0.0`                             | False                   | `[]`                                                            |
| `wrap-ansi@8.1.0`                             | False                   | `[]`                                                            |
| `wrappy@1.0.2`                                | False                   | `[]`                                                            |
| `ws@7.5.10`                                   | False                   | `[]`                                                            |
| `ws@8.18.0`                                   | False                   | `[]`                                                            |
| `y18n@5.0.8`                                  | False                   | `[]`                                                            |
| `yargs-parser@20.2.4`                         | False                   | `['mocha@10.2.0']`                                              |
| `yargs-parser@21.1.1`                         | False                   | `[]`                                                            |
| `yargs-unparser@2.0.0`                        | False                   | `['mocha@10.2.0']`                                              |
| `yargs@16.2.0`                                | False                   | `['mocha@10.2.0']`                                              |
| `yargs@17.7.2`                                | False                   | `[]`                                                            |
| `yauzl@2.10.0`                                | False                   | `[]`                                                            |
| `ylru@1.3.2`                                  | False                   | `[]`                                                            |
| `yocto-queue@0.1.0`                           | False                   | `[]`                                                            |
</details>

All packages have valid code signature.

All packages have code signature.

<details>
<summary>List of deprecated packages(8)</summary>
    


| package_name                          | deprecated_in_version   | all_deprecated   | parent             |
|:--------------------------------------|:------------------------|:-----------------|:-------------------|
| `@humanwhocodes/config-array@0.11.14` | True                    | True             | `[]`               |
| `@humanwhocodes/object-schema@2.0.2`  | True                    | True             | `[]`               |
| `eslint@8.56.0`                       | True                    | False            | `[]`               |
| `glob@7.2.0`                          | True                    | False            | `['mocha@10.2.0']` |
| `glob@7.2.3`                          | True                    | False            | `[]`               |
| `glob@8.1.0`                          | True                    | False            | `[]`               |
| `inflight@1.0.6`                      | True                    | True             | `[]`               |
| `rimraf@3.0.2`                        | True                    | False            | `[]`               |
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

Report created on 2025-05-13 00:39:27
- Tool version: 1dfb5543
- Project Name: chaijs/chai
- Project Version: 93409cd3f7975f67cae95c780c81a056eed364ac
- Package Manager: npm
