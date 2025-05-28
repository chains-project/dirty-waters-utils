
# Software Supply Chain Report of chains-project/maven-lockfile - cbed57cb317568cfdb497c5f26e36a34eb31958a

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
        

 ### Total packages in the supply chain: 466


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 75

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 0

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 0

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 1


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(75)</summary>
    


| package_name                                                                  | sha_exists   | tag_version                                 | is_sha   | sha   | tag_url   | message                                                             |   status_code_for_sha | parent                                                            | command           |
|:------------------------------------------------------------------------------|:-------------|:--------------------------------------------|:---------|:------|:----------|:--------------------------------------------------------------------|----------------------:|:------------------------------------------------------------------|:------------------|
| `commons-codec:commons-codec@1.17.1`                                          | False        | `1.17.1`                                    | False    |       |           | Tag 1.17.1 not found in the repo                                    |                   404 | `org.cyclonedx:cyclonedx-maven-plugin@2.9.1`                      | `resolve-plugins` |
| `commons-io:commons-io@2.18.0`                                                | False        | `2.18.0`                                    | False    |       |           | Tag 2.18.0 not found in the repo                                    |                   404 | `org.codehaus.gmavenplus:gmavenplus-plugin@4.2.0`                 | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.plexus@0.9.0.M3`                           | False        | `0.9.0.M3`                                  | False    |       |           | Tag 0.9.0.M3 not found in the repo                                  |                   404 | `io.quarkus:quarkus-bootstrap-maven-resolver@3.22.1`              | `tree`            |
| `org.eclipse.sisu:org.eclipse.sisu.inject@0.9.0.M3`                           | False        | `0.9.0.M3`                                  | False    |       |           | Tag 0.9.0.M3 not found in the repo                                  |                   404 | `io.quarkus:quarkus-junit5@3.22.1`                                | `tree`            |
| `org.apache.maven.doxia:doxia-decoration-model@1.11.1`                        | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.8.1`                                      | False        | `3.8.1`                                     | False    |       |           | Tag 3.8.1 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
| `org.apache.httpcomponents:httpclient@4.5.13`                                 | False        | `4.5.13`                                    | False    |       |           | Tag 4.5.13 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
| `org.apache.httpcomponents:httpcore@4.4.14`                                   | False        | `4.4.14`                                    | False    |       |           | Tag 4.4.14 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@1.11.1`                           | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@1.11.1`                              | False        | `1.11.1`                                    | False    |       |           | Tag 1.11.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
| `commons-io:commons-io@2.16.1`                                                | False        | `2.16.1`                                    | False    |       |           | Tag 2.16.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-enforcer-plugin@3.5.0`            | `resolve-plugins` |
| `org.apache.commons:commons-collections4@4.4`                                 | False        | `4.4`                                       | False    |       |           | Tag 4.4 not found in the repo                                       |                   404 | `io.quarkus.platform:quarkus-maven-plugin@3.22.1`                 | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.17.0`                                     | False        | `3.17.0`                                    | False    |       |           | Tag 3.17.0 not found in the repo                                    |                   404 | `org.kohsuke:github-api@1.326`                                    | `tree`            |
| `commons-codec:commons-codec@1.18.0`                                          | False        | `1.18.0`                                    | False    |       |           | Tag 1.18.0 not found in the repo                                    |                   404 | `io.smallrye.beanbag:smallrye-beanbag-maven@1.5.2`                | `tree`            |
| `org.apache.httpcomponents:httpclient@4.5.14`                                 | False        | `4.5.14`                                    | False    |       |           | Tag 4.5.14 not found in the repo                                    |                   404 | `io.smallrye.beanbag:smallrye-beanbag-maven@1.5.2`                | `tree`            |
| `org.apache.httpcomponents:httpcore@4.4.16`                                   | False        | `4.4.16`                                    | False    |       |           | Tag 4.4.16 not found in the repo                                    |                   404 | `io.smallrye.beanbag:smallrye-beanbag-maven@1.5.2`                | `tree`            |
| `com.google.guava:guava@33.4.8-jre`                                           | False        | `33.4.8-jre`                                | False    |       |           | Tag 33.4.8-jre not found in the repo                                |                   404 | `org.apache.maven:maven-embedder@3.9.9`                           | `tree`            |
| `commons-cli:commons-cli@1.8.0`                                               | False        | `1.8.0`                                     | False    |       |           | Tag 1.8.0 not found in the repo                                     |                   404 | `org.apache.maven:maven-embedder@3.9.9`                           | `tree`            |
| `org.aesh:aesh@2.8.2`                                                         | False        | `2.8.2`                                     | False    |       |           | Tag 2.8.2 not found in the repo                                     |                   404 | `io.quarkus:quarkus-core-deployment@3.22.1`                       | `tree`            |
| `io.github.crac:org-crac@0.1.3`                                               | False        | `0.1.3`                                     | False    |       |           | Tag 0.1.3 not found in the repo                                     |                   404 | `io.quarkus:quarkus-bootstrap-runner@3.22.1`                      | `tree`            |
| `org.junit.platform:junit-platform-launcher@1.12.2`                           | False        | `1.12.2`                                    | False    |       |           | Tag 1.12.2 not found in the repo                                    |                   404 | `io.quarkus:quarkus-core-deployment@3.22.1`                       | `tree`            |
| `org.junit.platform:junit-platform-engine@1.12.2`                             | False        | `1.12.2`                                    | False    |       |           | Tag 1.12.2 not found in the repo                                    |                   404 | `org.junit.jupiter:junit-jupiter-engine@5.12.2`                   | `tree`            |
| `org.junit.platform:junit-platform-commons@1.12.2`                            | False        | `1.12.2`                                    | False    |       |           | Tag 1.12.2 not found in the repo                                    |                   404 | `org.junit.jupiter:junit-jupiter-api@5.12.2`                      | `tree`            |
| `commons-io:commons-io@2.19.0`                                                | False        | `2.19.0`                                    | False    |       |           | Tag 2.19.0 not found in the repo                                    |                   404 | `io.quarkus:quarkus-test-common@3.22.1`                           | `tree`            |
| `org.apache.commons:commons-compress@1.27.1`                                  | False        | `1.27.1`                                    | False    |       |           | Tag 1.27.1 not found in the repo                                    |                   404 | `io.quarkus.platform:quarkus-maven-plugin@3.22.1`                 | `resolve-plugins` |
| `org.jdom:jdom2@2.0.6.1`                                                      | False        | `2.0.6.1`                                   | False    |       |           | Tag 2.0.6.1 not found in the repo                                   |                   404 | `io.quarkus.platform:quarkus-maven-plugin@3.22.1`                 | `resolve-plugins` |
| `jakarta.el:jakarta.el-api@5.0.1`                                             | False        | `5.0.1`                                     | False    |       |           | Tag 5.0.1 not found in the repo                                     |                   404 | `jakarta.enterprise:jakarta.enterprise.cdi-api@4.1.0`             | `tree`            |
| `jakarta.interceptor:jakarta.interceptor-api@2.2.0`                           | False        | `2.2.0`                                     | False    |       |           | Tag 2.2.0 not found in the repo                                     |                   404 | `jakarta.enterprise:jakarta.enterprise.cdi-api@4.1.0`             | `tree`            |
| `jakarta.json:jakarta.json-api@2.1.3`                                         | False        | `2.1.3`                                     | False    |       |           | Tag 2.1.3 not found in the repo                                     |                   404 | `io.smallrye:smallrye-graphql-client-implementation-vertx@2.13.0` | `tree`            |
| `org.twdata.maven:mojo-executor@2.4.0`                                        | False        | `2.4.0`                                     | False    |       |           | Tag 2.4.0 not found in the repo                                     |                   404 | `io.quarkus.platform:quarkus-maven-plugin@3.22.1`                 | `resolve-plugins` |
| `org.jboss.slf4j:slf4j-jboss-logmanager@2.0.0.Final`                          | False        | `2.0.0.Final`                               | False    |       |           | Tag 2.0.0.Final not found in the repo                               |                   404 | `io.quarkus:quarkus-core@3.22.1`                                  | `tree`            |
| `org.apache.commons:commons-compress@1.26.2`                                  | False        | `1.26.2`                                    | False    |       |           | Tag 1.26.2 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `commons-codec:commons-codec@1.17.0`                                          | False        | `1.17.0`                                    | False    |       |           | Tag 1.17.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.14.0`                                     | False        | `3.14.0`                                    | False    |       |           | Tag 3.14.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-enforcer-plugin@3.5.0`            | `resolve-plugins` |
| `commons-io:commons-io@2.11.0`                                                | False        | `2.11.0`                                    | False    |       |           | Tag 2.11.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`           | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.26.1`                                  | False        | `1.26.1`                                    | False    |       |           | Tag 1.26.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-jar-plugin@3.4.2`                 | `resolve-plugins` |
| `commons-codec:commons-codec@1.16.1`                                          | False        | `1.16.1`                                    | False    |       |           | Tag 1.16.1 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-jar-plugin@3.4.2`                 | `resolve-plugins` |
| `com.google.protobuf:protobuf-java-util@4.29.3`                               | False        | `4.29.3`                                    | False    |       |           | Tag 4.29.3 not found in the repo                                    |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
| `com.google.protobuf:protobuf-java@4.29.3`                                    | False        | `4.29.3`                                    | False    |       |           | Tag 4.29.3 not found in the repo                                    |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
| `com.google.guava:guava@32.0.1-jre`                                           | False        | `32.0.1-jre`                                | False    |       |           | Tag 32.0.1-jre not found in the repo                                |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
| `com.google.guava:listenablefuture@9999.0-empty-to-avoid-conflict-with-guava` | False        | `9999.0-empty-to-avoid-conflict-with-guava` | False    |       |           | Tag 9999.0-empty-to-avoid-conflict-with-guava not found in the repo |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
| `commons-codec:commons-codec@1.17.2`                                          | False        | `1.17.2`                                    | False    |       |           | Tag 1.17.2 not found in the repo                                    |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `tree`            |
| `com.google.code.gson:gson@2.12.1`                                            | False        | `2.12.1`                                    | False    |       |           | Tag 2.12.1 not found in the repo                                    |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
| `org.bouncycastle:bcpkix-jdk18on@1.80`                                        | False        | `1.80`                                      | False    |       |           | Tag 1.80 not found in the repo                                      |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
| `org.bouncycastle:bcutil-jdk18on@1.80`                                        | False        | `1.80`                                      | False    |       |           | Tag 1.80 not found in the repo                                      |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
| `org.bouncycastle:bcprov-jdk18on@1.80`                                        | False        | `1.80`                                      | False    |       |           | Tag 1.80 not found in the repo                                      |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
| `org.bouncycastle:bcpg-jdk18on@1.78.1`                                        | False        | `1.78.1`                                    | False    |       |           | Tag 1.78.1 not found in the repo                                    |                   404 | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
| `org.apache.commons:commons-text@1.12.0`                                      | False        | `1.12.0`                                    | False    |       |           | Tag 1.12.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-model@2.0.0`                               | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@2.0.0`                            | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@2.0.0`                               | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-integration-tools@2.0.0`                        | False        | `2.0.0`                                     | False    |       |           | Tag 2.0.0 not found in the repo                                     |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.eclipse.jetty:jetty-server@9.4.56.v20240826`                             | False        | `9.4.56.v20240826`                          | False    |       |           | Tag 9.4.56.v20240826 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.eclipse.jetty:jetty-io@9.4.56.v20240826`                                 | False        | `9.4.56.v20240826`                          | False    |       |           | Tag 9.4.56.v20240826 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.eclipse.jetty:jetty-http@9.4.56.v20240826`                               | False        | `9.4.56.v20240826`                          | False    |       |           | Tag 9.4.56.v20240826 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.eclipse.jetty:jetty-servlet@9.4.56.v20240826`                            | False        | `9.4.56.v20240826`                          | False    |       |           | Tag 9.4.56.v20240826 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.eclipse.jetty:jetty-security@9.4.56.v20240826`                           | False        | `9.4.56.v20240826`                          | False    |       |           | Tag 9.4.56.v20240826 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.eclipse.jetty:jetty-util-ajax@9.4.56.v20240826`                          | False        | `9.4.56.v20240826`                          | False    |       |           | Tag 9.4.56.v20240826 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.eclipse.jetty:jetty-webapp@9.4.56.v20240826`                             | False        | `9.4.56.v20240826`                          | False    |       |           | Tag 9.4.56.v20240826 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.eclipse.jetty:jetty-xml@9.4.56.v20240826`                                | False        | `9.4.56.v20240826`                          | False    |       |           | Tag 9.4.56.v20240826 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `org.eclipse.jetty:jetty-util@9.4.56.v20240826`                               | False        | `9.4.56.v20240826`                          | False    |       |           | Tag 9.4.56.v20240826 not found in the repo                          |                   404 | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
| `com.diffplug.spotless:spotless-maven-plugin@2.44.4`                          | False        | `2.44.4`                                    | False    |       |           | Tag 2.44.4 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `com.diffplug.spotless:spotless-lib@3.1.1`                                    | False        | `3.1.1`                                     | False    |       |           | Tag 3.1.1 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `com.diffplug.spotless:spotless-lib-extra@3.1.1`                              | False        | `3.1.1`                                     | False    |       |           | Tag 3.1.1 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `dev.equo.ide:solstice@1.8.1`                                                 | False        | `1.8.1`                                     | False    |       |           | Tag 1.8.1 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `org.jetbrains:annotations@13.0`                                              | False        | `13.0`                                      | False    |       |           | Tag 13.0 not found in the repo                                      |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `org.eclipse.platform:org.eclipse.osgi@3.23.0`                                | False        | `3.23.0`                                    | False    |       |           | Tag 3.23.0 not found in the repo                                    |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `com.diffplug.durian:durian-core@1.2.0`                                       | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `com.diffplug.durian:durian-io@1.2.0`                                         | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `com.diffplug.durian:durian-collect@1.2.0`                                    | False        | `1.2.0`                                     | False    |       |           | Tag 1.2.0 not found in the repo                                     |                   404 | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.12.0`                                     | False        | `3.12.0`                                    | False    |       |           | Tag 3.12.0 not found in the repo                                    |                   404 | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`           | `resolve-plugins` |
| `io.vertx:vertx-web-client@4.5.14`                                            | False        | `4.5.14`                                    | False    |       |           | Tag 4.5.14 not found in the repo                                    |                   404 | `io.smallrye:smallrye-graphql-client-implementation-vertx@2.13.0` | `tree`            |
| `io.vertx:vertx-uri-template@4.5.14`                                          | False        | `4.5.14`                                    | False    |       |           | Tag 4.5.14 not found in the repo                                    |                   404 | `io.vertx:vertx-web-client@4.5.14`                                | `tree`            |
| `io.vertx:vertx-web-common@4.5.14`                                            | False        | `4.5.14`                                    | False    |       |           | Tag 4.5.14 not found in the repo                                    |                   404 | `io.vertx:vertx-web-client@4.5.14`                                | `tree`            |
| `io.vertx:vertx-auth-common@4.5.14`                                           | False        | `4.5.14`                                    | False    |       |           | Tag 4.5.14 not found in the repo                                    |                   404 | `io.vertx:vertx-web-client@4.5.14`                                | `tree`            |
</details>
All analyzed packages have a source code repo.

The package manager (maven) does not support checking for provenance.

All packages have valid code signature.

<details>
<summary>List of packages without code signature(1)</summary>
    


| package_name                                           | signature_present   | parent                                     | command           |
|:-------------------------------------------------------|:--------------------|:-------------------------------------------|:------------------|
| `com.kohlschutter.junixsocket:junixsocket-core@2.10.1` | False               | `dev.sigstore:sigstore-maven-plugin@1.3.0` | `resolve-plugins` |
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
    
- Source code repo is not hosted on GitHub:  45

    This could be due, for example, to the package being hosted on a different platform.

    This does not mean that the source code URL is invalid.

    However, for non-GitHub repositories, not all checks can currently be performed.

|   index | package_name                                              | github_url                                                                                                            | parent                                                            | command           |
|--------:|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------|:------------------|
|       1 | `javax.inject:javax.inject@1`                             | http://code.google.com/p/atinject/source/checkout                                                                     | `io.smallrye.beanbag:smallrye-beanbag-maven@1.5.2`                | `tree`            |
|       2 | `org.apache.xbean:xbean-reflect@3.7`                      | http://svn.apache.org/viewvc/geronimo/xbean/tags/xbean-3.7/xbean-reflect                                              | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|       3 | `com.google.collections:google-collections@1.0`           | http://code.google.com/p/google-collections/source/browse/                                                            | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|       4 | `org.eclipse.aether:aether-spi@0.9.0.M2`                  | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-spi/                                                      | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|       5 | `org.eclipse.aether:aether-impl@0.9.0.M2`                 | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-impl/                                                     | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|       6 | `org.eclipse.aether:aether-api@0.9.0.M2`                  | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-api/                                                      | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|       7 | `org.eclipse.aether:aether-util@0.9.0.M2`                 | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-util/                                                     | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|       8 | `org.codehaus.plexus:plexus-component-annotations@1.5.5`  | http://fisheye.codehaus.org/browse/plexus/plexus-containers/tags/plexus-containers-1.5.5/plexus-component-annotations | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|       9 | `org.sonatype.plexus:plexus-sec-dispatcher@1.3`           | Could not find repo from package registry                                                                             | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      10 | `org.sonatype.plexus:plexus-cipher@1.4`                   | Could not find repo from package registry                                                                             | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      11 | `commons-logging:commons-logging@1.2`                     | http://svn.apache.org/repos/asf/commons/proper/logging/trunk                                                          | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
|      12 | `org.codehaus.plexus:plexus-i18n@1.0-beta-10`             | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10                              | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
|      13 | `org.apache.velocity:velocity@1.7`                        | http://svn.apache.org/viewvc/velocity/engine/trunk                                                                    | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      14 | `commons-lang:commons-lang@2.4`                           | http://svn.apache.org/viewvc/commons/proper/lang/trunk                                                                | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      15 | `org.apache.velocity:velocity-tools@2.0`                  | http://svn.apache.org/repos/asf/velocity/tools/trunk                                                                  | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      16 | `commons-beanutils:commons-beanutils@1.7.0`               | Could not find repo from package registry                                                                             | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      17 | `commons-digester:commons-digester@1.8`                   | http://svn.apache.org/repos/asf/jakarta/commons/proper/digester/trunk                                                 | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      18 | `commons-chain:commons-chain@1.1`                         | http://svn.apache.org/viewcvs.cgi                                                                                     | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      19 | `dom4j:dom4j@1.1`                                         | Could not find repo from package registry                                                                             | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      20 | `oro:oro@2.0.8`                                           | Could not find repo from package registry                                                                             | `org.apache.maven.plugins:maven-artifact-plugin@3.6.0`            | `resolve-plugins` |
|      21 | `commons-collections:commons-collections@3.2.2`           | http://svn.apache.org/viewvc/commons/proper/collections/trunk                                                         | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
|      22 | `org.yaml:snakeyaml@2.2`                                  | https://bitbucket.org/snakeyaml/snakeyaml/src                                                                         | `org.cyclonedx:cyclonedx-maven-plugin@2.9.1`                      | `resolve-plugins` |
|      23 | `org.ow2.asm:asm@9.7`                                     | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.cyclonedx:cyclonedx-maven-plugin@2.9.1`                      | `resolve-plugins` |
|      24 | `aopalliance:aopalliance@1.0`                             | http://aopalliance.sourceforge.net                                                                                    | `com.google.inject:guice@5.1.0`                                   | `tree`            |
|      25 | `org.ow2.asm:asm-util@9.8`                                | https://gitlab.ow2.org/asm/asm/                                                                                       | `io.quarkus.gizmo:gizmo@1.9.0`                                    | `tree`            |
|      26 | `org.ow2.asm:asm-analysis@9.8`                            | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.ow2.asm:asm-util@9.8`                                        | `tree`            |
|      27 | `org.ow2.asm:asm@9.8`                                     | https://gitlab.ow2.org/asm/asm/                                                                                       | `io.quarkus:quarkus-core-deployment@3.22.1`                       | `tree`            |
|      28 | `org.ow2.asm:asm-commons@9.8`                             | https://gitlab.ow2.org/asm/asm/                                                                                       | `io.quarkus:quarkus-core-deployment@3.22.1`                       | `tree`            |
|      29 | `org.ow2.asm:asm-tree@9.8`                                | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.ow2.asm:asm-commons@9.8`                                     | `tree`            |
|      30 | `org.yaml:snakeyaml@2.4`                                  | https://bitbucket.org/snakeyaml/snakeyaml/src                                                                         | `com.fasterxml.jackson.dataformat:jackson-dataformat-yaml@2.18.3` | `tree`            |
|      31 | `org.ow2.asm:asm@9.7.1`                                   | https://gitlab.ow2.org/asm/asm/                                                                                       | `org.apache.maven.plugins:maven-surefire-plugin@3.5.3`            | `tree`            |
|      32 | `org.tukaani:xz@1.9`                                      | https://git.tukaani.org/?p=xz-java.git                                                                                | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
|      33 | `org.apache.ant:ant@1.10.15`                              | https://gitbox.apache.org/repos/asf/ant.git/ant                                                                       | `org.codehaus.gmavenplus:gmavenplus-plugin@4.2.0`                 | `resolve-plugins` |
|      34 | `org.apache.ant:ant-launcher@1.10.15`                     | https://gitbox.apache.org/repos/asf/ant.git/ant-launcher                                                              | `org.codehaus.gmavenplus:gmavenplus-plugin@4.2.0`                 | `resolve-plugins` |
|      35 | `org.apache.ivy:ivy@2.5.3`                                | https://svn.apache.org/repos/asf/ant/ivy/core/trunk                                                                   | `org.codehaus.gmavenplus:gmavenplus-plugin@4.2.0`                 | `resolve-plugins` |
|      36 | `org.apache.maven.shared:maven-shared-incremental@1.1`    | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-incremental-1.1                                           | `org.apache.maven.plugins:maven-compiler-plugin@3.14.0`           | `resolve-plugins` |
|      37 | `org.iq80.snappy:snappy@0.4`                              | Could not find repo from package registry                                                                             | `org.apache.maven.plugins:maven-jar-plugin@3.4.2`                 | `resolve-plugins` |
|      38 | `com.google.code.findbugs:jsr305@3.0.2`                   | https://code.google.com/p/jsr-305/                                                                                    | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
|      39 | `com.google.j2objc:j2objc-annotations@2.8`                | http://svn.sonatype.org/spice/trunk/oss/oss-parent-9/j2objc-annotations                                               | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
|      40 | `com.google.android:annotations@4.1.1.4`                  | https://android.git.kernel.org/                                                                                       | `dev.sigstore:sigstore-maven-plugin@1.3.0`                        | `resolve-plugins` |
|      41 | `commons-beanutils:commons-beanutils@1.9.4`               | http://svn.apache.org/viewvc/commons/proper/beanutils/tags/BEANUTILS_1_9_3_RC3                                        | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
|      42 | `org.apache.commons:commons-digester3@3.2`                | http://svn.apache.org/viewvc/commons/proper/digester/tags/DIGESTER3_3_2_RC2                                           | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
|      43 | `javax.servlet:javax.servlet-api@3.1.0`                   | http://java.net/projects/glassfish/sources/svn/show/tags/javax.servlet-api-3.1.0                                      | `org.apache.maven.plugins:maven-site-plugin@3.21.0`               | `resolve-plugins` |
|      44 | `org.eclipse.jgit:org.eclipse.jgit@6.10.0.202406032230-r` | https://git.eclipse.org/r/plugins/gitiles/jgit/jgit/org.eclipse.jgit                                                  | `com.diffplug.spotless:spotless-maven-plugin@2.44.4`              | `resolve-plugins` |
|      45 | `org.sonatype.plexus:plexus-build-api@0.0.7`              | http://svn.sonatype.org/spice/tags/plexus-build-api-0.0.7                                                             | `org.apache.maven.plugins:maven-resources-plugin@3.3.1`           | `resolve-plugins` |
</details>


---

Report created by [dirty-waters](https://github.com/chains-project/dirty-waters/).

Report created on 2025-05-16 16:11:42
- Tool version: 6065c48e
- Project Name: chains-project/maven-lockfile
- Project Version: cbed57cb317568cfdb497c5f26e36a34eb31958a
- Package Manager: maven
