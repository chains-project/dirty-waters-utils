
# Software Supply Chain Report of juliangruber/brace-expansion - 6a39bdddcf944374b475d99b0e8292d3727c7ebe

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
        

 ### Total packages in the supply chain: 246


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 3

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 0

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 5

:black_square_button: Packages without build attestation (⚠️⚠️⚠️): 241

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 0

:x: Packages that are deprecated (⚠️⚠️): 6

:alien: Packages that are aliased (⚠️⚠️): 0


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(3)</summary>
    


| package_name          | sha_exists   | tag_version   | is_sha   | sha   | tag_url   | message                          |   status_code_for_sha | parent   |
|:----------------------|:-------------|:--------------|:---------|:------|:----------|:---------------------------------|----------------------:|:---------|
| `@types/json5@0.0.29` | False        | `0.0.29`      | False    |       |           | Tag 0.0.29 not found in the repo |                   404 | `[]`     |
| `keyv@4.5.3`          | False        | `4.5.3`       | False    |       |           | Tag 4.5.3 not found in the repo  |                   404 | `[]`     |
| `lodash.merge@4.6.2`  | False        | `4.6.2`       | False    |       |           | Tag 4.6.2 not found in the repo  |                   404 | `[]`     |
</details>

<details>
<summary>Source code links that could not be found(5)</summary>
    


|   index | package_name             | github_url                                    | github_exists   | parent                       |
|--------:|:-------------------------|:----------------------------------------------|:----------------|:-----------------------------|
|       1 | `concat-map@0.0.1`       | https://github.com/substack/node-concat-map   | False           | `['brace-expansion@1.1.11']` |
|       2 | `file-entry-cache@6.0.1` | https://github.com/royriojas/file-entry-cache | False           | `[]`                         |
|       3 | `flat-cache@3.1.1`       | https://github.com/jaredwray/flat-cache       | False           | `[]`                         |
|       4 | `minimist@1.2.6`         | https://github.com/substack/minimist          | False           | `[]`                         |
|       5 | `text-table@0.2.0`       | https://github.com/substack/text-table        | False           | `[]`                         |
</details>

<details>
<summary>List of packages without provenance(241)</summary>
    


| package_name                                  | provenance_in_version   | parent                          |
|:----------------------------------------------|:------------------------|:--------------------------------|
| `@aashutoshrathi/word-wrap@1.2.6`             | False                   | `[]`                            |
| `@c4312/matcha@1.3.1`                         | False                   | `[]`                            |
| `@eslint-community/eslint-utils@4.4.0`        | False                   | `[]`                            |
| `@eslint-community/regexpp@4.9.1`             | False                   | `[]`                            |
| `@eslint/js@8.51.0`                           | False                   | `['eslint@8.51.0']`             |
| `@humanwhocodes/config-array@0.11.11`         | False                   | `[]`                            |
| `@humanwhocodes/module-importer@1.0.1`        | False                   | `[]`                            |
| `@humanwhocodes/object-schema@1.2.1`          | False                   | `[]`                            |
| `@nodelib/fs.scandir@2.1.5`                   | False                   | `['@nodelib/fs.walk@1.2.8']`    |
| `@nodelib/fs.stat@2.0.5`                      | False                   | `['@nodelib/fs.scandir@2.1.5']` |
| `@nodelib/fs.walk@1.2.8`                      | False                   | `[]`                            |
| `@types/json5@0.0.29`                         | False                   | `[]`                            |
| `acorn-jsx@5.3.2`                             | False                   | `[]`                            |
| `acorn@8.10.0`                                | False                   | `[]`                            |
| `ajv@6.12.6`                                  | False                   | `[]`                            |
| `ansi-regex@5.0.1`                            | False                   | `[]`                            |
| `ansi-styles@4.3.0`                           | False                   | `[]`                            |
| `argparse@2.0.1`                              | False                   | `[]`                            |
| `array-buffer-byte-length@1.0.0`              | False                   | `[]`                            |
| `array-includes@3.1.7`                        | False                   | `[]`                            |
| `array.prototype.findlastindex@1.2.3`         | False                   | `[]`                            |
| `array.prototype.flat@1.3.2`                  | False                   | `[]`                            |
| `array.prototype.flatmap@1.3.2`               | False                   | `[]`                            |
| `array.prototype.tosorted@1.1.2`              | False                   | `[]`                            |
| `arraybuffer.prototype.slice@1.0.2`           | False                   | `[]`                            |
| `asynciterator.prototype@1.0.0`               | False                   | `[]`                            |
| `available-typed-arrays@1.0.5`                | False                   | `[]`                            |
| `balanced-match@1.0.2`                        | False                   | `[]`                            |
| `balanced-match@3.0.0`                        | False                   | `[]`                            |
| `benchmark@2.1.4`                             | False                   | `[]`                            |
| `brace-expansion@1.1.11`                      | False                   | `[]`                            |
| `builtins@5.0.1`                              | False                   | `[]`                            |
| `call-bind@1.0.2`                             | False                   | `[]`                            |
| `callsites@3.1.0`                             | False                   | `[]`                            |
| `chalk@3.0.0`                                 | False                   | `[]`                            |
| `chalk@4.1.2`                                 | False                   | `[]`                            |
| `color-convert@2.0.1`                         | False                   | `[]`                            |
| `color-name@1.1.4`                            | False                   | `[]`                            |
| `commander@4.1.1`                             | False                   | `[]`                            |
| `concat-map@0.0.1`                            | False                   | `['brace-expansion@1.1.11']`    |
| `cross-spawn@7.0.3`                           | False                   | `[]`                            |
| `debug@3.2.7`                                 | False                   | `[]`                            |
| `debug@4.3.4`                                 | False                   | `[]`                            |
| `deep-is@0.1.4`                               | False                   | `[]`                            |
| `define-data-property@1.1.0`                  | False                   | `[]`                            |
| `define-properties@1.2.1`                     | False                   | `[]`                            |
| `doctrine@2.1.0`                              | False                   | `[]`                            |
| `doctrine@3.0.0`                              | False                   | `[]`                            |
| `error-ex@1.3.2`                              | False                   | `[]`                            |
| `es-abstract@1.22.2`                          | False                   | `[]`                            |
| `es-iterator-helpers@1.0.15`                  | False                   | `[]`                            |
| `es-set-tostringtag@2.0.1`                    | False                   | `[]`                            |
| `es-shim-unscopables@1.0.0`                   | False                   | `[]`                            |
| `es-to-primitive@1.2.1`                       | False                   | `[]`                            |
| `escape-string-regexp@4.0.0`                  | False                   | `[]`                            |
| `eslint-config-standard-jsx@11.0.0`           | False                   | `[]`                            |
| `eslint-config-standard@17.1.0`               | False                   | `['standard@17.1.0']`           |
| `eslint-import-resolver-node@0.3.9`           | False                   | `[]`                            |
| `eslint-module-utils@2.8.0`                   | False                   | `[]`                            |
| `eslint-plugin-es@4.1.0`                      | False                   | `[]`                            |
| `eslint-plugin-import@2.28.1`                 | False                   | `[]`                            |
| `eslint-plugin-n@15.7.0`                      | False                   | `[]`                            |
| `eslint-plugin-promise@6.1.1`                 | False                   | `[]`                            |
| `eslint-plugin-react@7.33.2`                  | False                   | `[]`                            |
| `eslint-utils@2.1.0`                          | False                   | `[]`                            |
| `eslint-utils@3.0.0`                          | False                   | `[]`                            |
| `eslint-visitor-keys@1.3.0`                   | False                   | `[]`                            |
| `eslint-visitor-keys@2.1.0`                   | False                   | `[]`                            |
| `eslint@8.51.0`                               | False                   | `[]`                            |
| `esquery@1.5.0`                               | False                   | `[]`                            |
| `esrecurse@4.3.0`                             | False                   | `[]`                            |
| `estraverse@5.3.0`                            | False                   | `[]`                            |
| `esutils@2.0.3`                               | False                   | `[]`                            |
| `fast-deep-equal@3.1.3`                       | False                   | `[]`                            |
| `fast-json-stable-stringify@2.1.0`            | False                   | `[]`                            |
| `fast-levenshtein@2.0.6`                      | False                   | `[]`                            |
| `fastq@1.15.0`                                | False                   | `[]`                            |
| `file-entry-cache@6.0.1`                      | False                   | `[]`                            |
| `find-up@3.0.0`                               | False                   | `[]`                            |
| `find-up@5.0.0`                               | False                   | `[]`                            |
| `flat-cache@3.1.1`                            | False                   | `[]`                            |
| `flatted@3.2.9`                               | False                   | `[]`                            |
| `for-each@0.3.3`                              | False                   | `[]`                            |
| `fs.realpath@1.0.0`                           | False                   | `[]`                            |
| `function-bind@1.1.1`                         | False                   | `[]`                            |
| `function.prototype.name@1.1.6`               | False                   | `[]`                            |
| `functions-have-names@1.2.3`                  | False                   | `[]`                            |
| `get-intrinsic@1.2.1`                         | False                   | `[]`                            |
| `get-stdin@8.0.0`                             | False                   | `[]`                            |
| `get-symbol-description@1.0.0`                | False                   | `[]`                            |
| `glob-parent@6.0.2`                           | False                   | `[]`                            |
| `glob@7.2.3`                                  | False                   | `[]`                            |
| `globals@13.23.0`                             | False                   | `[]`                            |
| `globalthis@1.0.3`                            | False                   | `[]`                            |
| `gopd@1.0.1`                                  | False                   | `[]`                            |
| `graceful-fs@4.2.11`                          | False                   | `[]`                            |
| `graphemer@1.4.0`                             | False                   | `[]`                            |
| `has-bigints@1.0.2`                           | False                   | `[]`                            |
| `has-flag@4.0.0`                              | False                   | `[]`                            |
| `has-property-descriptors@1.0.0`              | False                   | `[]`                            |
| `has-proto@1.0.1`                             | False                   | `[]`                            |
| `has-symbols@1.0.3`                           | False                   | `[]`                            |
| `has-tostringtag@1.0.0`                       | False                   | `[]`                            |
| `has@1.0.3`                                   | False                   | `[]`                            |
| `ignore@5.2.4`                                | False                   | `[]`                            |
| `import-fresh@3.3.0`                          | False                   | `[]`                            |
| `imurmurhash@0.1.4`                           | False                   | `[]`                            |
| `inflight@1.0.6`                              | False                   | `[]`                            |
| `inherits@2.0.4`                              | False                   | `[]`                            |
| `internal-slot@1.0.5`                         | False                   | `[]`                            |
| `is-array-buffer@3.0.2`                       | False                   | `[]`                            |
| `is-arrayish@0.2.1`                           | False                   | `[]`                            |
| `is-async-function@2.0.0`                     | False                   | `[]`                            |
| `is-bigint@1.0.4`                             | False                   | `[]`                            |
| `is-boolean-object@1.1.2`                     | False                   | `[]`                            |
| `is-callable@1.2.7`                           | False                   | `[]`                            |
| `is-core-module@2.13.0`                       | False                   | `[]`                            |
| `is-date-object@1.0.5`                        | False                   | `[]`                            |
| `is-extglob@2.1.1`                            | False                   | `[]`                            |
| `is-finalizationregistry@1.0.2`               | False                   | `[]`                            |
| `is-generator-function@1.0.10`                | False                   | `[]`                            |
| `is-glob@4.0.3`                               | False                   | `[]`                            |
| `is-map@2.0.2`                                | False                   | `[]`                            |
| `is-negative-zero@2.0.2`                      | False                   | `[]`                            |
| `is-number-object@1.0.7`                      | False                   | `[]`                            |
| `is-path-inside@3.0.3`                        | False                   | `[]`                            |
| `is-regex@1.1.4`                              | False                   | `[]`                            |
| `is-set@2.0.2`                                | False                   | `[]`                            |
| `is-shared-array-buffer@1.0.2`                | False                   | `[]`                            |
| `is-string@1.0.7`                             | False                   | `[]`                            |
| `is-symbol@1.0.4`                             | False                   | `[]`                            |
| `is-typed-array@1.1.12`                       | False                   | `[]`                            |
| `is-weakmap@2.0.1`                            | False                   | `[]`                            |
| `is-weakref@1.0.2`                            | False                   | `[]`                            |
| `is-weakset@2.0.2`                            | False                   | `[]`                            |
| `isarray@2.0.5`                               | False                   | `[]`                            |
| `isexe@2.0.0`                                 | False                   | `[]`                            |
| `iterator.prototype@1.1.2`                    | False                   | `[]`                            |
| `js-tokens@4.0.0`                             | False                   | `[]`                            |
| `js-yaml@4.1.0`                               | False                   | `[]`                            |
| `json-buffer@3.0.1`                           | False                   | `['keyv@4.5.3']`                |
| `json-parse-better-errors@1.0.2`              | False                   | `[]`                            |
| `json-schema-traverse@0.4.1`                  | False                   | `[]`                            |
| `json-stable-stringify-without-jsonify@1.0.1` | False                   | `[]`                            |
| `json5@1.0.2`                                 | False                   | `[]`                            |
| `jsx-ast-utils@3.3.5`                         | False                   | `[]`                            |
| `keyv@4.5.3`                                  | False                   | `[]`                            |
| `levn@0.4.1`                                  | False                   | `[]`                            |
| `load-json-file@5.3.0`                        | False                   | `[]`                            |
| `locate-path@3.0.0`                           | False                   | `[]`                            |
| `locate-path@6.0.0`                           | False                   | `[]`                            |
| `lodash.merge@4.6.2`                          | False                   | `[]`                            |
| `lodash@4.17.21`                              | False                   | `[]`                            |
| `loose-envify@1.4.0`                          | False                   | `[]`                            |
| `lru-cache@6.0.0`                             | False                   | `[]`                            |
| `microtime@3.0.0`                             | False                   | `[]`                            |
| `minimatch@3.1.2`                             | False                   | `[]`                            |
| `minimist@1.2.6`                              | False                   | `[]`                            |
| `ms@2.1.2`                                    | False                   | `['debug@4.3.4']`               |
| `natural-compare@1.4.0`                       | False                   | `[]`                            |
| `node-addon-api@1.7.2`                        | False                   | `[]`                            |
| `node-gyp-build@3.9.0`                        | False                   | `[]`                            |
| `object-assign@4.1.1`                         | False                   | `[]`                            |
| `object-inspect@1.12.3`                       | False                   | `[]`                            |
| `object-keys@1.1.1`                           | False                   | `[]`                            |
| `object.assign@4.1.4`                         | False                   | `[]`                            |
| `object.entries@1.1.7`                        | False                   | `[]`                            |
| `object.fromentries@2.0.7`                    | False                   | `[]`                            |
| `object.groupby@1.0.1`                        | False                   | `[]`                            |
| `object.hasown@1.1.3`                         | False                   | `[]`                            |
| `object.values@1.1.7`                         | False                   | `[]`                            |
| `once@1.4.0`                                  | False                   | `[]`                            |
| `optionator@0.9.3`                            | False                   | `[]`                            |
| `p-limit@2.3.0`                               | False                   | `[]`                            |
| `p-limit@3.1.0`                               | False                   | `[]`                            |
| `p-locate@3.0.0`                              | False                   | `[]`                            |
| `p-locate@5.0.0`                              | False                   | `[]`                            |
| `p-try@2.2.0`                                 | False                   | `[]`                            |
| `parent-module@1.0.1`                         | False                   | `[]`                            |
| `parse-json@4.0.0`                            | False                   | `[]`                            |
| `path-exists@3.0.0`                           | False                   | `[]`                            |
| `path-exists@4.0.0`                           | False                   | `[]`                            |
| `path-is-absolute@1.0.1`                      | False                   | `[]`                            |
| `path-key@3.1.1`                              | False                   | `[]`                            |
| `path-parse@1.0.7`                            | False                   | `[]`                            |
| `pify@4.0.1`                                  | False                   | `[]`                            |
| `pkg-conf@3.1.0`                              | False                   | `[]`                            |
| `platform@1.3.6`                              | False                   | `[]`                            |
| `prelude-ls@1.2.1`                            | False                   | `[]`                            |
| `prop-types@15.8.1`                           | False                   | `[]`                            |
| `punycode@2.3.0`                              | False                   | `[]`                            |
| `queue-microtask@1.2.3`                       | False                   | `[]`                            |
| `react-is@16.13.1`                            | False                   | `[]`                            |
| `reflect.getprototypeof@1.0.4`                | False                   | `[]`                            |
| `regexp.prototype.flags@1.5.1`                | False                   | `[]`                            |
| `regexpp@3.2.0`                               | False                   | `[]`                            |
| `resolve-from@4.0.0`                          | False                   | `[]`                            |
| `resolve@1.22.6`                              | False                   | `[]`                            |
| `resolve@2.0.0-next.4`                        | False                   | `[]`                            |
| `reusify@1.0.4`                               | False                   | `[]`                            |
| `rimraf@3.0.2`                                | False                   | `[]`                            |
| `run-parallel@1.2.0`                          | False                   | `[]`                            |
| `safe-array-concat@1.0.1`                     | False                   | `[]`                            |
| `safe-regex-test@1.0.0`                       | False                   | `[]`                            |
| `semver@6.3.1`                                | False                   | `[]`                            |
| `set-function-name@2.0.1`                     | False                   | `[]`                            |
| `shebang-command@2.0.0`                       | False                   | `[]`                            |
| `shebang-regex@3.0.0`                         | False                   | `[]`                            |
| `side-channel@1.0.4`                          | False                   | `[]`                            |
| `standard-engine@15.1.0`                      | False                   | `[]`                            |
| `standard@17.1.0`                             | False                   | `[]`                            |
| `string.prototype.matchall@4.0.10`            | False                   | `[]`                            |
| `string.prototype.trim@1.2.8`                 | False                   | `[]`                            |
| `string.prototype.trimend@1.0.7`              | False                   | `[]`                            |
| `string.prototype.trimstart@1.0.7`            | False                   | `[]`                            |
| `strip-ansi@6.0.1`                            | False                   | `[]`                            |
| `strip-bom@3.0.0`                             | False                   | `[]`                            |
| `strip-json-comments@3.1.1`                   | False                   | `[]`                            |
| `supports-color@7.2.0`                        | False                   | `[]`                            |
| `supports-preserve-symlinks-flag@1.0.0`       | False                   | `[]`                            |
| `text-table@0.2.0`                            | False                   | `[]`                            |
| `tsconfig-paths@3.14.2`                       | False                   | `[]`                            |
| `type-check@0.4.0`                            | False                   | `[]`                            |
| `type-fest@0.20.2`                            | False                   | `[]`                            |
| `type-fest@0.3.1`                             | False                   | `[]`                            |
| `typed-array-buffer@1.0.0`                    | False                   | `[]`                            |
| `typed-array-byte-length@1.0.0`               | False                   | `[]`                            |
| `typed-array-byte-offset@1.0.0`               | False                   | `[]`                            |
| `typed-array-length@1.0.4`                    | False                   | `[]`                            |
| `unbox-primitive@1.0.2`                       | False                   | `[]`                            |
| `uri-js@4.4.1`                                | False                   | `[]`                            |
| `version-guard@1.1.1`                         | False                   | `[]`                            |
| `which-boxed-primitive@1.0.2`                 | False                   | `[]`                            |
| `which-builtin-type@1.1.3`                    | False                   | `[]`                            |
| `which-collection@1.0.1`                      | False                   | `[]`                            |
| `which-typed-array@1.1.11`                    | False                   | `[]`                            |
| `which@2.0.2`                                 | False                   | `[]`                            |
| `wrappy@1.0.2`                                | False                   | `[]`                            |
| `xdg-basedir@4.0.0`                           | False                   | `[]`                            |
| `yallist@4.0.0`                               | False                   | `[]`                            |
| `yocto-queue@0.1.0`                           | False                   | `[]`                            |
</details>

All packages have valid code signature.

All packages have code signature.

<details>
<summary>List of deprecated packages(6)</summary>
    


| package_name                          | deprecated_in_version   | all_deprecated   | parent   |
|:--------------------------------------|:------------------------|:-----------------|:---------|
| `@humanwhocodes/config-array@0.11.11` | True                    | True             | `[]`     |
| `@humanwhocodes/object-schema@1.2.1`  | True                    | True             | `[]`     |
| `eslint@8.51.0`                       | True                    | False            | `[]`     |
| `glob@7.2.3`                          | True                    | False            | `[]`     |
| `inflight@1.0.6`                      | True                    | True             | `[]`     |
| `rimraf@3.0.2`                        | True                    | False            | `[]`     |
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

Report created on 2025-05-13 00:46:53
- Tool version: 1dfb5543
- Project Name: juliangruber/brace-expansion
- Project Version: 6a39bdddcf944374b475d99b0e8292d3727c7ebe
- Package Manager: npm
