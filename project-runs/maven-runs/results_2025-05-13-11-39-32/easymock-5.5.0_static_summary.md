
# Software Supply Chain Report of easymock/easymock - easymock-5.5.0

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
        

 ### Total packages in the supply chain: 433


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 88

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 7

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 3

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 4

:lock: Packages without code signature (⚠️⚠️): 18


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(88)</summary>
    


| package_name                                                                  | sha_exists   | tag_version                                 | is_sha   | sha   | tag_url   | message                                                             |   status_code_for_sha | parent                                                             | command           |
|:------------------------------------------------------------------------------|:-------------|:--------------------------------------------|:---------|:------|:----------|:--------------------------------------------------------------------|----------------------:|:-------------------------------------------------------------------|:------------------|
| `org.apache.commons:commons-collections4@4.4`                                 | False        | `4.4`                                       | False    |       |           | Tag 4.4 not found in the repo                                       |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.8.0` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-model@2.0.0`                               | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-integration-tools@2.0.0`                        | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@2.0.0`                            | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@2.0.0`                               | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.26.2`                                  | False        | `1.26.2`                                    | False    |       |           | Tag 1.26.2 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `commons-codec:commons-codec@1.17.1`                                          | False        | `1.17.1`                                    | False    |       |           | Tag 1.17.1 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `commons-io:commons-io@2.17.0`                                                | False        | `2.17.0`                                    | False    |       |           | Tag 2.17.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.commons:commons-text@1.12.0`                                      | False        | `1.12.0`                                    | False    |       |           | Tag 1.12.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.17.0`                                     | False        | `3.17.0`                                    | False    |       |           | Tag 3.17.0 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.bouncycastle:bcpg-jdk18on@1.78.1`                                        | False        | `1.78.1`                                    | False    |       |           | Tag 1.78.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-gpg-plugin@3.2.7`                  | `resolve-plugins` |
| `org.bouncycastle:bcprov-jdk18on@1.78.1`                                      | False        | `1.78.1`                                    | False    |       |           | Tag 1.78.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-gpg-plugin@3.2.7`                  | `resolve-plugins` |
| `org.bouncycastle:bcutil-jdk18on@1.78.1`                                      | False        | `1.78.1`                                    | False    |       |           | Tag 1.78.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-gpg-plugin@3.2.7`                  | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.plexus@0.9.0.M3`                           | False        | `0.9.0.M3`                                  | False    |       |           | Tag 0.9.0.M3 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.inject@0.9.0.M3`                           | False        | `0.9.0.M3`                                  | False    |       |           | Tag 0.9.0.M3 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.httpcomponents:httpclient@4.5.14`                                 | False        | `4.5.14`                                    | False    |       |           | Tag 4.5.14 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.11.1`             | `resolve-plugins` |
| `org.apache.httpcomponents:httpcore@4.4.16`                                   | False        | `4.4.16`                                    | False    |       |           | Tag 4.4.16 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.11.1`             | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.26.1`                                  | False        | `1.26.1`                                    | False    |       |           | Tag 1.26.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `commons-codec:commons-codec@1.16.1`                                          | False        | `1.16.1`                                    | False    |       |           | Tag 1.16.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `com.google.guava:guava@31.0.1-jre`                                           | False        | `31.0.1-jre`                                | False    |       |           | Tag 31.0.1-jre not found in the repo                                |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.6.0`           | `resolve-plugins` |
| `com.google.guava:listenablefuture@9999.0-empty-to-avoid-conflict-with-guava` | False        | `9999.0-empty-to-avoid-conflict-with-guava` | False    |       |           | Tag 9999.0-empty-to-avoid-conflict-with-guava not found in the repo |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `tree`            |
| `org.javassist:javassist@3.28.0-GA`                                           | False        | `3.28.0-GA`                                 | False    |       |           | Tag 3.28.0-GA not found in the repo                                 |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.6.0`           | `resolve-plugins` |
| `javax.activation:javax.activation-api@1.2.0`                                 | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-checkstyle-plugin@3.6.0`           | `resolve-plugins` |
| `commons-io:commons-io@2.11.0`                                                | False        | `2.11.0`                                    | False    |       |           | Tag 2.11.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`            | `resolve-plugins` |
| `commons-codec:commons-codec@1.17.0`                                          | False        | `1.17.0`                                    | False    |       |           | Tag 1.17.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.8.0` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-model@2.0.0-M19`                           | False        | `2.0.0-M19`                                 | False    |       |           | Tag 2.0.0-M19 not found in the repo                                 |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.plexus@0.9.0.M2`                           | False        | `0.9.0.M2`                                  | False    |       |           | Tag 0.9.0.M2 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.inject@0.9.0.M2`                           | False        | `0.9.0.M2`                                  | False    |       |           | Tag 0.9.0.M2 not found in the repo                                  |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@2.0.0-M19`                        | False        | `2.0.0-M19`                                 | False    |       |           | Tag 2.0.0-M19 not found in the repo                                 |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@2.0.0-M19`                           | False        | `2.0.0-M19`                                 | False    |       |           | Tag 2.0.0-M19 not found in the repo                                 |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-integration-tools@2.0.0-M19`                    | False        | `2.0.0-M19`                                 | False    |       |           | Tag 2.0.0-M19 not found in the repo                                 |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.14.0`                                     | False        | `3.14.0`                                    | False    |       |           | Tag 3.14.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.eclipse.jetty:jetty-server@9.4.54.v20240208`                             | False        | `9.4.54.v20240208`                          | False    |       |           | Tag 9.4.54.v20240208 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.jetty:jetty-io@9.4.54.v20240208`                                 | False        | `9.4.54.v20240208`                          | False    |       |           | Tag 9.4.54.v20240208 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.jetty:jetty-http@9.4.54.v20240208`                               | False        | `9.4.54.v20240208`                          | False    |       |           | Tag 9.4.54.v20240208 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.jetty:jetty-servlet@9.4.54.v20240208`                            | False        | `9.4.54.v20240208`                          | False    |       |           | Tag 9.4.54.v20240208 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.jetty:jetty-security@9.4.54.v20240208`                           | False        | `9.4.54.v20240208`                          | False    |       |           | Tag 9.4.54.v20240208 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.jetty:jetty-util-ajax@9.4.54.v20240208`                          | False        | `9.4.54.v20240208`                          | False    |       |           | Tag 9.4.54.v20240208 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.jetty:jetty-webapp@9.4.54.v20240208`                             | False        | `9.4.54.v20240208`                          | False    |       |           | Tag 9.4.54.v20240208 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.jetty:jetty-xml@9.4.54.v20240208`                                | False        | `9.4.54.v20240208`                          | False    |       |           | Tag 9.4.54.v20240208 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.eclipse.jetty:jetty-util@9.4.54.v20240208`                               | False        | `9.4.54.v20240208`                          | False    |       |           | Tag 9.4.54.v20240208 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
| `org.dom4j:dom4j@2.1.4`                                                       | False        | `2.1.4`                                     | False    |       |           | Tag 2.1.4 not found in the repo                                     |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.commons:commons-text@1.10.0`                                      | False        | `1.10.0`                                    | False    |       |           | Tag 1.10.0 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.httpcomponents.client5:httpclient5@5.1.3`                         | False        | `5.1.3`                                     | False    |       |           | Tag 5.1.3 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.httpcomponents.core5:httpcore5-h2@5.1.3`                          | False        | `5.1.3`                                     | False    |       |           | Tag 5.1.3 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.httpcomponents.core5:httpcore5@5.1.3`                             | False        | `5.1.3`                                     | False    |       |           | Tag 5.1.3 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.logging.log4j:log4j-to-slf4j@2.24.1`                              | False        | `2.24.1`                                    | False    |       |           | Tag 2.24.1 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.logging.log4j:log4j-api@2.24.1`                                   | False        | `2.24.1`                                    | False    |       |           | Tag 2.24.1 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.bcel:bcel@6.10.0`                                                 | False        | `6.10.0`                                    | False    |       |           | Tag 6.10.0 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `com.google.code.gson:gson@2.11.0`                                            | False        | `2.11.0`                                    | False    |       |           | Tag 2.11.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.apache.groovy:groovy@4.0.24`                                             | False        | `4.0.24`                                    | False    |       |           | Tag 4.0.24 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.groovy:groovy-ant@4.0.24`                                         | False        | `4.0.24`                                    | False    |       |           | Tag 4.0.24 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.groovy:groovy-groovydoc@4.0.24`                                   | False        | `4.0.24`                                    | False    |       |           | Tag 4.0.24 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.groovy:groovy-dateutil@4.0.24`                                    | False        | `4.0.24`                                    | False    |       |           | Tag 4.0.24 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.groovy:groovy-docgenerator@4.0.24`                                | False        | `4.0.24`                                    | False    |       |           | Tag 4.0.24 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.groovy:groovy-json@4.0.24`                                        | False        | `4.0.24`                                    | False    |       |           | Tag 4.0.24 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.groovy:groovy-templates@4.0.24`                                   | False        | `4.0.24`                                    | False    |       |           | Tag 4.0.24 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.groovy:groovy-xml@4.0.24`                                         | False        | `4.0.24`                                    | False    |       |           | Tag 4.0.24 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `com.github.javaparser:javaparser-core@3.26.2`                                | False        | `3.26.2`                                    | False    |       |           | Tag 3.26.2 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `com.google.guava:guava@33.3.1-jre`                                           | False        | `33.3.1-jre`                                | False    |       |           | Tag 33.3.1-jre not found in the repo                                |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `org.apache.httpcomponents:httpclient@4.5.13`                                 | False        | `4.5.13`                                    | False    |       |           | Tag 4.5.13 not found in the repo                                    |                   404 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
| `org.apache.httpcomponents:httpcore@4.4.14`                                   | False        | `4.4.14`                                    | False    |       |           | Tag 4.4.14 not found in the repo                                    |                   404 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-decoration-model@1.11.1`                        | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@1.11.1`                           | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@1.11.1`                              | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-integration-tools@1.11.1`                       | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
| `commons-io:commons-io@2.16.1`                                                | False        | `2.16.1`                                    | False    |       |           | Tag 2.16.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.8.0` | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.23.0`                                  | False        | `1.23.0`                                    | False    |       |           | Tag 1.23.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-remote-resources-plugin@3.2.0`     | `resolve-plugins` |
| `commons-io:commons-io@2.15.1`                                                | False        | `2.15.1`                                    | False    |       |           | Tag 2.15.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-remote-resources-plugin@3.2.0`     | `resolve-plugins` |
| `commons-io:commons-io@2.8.0`                                                 | False        | `2.8.0`                                     | False    |       |           | Tag 2.8.0 not found in the repo                                     |                   404 | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
| `com.thoughtworks.xstream:xstream@1.4.19`                                     | False        | `1.4.19`                                    | False    |       |           | Tag 1.4.19 not found in the repo                                    |                   404 | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
| `io.github.x-stream:mxparser@1.2.2`                                           | False        | `1.2.2`                                     | False    |       |           | Tag 1.2.2 not found in the repo                                     |                   404 | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
| `commons-codec:commons-codec@1.15`                                            | False        | `1.15`                                      | False    |       |           | Tag 1.15 not found in the repo                                      |                   404 | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
| `org.apache.httpcomponents:httpcore@4.4.15`                                   | False        | `4.4.15`                                    | False    |       |           | Tag 4.4.15 not found in the repo                                    |                   404 | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.8.1`                                      | False        | `3.8.1`                                     | False    |       |           | Tag 3.8.1 not found in the repo                                     |                   404 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.12.0`                                     | False        | `3.12.0`                                    | False    |       |           | Tag 3.12.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`            | `resolve-plugins` |
| `org.apache.bcel:bcel@6.9.0`                                                  | False        | `6.9.0`                                     | False    |       |           | Tag 6.9.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.8.0` | `resolve-plugins` |
| `org.apache.commons:commons-text@1.11.0`                                      | False        | `1.11.0`                                    | False    |       |           | Tag 1.11.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.8.0` | `resolve-plugins` |
| `commons-validator:commons-validator@1.9.0`                                   | False        | `1.9.0`                                     | False    |       |           | Tag 1.9.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.8.0` | `resolve-plugins` |
| `commons-logging:commons-logging@1.3.2`                                       | False        | `1.3.2`                                     | False    |       |           | Tag 1.3.2 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.8.0` | `resolve-plugins` |
| `net.sourceforge.pmd:pmd-core@7.7.0`                                          | False        | `7.7.0`                                     | False    |       |           | Tag 7.7.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `com.github.oowekyala.ooxml:nice-xml-messages@3.1`                            | False        | `3.1`                                       | False    |       |           | Tag 3.1 not found in the repo                                       |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `net.sourceforge.pmd:pmd-java@7.7.0`                                          | False        | `7.7.0`                                     | False    |       |           | Tag 7.7.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `net.sourceforge.pmd:pmd-javascript@7.7.0`                                    | False        | `7.7.0`                                     | False    |       |           | Tag 7.7.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.mozilla:rhino@1.7.15`                                                    | False        | `1.7.15`                                    | False    |       |           | Tag 1.7.15 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `net.sourceforge.pmd:pmd-jsp@7.7.0`                                           | False        | `7.7.0`                                     | False    |       |           | Tag 7.7.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
| `org.junit.platform:junit-platform-commons@1.11.3`                            | False        | `1.11.3`                                    | False    |       |           | Tag 1.11.3 not found in the repo                                    |                   404 | `org.junit.jupiter:junit-jupiter-api@5.11.3`                       | `tree`            |
| `org.junit.platform:junit-platform-engine@1.11.3`                             | False        | `1.11.3`                                    | False    |       |           | Tag 1.11.3 not found in the repo                                    |                   404 | `org.junit.jupiter:junit-jupiter-engine@5.11.3`                    | `tree`            |
</details>

<details>
<summary>Source code links that could not be found(10)</summary>
    


|   index | package_name                                                 | github_url                                  | github_exists   | parent                                                  | command           |
|--------:|:-------------------------------------------------------------|:--------------------------------------------|:----------------|:--------------------------------------------------------|:------------------|
|       1 | `org.sonatype.plexus:plexus-sec-dispatcher@1.3`              | No_repo_info_found                          |                 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`      | `resolve-plugins` |
|       2 | `org.sonatype.plexus:plexus-cipher@1.4`                      | No_repo_info_found                          |                 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`      | `resolve-plugins` |
|       3 | `oro:oro@2.0.8`                                              | No_repo_info_found                          |                 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
|       4 | `org.sonatype.plexus:plexus-sec-dispatcher@1.4`              | No_repo_info_found                          |                 | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0` | `resolve-plugins` |
|       5 | `commons-beanutils:commons-beanutils@1.7.0`                  | No_repo_info_found                          |                 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
|       6 | `dom4j:dom4j@1.1`                                            | No_repo_info_found                          |                 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
|       7 | `jdepend:jdepend@2.9.1`                                      | No_repo_info_found                          |                 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
|       8 | `org.iq80.snappy:snappy@0.4`                                 | https://github.com/dain/snapy               | False           | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`      | `resolve-plugins` |
|       9 | `org.sonatype.nexus:nexus-client-core@2.15.1-02`             | https://github.com/sonatype/nexus2-internal | False           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0` | `resolve-plugins` |
|      10 | `org.sonatype.nexus.plugins:nexus-restlet1x-model@2.15.1-02` | https://github.com/sonatype/nexus2-internal | False           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0` | `resolve-plugins` |
</details>

The package manager (maven) does not support checking for provenance.

<details>
<summary>List of packages with an existing but invalid code signature(4)</summary>
    


| package_name                               | signature_valid   | parent                                             | command           |
|:-------------------------------------------|:------------------|:---------------------------------------------------|:------------------|
| `net.sourceforge.pmd:pmd-core@7.7.0`       | False             | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0` | `resolve-plugins` |
| `net.sourceforge.pmd:pmd-java@7.7.0`       | False             | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0` | `resolve-plugins` |
| `net.sourceforge.pmd:pmd-javascript@7.7.0` | False             | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0` | `resolve-plugins` |
| `net.sourceforge.pmd:pmd-jsp@7.7.0`        | False             | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0` | `resolve-plugins` |
</details>

<details>
<summary>List of packages without code signature(18)</summary>
    


| package_name                                           | signature_present   | parent                                                  | command           |
|:-------------------------------------------------------|:--------------------|:--------------------------------------------------------|:------------------|
| `javax.annotation:jsr250-api@1.0`                      | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `javax.inject:javax.inject@1`                          | False               | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`      | `resolve-plugins` |
| `org.codehaus.plexus:plexus-i18n@1.0-beta-10`          | False               | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`      | `resolve-plugins` |
| `com.kohlschutter.junixsocket:junixsocket-core@2.10.1` | False               | `org.apache.maven.plugins:maven-gpg-plugin@3.2.7`       | `resolve-plugins` |
| `aopalliance:aopalliance@1.0`                          | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `asm:asm@3.3.1`                                        | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `oro:oro@2.0.8`                                        | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `com.google.code.findbugs:jsr305@2.0.1`                | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0` | `resolve-plugins` |
| `xmlpull:xmlpull@1.1.3.1`                              | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0` | `resolve-plugins` |
| `javax.ws.rs:jsr311-api@1.1.1`                         | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0` | `resolve-plugins` |
| `javax.validation:validation-api@1.1.0.Final`          | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0` | `resolve-plugins` |
| `com.google.code.findbugs:jsr305@1.3.9`                | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `com.google.collections:google-collections@1.0`        | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `commons-beanutils:commons-beanutils@1.7.0`            | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `commons-digester:commons-digester@1.8`                | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `commons-chain:commons-chain@1.1`                      | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `dom4j:dom4j@1.1`                                      | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
| `jdepend:jdepend@2.9.1`                                | False               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`            | `resolve-plugins` |
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
    
- Source code repo is not hosted on GitHub:  90

    This could be due, for example, to the package being hosted on a different platform.

    This does not mean that the source code URL is invalid.

    However, for non-GitHub repositories, not all checks can currently be performed.

|   index | package_name                                                 | github_url                                                                                                            | parent                                                             | command           |
|--------:|:-------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|:------------------|
|       1 | `commons-beanutils:commons-beanutils@1.9.4`                  | http://svn.apache.org/viewvc/commons/proper/beanutils/tags/BEANUTILS_1_9_3_RC3                                        | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|       2 | `commons-logging:commons-logging@1.2`                        | http://svn.apache.org/repos/asf/commons/proper/logging/trunk                                                          | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|       3 | `commons-collections:commons-collections@3.2.2`              | http://svn.apache.org/viewvc/commons/proper/collections/trunk                                                         | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|       4 | `org.apache.commons:commons-digester3@3.2`                   | http://svn.apache.org/viewvc/commons/proper/digester/tags/DIGESTER3_3_2_RC2                                           | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|       5 | `org.tukaani:xz@1.9`                                         | https://git.tukaani.org/?p=xz-java.git                                                                                | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|       6 | `org.eclipse.sisu:org.eclipse.sisu.plexus@0.3.4`             | http://git.eclipse.org/c/sisu/org.eclipse.sisu.plexus.git/tree/org.eclipse.sisu.plexus/                               | `org.codehaus.mojo:versions-maven-plugin@2.18.0`                   | `resolve-plugins` |
|       7 | `javax.enterprise:cdi-api@1.0`                               | http://fisheye.jboss.org/browse/Weld/api/tags/1.0/build/tags/weld-parent-6/weld-api-bom/weld-api-parent/cdi-api       | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|       8 | `javax.annotation:jsr250-api@1.0`                            | http://jcp.org/aboutJava/communityprocess/final/jsr250/index.html                                                     | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|       9 | `org.eclipse.sisu:org.eclipse.sisu.inject@0.3.4`             | http://git.eclipse.org/c/sisu/org.eclipse.sisu.inject.git/tree/org.eclipse.sisu.inject/                               | `org.codehaus.mojo:versions-maven-plugin@2.18.0`                   | `resolve-plugins` |
|      10 | `org.codehaus.plexus:plexus-component-annotations@1.5.5`     | http://fisheye.codehaus.org/browse/plexus/plexus-containers/tags/plexus-containers-1.5.5/plexus-component-annotations | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      11 | `javax.inject:javax.inject@1`                                | http://code.google.com/p/atinject/source/checkout                                                                     | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      12 | `org.codehaus.plexus:plexus-i18n@1.0-beta-10`                | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10                              | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      13 | `commons-codec:commons-codec@1.11`                           | http://svn.apache.org/viewvc/commons/proper/codec/trunk                                                               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      14 | `org.ow2.asm:asm@9.7`                                        | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      15 | `com.google.code.findbugs:jsr305@3.0.2`                      | https://code.google.com/p/jsr-305/                                                                                    | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `tree`            |
|      16 | `com.google.j2objc:j2objc-annotations@1.3`                   | http://svn.sonatype.org/spice/tags/oss-parent-7/j2objc-annotations                                                    | `org.apache.maven.plugins:maven-checkstyle-plugin@3.6.0`           | `tree`            |
|      17 | `net.sf.saxon:Saxon-HE@10.6`                                 | https://dev.saxonica.com/repos/archive/opensource/                                                                    | `org.apache.maven.plugins:maven-checkstyle-plugin@3.6.0`           | `resolve-plugins` |
|      18 | `javax.annotation:javax.annotation-api@1.2`                  | http://java.net/projects/glassfish/sources/svn/show/tags/javax.annotation-api-1.2                                     | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
|      19 | `javax.servlet:javax.servlet-api@3.1.0`                      | http://java.net/projects/glassfish/sources/svn/show/tags/javax.servlet-api-3.1.0                                      | `org.apache.maven.plugins:maven-site-plugin@4.0.0-M16`             | `resolve-plugins` |
|      20 | `org.apache.maven.reporting:maven-reporting-api@3.0`         | http://svn.apache.org/viewvc/maven/shared/tags/maven-reporting-api-3.0                                                | `org.jacoco:jacoco-maven-plugin@0.8.12`                            | `resolve-plugins` |
|      21 | `org.apache.maven.doxia:doxia-sink-api@1.0`                  | https://svn.apache.org/viewvc/maven/doxia/doxia/tags/doxia-1.0/doxia-sink-api                                         | `org.jacoco:jacoco-maven-plugin@0.8.12`                            | `resolve-plugins` |
|      22 | `org.ow2.asm:asm-commons@9.7`                                | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.jacoco:jacoco-maven-plugin@0.8.12`                            | `resolve-plugins` |
|      23 | `org.ow2.asm:asm-tree@9.7`                                   | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.jacoco:jacoco-maven-plugin@0.8.12`                            | `resolve-plugins` |
|      24 | `net.sf.saxon:Saxon-HE@12.4`                                 | https://saxonica.plan.io/projects/saxonmirrorhe/repository                                                            | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      25 | `org.ow2.asm:asm@9.7.1`                                      | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.easymock:easymock@5.5.0`                                      | `resolve-plugins` |
|      26 | `org.ow2.asm:asm-analysis@9.7.1`                             | https://gitlab.ow2.org/asm/asm/                                                                                       | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      27 | `org.ow2.asm:asm-commons@9.7.1`                              | https://gitlab.ow2.org/asm/asm/                                                                                       | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      28 | `org.ow2.asm:asm-tree@9.7.1`                                 | https://gitlab.ow2.org/asm/asm/                                                                                       | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      29 | `org.ow2.asm:asm-util@9.7.1`                                 | https://gitlab.ow2.org/asm/asm/                                                                                       | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      30 | `org.apache.ant:ant@1.10.15`                                 | https://gitbox.apache.org/repos/asf/ant.git/ant                                                                       | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      31 | `org.apache.ant:ant-launcher@1.10.15`                        | https://gitbox.apache.org/repos/asf/ant.git/ant-launcher                                                              | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      32 | `com.thoughtworks.qdox:qdox@1.12.1`                          | http://svn.qdox.codehaus.org/browse/qdox/tags/qdox-1.12.1                                                             | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      33 | `org.eclipse.aether:aether-spi@0.9.0.M2`                     | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-spi/                                                      | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      34 | `org.eclipse.aether:aether-impl@0.9.0.M2`                    | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-impl/                                                     | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      35 | `org.eclipse.aether:aether-api@0.9.0.M2`                     | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-api/                                                      | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      36 | `org.eclipse.aether:aether-util@0.9.0.M2`                    | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-util/                                                     | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      37 | `org.eclipse.sisu:org.eclipse.sisu.plexus@0.0.0.M2a`         | http://git.eclipse.org/c/sisu/org.eclipse.sisu.plexus.git/tree/org.eclipse.sisu.plexus/                               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      38 | `aopalliance:aopalliance@1.0`                                | http://aopalliance.sourceforge.net                                                                                    | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      39 | `org.eclipse.sisu:org.eclipse.sisu.inject@0.0.0.M2a`         | http://git.eclipse.org/c/sisu/org.eclipse.sisu.inject.git/tree/org.eclipse.sisu.inject/                               | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      40 | `asm:asm@3.3.1`                                              | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm/                                                     | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      41 | `org.apache.velocity:velocity@1.7`                           | http://svn.apache.org/viewvc/velocity/engine/trunk                                                                    | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      42 | `org.apache.velocity:velocity-tools@2.0`                     | http://svn.apache.org/repos/asf/velocity/tools/trunk                                                                  | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      43 | `org.apache.maven:maven-model@2.2.1`                         | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-model                                               | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      44 | `commons-chain:commons-chain@1.2`                            | http://svn.apache.org/viewvc/commons/proper/chain/trunk/                                                              | `com.github.spotbugs:spotbugs-maven-plugin@4.8.6.6`                | `resolve-plugins` |
|      45 | `commons-digester:commons-digester@2.1`                      | http://svn.apache.org/viewvc/commons/proper/digester/tags/DIGESTER_2_1_RC2                                            | `org.apache.maven.plugins:maven-project-info-reports-plugin@3.8.0` | `resolve-plugins` |
|      46 | `commons-lang:commons-lang@2.6`                              | http://svn.apache.org/viewvc/commons/proper/lang/branches/LANG_2_X                                                    | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      47 | `org.sonatype.plexus:plexus-build-api@0.0.7`                 | http://svn.sonatype.org/spice/tags/plexus-build-api-0.0.7                                                             | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`            | `resolve-plugins` |
|      48 | `com.google.guava:guava@14.0.1`                              | http://code.google.com/p/guava-libraries/source/browse/guava                                                          | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      49 | `org.apache.maven:maven-plugin-api@3.0.4`                    | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-plugin-api                                          | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      50 | `org.apache.maven:maven-artifact@3.0.4`                      | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-artifact                                            | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      51 | `org.apache.maven:maven-model@3.0.4`                         | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-model                                               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      52 | `org.apache.maven:maven-compat@3.0.4`                        | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-compat                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      53 | `org.apache.maven:maven-model-builder@3.0.4`                 | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-model-builder                                       | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      54 | `org.apache.maven:maven-settings@3.0.4`                      | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-settings                                            | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      55 | `org.apache.maven:maven-core@3.0.4`                          | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-core                                                | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      56 | `org.apache.maven:maven-settings-builder@3.0.4`              | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-settings-builder                                    | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      57 | `org.apache.maven:maven-repository-metadata@3.0.4`           | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-repository-metadata                                 | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      58 | `org.apache.maven:maven-aether-provider@3.0.4`               | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-aether-provider                                     | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      59 | `org.apache.maven.wagon:wagon-provider-api@2.2`              | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-2.2/wagon-provider-api                                            | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      60 | `org.apache.maven.plugin-tools:maven-plugin-annotations@3.2` | http://svn.apache.org/viewvc/maven/plugin-tools/tags/maven-plugin-tools-3.2/maven-plugin-annotations                  | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      61 | `com.google.code.findbugs:jsr305@2.0.1`                      | http://findbugs.googlecode.com/svn/trunk/                                                                             | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      62 | `com.intellij:annotations@9.0.4`                             | http://git.jetbrains.org/idea/community.git                                                                           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      63 | `xmlpull:xmlpull@1.1.3.1`                                    | http://www.xmlpull.org                                                                                                | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      64 | `javax.ws.rs:jsr311-api@1.1.1`                               | https://jsr311.dev.java.net                                                                                           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      65 | `com.sun.jersey:jersey-core@1.17.1`                          | http://java.net/projects/jersey/sources/svn/show/trunk/jersey/jersey-core                                             | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      66 | `com.sun.jersey:jersey-client@1.17.1`                        | http://java.net/projects/jersey/sources/svn/show/trunk/jersey/jersey-client                                           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      67 | `com.sun.jersey.contribs:jersey-apache-client4@1.17.1`       | http://java.net/projects/jersey/sources/svn/show/trunk/jersey/jersey-contribs/jersey-apache-client4                   | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      68 | `org.fusesource.hawtbuf:hawtbuf-proto@1.9`                   | http://fusesource.com/forge/gitweb?p=hawtbuf.git/hawtbuf-proto                                                        | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      69 | `org.fusesource.hawtbuf:hawtbuf@1.9`                         | http://fusesource.com/forge/gitweb?p=hawtbuf.git/hawtbuf                                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.7.0`            | `resolve-plugins` |
|      70 | `com.google.guava:guava@10.0.1`                              | http://code.google.com/p/guava-libraries/source/browse/guava                                                          | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      71 | `com.google.code.findbugs:jsr305@1.3.9`                      | http://findbugs.googlecode.com/svn/trunk/                                                                             | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      72 | `org.apache.xbean:xbean-reflect@3.7`                         | http://svn.apache.org/viewvc/geronimo/xbean/tags/xbean-3.7/xbean-reflect                                              | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      73 | `com.google.collections:google-collections@1.0`              | http://code.google.com/p/google-collections/source/browse/                                                            | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      74 | `commons-lang:commons-lang@2.4`                              | http://svn.apache.org/viewvc/commons/proper/lang/trunk                                                                | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      75 | `commons-digester:commons-digester@1.8`                      | http://svn.apache.org/repos/asf/jakarta/commons/proper/digester/trunk                                                 | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      76 | `commons-chain:commons-chain@1.1`                            | http://svn.apache.org/viewcvs.cgi                                                                                     | `org.codehaus.mojo:jdepend-maven-plugin@2.1`                       | `resolve-plugins` |
|      77 | `org.apache.maven.shared:maven-shared-incremental@1.1`       | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-incremental-1.1                                           | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
|      78 | `org.ow2.asm:asm@9.6`                                        | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.apache.maven.plugins:maven-compiler-plugin@3.13.0`            | `resolve-plugins` |
|      79 | `org.apache.maven:maven-core@3.0`                            | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-core                                                  | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      80 | `org.apache.maven:maven-model@3.0`                           | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-model                                                 | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      81 | `org.apache.maven:maven-settings@3.0`                        | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-settings                                              | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      82 | `org.apache.maven:maven-settings-builder@3.0`                | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-settings-builder                                      | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      83 | `org.apache.maven:maven-repository-metadata@3.0`             | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-repository-metadata                                   | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      84 | `org.apache.maven:maven-plugin-api@3.0`                      | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-plugin-api                                            | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      85 | `org.apache.maven:maven-model-builder@3.0`                   | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-model-builder                                         | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      86 | `org.apache.maven:maven-aether-provider@3.0`                 | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-aether-provider                                       | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      87 | `org.apache.maven:maven-artifact@3.0`                        | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-artifact                                              | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      88 | `org.codehaus.plexus:plexus-interpolation@1.14`              | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-interpolation-1.14                            | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      89 | `org.codehaus.plexus:plexus-classworlds@2.2.3`               | http://fisheye.codehaus.org/browse/plexus/plexus-classworlds/tags/plexus-classworlds-2.2.3                            | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
|      90 | `net.sf.saxon:Saxon-HE@12.5`                                 | https://saxonica.plan.io/projects/saxonmirrorhe/repository                                                            | `org.apache.maven.plugins:maven-pmd-plugin@3.26.0`                 | `resolve-plugins` |
</details>


---

Report created by [dirty-waters](https://github.com/chains-project/dirty-waters/).

Report created on 2025-05-13 12:03:45
- Tool version: 1dfb5543
- Project Name: easymock/easymock
- Project Version: easymock-5.5.0
- Package Manager: maven
