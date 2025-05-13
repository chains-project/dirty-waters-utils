
# Software Supply Chain Report of isaacs/isexe - 8e5d06b2f0e6d7cfe83d19eb0a9c572d2c598232

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
        

 ### Total packages in the supply chain: 317


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 14

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 0

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 6

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 316

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 5

:alien: Packages that are aliased (⚠️⚠️): 3


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(14)</summary>
    


| package_name                         | sha_exists   | tag_version   | is_sha   | sha   | tag_url   | message                           |   status_code_for_sha | parent                            |
|:-------------------------------------|:-------------|:--------------|:---------|:------|:----------|:----------------------------------|----------------------:|:----------------------------------|
| `@bcoe/v8-coverage@0.2.3`            | False        | `0.2.3`       | False    |       |           | No tags found in the repo         |                   200 | `[]`                              |
| `@tsconfig/node10@1.0.9`             | False        | `1.0.9`       | False    |       |           | No tags found in the repo         |                   200 | `[]`                              |
| `@tsconfig/node12@1.0.11`            | False        | `1.0.11`      | False    |       |           | No tags found in the repo         |                   200 | `[]`                              |
| `@tsconfig/node14@1.0.3`             | False        | `1.0.3`       | False    |       |           | No tags found in the repo         |                   200 | `[]`                              |
| `@types/istanbul-lib-coverage@2.0.4` | False        | `2.0.4`       | False    |       |           | Tag 2.0.4 not found in the repo   |                   404 | `[]`                              |
| `@types/node@20.4.5`                 | False        | `20.4.5`      | False    |       |           | Tag 20.4.5 not found in the repo  |                   404 | `[]`                              |
| `@types/prop-types@15.7.5`           | False        | `15.7.5`      | False    |       |           | Tag 15.7.5 not found in the repo  |                   404 | `[]`                              |
| `@types/react@17.0.62`               | False        | `17.0.62`     | False    |       |           | Tag 17.0.62 not found in the repo |                   404 | `[]`                              |
| `@types/scheduler@0.16.3`            | False        | `0.16.3`      | False    |       |           | Tag 0.16.3 not found in the repo  |                   404 | `[]`                              |
| `@types/tap@15.0.8`                  | False        | `15.0.8`      | False    |       |           | Tag 15.0.8 not found in the repo  |                   404 | `[]`                              |
| `@types/yoga-layout@1.9.2`           | False        | `1.9.2`       | False    |       |           | Tag 1.9.2 not found in the repo   |                   404 | `['yoga-layout-prebuilt@1.10.0']` |
| `react-reconciler@0.26.2`            | False        | `0.26.2`      | False    |       |           | Tag 0.26.2 not found in the repo  |                   404 | `[]`                              |
| `scheduler@0.20.2`                   | False        | `0.20.2`      | False    |       |           | Tag 0.20.2 not found in the repo  |                   404 | `[]`                              |
| `vscode-textmate@8.0.0`              | False        | `8.0.0`       | False    |       |           | Tag 8.0.0 not found in the repo   |                   404 | `[]`                              |
</details>

<details>
<summary>Source code links that could not be found(6)</summary>
    


|   index | package_name           | github_url                                  | github_exists   | parent                       |
|--------:|:-----------------------|:--------------------------------------------|:----------------|:-----------------------------|
|       1 | `archy@1.0.0`          | https://github.com/substack/node-archy      | False           | `[]`                         |
|       2 | `commondir@1.0.1`      | https://github.com/substack/node-commondir  | False           | `[]`                         |
|       3 | `concat-map@0.0.1`     | https://github.com/substack/node-concat-map | False           | `['brace-expansion@1.1.11']` |
|       4 | `findit@2.0.0`         | https://github.com/substack/node-findit     | False           | `[]`                         |
|       5 | `mkdirp@0.5.6`         | https://github.com/substack/node-mkdirp     | False           | `[]`                         |
|       6 | `unicode-length@2.1.0` | https://github.com/jviotti/unicode-length   | False           | `[]`                         |
</details>

<details>
<summary>List of packages without provenance(316)</summary>
    


| package_name                                       | provenance_in_version   | parent                                    |
|:---------------------------------------------------|:------------------------|:------------------------------------------|
| `@ampproject/remapping@2.2.1`                      | False                   | `[]`                                      |
| `@babel/code-frame@7.22.5`                         | False                   | `[]`                                      |
| `@babel/compat-data@7.22.9`                        | False                   | `[]`                                      |
| `@babel/core@7.22.9`                               | False                   | `[]`                                      |
| `@babel/generator@7.22.9`                          | False                   | `[]`                                      |
| `@babel/helper-annotate-as-pure@7.22.5`            | False                   | `[]`                                      |
| `@babel/helper-compilation-targets@7.22.9`         | False                   | `[]`                                      |
| `@babel/helper-environment-visitor@7.22.5`         | False                   | `[]`                                      |
| `@babel/helper-function-name@7.22.5`               | False                   | `[]`                                      |
| `@babel/helper-hoist-variables@7.22.5`             | False                   | `[]`                                      |
| `@babel/helper-module-imports@7.22.5`              | False                   | `[]`                                      |
| `@babel/helper-module-transforms@7.22.9`           | False                   | `[]`                                      |
| `@babel/helper-plugin-utils@7.22.5`                | False                   | `[]`                                      |
| `@babel/helper-simple-access@7.22.5`               | False                   | `[]`                                      |
| `@babel/helper-split-export-declaration@7.22.6`    | False                   | `[]`                                      |
| `@babel/helper-string-parser@7.22.5`               | False                   | `[]`                                      |
| `@babel/helper-validator-identifier@7.22.5`        | False                   | `[]`                                      |
| `@babel/helper-validator-option@7.22.5`            | False                   | `[]`                                      |
| `@babel/helpers@7.22.6`                            | False                   | `[]`                                      |
| `@babel/highlight@7.22.5`                          | False                   | `[]`                                      |
| `@babel/parser@7.22.7`                             | False                   | `[]`                                      |
| `@babel/plugin-proposal-object-rest-spread@7.20.7` | False                   | `[]`                                      |
| `@babel/plugin-syntax-jsx@7.22.5`                  | False                   | `[]`                                      |
| `@babel/plugin-syntax-object-rest-spread@7.8.3`    | False                   | `[]`                                      |
| `@babel/plugin-transform-destructuring@7.22.5`     | False                   | `[]`                                      |
| `@babel/plugin-transform-parameters@7.22.5`        | False                   | `[]`                                      |
| `@babel/plugin-transform-react-jsx@7.22.5`         | False                   | `[]`                                      |
| `@babel/template@7.22.5`                           | False                   | `[]`                                      |
| `@babel/traverse@7.22.8`                           | False                   | `[]`                                      |
| `@babel/types@7.22.5`                              | False                   | `[]`                                      |
| `@bcoe/v8-coverage@0.2.3`                          | False                   | `[]`                                      |
| `@cspotcode/source-map-support@0.8.1`              | False                   | `[]`                                      |
| `@isaacs/cliui@8.0.2`                              | False                   | `[]`                                      |
| `@isaacs/import-jsx@4.0.1`                         | False                   | `[]`                                      |
| `@istanbuljs/load-nyc-config@1.1.0`                | False                   | `[]`                                      |
| `@istanbuljs/schema@0.1.3`                         | False                   | `[]`                                      |
| `@jridgewell/gen-mapping@0.3.3`                    | False                   | `[]`                                      |
| `@jridgewell/resolve-uri@3.1.0`                    | False                   | `['@jridgewell/trace-mapping@0.3.18']`    |
| `@jridgewell/set-array@1.1.2`                      | False                   | `[]`                                      |
| `@jridgewell/sourcemap-codec@1.4.14`               | False                   | `['@jridgewell/trace-mapping@0.3.18']`    |
| `@jridgewell/sourcemap-codec@1.4.15`               | False                   | `[]`                                      |
| `@jridgewell/trace-mapping@0.3.18`                 | False                   | `[]`                                      |
| `@jridgewell/trace-mapping@0.3.9`                  | False                   | `['@cspotcode/source-map-support@0.8.1']` |
| `@pkgjs/parseargs@0.11.0`                          | False                   | `[]`                                      |
| `@tsconfig/node10@1.0.9`                           | False                   | `[]`                                      |
| `@tsconfig/node12@1.0.11`                          | False                   | `[]`                                      |
| `@tsconfig/node14@1.0.3`                           | False                   | `[]`                                      |
| `@tsconfig/node16@1.0.4`                           | False                   | `[]`                                      |
| `@types/istanbul-lib-coverage@2.0.4`               | False                   | `[]`                                      |
| `@types/node@20.4.5`                               | False                   | `[]`                                      |
| `@types/prop-types@15.7.5`                         | False                   | `[]`                                      |
| `@types/react@17.0.62`                             | False                   | `[]`                                      |
| `@types/scheduler@0.16.3`                          | False                   | `[]`                                      |
| `@types/tap@15.0.8`                                | False                   | `[]`                                      |
| `@types/yoga-layout@1.9.2`                         | False                   | `['yoga-layout-prebuilt@1.10.0']`         |
| `acorn-walk@8.2.0`                                 | False                   | `[]`                                      |
| `acorn@8.10.0`                                     | False                   | `[]`                                      |
| `aggregate-error@3.1.0`                            | False                   | `[]`                                      |
| `ansi-escapes@4.3.2`                               | False                   | `[]`                                      |
| `ansi-regex@5.0.1`                                 | False                   | `[]`                                      |
| `ansi-regex@6.0.1`                                 | False                   | `[]`                                      |
| `ansi-sequence-parser@1.1.1`                       | False                   | `[]`                                      |
| `ansi-styles@3.2.1`                                | False                   | `[]`                                      |
| `ansi-styles@4.3.0`                                | False                   | `[]`                                      |
| `ansi-styles@6.2.1`                                | False                   | `[]`                                      |
| `ansicolors@0.3.2`                                 | False                   | `[]`                                      |
| `anymatch@3.1.3`                                   | False                   | `[]`                                      |
| `append-transform@2.0.0`                           | False                   | `[]`                                      |
| `archy@1.0.0`                                      | False                   | `[]`                                      |
| `arg@4.1.3`                                        | False                   | `[]`                                      |
| `argparse@1.0.10`                                  | False                   | `[]`                                      |
| `astral-regex@2.0.0`                               | False                   | `[]`                                      |
| `async-hook-domain@2.0.4`                          | False                   | `[]`                                      |
| `auto-bind@4.0.0`                                  | False                   | `['ink@3.2.0']`                           |
| `balanced-match@1.0.2`                             | False                   | `[]`                                      |
| `binary-extensions@2.2.0`                          | False                   | `[]`                                      |
| `bind-obj-methods@3.0.0`                           | False                   | `[]`                                      |
| `brace-expansion@1.1.11`                           | False                   | `[]`                                      |
| `brace-expansion@2.0.1`                            | False                   | `[]`                                      |
| `braces@3.0.2`                                     | False                   | `[]`                                      |
| `browserslist@4.21.9`                              | False                   | `[]`                                      |
| `buffer-from@1.1.2`                                | False                   | `[]`                                      |
| `c8@8.0.1`                                         | False                   | `[]`                                      |
| `caching-transform@4.0.0`                          | False                   | `[]`                                      |
| `caller-callsite@4.1.0`                            | False                   | `[]`                                      |
| `caller-path@3.0.1`                                | False                   | `[]`                                      |
| `callsites@3.1.0`                                  | False                   | `[]`                                      |
| `camelcase@5.3.1`                                  | False                   | `[]`                                      |
| `caniuse-lite@1.0.30001517`                        | False                   | `[]`                                      |
| `cardinal@2.1.1`                                   | False                   | `[]`                                      |
| `chalk@2.4.2`                                      | False                   | `[]`                                      |
| `chalk@3.0.0`                                      | False                   | `[]`                                      |
| `chalk@4.1.2`                                      | False                   | `[]`                                      |
| `chokidar@3.5.3`                                   | False                   | `[]`                                      |
| `ci-info@2.0.0`                                    | False                   | `[]`                                      |
| `clean-stack@2.2.0`                                | False                   | `[]`                                      |
| `cli-boxes@2.2.1`                                  | False                   | `[]`                                      |
| `cli-cursor@3.1.0`                                 | False                   | `[]`                                      |
| `cli-truncate@2.1.0`                               | False                   | `[]`                                      |
| `cliui@6.0.0`                                      | False                   | `[]`                                      |
| `cliui@7.0.4`                                      | False                   | `[]`                                      |
| `cliui@8.0.1`                                      | False                   | `[]`                                      |
| `code-excerpt@3.0.0`                               | False                   | `[]`                                      |
| `color-convert@1.9.3`                              | False                   | `[]`                                      |
| `color-convert@2.0.1`                              | False                   | `[]`                                      |
| `color-name@1.1.3`                                 | False                   | `['color-convert@1.9.3']`                 |
| `color-name@1.1.4`                                 | False                   | `[]`                                      |
| `color-support@1.1.3`                              | False                   | `[]`                                      |
| `commondir@1.0.1`                                  | False                   | `[]`                                      |
| `concat-map@0.0.1`                                 | False                   | `['brace-expansion@1.1.11']`              |
| `convert-source-map@1.9.0`                         | False                   | `[]`                                      |
| `convert-to-spaces@1.0.2`                          | False                   | `[]`                                      |
| `create-require@1.1.1`                             | False                   | `[]`                                      |
| `cross-spawn@7.0.3`                                | False                   | `[]`                                      |
| `csstype@3.1.2`                                    | False                   | `[]`                                      |
| `debug@4.3.4`                                      | False                   | `[]`                                      |
| `decamelize@1.2.0`                                 | False                   | `[]`                                      |
| `default-require-extensions@3.0.1`                 | False                   | `[]`                                      |
| `diff@4.0.2`                                       | False                   | `[]`                                      |
| `eastasianwidth@0.2.0`                             | False                   | `[]`                                      |
| `electron-to-chromium@1.4.477`                     | False                   | `[]`                                      |
| `emoji-regex@8.0.0`                                | False                   | `[]`                                      |
| `emoji-regex@9.2.2`                                | False                   | `[]`                                      |
| `es6-error@4.1.1`                                  | False                   | `[]`                                      |
| `escalade@3.1.1`                                   | False                   | `[]`                                      |
| `escape-string-regexp@1.0.5`                       | False                   | `[]`                                      |
| `escape-string-regexp@2.0.0`                       | False                   | `[]`                                      |
| `esprima@4.0.1`                                    | False                   | `[]`                                      |
| `events-to-array@1.1.2`                            | False                   | `[]`                                      |
| `fill-range@7.0.1`                                 | False                   | `[]`                                      |
| `find-cache-dir@3.3.2`                             | False                   | `[]`                                      |
| `find-up@4.1.0`                                    | False                   | `[]`                                      |
| `find-up@5.0.0`                                    | False                   | `[]`                                      |
| `findit@2.0.0`                                     | False                   | `[]`                                      |
| `foreground-child@2.0.0`                           | False                   | `[]`                                      |
| `foreground-child@3.1.1`                           | False                   | `[]`                                      |
| `fromentries@1.3.2`                                | False                   | `[]`                                      |
| `fs-exists-cached@1.0.0`                           | False                   | `[]`                                      |
| `fs.realpath@1.0.0`                                | False                   | `[]`                                      |
| `fsevents@2.3.2`                                   | False                   | `[]`                                      |
| `function-loop@2.0.1`                              | False                   | `[]`                                      |
| `gensync@1.0.0-beta.2`                             | False                   | `[]`                                      |
| `get-caller-file@2.0.5`                            | False                   | `[]`                                      |
| `get-package-type@0.1.0`                           | False                   | `[]`                                      |
| `glob-parent@5.1.2`                                | False                   | `[]`                                      |
| `glob@10.3.3`                                      | False                   | `[]`                                      |
| `glob@7.2.3`                                       | False                   | `[]`                                      |
| `globals@11.12.0`                                  | False                   | `[]`                                      |
| `graceful-fs@4.2.11`                               | False                   | `[]`                                      |
| `has-flag@3.0.0`                                   | False                   | `[]`                                      |
| `has-flag@4.0.0`                                   | False                   | `[]`                                      |
| `hasha@5.2.2`                                      | False                   | `[]`                                      |
| `html-escaper@2.0.2`                               | False                   | `[]`                                      |
| `imurmurhash@0.1.4`                                | False                   | `[]`                                      |
| `indent-string@4.0.0`                              | False                   | `[]`                                      |
| `inflight@1.0.6`                                   | False                   | `[]`                                      |
| `inherits@2.0.4`                                   | False                   | `[]`                                      |
| `ink@3.2.0`                                        | False                   | `[]`                                      |
| `is-binary-path@2.1.0`                             | False                   | `[]`                                      |
| `is-ci@2.0.0`                                      | False                   | `[]`                                      |
| `is-extglob@2.1.1`                                 | False                   | `[]`                                      |
| `is-fullwidth-code-point@3.0.0`                    | False                   | `[]`                                      |
| `is-glob@4.0.3`                                    | False                   | `[]`                                      |
| `is-number@7.0.0`                                  | False                   | `[]`                                      |
| `is-stream@2.0.1`                                  | False                   | `[]`                                      |
| `is-typedarray@1.0.0`                              | False                   | `[]`                                      |
| `is-windows@1.0.2`                                 | False                   | `[]`                                      |
| `isexe@2.0.0`                                      | False                   | `[]`                                      |
| `istanbul-lib-coverage@3.2.0`                      | False                   | `[]`                                      |
| `istanbul-lib-hook@3.0.0`                          | False                   | `[]`                                      |
| `istanbul-lib-instrument@4.0.3`                    | False                   | `[]`                                      |
| `istanbul-lib-processinfo@2.0.3`                   | False                   | `[]`                                      |
| `istanbul-lib-report@3.0.1`                        | False                   | `[]`                                      |
| `istanbul-lib-source-maps@4.0.1`                   | False                   | `[]`                                      |
| `istanbul-reports@3.1.6`                           | False                   | `[]`                                      |
| `jackspeak@1.4.2`                                  | False                   | `[]`                                      |
| `jackspeak@2.2.2`                                  | False                   | `[]`                                      |
| `js-tokens@4.0.0`                                  | False                   | `[]`                                      |
| `js-yaml@3.14.1`                                   | False                   | `[]`                                      |
| `jsesc@2.5.2`                                      | False                   | `[]`                                      |
| `json5@2.2.3`                                      | False                   | `[]`                                      |
| `jsonc-parser@3.2.0`                               | False                   | `[]`                                      |
| `libtap@1.4.1`                                     | False                   | `[]`                                      |
| `locate-path@5.0.0`                                | False                   | `[]`                                      |
| `locate-path@6.0.0`                                | False                   | `[]`                                      |
| `lodash.flattendeep@4.4.0`                         | False                   | `[]`                                      |
| `lodash@4.17.21`                                   | False                   | `[]`                                      |
| `loose-envify@1.4.0`                               | False                   | `[]`                                      |
| `lru-cache@10.0.0`                                 | False                   | `[]`                                      |
| `lru-cache@5.1.1`                                  | False                   | `[]`                                      |
| `lru-cache@6.0.0`                                  | False                   | `[]`                                      |
| `lunr@2.3.9`                                       | False                   | `[]`                                      |
| `make-dir@3.1.0`                                   | False                   | `[]`                                      |
| `make-dir@4.0.0`                                   | False                   | `[]`                                      |
| `make-error@1.3.6`                                 | False                   | `[]`                                      |
| `marked@4.3.0`                                     | False                   | `[]`                                      |
| `mimic-fn@2.1.0`                                   | False                   | `[]`                                      |
| `minimatch@3.1.2`                                  | False                   | `[]`                                      |
| `minimatch@9.0.3`                                  | False                   | `[]`                                      |
| `minimist@1.2.8`                                   | False                   | `[]`                                      |
| `minipass@3.3.6`                                   | False                   | `[]`                                      |
| `minipass@7.0.2`                                   | False                   | `[]`                                      |
| `mkdirp@0.5.6`                                     | False                   | `[]`                                      |
| `mkdirp@1.0.4`                                     | False                   | `[]`                                      |
| `mkdirp@3.0.1`                                     | False                   | `[]`                                      |
| `ms@2.1.2`                                         | False                   | `['debug@4.3.4']`                         |
| `node-preload@0.2.1`                               | False                   | `[]`                                      |
| `node-releases@2.0.13`                             | False                   | `[]`                                      |
| `normalize-path@3.0.0`                             | False                   | `[]`                                      |
| `nyc@15.1.0`                                       | False                   | `[]`                                      |
| `object-assign@4.1.1`                              | False                   | `[]`                                      |
| `once@1.4.0`                                       | False                   | `[]`                                      |
| `onetime@5.1.2`                                    | False                   | `[]`                                      |
| `opener@1.5.2`                                     | False                   | `[]`                                      |
| `own-or-env@1.0.2`                                 | False                   | `[]`                                      |
| `own-or@1.0.0`                                     | False                   | `[]`                                      |
| `p-limit@2.3.0`                                    | False                   | `[]`                                      |
| `p-limit@3.1.0`                                    | False                   | `[]`                                      |
| `p-locate@4.1.0`                                   | False                   | `[]`                                      |
| `p-locate@5.0.0`                                   | False                   | `[]`                                      |
| `p-map@3.0.0`                                      | False                   | `[]`                                      |
| `p-try@2.2.0`                                      | False                   | `[]`                                      |
| `package-hash@4.0.0`                               | False                   | `[]`                                      |
| `patch-console@1.0.0`                              | False                   | `[]`                                      |
| `path-exists@4.0.0`                                | False                   | `[]`                                      |
| `path-is-absolute@1.0.1`                           | False                   | `[]`                                      |
| `path-key@3.1.1`                                   | False                   | `[]`                                      |
| `path-scurry@1.10.1`                               | False                   | `[]`                                      |
| `picocolors@1.0.0`                                 | False                   | `[]`                                      |
| `picomatch@2.3.1`                                  | False                   | `[]`                                      |
| `pkg-dir@4.2.0`                                    | False                   | `[]`                                      |
| `prettier@2.8.8`                                   | False                   | `[]`                                      |
| `process-on-spawn@1.0.0`                           | False                   | `[]`                                      |
| `punycode@2.3.0`                                   | False                   | `[]`                                      |
| `react-devtools-core@4.28.0`                       | False                   | `[]`                                      |
| `react-reconciler@0.26.2`                          | False                   | `[]`                                      |
| `react@17.0.2`                                     | False                   | `[]`                                      |
| `readdirp@3.6.0`                                   | False                   | `[]`                                      |
| `redeyed@2.1.1`                                    | False                   | `[]`                                      |
| `release-zalgo@1.0.0`                              | False                   | `[]`                                      |
| `require-directory@2.1.1`                          | False                   | `[]`                                      |
| `require-main-filename@2.0.0`                      | False                   | `[]`                                      |
| `resolve-from@3.0.0`                               | False                   | `[]`                                      |
| `resolve-from@5.0.0`                               | False                   | `[]`                                      |
| `restore-cursor@3.1.0`                             | False                   | `[]`                                      |
| `rimraf@2.7.1`                                     | False                   | `[]`                                      |
| `rimraf@3.0.2`                                     | False                   | `[]`                                      |
| `rimraf@5.0.1`                                     | False                   | `[]`                                      |
| `scheduler@0.20.2`                                 | False                   | `[]`                                      |
| `semver@6.3.1`                                     | False                   | `[]`                                      |
| `set-blocking@2.0.0`                               | False                   | `[]`                                      |
| `shebang-command@2.0.0`                            | False                   | `[]`                                      |
| `shebang-regex@3.0.0`                              | False                   | `[]`                                      |
| `shell-quote@1.8.1`                                | False                   | `[]`                                      |
| `shiki@0.14.3`                                     | False                   | `[]`                                      |
| `signal-exit@3.0.7`                                | False                   | `[]`                                      |
| `signal-exit@4.1.0`                                | False                   | `[]`                                      |
| `slice-ansi@3.0.0`                                 | False                   | `[]`                                      |
| `source-map-support@0.5.21`                        | False                   | `[]`                                      |
| `source-map@0.6.1`                                 | False                   | `[]`                                      |
| `spawn-wrap@2.0.0`                                 | False                   | `[]`                                      |
| `sprintf-js@1.0.3`                                 | False                   | `[]`                                      |
| `stack-utils@2.0.6`                                | False                   | `[]`                                      |
| `string-width@4.2.3`                               | False                   | `[]`                                      |
| `string-width@5.1.2`                               | False                   | `[]`                                      |
| `strip-ansi@6.0.1`                                 | False                   | `[]`                                      |
| `strip-ansi@7.1.0`                                 | False                   | `[]`                                      |
| `strip-bom@4.0.0`                                  | False                   | `[]`                                      |
| `supports-color@5.5.0`                             | False                   | `[]`                                      |
| `supports-color@7.2.0`                             | False                   | `[]`                                      |
| `sync-content@1.0.2`                               | False                   | `[]`                                      |
| `tap-mocha-reporter@5.0.3`                         | False                   | `[]`                                      |
| `tap-parser@11.0.2`                                | False                   | `[]`                                      |
| `tap-yaml@1.0.2`                                   | False                   | `[]`                                      |
| `tap@16.3.8`                                       | False                   | `[]`                                      |
| `tcompare@5.0.7`                                   | False                   | `[]`                                      |
| `test-exclude@6.0.0`                               | False                   | `[]`                                      |
| `to-fast-properties@2.0.0`                         | False                   | `[]`                                      |
| `to-regex-range@5.0.1`                             | False                   | `[]`                                      |
| `treport@3.0.4`                                    | False                   | `[]`                                      |
| `trivial-deferred@1.1.2`                           | False                   | `[]`                                      |
| `ts-node@10.9.1`                                   | False                   | `[]`                                      |
| `type-fest@0.12.0`                                 | False                   | `[]`                                      |
| `type-fest@0.21.3`                                 | False                   | `[]`                                      |
| `type-fest@0.8.1`                                  | False                   | `[]`                                      |
| `typedarray-to-buffer@3.1.5`                       | False                   | `[]`                                      |
| `typedoc@0.24.8`                                   | False                   | `[]`                                      |
| `typescript@5.1.6`                                 | False                   | `[]`                                      |
| `unicode-length@2.1.0`                             | False                   | `[]`                                      |
| `update-browserslist-db@1.0.11`                    | False                   | `[]`                                      |
| `uuid@8.3.2`                                       | False                   | `[]`                                      |
| `v8-compile-cache-lib@3.0.1`                       | False                   | `[]`                                      |
| `v8-to-istanbul@9.1.0`                             | False                   | `[]`                                      |
| `vscode-oniguruma@1.7.0`                           | False                   | `[]`                                      |
| `vscode-textmate@8.0.0`                            | False                   | `[]`                                      |
| `which-module@2.0.1`                               | False                   | `[]`                                      |
| `which@2.0.2`                                      | False                   | `[]`                                      |
| `widest-line@3.1.0`                                | False                   | `[]`                                      |
| `wrap-ansi@6.2.0`                                  | False                   | `[]`                                      |
| `wrap-ansi@7.0.0`                                  | False                   | `[]`                                      |
| `wrap-ansi@8.1.0`                                  | False                   | `[]`                                      |
| `wrappy@1.0.2`                                     | False                   | `[]`                                      |
| `write-file-atomic@3.0.3`                          | False                   | `[]`                                      |
| `ws@7.5.9`                                         | False                   | `[]`                                      |
| `y18n@4.0.3`                                       | False                   | `[]`                                      |
| `y18n@5.0.8`                                       | False                   | `[]`                                      |
| `yallist@3.1.1`                                    | False                   | `[]`                                      |
| `yallist@4.0.0`                                    | False                   | `[]`                                      |
| `yaml@1.10.2`                                      | False                   | `[]`                                      |
| `yargs-parser@18.1.3`                              | False                   | `[]`                                      |
| `yargs-parser@21.1.1`                              | False                   | `[]`                                      |
| `yargs@15.4.1`                                     | False                   | `[]`                                      |
| `yargs@17.7.2`                                     | False                   | `[]`                                      |
| `yn@3.1.1`                                         | False                   | `['ts-node@10.9.1']`                      |
| `yocto-queue@0.1.0`                                | False                   | `[]`                                      |
| `yoga-layout-prebuilt@1.10.0`                      | False                   | `[]`                                      |
</details>

All packages have valid code signature.

All packages have code signature.

<details>
<summary>List of deprecated packages(5)</summary>
    


| package_name                                       | deprecated_in_version   | all_deprecated   | parent   |
|:---------------------------------------------------|:------------------------|:-----------------|:---------|
| `@babel/plugin-proposal-object-rest-spread@7.20.7` | True                    | True             | `[]`     |
| `glob@7.2.3`                                       | True                    | False            | `[]`     |
| `inflight@1.0.6`                                   | True                    | True             | `[]`     |
| `rimraf@2.7.1`                                     | True                    | False            | `[]`     |
| `rimraf@3.0.2`                                     | True                    | False            | `[]`     |
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

Report created on 2025-05-13 00:49:31
- Tool version: 1dfb5543
- Project Name: isaacs/isexe
- Project Version: 8e5d06b2f0e6d7cfe83d19eb0a9c572d2c598232
- Package Manager: npm
