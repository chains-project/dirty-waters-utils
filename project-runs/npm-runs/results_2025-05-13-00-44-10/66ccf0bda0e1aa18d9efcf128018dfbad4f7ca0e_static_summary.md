
# Software Supply Chain Report of terkelg/prompts - 66ccf0bda0e1aa18d9efcf128018dfbad4f7ca0e

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
        

 ### Total packages in the supply chain: 285


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 2

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 1

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 5

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 285

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 18

:alien: Packages that are aliased (⚠️⚠️): 0


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(2)</summary>
    


| package_name             | sha_exists   | tag_version   | is_sha   | sha                                      | tag_url   | message                           |   status_code_for_sha | parent   |
|:-------------------------|:-------------|:--------------|:---------|:-----------------------------------------|:----------|:----------------------------------|----------------------:|:---------|
| `lodash.debounce@4.0.8`  | False        | `4.0.8`       | False    |                                          |           | Tag 4.0.8 not found in the repo   |                   404 | `[]`     |
| `string_decoder@0.10.31` | False        | `0.10.31`     | True     | d46d4fd87cf1d06e031c23f1ba170ca7d4ade9a0 |           | Tag 0.10.31 not found in the repo |                   404 | `[]`     |
</details>

<details>
<summary>Source code links that could not be found(6)</summary>
    


|   index | package_name       | github_url                                  | github_exists   | parent                       |
|--------:|:-------------------|:--------------------------------------------|:----------------|:-----------------------------|
|       1 | `pinkie@2.0.4`     | No_repo_info_found                          |                 | `[]`                         |
|       2 | `concat-map@0.0.1` | https://github.com/substack/node-concat-map | False           | `['brace-expansion@1.1.11']` |
|       3 | `defined@1.0.0`    | https://github.com/substack/defined         | False           | `[]`                         |
|       4 | `minimist@0.2.1`   | https://github.com/substack/minimist        | False           | `[]`                         |
|       5 | `minimist@1.2.5`   | https://github.com/substack/minimist        | False           | `[]`                         |
|       6 | `resumer@0.0.0`    | https://github.com/substack/resumer         | False           | `[]`                         |
</details>

<details>
<summary>List of packages without provenance(285)</summary>
    


| package_name                                                            | provenance_in_version   | parent                                                 |
|:------------------------------------------------------------------------|:------------------------|:-------------------------------------------------------|
| `@babel/cli@7.15.7`                                                     | False                   | `[]`                                                   |
| `@babel/code-frame@7.15.8`                                              | False                   | `[]`                                                   |
| `@babel/compat-data@7.15.0`                                             | False                   | `[]`                                                   |
| `@babel/core@7.15.8`                                                    | False                   | `[]`                                                   |
| `@babel/generator@7.15.8`                                               | False                   | `[]`                                                   |
| `@babel/helper-annotate-as-pure@7.15.4`                                 | False                   | `[]`                                                   |
| `@babel/helper-builder-binary-assignment-operator-visitor@7.15.4`       | False                   | `[]`                                                   |
| `@babel/helper-compilation-targets@7.15.4`                              | False                   | `[]`                                                   |
| `@babel/helper-create-class-features-plugin@7.15.4`                     | False                   | `[]`                                                   |
| `@babel/helper-create-regexp-features-plugin@7.14.5`                    | False                   | `[]`                                                   |
| `@babel/helper-define-polyfill-provider@0.2.3`                          | False                   | `[]`                                                   |
| `@babel/helper-explode-assignable-expression@7.15.4`                    | False                   | `[]`                                                   |
| `@babel/helper-function-name@7.15.4`                                    | False                   | `[]`                                                   |
| `@babel/helper-get-function-arity@7.15.4`                               | False                   | `[]`                                                   |
| `@babel/helper-hoist-variables@7.15.4`                                  | False                   | `[]`                                                   |
| `@babel/helper-member-expression-to-functions@7.15.4`                   | False                   | `[]`                                                   |
| `@babel/helper-module-imports@7.15.4`                                   | False                   | `[]`                                                   |
| `@babel/helper-module-transforms@7.15.8`                                | False                   | `[]`                                                   |
| `@babel/helper-optimise-call-expression@7.15.4`                         | False                   | `[]`                                                   |
| `@babel/helper-plugin-utils@7.14.5`                                     | False                   | `[]`                                                   |
| `@babel/helper-remap-async-to-generator@7.15.4`                         | False                   | `[]`                                                   |
| `@babel/helper-replace-supers@7.15.4`                                   | False                   | `[]`                                                   |
| `@babel/helper-simple-access@7.15.4`                                    | False                   | `[]`                                                   |
| `@babel/helper-skip-transparent-expression-wrappers@7.15.4`             | False                   | `[]`                                                   |
| `@babel/helper-split-export-declaration@7.15.4`                         | False                   | `[]`                                                   |
| `@babel/helper-validator-identifier@7.15.7`                             | False                   | `[]`                                                   |
| `@babel/helper-validator-option@7.14.5`                                 | False                   | `[]`                                                   |
| `@babel/helper-wrap-function@7.15.4`                                    | False                   | `[]`                                                   |
| `@babel/helpers@7.15.4`                                                 | False                   | `[]`                                                   |
| `@babel/highlight@7.14.5`                                               | False                   | `[]`                                                   |
| `@babel/parser@7.15.8`                                                  | False                   | `[]`                                                   |
| `@babel/plugin-bugfix-v8-spread-parameters-in-optional-chaining@7.15.4` | False                   | `[]`                                                   |
| `@babel/plugin-proposal-async-generator-functions@7.15.8`               | False                   | `[]`                                                   |
| `@babel/plugin-proposal-class-properties@7.14.5`                        | False                   | `[]`                                                   |
| `@babel/plugin-proposal-class-static-block@7.15.4`                      | False                   | `[]`                                                   |
| `@babel/plugin-proposal-dynamic-import@7.14.5`                          | False                   | `[]`                                                   |
| `@babel/plugin-proposal-export-namespace-from@7.14.5`                   | False                   | `[]`                                                   |
| `@babel/plugin-proposal-json-strings@7.14.5`                            | False                   | `[]`                                                   |
| `@babel/plugin-proposal-logical-assignment-operators@7.14.5`            | False                   | `[]`                                                   |
| `@babel/plugin-proposal-nullish-coalescing-operator@7.14.5`             | False                   | `[]`                                                   |
| `@babel/plugin-proposal-numeric-separator@7.14.5`                       | False                   | `[]`                                                   |
| `@babel/plugin-proposal-object-rest-spread@7.15.6`                      | False                   | `[]`                                                   |
| `@babel/plugin-proposal-optional-catch-binding@7.14.5`                  | False                   | `[]`                                                   |
| `@babel/plugin-proposal-optional-chaining@7.14.5`                       | False                   | `[]`                                                   |
| `@babel/plugin-proposal-private-methods@7.14.5`                         | False                   | `[]`                                                   |
| `@babel/plugin-proposal-private-property-in-object@7.15.4`              | False                   | `[]`                                                   |
| `@babel/plugin-proposal-unicode-property-regex@7.14.5`                  | False                   | `[]`                                                   |
| `@babel/plugin-syntax-async-generators@7.8.4`                           | False                   | `[]`                                                   |
| `@babel/plugin-syntax-class-properties@7.12.13`                         | False                   | `[]`                                                   |
| `@babel/plugin-syntax-class-static-block@7.14.5`                        | False                   | `[]`                                                   |
| `@babel/plugin-syntax-dynamic-import@7.8.3`                             | False                   | `[]`                                                   |
| `@babel/plugin-syntax-export-namespace-from@7.8.3`                      | False                   | `[]`                                                   |
| `@babel/plugin-syntax-json-strings@7.8.3`                               | False                   | `[]`                                                   |
| `@babel/plugin-syntax-logical-assignment-operators@7.10.4`              | False                   | `[]`                                                   |
| `@babel/plugin-syntax-nullish-coalescing-operator@7.8.3`                | False                   | `[]`                                                   |
| `@babel/plugin-syntax-numeric-separator@7.10.4`                         | False                   | `[]`                                                   |
| `@babel/plugin-syntax-object-rest-spread@7.8.3`                         | False                   | `[]`                                                   |
| `@babel/plugin-syntax-optional-catch-binding@7.8.3`                     | False                   | `[]`                                                   |
| `@babel/plugin-syntax-optional-chaining@7.8.3`                          | False                   | `[]`                                                   |
| `@babel/plugin-syntax-private-property-in-object@7.14.5`                | False                   | `[]`                                                   |
| `@babel/plugin-syntax-top-level-await@7.14.5`                           | False                   | `[]`                                                   |
| `@babel/plugin-transform-arrow-functions@7.14.5`                        | False                   | `[]`                                                   |
| `@babel/plugin-transform-async-to-generator@7.14.5`                     | False                   | `[]`                                                   |
| `@babel/plugin-transform-block-scoped-functions@7.14.5`                 | False                   | `[]`                                                   |
| `@babel/plugin-transform-block-scoping@7.15.3`                          | False                   | `[]`                                                   |
| `@babel/plugin-transform-classes@7.15.4`                                | False                   | `[]`                                                   |
| `@babel/plugin-transform-computed-properties@7.14.5`                    | False                   | `[]`                                                   |
| `@babel/plugin-transform-destructuring@7.14.7`                          | False                   | `[]`                                                   |
| `@babel/plugin-transform-dotall-regex@7.14.5`                           | False                   | `[]`                                                   |
| `@babel/plugin-transform-duplicate-keys@7.14.5`                         | False                   | `[]`                                                   |
| `@babel/plugin-transform-exponentiation-operator@7.14.5`                | False                   | `[]`                                                   |
| `@babel/plugin-transform-for-of@7.15.4`                                 | False                   | `[]`                                                   |
| `@babel/plugin-transform-function-name@7.14.5`                          | False                   | `[]`                                                   |
| `@babel/plugin-transform-literals@7.14.5`                               | False                   | `[]`                                                   |
| `@babel/plugin-transform-member-expression-literals@7.14.5`             | False                   | `[]`                                                   |
| `@babel/plugin-transform-modules-amd@7.14.5`                            | False                   | `[]`                                                   |
| `@babel/plugin-transform-modules-commonjs@7.15.4`                       | False                   | `[]`                                                   |
| `@babel/plugin-transform-modules-systemjs@7.15.4`                       | False                   | `[]`                                                   |
| `@babel/plugin-transform-modules-umd@7.14.5`                            | False                   | `[]`                                                   |
| `@babel/plugin-transform-named-capturing-groups-regex@7.14.9`           | False                   | `[]`                                                   |
| `@babel/plugin-transform-new-target@7.14.5`                             | False                   | `[]`                                                   |
| `@babel/plugin-transform-object-super@7.14.5`                           | False                   | `[]`                                                   |
| `@babel/plugin-transform-parameters@7.15.4`                             | False                   | `[]`                                                   |
| `@babel/plugin-transform-property-literals@7.14.5`                      | False                   | `[]`                                                   |
| `@babel/plugin-transform-regenerator@7.14.5`                            | False                   | `[]`                                                   |
| `@babel/plugin-transform-reserved-words@7.14.5`                         | False                   | `[]`                                                   |
| `@babel/plugin-transform-shorthand-properties@7.14.5`                   | False                   | `[]`                                                   |
| `@babel/plugin-transform-spread@7.15.8`                                 | False                   | `[]`                                                   |
| `@babel/plugin-transform-sticky-regex@7.14.5`                           | False                   | `[]`                                                   |
| `@babel/plugin-transform-template-literals@7.14.5`                      | False                   | `[]`                                                   |
| `@babel/plugin-transform-typeof-symbol@7.14.5`                          | False                   | `[]`                                                   |
| `@babel/plugin-transform-unicode-escapes@7.14.5`                        | False                   | `[]`                                                   |
| `@babel/plugin-transform-unicode-regex@7.14.5`                          | False                   | `[]`                                                   |
| `@babel/preset-env@7.15.8`                                              | False                   | `[]`                                                   |
| `@babel/preset-modules@0.1.4`                                           | False                   | `[]`                                                   |
| `@babel/runtime@7.15.4`                                                 | False                   | `[]`                                                   |
| `@babel/template@7.15.4`                                                | False                   | `[]`                                                   |
| `@babel/traverse@7.15.4`                                                | False                   | `[]`                                                   |
| `@babel/types@7.15.6`                                                   | False                   | `[]`                                                   |
| `@nicolo-ribaudo/chokidar-2@2.1.8-no-fsevents.3`                        | False                   | `[]`                                                   |
| `ansi-regex@2.1.1`                                                      | False                   | `[]`                                                   |
| `ansi-styles@2.2.1`                                                     | False                   | `[]`                                                   |
| `ansi-styles@3.2.1`                                                     | False                   | `[]`                                                   |
| `anymatch@3.1.2`                                                        | False                   | `[]`                                                   |
| `array-find-index@1.0.2`                                                | False                   | `[]`                                                   |
| `babel-plugin-dynamic-import-node@2.3.3`                                | False                   | `[]`                                                   |
| `babel-plugin-polyfill-corejs2@0.2.2`                                   | False                   | `[]`                                                   |
| `babel-plugin-polyfill-corejs3@0.2.5`                                   | False                   | `[]`                                                   |
| `babel-plugin-polyfill-regenerator@0.2.2`                               | False                   | `[]`                                                   |
| `balanced-match@1.0.2`                                                  | False                   | `[]`                                                   |
| `binary-extensions@2.2.0`                                               | False                   | `[]`                                                   |
| `brace-expansion@1.1.11`                                                | False                   | `[]`                                                   |
| `braces@3.0.2`                                                          | False                   | `[]`                                                   |
| `browserslist@4.17.3`                                                   | False                   | `[]`                                                   |
| `call-bind@1.0.2`                                                       | False                   | `[]`                                                   |
| `camelcase-keys@2.1.0`                                                  | False                   | `[]`                                                   |
| `camelcase@2.1.1`                                                       | False                   | `[]`                                                   |
| `caniuse-lite@1.0.30001265`                                             | False                   | `[]`                                                   |
| `chalk@1.1.3`                                                           | False                   | `[]`                                                   |
| `chalk@2.4.2`                                                           | False                   | `[]`                                                   |
| `chokidar@3.5.2`                                                        | False                   | `[]`                                                   |
| `color-convert@1.9.3`                                                   | False                   | `[]`                                                   |
| `color-name@1.1.3`                                                      | False                   | `['color-convert@1.9.3']`                              |
| `commander@4.1.1`                                                       | False                   | `[]`                                                   |
| `concat-map@0.0.1`                                                      | False                   | `['brace-expansion@1.1.11']`                           |
| `convert-source-map@1.8.0`                                              | False                   | `[]`                                                   |
| `core-js-compat@3.18.2`                                                 | False                   | `[]`                                                   |
| `core-util-is@1.0.3`                                                    | False                   | `[]`                                                   |
| `currently-unhandled@0.4.1`                                             | False                   | `[]`                                                   |
| `debug@4.3.2`                                                           | False                   | `[]`                                                   |
| `decamelize@1.2.0`                                                      | False                   | `[]`                                                   |
| `deep-equal@1.1.1`                                                      | False                   | `[]`                                                   |
| `define-properties@1.1.3`                                               | False                   | `[]`                                                   |
| `defined@1.0.0`                                                         | False                   | `[]`                                                   |
| `dotignore@0.1.2`                                                       | False                   | `[]`                                                   |
| `duplexer@0.1.2`                                                        | False                   | `[]`                                                   |
| `electron-to-chromium@1.3.861`                                          | False                   | `[]`                                                   |
| `error-ex@1.3.2`                                                        | False                   | `[]`                                                   |
| `es-abstract@1.19.1`                                                    | False                   | `[]`                                                   |
| `es-to-primitive@1.2.1`                                                 | False                   | `[]`                                                   |
| `escalade@3.1.1`                                                        | False                   | `[]`                                                   |
| `escape-string-regexp@1.0.5`                                            | False                   | `[]`                                                   |
| `esutils@2.0.3`                                                         | False                   | `[]`                                                   |
| `fill-range@7.0.1`                                                      | False                   | `[]`                                                   |
| `find-up@1.1.2`                                                         | False                   | `[]`                                                   |
| `for-each@0.3.3`                                                        | False                   | `[]`                                                   |
| `fs-readdir-recursive@1.1.0`                                            | False                   | `[]`                                                   |
| `fs.realpath@1.0.0`                                                     | False                   | `[]`                                                   |
| `fsevents@2.3.2`                                                        | False                   | `[]`                                                   |
| `function-bind@1.1.1`                                                   | False                   | `[]`                                                   |
| `gensync@1.0.0-beta.2`                                                  | False                   | `[]`                                                   |
| `get-intrinsic@1.1.1`                                                   | False                   | `[]`                                                   |
| `get-stdin@4.0.1`                                                       | False                   | `[]`                                                   |
| `get-symbol-description@1.0.0`                                          | False                   | `[]`                                                   |
| `glob-parent@5.1.2`                                                     | False                   | `[]`                                                   |
| `glob@7.1.7`                                                            | False                   | `[]`                                                   |
| `glob@7.2.0`                                                            | False                   | `[]`                                                   |
| `globals@11.12.0`                                                       | False                   | `[]`                                                   |
| `graceful-fs@4.2.8`                                                     | False                   | `[]`                                                   |
| `has-ansi@2.0.0`                                                        | False                   | `[]`                                                   |
| `has-bigints@1.0.1`                                                     | False                   | `[]`                                                   |
| `has-flag@3.0.0`                                                        | False                   | `[]`                                                   |
| `has-symbols@1.0.2`                                                     | False                   | `[]`                                                   |
| `has-tostringtag@1.0.0`                                                 | False                   | `[]`                                                   |
| `has@1.0.3`                                                             | False                   | `[]`                                                   |
| `hosted-git-info@2.8.9`                                                 | False                   | `[]`                                                   |
| `indent-string@2.1.0`                                                   | False                   | `[]`                                                   |
| `inflight@1.0.6`                                                        | False                   | `[]`                                                   |
| `inherits@2.0.4`                                                        | False                   | `[]`                                                   |
| `internal-slot@1.0.3`                                                   | False                   | `[]`                                                   |
| `is-arguments@1.1.1`                                                    | False                   | `[]`                                                   |
| `is-arrayish@0.2.1`                                                     | False                   | `[]`                                                   |
| `is-bigint@1.0.4`                                                       | False                   | `[]`                                                   |
| `is-binary-path@2.1.0`                                                  | False                   | `[]`                                                   |
| `is-boolean-object@1.1.2`                                               | False                   | `[]`                                                   |
| `is-callable@1.2.4`                                                     | False                   | `[]`                                                   |
| `is-core-module@2.7.0`                                                  | False                   | `[]`                                                   |
| `is-date-object@1.0.5`                                                  | False                   | `[]`                                                   |
| `is-extglob@2.1.1`                                                      | False                   | `[]`                                                   |
| `is-finite@1.1.0`                                                       | False                   | `[]`                                                   |
| `is-glob@4.0.3`                                                         | False                   | `[]`                                                   |
| `is-negative-zero@2.0.1`                                                | False                   | `[]`                                                   |
| `is-number-object@1.0.6`                                                | False                   | `[]`                                                   |
| `is-number@7.0.0`                                                       | False                   | `[]`                                                   |
| `is-regex@1.1.4`                                                        | False                   | `[]`                                                   |
| `is-shared-array-buffer@1.0.1`                                          | False                   | `[]`                                                   |
| `is-string@1.0.7`                                                       | False                   | `[]`                                                   |
| `is-symbol@1.0.4`                                                       | False                   | `[]`                                                   |
| `is-utf8@0.2.1`                                                         | False                   | `[]`                                                   |
| `is-weakref@1.0.1`                                                      | False                   | `[]`                                                   |
| `isarray@0.0.1`                                                         | False                   | `['readable-stream@1.0.34', 'readable-stream@1.1.14']` |
| `js-tokens@4.0.0`                                                       | False                   | `[]`                                                   |
| `jsesc@0.5.0`                                                           | False                   | `[]`                                                   |
| `jsesc@2.5.2`                                                           | False                   | `[]`                                                   |
| `json5@2.2.0`                                                           | False                   | `[]`                                                   |
| `kleur@3.0.3`                                                           | False                   | `[]`                                                   |
| `load-json-file@1.1.0`                                                  | False                   | `[]`                                                   |
| `lodash.debounce@4.0.8`                                                 | False                   | `[]`                                                   |
| `loud-rejection@1.6.0`                                                  | False                   | `[]`                                                   |
| `make-dir@2.1.0`                                                        | False                   | `[]`                                                   |
| `map-obj@1.0.1`                                                         | False                   | `[]`                                                   |
| `meow@3.7.0`                                                            | False                   | `[]`                                                   |
| `minimatch@3.0.4`                                                       | False                   | `[]`                                                   |
| `minimist@0.2.1`                                                        | False                   | `[]`                                                   |
| `minimist@1.2.5`                                                        | False                   | `[]`                                                   |
| `ms@2.1.2`                                                              | False                   | `['debug@4.3.2']`                                      |
| `node-releases@1.1.77`                                                  | False                   | `[]`                                                   |
| `normalize-package-data@2.5.0`                                          | False                   | `[]`                                                   |
| `normalize-path@3.0.0`                                                  | False                   | `[]`                                                   |
| `object-assign@4.1.1`                                                   | False                   | `[]`                                                   |
| `object-inspect@1.11.0`                                                 | False                   | `[]`                                                   |
| `object-is@1.1.5`                                                       | False                   | `[]`                                                   |
| `object-keys@1.1.1`                                                     | False                   | `[]`                                                   |
| `object.assign@4.1.2`                                                   | False                   | `[]`                                                   |
| `once@1.4.0`                                                            | False                   | `[]`                                                   |
| `parse-json@2.2.0`                                                      | False                   | `[]`                                                   |
| `parse-ms@1.0.1`                                                        | False                   | `[]`                                                   |
| `path-exists@2.1.0`                                                     | False                   | `[]`                                                   |
| `path-is-absolute@1.0.1`                                                | False                   | `[]`                                                   |
| `path-parse@1.0.7`                                                      | False                   | `[]`                                                   |
| `path-type@1.1.0`                                                       | False                   | `[]`                                                   |
| `picocolors@0.2.1`                                                      | False                   | `[]`                                                   |
| `picomatch@2.3.0`                                                       | False                   | `[]`                                                   |
| `pify@2.3.0`                                                            | False                   | `[]`                                                   |
| `pify@4.0.1`                                                            | False                   | `[]`                                                   |
| `pinkie-promise@2.0.1`                                                  | False                   | `[]`                                                   |
| `pinkie@2.0.4`                                                          | False                   | `[]`                                                   |
| `plur@1.0.0`                                                            | False                   | `[]`                                                   |
| `pretty-ms@1.4.0`                                                       | False                   | `[]`                                                   |
| `read-pkg-up@1.0.1`                                                     | False                   | `[]`                                                   |
| `read-pkg@1.1.0`                                                        | False                   | `[]`                                                   |
| `readable-stream@1.0.34`                                                | False                   | `[]`                                                   |
| `readable-stream@1.1.14`                                                | False                   | `[]`                                                   |
| `readdirp@3.6.0`                                                        | False                   | `[]`                                                   |
| `redent@1.0.0`                                                          | False                   | `[]`                                                   |
| `regenerate-unicode-properties@9.0.0`                                   | False                   | `[]`                                                   |
| `regenerate@1.4.2`                                                      | False                   | `[]`                                                   |
| `regenerator-runtime@0.13.9`                                            | False                   | `[]`                                                   |
| `regenerator-transform@0.14.5`                                          | False                   | `[]`                                                   |
| `regexp.prototype.flags@1.3.1`                                          | False                   | `[]`                                                   |
| `regexpu-core@4.8.0`                                                    | False                   | `[]`                                                   |
| `regjsgen@0.5.2`                                                        | False                   | `[]`                                                   |
| `regjsparser@0.7.0`                                                     | False                   | `[]`                                                   |
| `repeating@2.0.1`                                                       | False                   | `[]`                                                   |
| `resolve@1.20.0`                                                        | False                   | `[]`                                                   |
| `resumer@0.0.0`                                                         | False                   | `[]`                                                   |
| `safe-buffer@5.1.2`                                                     | False                   | `[]`                                                   |
| `semver@5.7.1`                                                          | False                   | `[]`                                                   |
| `semver@6.3.0`                                                          | False                   | `[]`                                                   |
| `semver@7.0.0`                                                          | False                   | `['core-js-compat@3.18.2']`                            |
| `side-channel@1.0.4`                                                    | False                   | `[]`                                                   |
| `signal-exit@3.0.5`                                                     | False                   | `[]`                                                   |
| `sisteransi@1.0.5`                                                      | False                   | `[]`                                                   |
| `slash@2.0.0`                                                           | False                   | `[]`                                                   |
| `source-map@0.5.7`                                                      | False                   | `[]`                                                   |
| `spdx-correct@3.1.1`                                                    | False                   | `[]`                                                   |
| `spdx-exceptions@2.3.0`                                                 | False                   | `[]`                                                   |
| `spdx-expression-parse@3.0.1`                                           | False                   | `[]`                                                   |
| `spdx-license-ids@3.0.10`                                               | False                   | `[]`                                                   |
| `string.prototype.trim@1.2.5`                                           | False                   | `[]`                                                   |
| `string.prototype.trimend@1.0.4`                                        | False                   | `[]`                                                   |
| `string.prototype.trimstart@1.0.4`                                      | False                   | `[]`                                                   |
| `string_decoder@0.10.31`                                                | False                   | `[]`                                                   |
| `strip-ansi@3.0.1`                                                      | False                   | `[]`                                                   |
| `strip-bom@2.0.0`                                                       | False                   | `[]`                                                   |
| `strip-indent@1.0.1`                                                    | False                   | `[]`                                                   |
| `supports-color@2.0.0`                                                  | False                   | `[]`                                                   |
| `supports-color@5.5.0`                                                  | False                   | `[]`                                                   |
| `tap-parser@0.7.0`                                                      | False                   | `[]`                                                   |
| `tap-spec@2.2.2`                                                        | False                   | `[]`                                                   |
| `tape@4.14.0`                                                           | False                   | `[]`                                                   |
| `through2@0.6.5`                                                        | False                   | `[]`                                                   |
| `through@2.3.8`                                                         | False                   | `[]`                                                   |
| `to-fast-properties@2.0.0`                                              | False                   | `[]`                                                   |
| `to-regex-range@5.0.1`                                                  | False                   | `[]`                                                   |
| `trim-newlines@1.0.0`                                                   | False                   | `[]`                                                   |
| `unbox-primitive@1.0.1`                                                 | False                   | `[]`                                                   |
| `unicode-canonical-property-names-ecmascript@2.0.0`                     | False                   | `[]`                                                   |
| `unicode-match-property-ecmascript@2.0.0`                               | False                   | `[]`                                                   |
| `unicode-match-property-value-ecmascript@2.0.0`                         | False                   | `[]`                                                   |
| `unicode-property-aliases-ecmascript@2.0.0`                             | False                   | `[]`                                                   |
| `validate-npm-package-license@3.0.4`                                    | False                   | `[]`                                                   |
| `which-boxed-primitive@1.0.2`                                           | False                   | `[]`                                                   |
| `wrappy@1.0.2`                                                          | False                   | `[]`                                                   |
| `xtend@4.0.2`                                                           | False                   | `[]`                                                   |
</details>

All packages have valid code signature.

All packages have code signature.

<details>
<summary>List of deprecated packages(18)</summary>
    


| package_name                                                 | deprecated_in_version   | all_deprecated   | parent   |
|:-------------------------------------------------------------|:------------------------|:-----------------|:---------|
| `@babel/plugin-proposal-async-generator-functions@7.15.8`    | True                    | True             | `[]`     |
| `@babel/plugin-proposal-class-properties@7.14.5`             | True                    | True             | `[]`     |
| `@babel/plugin-proposal-class-static-block@7.15.4`           | True                    | True             | `[]`     |
| `@babel/plugin-proposal-dynamic-import@7.14.5`               | True                    | True             | `[]`     |
| `@babel/plugin-proposal-export-namespace-from@7.14.5`        | True                    | True             | `[]`     |
| `@babel/plugin-proposal-json-strings@7.14.5`                 | True                    | True             | `[]`     |
| `@babel/plugin-proposal-logical-assignment-operators@7.14.5` | True                    | True             | `[]`     |
| `@babel/plugin-proposal-nullish-coalescing-operator@7.14.5`  | True                    | True             | `[]`     |
| `@babel/plugin-proposal-numeric-separator@7.14.5`            | True                    | True             | `[]`     |
| `@babel/plugin-proposal-object-rest-spread@7.15.6`           | True                    | True             | `[]`     |
| `@babel/plugin-proposal-optional-catch-binding@7.14.5`       | True                    | True             | `[]`     |
| `@babel/plugin-proposal-optional-chaining@7.14.5`            | True                    | True             | `[]`     |
| `@babel/plugin-proposal-private-methods@7.14.5`              | True                    | True             | `[]`     |
| `@babel/plugin-proposal-private-property-in-object@7.15.4`   | True                    | False            | `[]`     |
| `@babel/plugin-proposal-unicode-property-regex@7.14.5`       | True                    | True             | `[]`     |
| `glob@7.1.7`                                                 | True                    | False            | `[]`     |
| `glob@7.2.0`                                                 | True                    | False            | `[]`     |
| `inflight@1.0.6`                                             | True                    | True             | `[]`     |
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

Report created on 2025-05-13 00:44:28
- Tool version: 1dfb5543
- Project Name: terkelg/prompts
- Project Version: 66ccf0bda0e1aa18d9efcf128018dfbad4f7ca0e
- Package Manager: npm
