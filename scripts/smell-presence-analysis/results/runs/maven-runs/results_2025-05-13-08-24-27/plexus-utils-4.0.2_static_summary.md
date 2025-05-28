
# Software Supply Chain Report of codehaus-plexus/plexus-utils - plexus-utils-4.0.2

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
        

 ### Total packages in the supply chain: 308


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 57

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 5

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 1

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 10


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(57)</summary>
    


| package_name                                                                  | sha_exists   | tag_version                                 | is_sha   | sha   | tag_url   | message                                                             |   status_code_for_sha | parent                                                             | command           |
|:------------------------------------------------------------------------------|:-------------|:--------------------------------------------|:---------|:------|:----------|:--------------------------------------------------------------------|----------------------:|:-------------------------------------------------------------------|:------------------|
| `org.apache.commons:commons-compress@1.20`                                    | False        | `1.20`                                      | False    |       |           | Tag 1.20 not found in the repo                                      |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.8.1`                                      | False        | `3.8.1`                                     | False    |       |           | Tag 3.8.1 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.apache.httpcomponents:httpclient@4.5.13`                                 | False        | `4.5.13`                                    | False    |       |           | Tag 4.5.13 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `org.apache.httpcomponents:httpcore@4.4.14`                                   | False        | `4.4.14`                                    | False    |       |           | Tag 4.4.14 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-decoration-model@1.11.1`                        | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@1.11.1`                           | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@1.11.1`                              | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-integration-tools@1.11.1`                       | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `org.eclipse.jetty:jetty-server@9.4.46.v20220331`                             | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-http@9.4.46.v20220331`                               | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-io@9.4.46.v20220331`                                 | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-servlet@9.4.46.v20220331`                            | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-security@9.4.46.v20220331`                           | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-util-ajax@9.4.46.v20220331`                          | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-webapp@9.4.46.v20220331`                             | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-xml@9.4.46.v20220331`                                | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-util@9.4.46.v20220331`                               | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-model@2.0.0`                               | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@2.0.0`                            | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@2.0.0`                               | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.26.1`                                  | False        | `1.26.1`                                    | False    |       |           | Tag 1.26.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-jar-plugin@3.4.1`                  | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.plexus@0.9.0.M3`                           | False        | `0.9.0.M3`                                  | False    |       |           | Tag 0.9.0.M3 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.inject@0.9.0.M3`                           | False        | `0.9.0.M3`                                  | False    |       |           | Tag 0.9.0.M3 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `commons-codec:commons-codec@1.17.1`                                          | False        | `1.17.1`                                    | False    |       |           | Tag 1.17.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.bcel:bcel@6.10.0`                                                 | False        | `6.10.0`                                    | False    |       |           | Tag 6.10.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.17.0`                                     | False        | `3.17.0`                                    | False    |       |           | Tag 3.17.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.commons:commons-collections4@4.4`                                 | False        | `4.4`                                       | False    |       |           | Tag 4.4 not found in the repo                                       |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `commons-io:commons-io@2.16.1`                                                | False        | `2.16.1`                                    | False    |       |           | Tag 2.16.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-jar-plugin@3.4.1`                  | `resolve-plugins` |
| `org.apache.commons:commons-text@1.11.0`                                      | False        | `1.11.0`                                    | False    |       |           | Tag 1.11.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-integration-tools@2.0.0`                        | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `commons-validator:commons-validator@1.9.0`                                   | False        | `1.9.0`                                     | False    |       |           | Tag 1.9.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `commons-logging:commons-logging@1.3.2`                                       | False        | `1.3.2`                                     | False    |       |           | Tag 1.3.2 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.14.0`                                     | False        | `3.14.0`                                    | False    |       |           | Tag 3.14.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-jar-plugin@3.4.1`                  | `resolve-plugins` |
| `commons-codec:commons-codec@1.16.1`                                          | False        | `1.16.1`                                    | False    |       |           | Tag 1.16.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-jar-plugin@3.4.1`                  | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.plexus@0.9.0.M2`                           | False        | `0.9.0.M2`                                  | False    |       |           | Tag 0.9.0.M2 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.inject@0.9.0.M2`                           | False        | `0.9.0.M2`                                  | False    |       |           | Tag 0.9.0.M2 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `commons-io:commons-io@2.15.1`                                                | False        | `2.15.1`                                    | False    |       |           | Tag 2.15.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-surefire-plugin@3.2.5`             | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.13.0`                                     | False        | `3.13.0`                                    | False    |       |           | Tag 3.13.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-enforcer-plugin@3.4.1`             | `resolve-plugins` |
| `commons-codec:commons-codec@1.16.0`                                          | False        | `1.16.0`                                    | False    |       |           | Tag 1.16.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `commons-io:commons-io@2.13.0`                                                | False        | `2.13.0`                                    | False    |       |           | Tag 2.13.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-enforcer-plugin@3.4.1`             | `resolve-plugins` |
| `com.google.guava:guava@31.0.1-jre`                                           | False        | `31.0.1-jre`                                | False    |       |           | Tag 31.0.1-jre not found in the repo                                |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `com.google.guava:listenablefuture@9999.0-empty-to-avoid-conflict-with-guava` | False        | `9999.0-empty-to-avoid-conflict-with-guava` | False    |       |           | Tag 9999.0-empty-to-avoid-conflict-with-guava not found in the repo |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `tree`            |
| `org.javassist:javassist@3.28.0-GA`                                           | False        | `3.28.0-GA`                                 | False    |       |           | Tag 3.28.0-GA not found in the repo                                 |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.12.0`                                     | False        | `3.12.0`                                    | False    |       |           | Tag 3.12.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`            | `resolve-plugins` |
| `javax.activation:javax.activation-api@1.2.0`                                 | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
| `com.diffplug.spotless:spotless-maven-plugin@2.43.0`                          | False        | `2.43.0`                                    | False    |       |           | Tag 2.43.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.spotless:spotless-lib@2.45.0`                                   | False        | `2.45.0`                                    | False    |       |           | Tag 2.45.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.spotless:spotless-lib-extra@2.45.0`                             | False        | `2.45.0`                                    | False    |       |           | Tag 2.45.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `dev.equo.ide:solstice@1.7.5`                                                 | False        | `1.7.5`                                     | False    |       |           | Tag 1.7.5 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `org.eclipse.platform:org.eclipse.osgi@3.18.300`                              | False        | `3.18.300`                                  | False    |       |           | Tag 3.18.300 not found in the repo                                  |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `org.jetbrains:annotations@13.0`                                              | False        | `13.0`                                      | False    |       |           | Tag 13.0 not found in the repo                                      |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.durian:durian-core@1.2.0`                                       | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.durian:durian-io@1.2.0`                                         | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.durian:durian-collect@1.2.0`                                    | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `org.jdom:jdom2@2.0.6.1`                                                      | False        | `2.0.6.1`                                   | False    |       |           | Tag 2.0.6.1 not found in the repo                                   |                   404 | `org.apache.maven.plugins:maven-scm-publish-plugin@3.2.1`          | `resolve-plugins` |
| `commons-io:commons-io@2.11.0`                                                | False        | `2.11.0`                                    | False    |       |           | Tag 2.11.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
| `org.junit.platform:junit-platform-commons@1.10.2`                            | False        | `1.10.2`                                    | False    |       |           | Tag 1.10.2 not found in the repo                                    |                   404 | `org.junit.jupiter:junit-jupiter-api@5.10.2`                       | `tree`            |
</details>

<details>
<summary>Source code links that could not be found(6)</summary>
    


|   index | package_name                                    | github_url                    | github_exists   | parent                                                   | command           |
|--------:|:------------------------------------------------|:------------------------------|:----------------|:---------------------------------------------------------|:------------------|
|       1 | `org.sonatype.plexus:plexus-sec-dispatcher@1.3` | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1` | `resolve-plugins` |
|       2 | `org.sonatype.plexus:plexus-cipher@1.4`         | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1` | `resolve-plugins` |
|       3 | `commons-beanutils:commons-beanutils@1.7.0`     | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`      | `resolve-plugins` |
|       4 | `dom4j:dom4j@1.1`                               | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1` | `resolve-plugins` |
|       5 | `oro:oro@2.0.8`                                 | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1` | `resolve-plugins` |
|       6 | `org.iq80.snappy:snappy@0.4`                    | https://github.com/dain/snapy | False           | `org.apache.maven.plugins:maven-jar-plugin@3.4.1`        | `resolve-plugins` |
</details>

The package manager (maven) does not support checking for provenance.

All packages have valid code signature.

<details>
<summary>List of packages without code signature(10)</summary>
    


| package_name                                              | signature_present   | parent                                                    | command           |
|:----------------------------------------------------------|:--------------------|:----------------------------------------------------------|:------------------|
| `javax.inject:javax.inject@1`                             | False               | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`   | `resolve-plugins` |
| `aopalliance:aopalliance@1.0`                             | False               | `org.apache.maven.plugins:maven-surefire-plugin@3.2.5`    | `resolve-plugins` |
| `org.codehaus.plexus:plexus-i18n@1.0-beta-10`             | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`  | `resolve-plugins` |
| `com.google.collections:google-collections@1.0`           | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`  | `resolve-plugins` |
| `commons-beanutils:commons-beanutils@1.7.0`               | False               | `org.apache.maven.plugins:maven-site-plugin@3.12.1`       | `resolve-plugins` |
| `commons-digester:commons-digester@1.8`                   | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`  | `resolve-plugins` |
| `commons-chain:commons-chain@1.1`                         | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`  | `resolve-plugins` |
| `dom4j:dom4j@1.1`                                         | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`  | `resolve-plugins` |
| `oro:oro@2.0.8`                                           | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`  | `resolve-plugins` |
| `org.apache.maven.scm:maven-scm-providers-standard@2.0.0` | False               | `org.apache.maven.plugins:maven-scm-publish-plugin@3.2.1` | `resolve-plugins` |
</details>

The package manager (maven) does not support checking for deprecated packages.

The package manager (maven) does not support checking for aliased packages.

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
    
- Source code repo is not hosted on GitHub:  41

    This could be due, for example, to the package being hosted on a different platform.

    This does not mean that the source code URL is invalid.

    However, for non-GitHub repositories, not all checks can currently be performed.

|   index | package_name                                                         | github_url                                                                                                            | parent                                                             | command           |
|--------:|:---------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|:------------------|
|       1 | `org.eclipse.aether:aether-spi@1.0.0.v20140518`                      | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-spi/                                                      | `org.apache.maven.plugins:maven-surefire-plugin@3.2.5`             | `resolve-plugins` |
|       2 | `org.eclipse.aether:aether-impl@1.0.0.v20140518`                     | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-impl/                                                     | `org.apache.maven.plugins:maven-surefire-plugin@3.2.5`             | `resolve-plugins` |
|       3 | `org.eclipse.aether:aether-api@1.0.0.v20140518`                      | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-api/                                                      | `org.apache.maven.plugins:maven-scm-publish-plugin@3.2.1`          | `resolve-plugins` |
|       4 | `org.eclipse.sisu:org.eclipse.sisu.plexus@0.3.5`                     | http://git.eclipse.org/c/sisu/org.eclipse.sisu.plexus.git/tree/org.eclipse.sisu.plexus/                               | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|       5 | `javax.annotation:javax.annotation-api@1.2`                          | http://java.net/projects/glassfish/sources/svn/show/tags/javax.annotation-api-1.2                                     | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|       6 | `org.eclipse.sisu:org.eclipse.sisu.inject@0.3.5`                     | http://git.eclipse.org/c/sisu/org.eclipse.sisu.inject.git/tree/org.eclipse.sisu.inject/                               | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|       7 | `javax.inject:javax.inject@1`                                        | http://code.google.com/p/atinject/source/checkout                                                                     | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
|       8 | `aopalliance:aopalliance@1.0`                                        | http://aopalliance.sourceforge.net                                                                                    | `org.apache.maven.plugins:maven-surefire-plugin@3.2.5`             | `resolve-plugins` |
|       9 | `com.google.guava:guava@16.0.1`                                      | http://code.google.com/p/guava-libraries/source/browse/guava                                                          | `org.apache.maven.plugins:maven-surefire-plugin@3.2.5`             | `resolve-plugins` |
|      10 | `org.eclipse.aether:aether-util@1.0.0.v20140518`                     | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-util/                                                     | `org.apache.maven.plugins:maven-scm-publish-plugin@3.2.1`          | `resolve-plugins` |
|      11 | `org.tukaani:xz@1.9`                                                 | https://git.tukaani.org/?p=xz-java.git                                                                                | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
|      12 | `org.codehaus.plexus:plexus-i18n@1.0-beta-10`                        | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10                              | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      13 | `org.apache.xbean:xbean-reflect@3.7`                                 | http://svn.apache.org/viewvc/geronimo/xbean/tags/xbean-3.7/xbean-reflect                                              | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      14 | `com.google.collections:google-collections@1.0`                      | http://code.google.com/p/google-collections/source/browse/                                                            | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      15 | `commons-logging:commons-logging@1.2`                                | http://svn.apache.org/repos/asf/commons/proper/logging/trunk                                                          | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      16 | `commons-codec:commons-codec@1.11`                                   | http://svn.apache.org/viewvc/commons/proper/codec/trunk                                                               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      17 | `org.apache.velocity:velocity@1.7`                                   | http://svn.apache.org/viewvc/velocity/engine/trunk                                                                    | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      18 | `commons-lang:commons-lang@2.4`                                      | http://svn.apache.org/viewvc/commons/proper/lang/trunk                                                                | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      19 | `org.apache.velocity:velocity-tools@2.0`                             | http://svn.apache.org/repos/asf/velocity/tools/trunk                                                                  | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      20 | `commons-digester:commons-digester@1.8`                              | http://svn.apache.org/repos/asf/jakarta/commons/proper/digester/trunk                                                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      21 | `commons-chain:commons-chain@1.1`                                    | http://svn.apache.org/viewcvs.cgi                                                                                     | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      22 | `commons-collections:commons-collections@3.2.2`                      | http://svn.apache.org/viewvc/commons/proper/collections/trunk                                                         | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      23 | `javax.servlet:javax.servlet-api@3.1.0`                              | http://java.net/projects/glassfish/sources/svn/show/tags/javax.servlet-api-3.1.0                                      | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      24 | `org.apache.commons:commons-digester3@3.2`                           | http://svn.apache.org/viewvc/commons/proper/digester/tags/DIGESTER3_3_2_RC2                                           | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
|      25 | `commons-beanutils:commons-beanutils@1.9.4`                          | http://svn.apache.org/viewvc/commons/proper/beanutils/tags/BEANUTILS_1_9_3_RC3                                        | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      26 | `commons-digester:commons-digester@2.1`                              | http://svn.apache.org/viewvc/commons/proper/digester/tags/DIGESTER_2_1_RC2                                            | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
|      27 | `org.codehaus.plexus:plexus-component-annotations@1.5.5`             | http://fisheye.codehaus.org/browse/plexus/plexus-containers/tags/plexus-containers-1.5.5/plexus-component-annotations | `org.apache.maven.plugins:maven-surefire-plugin@3.2.5`             | `resolve-plugins` |
|      28 | `org.ow2.asm:asm@9.6`                                                | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
|      29 | `org.eclipse.aether:aether-spi@0.9.0.M2`                             | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-spi/                                                      | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      30 | `org.eclipse.aether:aether-impl@0.9.0.M2`                            | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-impl/                                                     | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      31 | `org.eclipse.aether:aether-api@0.9.0.M2`                             | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-api/                                                      | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      32 | `org.eclipse.aether:aether-util@0.9.0.M2`                            | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-util/                                                     | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      33 | `org.apache.maven:maven-model@2.2.1`                                 | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-model                                               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      34 | `com.google.code.findbugs:jsr305@3.0.2`                              | https://code.google.com/p/jsr-305/                                                                                    | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `tree`            |
|      35 | `com.google.j2objc:j2objc-annotations@1.3`                           | http://svn.sonatype.org/spice/tags/oss-parent-7/j2objc-annotations                                                    | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `tree`            |
|      36 | `net.sf.saxon:Saxon-HE@10.6`                                         | https://dev.saxonica.com/repos/archive/opensource/                                                                    | `org.apache.maven.plugins:maven-checkstyle-plugin@3.3.1`           | `resolve-plugins` |
|      37 | `org.eclipse.jgit:org.eclipse.jgit@6.7.0.202309050840-r`             | https://git.eclipse.org/r/plugins/gitiles/jgit/jgit/org.eclipse.jgit                                                  | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
|      38 | `org.sonatype.plexus:plexus-build-api@0.0.7`                         | http://svn.sonatype.org/spice/tags/plexus-build-api-0.0.7                                                             | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`            | `resolve-plugins` |
|      39 | `org.eclipse.jgit:org.eclipse.jgit@5.13.1.202206130422-r`            | https://git.eclipse.org/r/plugins/gitiles/jgit/jgit/org.eclipse.jgit                                                  | `org.apache.maven.plugins:maven-scm-publish-plugin@3.2.1`          | `resolve-plugins` |
|      40 | `org.eclipse.jgit:org.eclipse.jgit.ssh.apache@5.13.1.202206130422-r` | https://git.eclipse.org/r/plugins/gitiles/jgit/jgit/org.eclipse.jgit.ssh.apache                                       | `org.apache.maven.plugins:maven-scm-publish-plugin@3.2.1`          | `resolve-plugins` |
|      41 | `org.apache.maven.shared:maven-shared-incremental@1.1`               | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-incremental-1.1                                           | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
</details>


---

Report created by [dirty-waters](https://github.com/chains-project/dirty-waters/).

Report created on 2025-05-13 08:42:54
- Tool version: 1dfb5543
- Project Name: codehaus-plexus/plexus-utils
- Project Version: plexus-utils-4.0.2
- Package Manager: maven
