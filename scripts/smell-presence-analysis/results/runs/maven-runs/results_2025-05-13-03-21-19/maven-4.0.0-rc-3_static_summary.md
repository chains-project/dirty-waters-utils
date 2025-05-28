
# Software Supply Chain Report of apache/maven - maven-4.0.0-rc-3

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
        

 ### Total packages in the supply chain: 376


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 62

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 11

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 2

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 36


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(62)</summary>
    


| package_name                                                                  | sha_exists   | tag_version                                 | is_sha   | sha   | tag_url   | message                                                             |   status_code_for_sha | parent                                                             | command           |
|:------------------------------------------------------------------------------|:-------------|:--------------------------------------------|:---------|:------|:----------|:--------------------------------------------------------------------|----------------------:|:-------------------------------------------------------------------|:------------------|
| `org.apache.rat:apache-rat-plugin@0.16.1`                                     | False        | `0.16.1`                                    | False    |       |           | Tag 0.16.1 not found in the repo                                    |                   404 | `org.apache.rat:apache-rat-plugin@0.16.1`                          | `resolve-plugins` |
| `org.apache.rat:apache-rat-core@0.16.1`                                       | False        | `0.16.1`                                    | False    |       |           | Tag 0.16.1 not found in the repo                                    |                   404 | `org.apache.rat:apache-rat-plugin@0.16.1`                          | `resolve-plugins` |
| `org.apache.commons:commons-collections4@4.4`                                 | False        | `4.4`                                       | False    |       |           | Tag 4.4 not found in the repo                                       |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `commons-io:commons-io@2.15.1`                                                | False        | `2.15.1`                                    | False    |       |           | Tag 2.15.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-remote-resources-plugin@3.2.0`     | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.25.0`                                  | False        | `1.25.0`                                    | False    |       |           | Tag 1.25.0 not found in the repo                                    |                   404 | `org.apache.rat:apache-rat-plugin@0.16.1`                          | `resolve-plugins` |
| `commons-cli:commons-cli@1.6.0`                                               | False        | `1.6.0`                                     | False    |       |           | Tag 1.6.0 not found in the repo                                     |                   404 | `org.apache.rat:apache-rat-plugin@0.16.1`                          | `resolve-plugins` |
| `org.apache.httpcomponents:httpclient@4.5.13`                                 | False        | `4.5.13`                                    | False    |       |           | Tag 4.5.13 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `org.apache.httpcomponents:httpcore@4.4.14`                                   | False        | `4.4.14`                                    | False    |       |           | Tag 4.4.14 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-decoration-model@1.11.1`                        | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-integration-tools@1.11.1`                       | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@1.11.1`                           | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@1.11.1`                              | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.14.0`                                     | False        | `3.14.0`                                    | False    |       |           | Tag 3.14.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.20`                                    | False        | `1.20`                                      | False    |       |           | Tag 1.20 not found in the repo                                      |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.8.1`                                      | False        | `3.8.1`                                     | False    |       |           | Tag 3.8.1 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.7.1`           | `resolve-plugins` |
| `org.eclipse.jetty:jetty-server@9.4.46.v20220331`                             | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-http@9.4.46.v20220331`                               | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-io@9.4.46.v20220331`                                 | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-servlet@9.4.46.v20220331`                            | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-security@9.4.46.v20220331`                           | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-util-ajax@9.4.46.v20220331`                          | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-webapp@9.4.46.v20220331`                             | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-xml@9.4.46.v20220331`                                | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.eclipse.jetty:jetty-util@9.4.46.v20220331`                               | False        | `9.4.46.v20220331`                          | False    |       |           | Tag 9.4.46.v20220331 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
| `org.twdata.maven:mojo-executor@2.4.0`                                        | False        | `2.4.0`                                     | False    |       |           | Tag 2.4.0 not found in the repo                                     |                   404 | `dev.jbang:jbang-maven-plugin@0.0.8`                               | `resolve-plugins` |
| `org.apache.commons:commons-text@1.12.0`                                      | False        | `1.12.0`                                    | False    |       |           | Tag 1.12.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.7.1`           | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.26.1`                                  | False        | `1.26.1`                                    | False    |       |           | Tag 1.26.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-jar-plugin@3.4.2`                  | `resolve-plugins` |
| `commons-codec:commons-codec@1.16.1`                                          | False        | `1.16.1`                                    | False    |       |           | Tag 1.16.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-jar-plugin@3.4.2`                  | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-model@2.0.0`                               | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@2.0.0`                            | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@2.0.0`                               | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.plexus@0.9.0.M3`                           | False        | `0.9.0.M3`                                  | False    |       |           | Tag 0.9.0.M3 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.inject@0.9.0.M3`                           | False        | `0.9.0.M3`                                  | False    |       |           | Tag 0.9.0.M3 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `commons-codec:commons-codec@1.17.1`                                          | False        | `1.17.1`                                    | False    |       |           | Tag 1.17.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.bcel:bcel@6.10.0`                                                 | False        | `6.10.0`                                    | False    |       |           | Tag 6.10.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.17.0`                                     | False        | `3.17.0`                                    | False    |       |           | Tag 3.17.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `commons-io:commons-io@2.16.1`                                                | False        | `2.16.1`                                    | False    |       |           | Tag 2.16.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-enforcer-plugin@3.5.0`             | `resolve-plugins` |
| `org.apache.commons:commons-text@1.11.0`                                      | False        | `1.11.0`                                    | False    |       |           | Tag 1.11.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-integration-tools@2.0.0`                        | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `commons-validator:commons-validator@1.9.0`                                   | False        | `1.9.0`                                     | False    |       |           | Tag 1.9.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `commons-logging:commons-logging@1.3.2`                                       | False        | `1.3.2`                                     | False    |       |           | Tag 1.3.2 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.23.0`                                  | False        | `1.23.0`                                    | False    |       |           | Tag 1.23.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-remote-resources-plugin@3.2.0`     | `resolve-plugins` |
| `commons-codec:commons-codec@1.17.0`                                          | False        | `1.17.0`                                    | False    |       |           | Tag 1.17.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-enforcer-plugin@3.5.0`             | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.plexus@0.9.0.M2`                           | False        | `0.9.0.M2`                                  | False    |       |           | Tag 0.9.0.M2 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.inject@0.9.0.M2`                           | False        | `0.9.0.M2`                                  | False    |       |           | Tag 0.9.0.M2 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `com.google.guava:guava@31.0.1-jre`                                           | False        | `31.0.1-jre`                                | False    |       |           | Tag 31.0.1-jre not found in the repo                                |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `com.google.guava:listenablefuture@9999.0-empty-to-avoid-conflict-with-guava` | False        | `9999.0-empty-to-avoid-conflict-with-guava` | False    |       |           | Tag 9999.0-empty-to-avoid-conflict-with-guava not found in the repo |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `tree`            |
| `org.javassist:javassist@3.28.0-GA`                                           | False        | `3.28.0-GA`                                 | False    |       |           | Tag 3.28.0-GA not found in the repo                                 |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `javax.activation:javax.activation-api@1.2.0`                                 | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
| `com.diffplug.spotless:spotless-maven-plugin@2.43.0`                          | False        | `2.43.0`                                    | False    |       |           | Tag 2.43.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.spotless:spotless-lib@2.45.0`                                   | False        | `2.45.0`                                    | False    |       |           | Tag 2.45.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.spotless:spotless-lib-extra@2.45.0`                             | False        | `2.45.0`                                    | False    |       |           | Tag 2.45.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `dev.equo.ide:solstice@1.7.5`                                                 | False        | `1.7.5`                                     | False    |       |           | Tag 1.7.5 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `org.eclipse.platform:org.eclipse.osgi@3.18.300`                              | False        | `3.18.300`                                  | False    |       |           | Tag 3.18.300 not found in the repo                                  |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `org.jetbrains:annotations@13.0`                                              | False        | `13.0`                                      | False    |       |           | Tag 13.0 not found in the repo                                      |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.durian:durian-core@1.2.0`                                       | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.durian:durian-io@1.2.0`                                         | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `com.diffplug.durian:durian-collect@1.2.0`                                    | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `commons-codec:commons-codec@1.16.0`                                          | False        | `1.16.0`                                    | False    |       |           | Tag 1.16.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
| `commons-io:commons-io@2.11.0`                                                | False        | `2.11.0`                                    | False    |       |           | Tag 2.11.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.12.0`                                     | False        | `3.12.0`                                    | False    |       |           | Tag 3.12.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`            | `resolve-plugins` |
| `org.junit.platform:junit-platform-commons@1.12.0`                            | False        | `1.12.0`                                    | False    |       |           | Tag 1.12.0 not found in the repo                                    |                   404 | `org.junit.jupiter:junit-jupiter-api@5.12.0`                       | `tree`            |
</details>

<details>
<summary>Source code links that could not be found(13)</summary>
    


|   index | package_name                                    | github_url                    | github_exists   | parent                                                         | command           |
|--------:|:------------------------------------------------|:------------------------------|:----------------|:---------------------------------------------------------------|:------------------|
|       1 | `dom4j:dom4j@1.1`                               | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`       | `resolve-plugins` |
|       2 | `oro:oro@2.0.8`                                 | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`       | `resolve-plugins` |
|       3 | `org.sonatype.plexus:plexus-sec-dispatcher@1.3` | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`       | `resolve-plugins` |
|       4 | `org.sonatype.plexus:plexus-cipher@1.4`         | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`       | `resolve-plugins` |
|       5 | `commons-beanutils:commons-beanutils@1.7.0`     | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-dependency-plugin@3.7.1`       | `resolve-plugins` |
|       6 | `commons-validator:commons-validator@1.1.4`     | No_repo_info_found            |                 | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`            | `resolve-plugins` |
|       7 | `oro:oro@2.0.7`                                 | No_repo_info_found            |                 | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`            | `resolve-plugins` |
|       8 | `commons-collections:commons-collections@2.0`   | No_repo_info_found            |                 | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`            | `resolve-plugins` |
|       9 | `commons-logging:commons-logging-api@1.0.4`     | No_repo_info_found            |                 | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`            | `resolve-plugins` |
|      10 | `xerces:xercesImpl@2.7.1`                       | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-doap-plugin@1.2`               | `resolve-plugins` |
|      11 | `commons-codec:commons-codec@1.2`               | No_repo_info_found            |                 | `org.apache.maven.plugins:maven-doap-plugin@1.2`               | `resolve-plugins` |
|      12 | `org.iq80.snappy:snappy@0.4`                    | https://github.com/dain/snapy | False           | `org.apache.maven.plugins:maven-remote-resources-plugin@3.2.0` | `resolve-plugins` |
|      13 | `org.slf4j:slf4j-api@1.7.2`                     | https://github.com/ceki/slf4j | False           | `dev.jbang:jbang-maven-plugin@0.0.8`                           | `resolve-plugins` |
</details>

The package manager (maven) does not support checking for provenance.

All packages have valid code signature.

<details>
<summary>List of packages without code signature(36)</summary>
    


| package_name                                                        | signature_present   | parent                                                   | command           |
|:--------------------------------------------------------------------|:--------------------|:---------------------------------------------------------|:------------------|
| `org.codehaus.plexus:plexus-i18n@1.0-beta-10`                       | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0` | `resolve-plugins` |
| `commons-digester:commons-digester@1.8`                             | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0` | `resolve-plugins` |
| `commons-chain:commons-chain@1.1`                                   | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0` | `resolve-plugins` |
| `dom4j:dom4j@1.1`                                                   | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0` | `resolve-plugins` |
| `oro:oro@2.0.8`                                                     | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0` | `resolve-plugins` |
| `javax.inject:javax.inject@1`                                       | False               | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`  | `resolve-plugins` |
| `aopalliance:aopalliance@1.0`                                       | False               | `org.apache.maven.plugins:maven-site-plugin@3.12.1`      | `resolve-plugins` |
| `com.google.collections:google-collections@1.0`                     | False               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0` | `resolve-plugins` |
| `commons-beanutils:commons-beanutils@1.7.0`                         | False               | `org.apache.maven.plugins:maven-dependency-plugin@3.7.1` | `resolve-plugins` |
| `org.apache.maven.wagon:wagon-provider-api@1.0-beta-2`              | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `org.codehaus.plexus:plexus-utils@1.5.1`                            | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `org.codehaus.plexus:plexus-container-default@1.0-alpha-9-stable-1` | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `junit:junit@3.8.1`                                                 | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `classworlds:classworlds@1.1-alpha-2`                               | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `commons-validator:commons-validator@1.1.4`                         | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `oro:oro@2.0.7`                                                     | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `org.codehaus.plexus:plexus-i18n@1.0-beta-6`                        | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `org.codehaus.plexus:plexus-velocity@1.1.2`                         | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `plexus:plexus-utils@1.0.2`                                         | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `commons-collections:commons-collections@2.0`                       | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `commons-logging:commons-logging-api@1.0.4`                         | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `velocity:velocity@1.4`                                             | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `velocity:velocity-dep@1.4`                                         | False               | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`      | `resolve-plugins` |
| `backport-util-concurrent:backport-util-concurrent@3.1`             | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `org.netbeans.lib:cvsclient@20060125`                               | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `ch.ethz.ganymed:ganymed-ssh2@build210`                             | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `com.hp.hpl.jena:jena@2.6.3`                                        | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `com.hp.hpl.jena:iri@0.8`                                           | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `com.ibm.icu:icu4j@3.4.4`                                           | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `xerces:xercesImpl@2.7.1`                                           | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `org.slf4j:slf4j-api@1.5.8`                                         | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `org.slf4j:slf4j-log4j12@1.5.8`                                     | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `log4j:log4j@1.2.13`                                                | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `commons-logging:commons-logging@1.0.4`                             | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `commons-codec:commons-codec@1.2`                                   | False               | `org.apache.maven.plugins:maven-doap-plugin@1.2`         | `resolve-plugins` |
| `org.apache.maven:apache-maven@4.0.0-rc-3`                          | False               | `None`                                                   | `tree`            |
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
    
- Source code repo is not hosted on GitHub:  87

    This could be due, for example, to the package being hosted on a different platform.

    This does not mean that the source code URL is invalid.

    However, for non-GitHub repositories, not all checks can currently be performed.

|   index | package_name                                                        | github_url                                                                                               | parent                                                             | command           |
|--------:|:--------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|:------------------|
|       1 | `commons-beanutils:commons-beanutils@1.9.4`                         | http://svn.apache.org/viewvc/commons/proper/beanutils/tags/BEANUTILS_1_9_3_RC3                           | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|       2 | `commons-logging:commons-logging@1.2`                               | http://svn.apache.org/repos/asf/commons/proper/logging/trunk                                             | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|       3 | `commons-codec:commons-codec@1.11`                                  | http://svn.apache.org/viewvc/commons/proper/codec/trunk                                                  | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|       4 | `org.apache.maven:maven-artifact@2.2.1`                             | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-artifact                               | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|       5 | `org.apache.maven:maven-model@2.2.1`                                | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-model                                  | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|       6 | `org.apache.maven:maven-plugin-api@2.2.1`                           | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-plugin-api                             | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|       7 | `org.codehaus.plexus:plexus-i18n@1.0-beta-10`                       | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|       8 | `org.apache.velocity:velocity@1.7`                                  | http://svn.apache.org/viewvc/velocity/engine/trunk                                                       | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|       9 | `commons-lang:commons-lang@2.4`                                     | http://svn.apache.org/viewvc/commons/proper/lang/trunk                                                   | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      10 | `org.apache.velocity:velocity-tools@2.0`                            | http://svn.apache.org/repos/asf/velocity/tools/trunk                                                     | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      11 | `commons-digester:commons-digester@1.8`                             | http://svn.apache.org/repos/asf/jakarta/commons/proper/digester/trunk                                    | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      12 | `commons-chain:commons-chain@1.1`                                   | http://svn.apache.org/viewcvs.cgi                                                                        | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      13 | `commons-collections:commons-collections@3.2.2`                     | http://svn.apache.org/viewvc/commons/proper/collections/trunk                                            | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      14 | `org.eclipse.aether:aether-spi@1.0.0.v20140518`                     | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-spi/                                         | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      15 | `org.eclipse.aether:aether-impl@1.0.0.v20140518`                    | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-impl/                                        | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      16 | `org.eclipse.aether:aether-api@1.0.0.v20140518`                     | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-api/                                         | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      17 | `org.eclipse.sisu:org.eclipse.sisu.plexus@0.3.5`                    | http://git.eclipse.org/c/sisu/org.eclipse.sisu.plexus.git/tree/org.eclipse.sisu.plexus/                  | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      18 | `javax.annotation:javax.annotation-api@1.2`                         | http://java.net/projects/glassfish/sources/svn/show/tags/javax.annotation-api-1.2                        | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      19 | `org.eclipse.sisu:org.eclipse.sisu.inject@0.3.5`                    | http://git.eclipse.org/c/sisu/org.eclipse.sisu.inject.git/tree/org.eclipse.sisu.inject/                  | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      20 | `javax.inject:javax.inject@1`                                       | http://code.google.com/p/atinject/source/checkout                                                        | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
|      21 | `aopalliance:aopalliance@1.0`                                       | http://aopalliance.sourceforge.net                                                                       | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      22 | `com.google.guava:guava@16.0.1`                                     | http://code.google.com/p/guava-libraries/source/browse/guava                                             | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      23 | `org.eclipse.aether:aether-util@1.0.0.v20140518`                    | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-util/                                        | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      24 | `org.tukaani:xz@1.9`                                                | https://git.tukaani.org/?p=xz-java.git                                                                   | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
|      25 | `org.apache.xbean:xbean-reflect@3.7`                                | http://svn.apache.org/viewvc/geronimo/xbean/tags/xbean-3.7/xbean-reflect                                 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      26 | `com.google.collections:google-collections@1.0`                     | http://code.google.com/p/google-collections/source/browse/                                               | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      27 | `javax.servlet:javax.servlet-api@3.1.0`                             | http://java.net/projects/glassfish/sources/svn/show/tags/javax.servlet-api-3.1.0                         | `org.apache.maven.plugins:maven-site-plugin@3.12.1`                | `resolve-plugins` |
|      28 | `org.ow2.asm:asm@9.7`                                               | https://gitlab.ow2.org/asm/asm/                                                                          | `org.apache.maven.plugins:maven-surefire-plugin@3.5.2`             | `resolve-plugins` |
|      29 | `org.sonatype.plexus:plexus-build-api@0.0.7`                        | http://svn.sonatype.org/spice/tags/plexus-build-api-0.0.7                                                | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`            | `resolve-plugins` |
|      30 | `org.apache.commons:commons-digester3@3.2`                          | http://svn.apache.org/viewvc/commons/proper/digester/tags/DIGESTER3_3_2_RC2                              | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
|      31 | `commons-digester:commons-digester@2.1`                             | http://svn.apache.org/viewvc/commons/proper/digester/tags/DIGESTER_2_1_RC2                               | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.9.0` | `resolve-plugins` |
|      32 | `org.apache.maven:maven-plugin-api@2.0.9`                           | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-plugin-api                      | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      33 | `org.apache.maven:maven-project@2.0.9`                              | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-project                         | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      34 | `org.apache.maven:maven-settings@2.0.9`                             | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-settings                        | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      35 | `org.apache.maven:maven-profile@2.0.9`                              | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-profile                         | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      36 | `org.apache.maven:maven-model@2.0.9`                                | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-model                           | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      37 | `org.apache.maven:maven-artifact-manager@2.0.9`                     | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-artifact-manager                | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      38 | `org.apache.maven:maven-repository-metadata@2.0.9`                  | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-repository-metadata             | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      39 | `org.apache.maven.wagon:wagon-provider-api@1.0-beta-2`              | https://svn.apache.org/repos/asf/maven/wagon/tags/wagon-1.0-beta-2/wagon-provider-api                    | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      40 | `org.apache.maven:maven-plugin-registry@2.0.9`                      | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-plugin-registry                 | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      41 | `org.codehaus.plexus:plexus-utils@1.5.1`                            | http://fisheye.codehaus.org/browse/plexus/plexus-utils/tags/plexus-utils-1.5.1                           | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      42 | `org.apache.maven:maven-artifact@2.0.9`                             | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-artifact                        | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      43 | `org.codehaus.plexus:plexus-container-default@1.0-alpha-9-stable-1` | scm:svn:svn://svn.codehaus.org/plexus/scm/trunk/plexus-containers/plexus-container-default/              | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      44 | `junit:junit@3.8.1`                                                 | http://junit.cvs.sourceforge.net/junit/                                                                  | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      45 | `classworlds:classworlds@1.1-alpha-2`                               | http://cvs.classworlds.codehaus.org/                                                                     | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      46 | `org.apache.maven.shared:maven-dependency-tree@1.2`                 | http://svn.apache.org/viewcvs.cgi/maven/shared/tags/maven-dependency-tree-1.2                            | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      47 | `org.apache.maven.reporting:maven-reporting-api@3.0`                | http://svn.apache.org/viewvc/maven/shared/tags/maven-reporting-api-3.0                                   | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      48 | `org.apache.maven.doxia:doxia-sink-api@1.0`                         | https://svn.apache.org/viewvc/maven/doxia/doxia/tags/doxia-1.0/doxia-sink-api                            | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      49 | `org.apache.maven.reporting:maven-reporting-impl@2.0.2`             | http://svn.apache.org/viewcvs.cgi/maven/components/tags/maven-2.0.2/maven-reporting/maven-reporting-impl | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      50 | `org.apache.maven.doxia:doxia-core@1.0-alpha-7`                     | http://svn.apache.org/viewcvs.cgi/maven/doxia/tags/doxia-1.0-alpha-7/doxia-core                          | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      51 | `org.apache.maven.doxia:doxia-site-renderer@1.0-alpha-7`            | http://svn.apache.org/viewcvs.cgi/maven/doxia/tags/doxia-1.0-alpha-7/doxia-site-renderer                 | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      52 | `org.codehaus.plexus:plexus-i18n@1.0-beta-6`                        | scm:svn:svn://svn.codehaus.org/plexus/scm/trunk/plexus-components/plexus-i18n/                           | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      53 | `org.codehaus.plexus:plexus-velocity@1.1.2`                         | scm:svn:svn://svn.codehaus.org/plexus/scm/trunk/plexus-components/plexus-velocity                        | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      54 | `plexus:plexus-utils@1.0.2`                                         | scm:svn:svn://svn.codehaus.org/plexus/scm/trunk/plexus-utils/                                            | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      55 | `velocity:velocity@1.4`                                             | http://cvs.apache.org/viewcvs/jakarta-turbine-maven/                                                     | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      56 | `velocity:velocity-dep@1.4`                                         | http://cvs.apache.org/viewcvs/jakarta-turbine-maven/                                                     | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      57 | `org.apache.maven.doxia:doxia-decoration-model@1.0-alpha-7`         | http://svn.apache.org/viewcvs.cgi/maven/doxia/tags/doxia-1.0-alpha-7/doxia-decoration-model              | `org.fusesource.mvnplugins:maven-graph-plugin@1.45`                | `resolve-plugins` |
|      58 | `org.apache.maven.plugins:maven-doap-plugin@1.2`                    | http://svn.apache.org/viewvc/maven/plugins/tags/maven-doap-plugin-1.2                                    | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      59 | `org.apache.maven:maven-project@2.2.1`                              | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-project                                | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      60 | `org.apache.maven:maven-settings@2.2.1`                             | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-settings                               | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      61 | `org.apache.maven:maven-profile@2.2.1`                              | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-profile                                | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      62 | `org.apache.maven:maven-artifact-manager@2.2.1`                     | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-artifact-manager                       | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      63 | `org.apache.maven:maven-repository-metadata@2.2.1`                  | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-repository-metadata                    | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      64 | `org.apache.maven.wagon:wagon-provider-api@1.0-beta-6`              | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-provider-api                        | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      65 | `backport-util-concurrent:backport-util-concurrent@3.1`             | svn://dcl.mathcs.emory.edu/software/harness2/trunk/util/backport-util-concurrent/                        | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      66 | `org.apache.maven:maven-plugin-registry@2.2.1`                      | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-plugin-registry                        | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      67 | `commons-lang:commons-lang@2.6`                                     | http://svn.apache.org/viewvc/commons/proper/lang/branches/LANG_2_X                                       | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      68 | `org.netbeans.lib:cvsclient@20060125`                               | http://javacvs.netbeans.org/source/browse/javacvs/libsrc/                                                | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      69 | `ch.ethz.ganymed:ganymed-ssh2@build210`                             | http://www.ganymed.ethz.ch/ssh2/                                                                         | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      70 | `com.hp.hpl.jena:jena@2.6.3`                                        | http://jena.cvs.sourceforge.net/jena/jena2/                                                              | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      71 | `com.hp.hpl.jena:iri@0.8`                                           | http://jena.cvs.sourceforge.net/jena/iri                                                                 | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      72 | `com.ibm.icu:icu4j@3.4.4`                                           | http://www-306.ibm.com/software/globalization/icu/                                                       | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      73 | `org.slf4j:slf4j-api@1.5.8`                                         | http://svn.slf4j.org/viewvc/slf4j/trunk/slf4j-api/                                                       | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      74 | `org.slf4j:slf4j-log4j12@1.5.8`                                     | http://svn.slf4j.org/viewvc/slf4j/trunk/slf4j-log4j12/                                                   | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      75 | `log4j:log4j@1.2.13`                                                | http://svn.apache.org/viewcvs.cgi/logging/log4j/tags/v1_2_13/                                            | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      76 | `commons-httpclient:commons-httpclient@3.1`                         | http://svn.apache.org/repos/asf/jakarta/httpcomponents/oac.hc3x/trunk                                    | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      77 | `commons-logging:commons-logging@1.0.4`                             | http://cvs.apache.org/viewcvs/jakarta-commons/logging/                                                   | `org.apache.maven.plugins:maven-doap-plugin@1.2`                   | `resolve-plugins` |
|      78 | `org.eclipse.aether:aether-spi@0.9.0.M2`                            | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-spi/                                         | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      79 | `org.eclipse.aether:aether-impl@0.9.0.M2`                           | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-impl/                                        | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      80 | `org.eclipse.aether:aether-api@0.9.0.M2`                            | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-api/                                         | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      81 | `org.eclipse.aether:aether-util@0.9.0.M2`                           | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-util/                                        | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      82 | `com.google.code.findbugs:jsr305@3.0.2`                             | https://code.google.com/p/jsr-305/                                                                       | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `tree`            |
|      83 | `com.google.j2objc:j2objc-annotations@1.3`                          | http://svn.sonatype.org/spice/tags/oss-parent-7/j2objc-annotations                                       | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `tree`            |
|      84 | `net.sf.saxon:Saxon-HE@10.6`                                        | https://dev.saxonica.com/repos/archive/opensource/                                                       | `org.apache.maven.plugins:maven-checkstyle-plugin@3.4.0`           | `resolve-plugins` |
|      85 | `org.eclipse.jgit:org.eclipse.jgit@6.7.0.202309050840-r`            | https://git.eclipse.org/r/plugins/gitiles/jgit/jgit/org.eclipse.jgit                                     | `com.diffplug.spotless:spotless-maven-plugin@2.43.0`               | `resolve-plugins` |
|      86 | `org.apache.maven.shared:maven-shared-incremental@1.1`              | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-incremental-1.1                              | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
|      87 | `org.ow2.asm:asm@9.6`                                               | https://gitlab.ow2.org/asm/asm/                                                                          | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
</details>


---

Report created by [dirty-waters](https://github.com/chains-project/dirty-waters/).

Report created on 2025-05-13 03:43:28
- Tool version: 1dfb5543
- Project Name: apache/maven
- Project Version: maven-4.0.0-rc-3
- Package Manager: maven
