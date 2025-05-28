
# Software Supply Chain Report of jshttp/cookie - e739f419e56442b754e4fea6dbcf98c1c8d00dda

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
        

 ### Total packages in the supply chain: 299


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 9

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 0

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 1

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 283

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 0

:alien: Packages that are aliased (⚠️⚠️): 3


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(9)</summary>
    


| package_name                        | sha_exists   | tag_version   | is_sha   | sha   | tag_url   | message                          |   status_code_for_sha | parent              |
|:------------------------------------|:-------------|:--------------|:---------|:------|:----------|:---------------------------------|----------------------:|:--------------------|
| `@bcoe/v8-coverage@0.2.3`           | False        | `0.2.3`       | False    |       |           | No tags found in the repo        |                   200 | `[]`                |
| `@types/cacheable-request@6.0.3`    | False        | `6.0.3`       | False    |       |           | Tag 6.0.3 not found in the repo  |                   404 | `[]`                |
| `@types/estree@1.0.6`               | False        | `1.0.6`       | False    |       |           | Tag 1.0.6 not found in the repo  |                   404 | `['rollup@4.24.0']` |
| `@types/http-cache-semantics@4.0.4` | False        | `4.0.4`       | False    |       |           | Tag 4.0.4 not found in the repo  |                   404 | `[]`                |
| `@types/keyv@3.1.4`                 | False        | `3.1.4`       | False    |       |           | Tag 3.1.4 not found in the repo  |                   404 | `[]`                |
| `@types/node@22.7.4`                | False        | `22.7.4`      | False    |       |           | Tag 22.7.4 not found in the repo |                   404 | `[]`                |
| `@types/responselike@1.0.3`         | False        | `1.0.3`       | False    |       |           | Tag 1.0.3 not found in the repo  |                   404 | `[]`                |
| `boolbase@1.0.0`                    | False        | `1.0.0`       | False    |       |           | No tags found in the repo        |                   200 | `[]`                |
| `keyv@4.5.4`                        | False        | `4.5.4`       | False    |       |           | Tag 4.5.4 not found in the repo  |                   404 | `[]`                |
</details>

<details>
<summary>Source code links that could not be found(1)</summary>
    


|   index | package_name              | github_url                                      | github_exists   | parent   |
|--------:|:--------------------------|:------------------------------------------------|:----------------|:---------|
|       1 | `cacheable-request@7.0.4` | https://github.com/lukechilds/cacheable-request | False           | `[]`     |
</details>

<details>
<summary>List of packages without provenance(283)</summary>
    


| package_name                                  | provenance_in_version   | parent                                  |
|:----------------------------------------------|:------------------------|:----------------------------------------|
| `@ampproject/remapping@2.3.0`                 | False                   | `[]`                                    |
| `@babel/helper-string-parser@7.24.8`          | False                   | `[]`                                    |
| `@babel/helper-validator-identifier@7.24.7`   | False                   | `[]`                                    |
| `@babel/parser@7.25.6`                        | False                   | `[]`                                    |
| `@babel/types@7.25.6`                         | False                   | `[]`                                    |
| `@bcoe/v8-coverage@0.2.3`                     | False                   | `[]`                                    |
| `@borderless/ts-scripts@0.15.0`               | False                   | `[]`                                    |
| `@esbuild/aix-ppc64@0.21.5`                   | False                   | `[]`                                    |
| `@esbuild/android-arm64@0.21.5`               | False                   | `[]`                                    |
| `@esbuild/android-arm@0.21.5`                 | False                   | `[]`                                    |
| `@esbuild/android-x64@0.21.5`                 | False                   | `[]`                                    |
| `@esbuild/darwin-arm64@0.21.5`                | False                   | `[]`                                    |
| `@esbuild/darwin-x64@0.21.5`                  | False                   | `[]`                                    |
| `@esbuild/freebsd-arm64@0.21.5`               | False                   | `[]`                                    |
| `@esbuild/freebsd-x64@0.21.5`                 | False                   | `[]`                                    |
| `@esbuild/linux-arm64@0.21.5`                 | False                   | `[]`                                    |
| `@esbuild/linux-arm@0.21.5`                   | False                   | `[]`                                    |
| `@esbuild/linux-ia32@0.21.5`                  | False                   | `[]`                                    |
| `@esbuild/linux-loong64@0.21.5`               | False                   | `[]`                                    |
| `@esbuild/linux-mips64el@0.21.5`              | False                   | `[]`                                    |
| `@esbuild/linux-ppc64@0.21.5`                 | False                   | `[]`                                    |
| `@esbuild/linux-riscv64@0.21.5`               | False                   | `[]`                                    |
| `@esbuild/linux-s390x@0.21.5`                 | False                   | `[]`                                    |
| `@esbuild/linux-x64@0.21.5`                   | False                   | `[]`                                    |
| `@esbuild/netbsd-x64@0.21.5`                  | False                   | `[]`                                    |
| `@esbuild/openbsd-x64@0.21.5`                 | False                   | `[]`                                    |
| `@esbuild/sunos-x64@0.21.5`                   | False                   | `[]`                                    |
| `@esbuild/win32-arm64@0.21.5`                 | False                   | `[]`                                    |
| `@esbuild/win32-ia32@0.21.5`                  | False                   | `[]`                                    |
| `@esbuild/win32-x64@0.21.5`                   | False                   | `[]`                                    |
| `@isaacs/cliui@8.0.2`                         | False                   | `[]`                                    |
| `@istanbuljs/schema@0.1.3`                    | False                   | `[]`                                    |
| `@jridgewell/gen-mapping@0.3.5`               | False                   | `[]`                                    |
| `@jridgewell/resolve-uri@3.1.2`               | False                   | `[]`                                    |
| `@jridgewell/set-array@1.2.1`                 | False                   | `[]`                                    |
| `@jridgewell/sourcemap-codec@1.5.0`           | False                   | `[]`                                    |
| `@jridgewell/trace-mapping@0.3.25`            | False                   | `[]`                                    |
| `@nodelib/fs.scandir@2.1.5`                   | False                   | `['@nodelib/fs.walk@1.2.8']`            |
| `@nodelib/fs.stat@2.0.5`                      | False                   | `['@nodelib/fs.scandir@2.1.5']`         |
| `@nodelib/fs.walk@1.2.8`                      | False                   | `[]`                                    |
| `@pkgjs/parseargs@0.11.0`                     | False                   | `[]`                                    |
| `@pkgr/core@0.1.1`                            | False                   | `[]`                                    |
| `@rollup/rollup-android-arm-eabi@4.24.0`      | False                   | `[]`                                    |
| `@rollup/rollup-android-arm64@4.24.0`         | False                   | `[]`                                    |
| `@rollup/rollup-darwin-arm64@4.24.0`          | False                   | `[]`                                    |
| `@rollup/rollup-darwin-x64@4.24.0`            | False                   | `[]`                                    |
| `@rollup/rollup-linux-arm-gnueabihf@4.24.0`   | False                   | `[]`                                    |
| `@rollup/rollup-linux-arm-musleabihf@4.24.0`  | False                   | `[]`                                    |
| `@rollup/rollup-linux-arm64-gnu@4.24.0`       | False                   | `[]`                                    |
| `@rollup/rollup-linux-arm64-musl@4.24.0`      | False                   | `[]`                                    |
| `@rollup/rollup-linux-powerpc64le-gnu@4.24.0` | False                   | `[]`                                    |
| `@rollup/rollup-linux-riscv64-gnu@4.24.0`     | False                   | `[]`                                    |
| `@rollup/rollup-linux-s390x-gnu@4.24.0`       | False                   | `[]`                                    |
| `@rollup/rollup-linux-x64-gnu@4.24.0`         | False                   | `[]`                                    |
| `@rollup/rollup-linux-x64-musl@4.24.0`        | False                   | `[]`                                    |
| `@rollup/rollup-win32-arm64-msvc@4.24.0`      | False                   | `[]`                                    |
| `@rollup/rollup-win32-ia32-msvc@4.24.0`       | False                   | `[]`                                    |
| `@rollup/rollup-win32-x64-msvc@4.24.0`        | False                   | `[]`                                    |
| `@sindresorhus/is@4.6.0`                      | False                   | `[]`                                    |
| `@szmarczak/http-timer@4.0.6`                 | False                   | `[]`                                    |
| `@types/cacheable-request@6.0.3`              | False                   | `[]`                                    |
| `@types/estree@1.0.6`                         | False                   | `['rollup@4.24.0']`                     |
| `@types/http-cache-semantics@4.0.4`           | False                   | `[]`                                    |
| `@types/keyv@3.1.4`                           | False                   | `[]`                                    |
| `@types/node@22.7.4`                          | False                   | `[]`                                    |
| `@types/responselike@1.0.3`                   | False                   | `[]`                                    |
| `aggregate-error@3.1.0`                       | False                   | `[]`                                    |
| `ansi-escapes@7.0.0`                          | False                   | `[]`                                    |
| `ansi-regex@5.0.1`                            | False                   | `[]`                                    |
| `ansi-regex@6.1.0`                            | False                   | `[]`                                    |
| `ansi-styles@4.3.0`                           | False                   | `[]`                                    |
| `ansi-styles@6.2.1`                           | False                   | `[]`                                    |
| `arg@5.0.2`                                   | False                   | `[]`                                    |
| `assertion-error@2.0.1`                       | False                   | `[]`                                    |
| `balanced-match@1.0.2`                        | False                   | `[]`                                    |
| `boolbase@1.0.0`                              | False                   | `[]`                                    |
| `brace-expansion@2.0.1`                       | False                   | `[]`                                    |
| `braces@3.0.3`                                | False                   | `[]`                                    |
| `cac@6.7.14`                                  | False                   | `[]`                                    |
| `cacheable-lookup@5.0.4`                      | False                   | `[]`                                    |
| `cacheable-request@7.0.4`                     | False                   | `[]`                                    |
| `chai@5.1.1`                                  | False                   | `[]`                                    |
| `chalk@5.3.0`                                 | False                   | `[]`                                    |
| `check-error@2.1.1`                           | False                   | `[]`                                    |
| `cheerio-select@2.1.0`                        | False                   | `[]`                                    |
| `cheerio@1.0.0`                               | False                   | `[]`                                    |
| `ci-info@3.9.0`                               | False                   | `[]`                                    |
| `clean-stack@2.2.0`                           | False                   | `[]`                                    |
| `cli-cursor@5.0.0`                            | False                   | `[]`                                    |
| `cli-truncate@4.0.0`                          | False                   | `[]`                                    |
| `clone-response@1.0.3`                        | False                   | `[]`                                    |
| `color-convert@2.0.1`                         | False                   | `[]`                                    |
| `color-name@1.1.4`                            | False                   | `[]`                                    |
| `colorette@2.0.20`                            | False                   | `[]`                                    |
| `commander@12.1.0`                            | False                   | `[]`                                    |
| `cross-spawn@7.0.3`                           | False                   | `[]`                                    |
| `css-select@5.1.0`                            | False                   | `[]`                                    |
| `css-what@6.1.0`                              | False                   | `[]`                                    |
| `debug@4.3.7`                                 | False                   | `[]`                                    |
| `decompress-response@6.0.0`                   | False                   | `[]`                                    |
| `deep-eql@5.0.2`                              | False                   | `[]`                                    |
| `defer-to-connect@2.0.1`                      | False                   | `[]`                                    |
| `detect-indent@6.1.0`                         | False                   | `[]`                                    |
| `detect-indent@7.0.1`                         | False                   | `[]`                                    |
| `detect-newline@4.0.1`                        | False                   | `[]`                                    |
| `dir-glob@3.0.1`                              | False                   | `[]`                                    |
| `dom-serializer@2.0.0`                        | False                   | `[]`                                    |
| `domelementtype@2.3.0`                        | False                   | `[]`                                    |
| `domhandler@5.0.3`                            | False                   | `[]`                                    |
| `domutils@3.1.0`                              | False                   | `[]`                                    |
| `eastasianwidth@0.2.0`                        | False                   | `[]`                                    |
| `emoji-regex@10.4.0`                          | False                   | `[]`                                    |
| `emoji-regex@8.0.0`                           | False                   | `[]`                                    |
| `emoji-regex@9.2.2`                           | False                   | `[]`                                    |
| `encoding-sniffer@0.2.0`                      | False                   | `[]`                                    |
| `end-of-stream@1.4.4`                         | False                   | `[]`                                    |
| `entities@4.5.0`                              | False                   | `[]`                                    |
| `environment@1.1.0`                           | False                   | `[]`                                    |
| `esbuild@0.21.5`                              | False                   | `[]`                                    |
| `estree-walker@3.0.3`                         | False                   | `[]`                                    |
| `eventemitter3@5.0.1`                         | False                   | `[]`                                    |
| `execa@8.0.1`                                 | False                   | `[]`                                    |
| `fast-glob@3.3.2`                             | False                   | `[]`                                    |
| `fastq@1.17.1`                                | False                   | `[]`                                    |
| `fill-range@7.1.1`                            | False                   | `[]`                                    |
| `find-up@6.3.0`                               | False                   | `[]`                                    |
| `foreground-child@3.3.0`                      | False                   | `[]`                                    |
| `fsevents@2.3.3`                              | False                   | `[]`                                    |
| `get-east-asian-width@1.2.0`                  | False                   | `[]`                                    |
| `get-func-name@2.0.2`                         | False                   | `[]`                                    |
| `get-stdin@9.0.0`                             | False                   | `[]`                                    |
| `get-stream@5.2.0`                            | False                   | `[]`                                    |
| `get-stream@8.0.1`                            | False                   | `[]`                                    |
| `git-hooks-list@3.1.0`                        | False                   | `[]`                                    |
| `glob-parent@5.1.2`                           | False                   | `[]`                                    |
| `glob@10.4.5`                                 | False                   | `[]`                                    |
| `globby@13.2.2`                               | False                   | `[]`                                    |
| `got@11.8.6`                                  | False                   | `[]`                                    |
| `graceful-fs@4.2.11`                          | False                   | `[]`                                    |
| `has-flag@4.0.0`                              | False                   | `[]`                                    |
| `html-escaper@2.0.2`                          | False                   | `[]`                                    |
| `htmlparser2@9.1.0`                           | False                   | `[]`                                    |
| `http-cache-semantics@4.1.1`                  | False                   | `[]`                                    |
| `http2-wrapper@1.0.3`                         | False                   | `[]`                                    |
| `human-signals@5.0.0`                         | False                   | `[]`                                    |
| `husky@8.0.3`                                 | False                   | `[]`                                    |
| `iconv-lite@0.6.3`                            | False                   | `['whatwg-encoding@3.1.1']`             |
| `ignore@5.3.2`                                | False                   | `[]`                                    |
| `imurmurhash@0.1.4`                           | False                   | `[]`                                    |
| `indent-string@4.0.0`                         | False                   | `[]`                                    |
| `is-extglob@2.1.1`                            | False                   | `[]`                                    |
| `is-fullwidth-code-point@3.0.0`               | False                   | `[]`                                    |
| `is-fullwidth-code-point@4.0.0`               | False                   | `[]`                                    |
| `is-fullwidth-code-point@5.0.0`               | False                   | `[]`                                    |
| `is-glob@4.0.3`                               | False                   | `[]`                                    |
| `is-number@7.0.0`                             | False                   | `[]`                                    |
| `is-plain-obj@2.1.0`                          | False                   | `[]`                                    |
| `is-plain-obj@4.1.0`                          | False                   | `[]`                                    |
| `is-stream@3.0.0`                             | False                   | `[]`                                    |
| `is-typedarray@1.0.0`                         | False                   | `[]`                                    |
| `isexe@2.0.0`                                 | False                   | `[]`                                    |
| `istanbul-lib-coverage@3.2.2`                 | False                   | `[]`                                    |
| `istanbul-lib-report@3.0.1`                   | False                   | `[]`                                    |
| `istanbul-lib-source-maps@5.0.6`              | False                   | `[]`                                    |
| `istanbul-reports@3.1.7`                      | False                   | `[]`                                    |
| `jackspeak@3.4.3`                             | False                   | `[]`                                    |
| `json-buffer@3.0.1`                           | False                   | `['keyv@4.5.4']`                        |
| `keyv@4.5.4`                                  | False                   | `[]`                                    |
| `lilconfig@3.1.2`                             | False                   | `[]`                                    |
| `listr2@8.2.5`                                | False                   | `[]`                                    |
| `load-json-file@7.0.1`                        | False                   | `[]`                                    |
| `locate-path@7.2.0`                           | False                   | `[]`                                    |
| `lodash@4.17.21`                              | False                   | `[]`                                    |
| `log-update@6.1.0`                            | False                   | `[]`                                    |
| `lowercase-keys@2.0.0`                        | False                   | `[]`                                    |
| `lru-cache@10.4.3`                            | False                   | `[]`                                    |
| `magic-string@0.30.11`                        | False                   | `[]`                                    |
| `magicast@0.3.5`                              | False                   | `[]`                                    |
| `make-dir@3.1.0`                              | False                   | `[]`                                    |
| `make-dir@4.0.0`                              | False                   | `[]`                                    |
| `merge-stream@2.0.0`                          | False                   | `[]`                                    |
| `merge2@1.4.1`                                | False                   | `[]`                                    |
| `micromatch@4.0.8`                            | False                   | `[]`                                    |
| `mimic-fn@4.0.0`                              | False                   | `[]`                                    |
| `mimic-function@5.0.1`                        | False                   | `[]`                                    |
| `mimic-response@1.0.1`                        | False                   | `[]`                                    |
| `mimic-response@3.1.0`                        | False                   | `[]`                                    |
| `minimatch@9.0.5`                             | False                   | `[]`                                    |
| `minipass@7.1.2`                              | False                   | `[]`                                    |
| `ms@2.1.3`                                    | False                   | `[]`                                    |
| `nanoid@3.3.7`                                | False                   | `[]`                                    |
| `normalize-url@6.1.0`                         | False                   | `[]`                                    |
| `npm-run-path@5.3.0`                          | False                   | `[]`                                    |
| `nth-check@2.1.1`                             | False                   | `[]`                                    |
| `once@1.4.0`                                  | False                   | `[]`                                    |
| `onetime@6.0.0`                               | False                   | `[]`                                    |
| `onetime@7.0.0`                               | False                   | `[]`                                    |
| `p-any@3.0.0`                                 | False                   | `[]`                                    |
| `p-cancelable@2.1.1`                          | False                   | `['top-sites@1.1.194']`                 |
| `p-limit@4.0.0`                               | False                   | `[]`                                    |
| `p-locate@6.0.0`                              | False                   | `[]`                                    |
| `p-some@5.0.0`                                | False                   | `[]`                                    |
| `package-json-from-dist@1.0.1`                | False                   | `[]`                                    |
| `papaparse@5.4.1`                             | False                   | `[]`                                    |
| `parse-decimal-number@1.0.0`                  | False                   | `[]`                                    |
| `parse5-htmlparser2-tree-adapter@7.0.0`       | False                   | `[]`                                    |
| `parse5-parser-stream@7.1.2`                  | False                   | `[]`                                    |
| `parse5@7.1.2`                                | False                   | `[]`                                    |
| `path-exists@5.0.0`                           | False                   | `[]`                                    |
| `path-key@3.1.1`                              | False                   | `[]`                                    |
| `path-key@4.0.0`                              | False                   | `[]`                                    |
| `path-scurry@1.11.1`                          | False                   | `[]`                                    |
| `path-type@4.0.0`                             | False                   | `[]`                                    |
| `pathe@1.1.2`                                 | False                   | `[]`                                    |
| `pathval@2.0.0`                               | False                   | `[]`                                    |
| `picocolors@1.1.0`                            | False                   | `[]`                                    |
| `picomatch@2.3.1`                             | False                   | `[]`                                    |
| `pidtree@0.6.0`                               | False                   | `[]`                                    |
| `pkg-conf@4.0.0`                              | False                   | `[]`                                    |
| `postcss@8.4.47`                              | False                   | `[]`                                    |
| `prettier-plugin-packagejson@2.5.2`           | False                   | `[]`                                    |
| `prettier@3.3.3`                              | False                   | `[]`                                    |
| `pump@3.0.2`                                  | False                   | `[]`                                    |
| `queue-microtask@1.2.3`                       | False                   | `[]`                                    |
| `quick-lru@5.1.1`                             | False                   | `[]`                                    |
| `resolve-alpn@1.2.1`                          | False                   | `[]`                                    |
| `responselike@2.0.1`                          | False                   | `[]`                                    |
| `restore-cursor@5.1.0`                        | False                   | `[]`                                    |
| `reusify@1.0.4`                               | False                   | `[]`                                    |
| `rfdc@1.4.1`                                  | False                   | `[]`                                    |
| `rimraf@5.0.10`                               | False                   | `[]`                                    |
| `rollup@4.24.0`                               | False                   | `[]`                                    |
| `run-parallel@1.2.0`                          | False                   | `[]`                                    |
| `safer-buffer@2.1.2`                          | False                   | `[]`                                    |
| `semver@6.3.1`                                | False                   | `[]`                                    |
| `shebang-command@2.0.0`                       | False                   | `[]`                                    |
| `shebang-regex@3.0.0`                         | False                   | `[]`                                    |
| `siginfo@2.0.0`                               | False                   | `[]`                                    |
| `signal-exit@3.0.7`                           | False                   | `[]`                                    |
| `signal-exit@4.1.0`                           | False                   | `[]`                                    |
| `slash@4.0.0`                                 | False                   | `[]`                                    |
| `slice-ansi@5.0.0`                            | False                   | `[]`                                    |
| `slice-ansi@7.1.0`                            | False                   | `[]`                                    |
| `sort-keys@4.2.0`                             | False                   | `[]`                                    |
| `sort-object-keys@1.1.3`                      | False                   | `[]`                                    |
| `sort-package-json@2.10.1`                    | False                   | `['prettier-plugin-packagejson@2.5.2']` |
| `source-map-js@1.2.1`                         | False                   | `[]`                                    |
| `stackback@0.0.2`                             | False                   | `['why-is-node-running@2.3.0']`         |
| `std-env@3.7.0`                               | False                   | `[]`                                    |
| `string-argv@0.3.2`                           | False                   | `[]`                                    |
| `string-width@4.2.3`                          | False                   | `[]`                                    |
| `string-width@5.1.2`                          | False                   | `[]`                                    |
| `string-width@7.2.0`                          | False                   | `[]`                                    |
| `strip-ansi@6.0.1`                            | False                   | `[]`                                    |
| `strip-ansi@7.1.0`                            | False                   | `[]`                                    |
| `strip-final-newline@3.0.0`                   | False                   | `[]`                                    |
| `supports-color@7.2.0`                        | False                   | `[]`                                    |
| `synckit@0.9.1`                               | False                   | `['prettier-plugin-packagejson@2.5.2']` |
| `test-exclude@7.0.1`                          | False                   | `[]`                                    |
| `tinybench@2.9.0`                             | False                   | `[]`                                    |
| `tinypool@1.0.1`                              | False                   | `[]`                                    |
| `tinyrainbow@1.2.0`                           | False                   | `[]`                                    |
| `tinyspy@3.0.2`                               | False                   | `[]`                                    |
| `to-fast-properties@2.0.0`                    | False                   | `[]`                                    |
| `to-regex-range@5.0.1`                        | False                   | `[]`                                    |
| `top-sites@1.1.194`                           | False                   | `[]`                                    |
| `tslib@2.7.0`                                 | False                   | `[]`                                    |
| `typedarray-to-buffer@3.1.5`                  | False                   | `[]`                                    |
| `typescript@5.6.2`                            | False                   | `[]`                                    |
| `undici-types@6.19.8`                         | False                   | `[]`                                    |
| `undici@6.19.8`                               | False                   | `[]`                                    |
| `whatwg-encoding@3.1.1`                       | False                   | `[]`                                    |
| `whatwg-mimetype@4.0.0`                       | False                   | `[]`                                    |
| `which@2.0.2`                                 | False                   | `[]`                                    |
| `why-is-node-running@2.3.0`                   | False                   | `[]`                                    |
| `wrap-ansi@7.0.0`                             | False                   | `[]`                                    |
| `wrap-ansi@8.1.0`                             | False                   | `[]`                                    |
| `wrap-ansi@9.0.0`                             | False                   | `[]`                                    |
| `wrappy@1.0.2`                                | False                   | `[]`                                    |
| `write-file-atomic@3.0.3`                     | False                   | `[]`                                    |
| `write-json-file@4.3.0`                       | False                   | `[]`                                    |
| `yaml@2.5.1`                                  | False                   | `[]`                                    |
| `yocto-queue@1.1.1`                           | False                   | `[]`                                    |
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

Report created on 2025-05-13 00:43:39
- Tool version: 1dfb5543
- Project Name: jshttp/cookie
- Project Version: e739f419e56442b754e4fea6dbcf98c1c8d00dda
- Package Manager: npm
