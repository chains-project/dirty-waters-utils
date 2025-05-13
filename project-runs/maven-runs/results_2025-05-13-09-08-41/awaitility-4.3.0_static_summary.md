
# Software Supply Chain Report of awaitility/awaitility - awaitility-4.3.0

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
        

 ### Total packages in the supply chain: 405


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 38

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 16

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 0

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 72


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(38)</summary>
    


| package_name                                           | sha_exists   | tag_version         | is_sha   | sha   | tag_url   | message                                     |   status_code_for_sha | parent                                                   | command           |
|:-------------------------------------------------------|:-------------|:--------------------|:---------|:------|:----------|:--------------------------------------------|----------------------:|:---------------------------------------------------------|:------------------|
| `org.apache.commons:commons-lang3@3.14.0`              | False        | `3.14.0`            | False    |       |           | Tag 3.14.0 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
| `org.apache.commons:commons-text@1.11.0`               | False        | `1.11.0`            | False    |       |           | Tag 1.11.0 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
| `commons-io:commons-io@2.11.0`                         | False        | `2.11.0`            | False    |       |           | Tag 2.11.0 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-compiler-plugin@3.14.0`  | `resolve-plugins` |
| `org.jdom:jdom2@2.0.6.1`                               | False        | `2.0.6.1`           | False    |       |           | Tag 2.0.6.1 not found in the repo           |                   404 | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
| `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`   | False        | `1.18`              | False    |       |           | Tag 1.18 not found in the repo              |                   404 | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
| `org.codehaus.mojo:animal-sniffer@1.18`                | False        | `1.18`              | False    |       |           | Tag 1.18 not found in the repo              |                   404 | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
| `org.codehaus.mojo:java-boot-classpath-detector@1.18`  | False        | `1.18`              | False    |       |           | Tag 1.18 not found in the repo              |                   404 | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
| `org.hamcrest:hamcrest-core@1.3`                       | False        | `1.3`               | False    |       |           | Tag 1.3 not found in the repo               |                   404 | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `tree`            |
| `org.apache.commons:commons-lang3@3.7`                 | False        | `3.7`               | False    |       |           | Tag 3.7 not found in the repo               |                   404 | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
| `org.apache.commons:commons-collections4@4.4`          | False        | `4.4`               | False    |       |           | Tag 4.4 not found in the repo               |                   404 | `org.codehaus.mojo:versions-maven-plugin@2.18.0`         | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-model@2.0.0`        | False        | `2.0.0`             | False    |       |           | Tag 2.0.0 not found in the repo             |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-integration-tools@2.0.0` | False        | `2.0.0`             | False    |       |           | Tag 2.0.0 not found in the repo             |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@2.0.0`     | False        | `2.0.0`             | False    |       |           | Tag 2.0.0 not found in the repo             |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@2.0.0`        | False        | `2.0.0`             | False    |       |           | Tag 2.0.0 not found in the repo             |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.26.2`           | False        | `1.26.2`            | False    |       |           | Tag 1.26.2 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `commons-codec:commons-codec@1.17.1`                   | False        | `1.17.1`            | False    |       |           | Tag 1.17.1 not found in the repo            |                   404 | `org.codehaus.mojo:versions-maven-plugin@2.18.0`         | `resolve-plugins` |
| `commons-io:commons-io@2.17.0`                         | False        | `2.17.0`            | False    |       |           | Tag 2.17.0 not found in the repo            |                   404 | `org.codehaus.mojo:versions-maven-plugin@2.18.0`         | `resolve-plugins` |
| `org.apache.commons:commons-text@1.12.0`               | False        | `1.12.0`            | False    |       |           | Tag 1.12.0 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.17.0`              | False        | `3.17.0`            | False    |       |           | Tag 3.17.0 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.plexus@0.9.0.M3`    | False        | `0.9.0.M3`          | False    |       |           | Tag 0.9.0.M3 not found in the repo          |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.eclipse.sisu:org.eclipse.sisu.inject@0.9.0.M3`    | False        | `0.9.0.M3`          | False    |       |           | Tag 0.9.0.M3 not found in the repo          |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.apache.httpcomponents:httpclient@4.5.14`          | False        | `4.5.14`            | False    |       |           | Tag 4.5.14 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.11.2`   | `resolve-plugins` |
| `org.apache.httpcomponents:httpcore@4.4.16`            | False        | `4.4.16`            | False    |       |           | Tag 4.4.16 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.11.2`   | `resolve-plugins` |
| `commons-io:commons-io@2.18.0`                         | False        | `2.18.0`            | False    |       |           | Tag 2.18.0 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.11.2`   | `resolve-plugins` |
| `commons-io:commons-io@2.16.1`                         | False        | `2.16.1`            | False    |       |           | Tag 2.16.1 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `commons-codec:commons-codec@1.17.0`                   | False        | `1.17.0`            | False    |       |           | Tag 1.17.0 not found in the repo            |                   404 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.fusesource.jansi:jansi@1.17.1`                    | False        | `1.17.1`            | False    |       |           | Tag 1.17.1 not found in the repo            |                   404 | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
| `org.apache.groovy:groovy@4.0.19`                      | False        | `4.0.19`            | False    |       |           | Tag 4.0.19 not found in the repo            |                   404 | `None`                                                   | `tree`            |
| `org.spockframework:spock-core@2.4-M2-groovy-4.0`      | False        | `2.4-M2-groovy-4.0` | False    |       |           | Tag 2.4-M2-groovy-4.0 not found in the repo |                   404 | `None`                                                   | `tree`            |
| `org.junit.platform:junit-platform-engine@1.10.2`      | False        | `1.10.2`            | False    |       |           | Tag 1.10.2 not found in the repo            |                   404 | `org.spockframework:spock-core@2.4-M2-groovy-4.0`        | `tree`            |
| `org.junit.platform:junit-platform-commons@1.10.2`     | False        | `1.10.2`            | False    |       |           | Tag 1.10.2 not found in the repo            |                   404 | `org.junit.platform:junit-platform-engine@1.10.2`        | `tree`            |
| `org.apache.groovy:groovy-json@4.0.19`                 | False        | `4.0.19`            | False    |       |           | Tag 4.0.19 not found in the repo            |                   404 | `None`                                                   | `tree`            |
| `org.apache.groovy:groovy-nio@4.0.19`                  | False        | `4.0.19`            | False    |       |           | Tag 4.0.19 not found in the repo            |                   404 | `None`                                                   | `tree`            |
| `org.apache.groovy:groovy-macro@4.0.19`                | False        | `4.0.19`            | False    |       |           | Tag 4.0.19 not found in the repo            |                   404 | `None`                                                   | `tree`            |
| `org.apache.groovy:groovy-templates@4.0.19`            | False        | `4.0.19`            | False    |       |           | Tag 4.0.19 not found in the repo            |                   404 | `None`                                                   | `tree`            |
| `org.apache.groovy:groovy-test@4.0.19`                 | False        | `4.0.19`            | False    |       |           | Tag 4.0.19 not found in the repo            |                   404 | `None`                                                   | `tree`            |
| `org.apache.groovy:groovy-sql@4.0.19`                  | False        | `4.0.19`            | False    |       |           | Tag 4.0.19 not found in the repo            |                   404 | `None`                                                   | `tree`            |
| `org.apache.groovy:groovy-xml@4.0.19`                  | False        | `4.0.19`            | False    |       |           | Tag 4.0.19 not found in the repo            |                   404 | `None`                                                   | `tree`            |
</details>

<details>
<summary>Source code links that could not be found(16)</summary>
    


|   index | package_name                                    | github_url         | github_exists   | parent                                                | command           |
|--------:|:------------------------------------------------|:-------------------|:----------------|:------------------------------------------------------|:------------------|
|       1 | `commons-cli:commons-cli@1.0`                   | No_repo_info_found |                 | `org.apache.maven.plugins:maven-resources-plugin@2.6` | `resolve-plugins` |
|       2 | `slide:slide-webdavlib@2.1`                     | No_repo_info_found |                 | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`  | `resolve-plugins` |
|       3 | `jdom:jdom@1.0`                                 | No_repo_info_found |                 | `org.apache.maven.plugins:maven-help-plugin@2.2`      | `resolve-plugins` |
|       4 | `org.beanshell:bsh@2.0b4`                       | No_repo_info_found |                 | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`  | `resolve-plugins` |
|       5 | `commons-lang:commons-lang@1.0`                 | No_repo_info_found |                 | `org.apache.maven.plugins:maven-release-plugin@3.1.1` | `resolve-plugins` |
|       6 | `nekohtml:xercesMinimal@1.9.6.2`                | No_repo_info_found |                 | `org.apache.maven.plugins:maven-help-plugin@2.2`      | `resolve-plugins` |
|       7 | `commons-codec:commons-codec@1.2`               | No_repo_info_found |                 | `org.apache.maven.plugins:maven-help-plugin@2.2`      | `resolve-plugins` |
|       8 | `org.sonatype.plexus:plexus-sec-dispatcher@1.3` | No_repo_info_found |                 | `org.apache.maven.plugins:maven-help-plugin@2.2`      | `resolve-plugins` |
|       9 | `org.sonatype.plexus:plexus-cipher@1.4`         | No_repo_info_found |                 | `org.apache.maven.plugins:maven-help-plugin@2.2`      | `resolve-plugins` |
|      10 | `org.sonatype.plexus:plexus-build-api@0.0.4`    | No_repo_info_found |                 | `org.apache.maven.plugins:maven-resources-plugin@2.6` | `resolve-plugins` |
|      11 | `javax.servlet:servlet-api@2.5`                 | No_repo_info_found |                 | `org.apache.maven.plugins:maven-site-plugin@3.3`      | `resolve-plugins` |
|      12 | `commons-beanutils:commons-beanutils@1.7.0`     | No_repo_info_found |                 | `org.apache.maven.plugins:maven-site-plugin@3.3`      | `resolve-plugins` |
|      13 | `dom4j:dom4j@1.1`                               | No_repo_info_found |                 | `org.apache.maven.plugins:maven-site-plugin@3.3`      | `resolve-plugins` |
|      14 | `sslext:sslext@1.2-0`                           | No_repo_info_found |                 | `org.apache.maven.plugins:maven-site-plugin@3.3`      | `resolve-plugins` |
|      15 | `antlr:antlr@2.7.2`                             | No_repo_info_found |                 | `org.apache.maven.plugins:maven-site-plugin@3.3`      | `resolve-plugins` |
|      16 | `oro:oro@2.0.8`                                 | No_repo_info_found |                 | `org.apache.maven.plugins:maven-site-plugin@3.3`      | `resolve-plugins` |
</details>

The package manager (maven) does not support checking for provenance.

All packages have valid code signature.

<details>
<summary>List of packages without code signature(72)</summary>
    


| package_name                                                        | signature_present   | parent                                                   | command           |
|:--------------------------------------------------------------------|:--------------------|:---------------------------------------------------------|:------------------|
| `org.apache.maven.wagon:wagon-provider-api@1.0-beta-2`              | False               | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
| `org.codehaus.plexus:plexus-container-default@1.0-alpha-9-stable-1` | False               | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
| `junit:junit@3.8.1`                                                 | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `classworlds:classworlds@1.1-alpha-2`                               | False               | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
| `org.codehaus.plexus:plexus-utils@1.5.6`                            | False               | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
| `org.apache.maven.wagon:wagon-file@1.0-beta-2`                      | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `org.apache.maven.wagon:wagon-http-lightweight@1.0-beta-2`          | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `org.apache.maven.wagon:wagon-http-shared@1.0-beta-2`               | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `jtidy:jtidy@4aug2000r7-dev`                                        | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `xml-apis:xml-apis@1.0.b2`                                          | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `commons-cli:commons-cli@1.0`                                       | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `org.apache.maven.wagon:wagon-ssh-external@1.0-beta-2`              | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `org.apache.maven.wagon:wagon-ssh-common@1.0-beta-2`                | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `org.codehaus.plexus:plexus-interactivity-api@1.0-alpha-4`          | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `org.apache.maven.wagon:wagon-ssh@1.0-beta-2`                       | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `com.jcraft:jsch@0.1.27`                                            | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `commons-lang:commons-lang@2.1`                                     | False               | `org.apache.maven.plugins:maven-jar-plugin@2.4`          | `resolve-plugins` |
| `junit:junit@3.8.2`                                                 | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `org.apache.maven.wagon:wagon-webdav@1.0-beta-2`                    | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `slide:slide-webdavlib@2.1`                                         | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `commons-httpclient:commons-httpclient@2.0.2`                       | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `jdom:jdom@1.0`                                                     | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `de.zeigermann.xml:xml-im-exporter@1.1`                             | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `commons-logging:commons-logging@1.0.4`                             | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `classworlds:classworlds@1.1`                                       | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-utils@1.5.8`                            | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `org.codehaus.plexus:plexus-archiver@1.0-alpha-7`                   | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `org.beanshell:bsh@2.0b4`                                           | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `org.codehaus.plexus:plexus-i18n@1.0-beta-6`                        | False               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
| `javax.inject:javax.inject@1`                                       | False               | `org.apache.maven.plugins:maven-compiler-plugin@3.14.0`  | `resolve-plugins` |
| `org.apache.maven.scm:maven-scm-providers-standard@2.1.0`           | False               | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
| `com.google.code.findbugs:jsr305@2.0.0`                             | False               | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
| `commons-lang:commons-lang@1.0`                                     | False               | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
| `org.ow2.asm:asm@7.0`                                               | False               | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
| `nekohtml:xercesMinimal@1.9.6.2`                                    | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `nekohtml:nekohtml@1.9.6.2`                                         | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `commons-httpclient:commons-httpclient@3.0`                         | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `commons-codec:commons-codec@1.2`                                   | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `org.slf4j:slf4j-nop@1.5.3`                                         | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `org.slf4j:slf4j-jdk14@1.5.6`                                       | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `org.slf4j:slf4j-api@1.5.6`                                         | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `org.slf4j:jcl-over-slf4j@1.5.6`                                    | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `backport-util-concurrent:backport-util-concurrent@3.1`             | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `com.jcraft:jsch@0.1.38`                                            | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-interpolation@1.11`                     | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `javax.annotation:jsr250-api@1.0`                                   | False               | `org.codehaus.mojo:versions-maven-plugin@2.18.0`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-i18n@1.0-beta-10`                       | False               | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
| `org.sonatype.plexus:plexus-build-api@0.0.4`                        | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `org.codehaus.plexus:plexus-interpolation@1.13`                     | False               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
| `org.codehaus.plexus:plexus-digest@1.0`                             | False               | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
| `com.google.code.findbugs:jsr305@2.0.1`                             | False               | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
| `org.codehaus.plexus:plexus-container-default@1.0-alpha-30`         | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `xerces:xercesImpl@2.9.1`                                           | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `xml-apis:xml-apis@1.3.04`                                          | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `commons-codec:commons-codec@1.3`                                   | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `javax.servlet:servlet-api@2.5`                                     | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `commons-beanutils:commons-beanutils@1.7.0`                         | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `commons-digester:commons-digester@1.8`                             | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `commons-chain:commons-chain@1.1`                                   | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `dom4j:dom4j@1.1`                                                   | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `sslext:sslext@1.2-0`                                               | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `antlr:antlr@2.7.2`                                                 | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-i18n@1.0-beta-7`                        | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `org.apache.velocity:velocity@1.5`                                  | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `oro:oro@2.0.8`                                                     | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-velocity@1.1.8`                         | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-utils@1.5.10`                           | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `org.mortbay.jetty:servlet-api@2.5-20081211`                        | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-container-default@1.0-alpha-9`          | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-utils@1.5.7`                            | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `xmlpull:xmlpull@1.1.3.1`                                           | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
| `xpp3:xpp3_min@1.1.4c`                                              | False               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
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
    
- Source code repo is not hosted on GitHub:  228

    This could be due, for example, to the package being hosted on a different platform.

    This does not mean that the source code URL is invalid.

    However, for non-GitHub repositories, not all checks can currently be performed.

|   index | package_name                                                         | github_url                                                                                                               | parent                                                   | command           |
|--------:|:---------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|:------------------|
|       1 | `org.apache.maven.plugins:maven-deploy-plugin@2.7`                   | http://svn.apache.org/viewvc/maven/plugins/tags/maven-deploy-plugin-2.7                                                  | `org.apache.maven.plugins:maven-deploy-plugin@2.7`       | `resolve-plugins` |
|       2 | `org.apache.maven:maven-plugin-api@2.0.6`                            | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-plugin-api                                      | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|       3 | `org.apache.maven:maven-project@2.0.6`                               | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-project                                         | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|       4 | `org.apache.maven:maven-settings@2.0.6`                              | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-settings                                        | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|       5 | `org.apache.maven:maven-profile@2.0.6`                               | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-profile                                         | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|       6 | `org.apache.maven:maven-artifact-manager@2.0.6`                      | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-artifact-manager                                | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|       7 | `org.apache.maven:maven-repository-metadata@2.0.6`                   | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-repository-metadata                             | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|       8 | `org.apache.maven.wagon:wagon-provider-api@1.0-beta-2`               | https://svn.apache.org/repos/asf/maven/wagon/tags/wagon-1.0-beta-2/wagon-provider-api                                    | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|       9 | `org.apache.maven:maven-plugin-registry@2.0.6`                       | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-plugin-registry                                 | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|      10 | `org.codehaus.plexus:plexus-container-default@1.0-alpha-9-stable-1`  | scm:svn:svn://svn.codehaus.org/plexus/scm/trunk/plexus-containers/plexus-container-default/                              | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|      11 | `junit:junit@3.8.1`                                                  | http://junit.cvs.sourceforge.net/junit/                                                                                  | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      12 | `classworlds:classworlds@1.1-alpha-2`                                | http://cvs.classworlds.codehaus.org/                                                                                     | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|      13 | `org.apache.maven:maven-model@2.0.6`                                 | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-model                                           | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|      14 | `org.apache.maven:maven-artifact@2.0.6`                              | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-artifact                                        | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|      15 | `org.codehaus.plexus:plexus-utils@1.5.6`                             | http://fisheye.codehaus.org/browse/plexus/plexus-utils/tags/plexus-utils-1.5.6                                           | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
|      16 | `org.apache.maven.plugins:maven-jar-plugin@2.4`                      | http://svn.apache.org/viewvc/maven/plugins/tags/maven-jar-plugin-2.4                                                     | `org.apache.maven.plugins:maven-jar-plugin@2.4`          | `resolve-plugins` |
|      17 | `org.apache.maven:maven-archiver@2.5`                                | http://svn.apache.org/viewvc/maven/shared/tags/maven-archiver-2.5                                                        | `org.apache.maven.plugins:maven-jar-plugin@2.4`          | `resolve-plugins` |
|      18 | `org.apache.maven:maven-core@2.0.6`                                  | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-core                                            | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      19 | `org.apache.maven.wagon:wagon-file@1.0-beta-2`                       | https://svn.apache.org/repos/asf/maven/wagon/tags/wagon-1.0-beta-2/wagon-providers/wagon-file                            | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      20 | `org.apache.maven:maven-plugin-parameter-documenter@2.0.6`           | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-plugin-parameter-documenter                     | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      21 | `org.apache.maven.wagon:wagon-http-lightweight@1.0-beta-2`           | https://svn.apache.org/repos/asf/maven/wagon/tags/wagon-1.0-beta-2/wagon-providers/wagon-http-lightweight                | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      22 | `org.apache.maven.wagon:wagon-http-shared@1.0-beta-2`                | https://svn.apache.org/repos/asf/maven/wagon/tags/wagon-1.0-beta-2/wagon-providers/wagon-http-shared                     | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      23 | `jtidy:jtidy@4aug2000r7-dev`                                         | http://svn.sourceforge.net/viewcvs.cgi/jtidy/trunk/jtidy/                                                                | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      24 | `xml-apis:xml-apis@1.0.b2`                                           | http://svn.apache.org/viewvc/xml/commons/tags/xml-commons-1_0_b2                                                         | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      25 | `org.apache.maven.reporting:maven-reporting-api@2.0.6`               | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-reporting/maven-reporting-api                   | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      26 | `org.apache.maven.doxia:doxia-sink-api@1.0-alpha-7`                  | http://svn.apache.org/viewcvs.cgi/maven/doxia/tags/doxia-1.0-alpha-7/doxia-sink-api                                      | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      27 | `org.apache.maven:maven-error-diagnostics@2.0.6`                     | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-error-diagnostics                               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      28 | `org.apache.maven.wagon:wagon-ssh-external@1.0-beta-2`               | https://svn.apache.org/repos/asf/maven/wagon/tags/wagon-1.0-beta-2/wagon-providers/wagon-ssh-external                    | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      29 | `org.apache.maven.wagon:wagon-ssh-common@1.0-beta-2`                 | https://svn.apache.org/repos/asf/maven/wagon/tags/wagon-1.0-beta-2/wagon-providers/wagon-ssh-common                      | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      30 | `org.apache.maven:maven-plugin-descriptor@2.0.6`                     | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-plugin-descriptor                               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      31 | `org.codehaus.plexus:plexus-interactivity-api@1.0-alpha-4`           | scm:svn:svn://svn.codehaus.org/plexus/scm/trunk/plexus-components/plexus-interactivity/plexus-interactivity-api          | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      32 | `org.apache.maven:maven-monitor@2.0.6`                               | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-monitor                                         | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      33 | `org.apache.maven.wagon:wagon-ssh@1.0-beta-2`                        | https://svn.apache.org/repos/asf/maven/wagon/tags/wagon-1.0-beta-2/wagon-providers/wagon-ssh                             | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      34 | `com.jcraft:jsch@0.1.27`                                             | http://www.jcraft.com/jsch/                                                                                              | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|      35 | `commons-lang:commons-lang@2.1`                                      | http://svn.apache.org/viewcvs/jakarta/commons/proper/${pom.artifactId.substring(8)}/trunk                                | `org.apache.maven.plugins:maven-jar-plugin@2.4`          | `resolve-plugins` |
|      36 | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`                 | http://svn.apache.org/viewcvs.cgi/maven/enforcer/tags/enforcer-1.2/maven-enforcer-plugin                                 | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      37 | `org.apache.maven:maven-artifact@2.0.9`                              | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-artifact                                        | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      38 | `org.apache.maven:maven-plugin-api@2.0.9`                            | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-plugin-api                                      | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      39 | `org.apache.maven:maven-project@2.0.9`                               | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-project                                         | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      40 | `org.apache.maven:maven-settings@2.0.9`                              | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-settings                                        | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      41 | `org.apache.maven:maven-profile@2.0.9`                               | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-profile                                         | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      42 | `org.apache.maven:maven-model@2.0.9`                                 | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-model                                           | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      43 | `org.apache.maven:maven-artifact-manager@2.0.9`                      | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-artifact-manager                                | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      44 | `org.apache.maven:maven-plugin-registry@2.0.9`                       | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-plugin-registry                                 | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      45 | `junit:junit@3.8.2`                                                  | http://junit.cvs.sourceforge.net/junit/                                                                                  | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      46 | `org.apache.maven:maven-core@2.0.9`                                  | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-core                                            | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      47 | `org.apache.maven:maven-plugin-parameter-documenter@2.0.9`           | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-plugin-parameter-documenter                     | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      48 | `org.apache.maven.wagon:wagon-webdav@1.0-beta-2`                     | https://svn.apache.org/repos/asf/maven/wagon/tags/wagon-1.0-beta-2/wagon-providers/wagon-webdav                          | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      49 | `commons-httpclient:commons-httpclient@2.0.2`                        | http://cvs.apache.org/viewcvs.cgi/jakarta-commons/httpclient/                                                            | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      50 | `de.zeigermann.xml:xml-im-exporter@1.1`                              | http://xml-im-exporter.sourceforge.net                                                                                   | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      51 | `commons-logging:commons-logging@1.0.4`                              | http://cvs.apache.org/viewcvs/jakarta-commons/logging/                                                                   | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      52 | `org.apache.maven.reporting:maven-reporting-api@2.0.9`               | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-reporting/maven-reporting-api                   | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      53 | `org.apache.maven.doxia:doxia-sink-api@1.0-alpha-10`                 | https://svn.apache.org/repos/asf/maven/doxia/doxia/tags/doxia-1.0-alpha-10/doxia-sink-api                                | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      54 | `org.apache.maven:maven-repository-metadata@2.0.9`                   | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-repository-metadata                             | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      55 | `org.apache.maven:maven-error-diagnostics@2.0.9`                     | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-error-diagnostics                               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      56 | `org.apache.maven:maven-plugin-descriptor@2.0.9`                     | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-plugin-descriptor                               | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      57 | `org.apache.maven:maven-monitor@2.0.9`                               | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-monitor                                         | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      58 | `classworlds:classworlds@1.1`                                        | http://cvs.classworlds.codehaus.org/                                                                                     | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      59 | `org.codehaus.plexus:plexus-utils@1.5.8`                             | http://fisheye.codehaus.org/browse/plexus/plexus-utils/tags/plexus-utils-1.5.8                                           | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      60 | `commons-lang:commons-lang@2.3`                                      | http://svn.apache.org/viewvc/jakarta/commons/proper/lang/trunk                                                           | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      61 | `org.apache.maven.enforcer:enforcer-api@1.2`                         | http://svn.apache.org/viewcvs.cgi/maven/enforcer/tags/enforcer-1.2/enforcer-api                                          | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      62 | `org.apache.maven.enforcer:enforcer-rules@1.2`                       | http://svn.apache.org/viewcvs.cgi/maven/enforcer/tags/enforcer-1.2/enforcer-rules                                        | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      63 | `org.apache.maven.shared:maven-common-artifact-filters@1.2`          | http://svn.apache.org/viewvc/maven/shared/tags/maven-common-artifact-filters-1.2                                         | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      64 | `org.apache.maven.shared:maven-plugin-testing-harness@1.1`           | https://svn.apache.org/repos/asf/maven/shared/tags/maven-plugin-testing-harness-1.1                                      | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      65 | `org.codehaus.plexus:plexus-archiver@1.0-alpha-7`                    | scm:svn:https://svn.codehaus.org/plexus/tags/plexus-archiver-1.0-alpha-7                                                 | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      66 | `org.apache.maven.shared:maven-dependency-tree@2.0`                  | http://svn.apache.org/viewvc/maven/shared/tags/maven-dependency-tree-2.0                                                 | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      67 | `org.codehaus.plexus:plexus-component-annotations@1.5.5`             | http://fisheye.codehaus.org/browse/plexus/plexus-containers/tags/plexus-containers-1.5.5/plexus-component-annotations    | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|      68 | `org.codehaus.plexus:plexus-i18n@1.0-beta-6`                         | scm:svn:svn://svn.codehaus.org/plexus/scm/trunk/plexus-components/plexus-i18n/                                           | `org.apache.maven.plugins:maven-enforcer-plugin@1.2`     | `resolve-plugins` |
|      69 | `javax.inject:javax.inject@1`                                        | http://code.google.com/p/atinject/source/checkout                                                                        | `org.apache.maven.plugins:maven-compiler-plugin@3.14.0`  | `resolve-plugins` |
|      70 | `org.eclipse.jgit:org.eclipse.jgit@5.13.3.202401111512-r`            | https://git.eclipse.org/r/plugins/gitiles/jgit/jgit/org.eclipse.jgit                                                     | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
|      71 | `org.eclipse.jgit:org.eclipse.jgit.ssh.apache@5.13.3.202401111512-r` | https://git.eclipse.org/r/plugins/gitiles/jgit/jgit/org.eclipse.jgit.ssh.apache                                          | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
|      72 | `com.google.code.findbugs:jsr305@2.0.0`                              | http://findbugs.googlecode.com/svn/trunk/                                                                                | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
|      73 | `org.ow2.asm:asm@5.0.3`                                              | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm/                                                        | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
|      74 | `org.ow2.asm:asm-commons@5.0.3`                                      | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm-commons/                                                | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
|      75 | `org.ow2.asm:asm-tree@5.0.3`                                         | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm-tree/                                                   | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
|      76 | `de.tototec:de.tototec.cmdoption@0.2.0`                              | http://cmdoption.tototec.de/svn/cmdoption                                                                                | `org.apache.maven.plugins:maven-release-plugin@3.1.1`    | `resolve-plugins` |
|      77 | `org.ow2.asm:asm@7.0`                                                | https://gitlab.ow2.org/asm/asm/                                                                                          | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
|      78 | `org.apache.maven:maven-plugin-api@3.0`                              | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-plugin-api                                               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|      79 | `org.apache.maven:maven-model@3.0`                                   | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-model                                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|      80 | `org.codehaus.plexus:plexus-component-annotations@1.5.4`             | http://fisheye.codehaus.org/browse/plexus/plexus-containers/tags/plexus-containers-1.5.4/plexus-component-annotations    | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
|      81 | `org.codehaus.plexus:plexus-classworlds@2.2.3`                       | http://fisheye.codehaus.org/browse/plexus/plexus-classworlds/tags/plexus-classworlds-2.2.3                               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|      82 | `org.apache.maven:maven-core@2.2.1`                                  | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-core                                                   | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      83 | `org.apache.maven:maven-settings@2.2.1`                              | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-settings                                               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      84 | `org.apache.maven.wagon:wagon-file@1.0-beta-6`                       | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-providers/wagon-file                                | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      85 | `org.apache.maven:maven-plugin-parameter-documenter@2.2.1`           | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-plugin-parameter-documenter                            | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      86 | `org.apache.maven.wagon:wagon-http-lightweight@1.0-beta-6`           | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-providers/wagon-http-lightweight                    | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      87 | `org.apache.maven.wagon:wagon-http-shared@1.0-beta-6`                | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-providers/wagon-http-shared                         | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      88 | `nekohtml:nekohtml@1.9.6.2`                                          | http://nekohtml.svn.sourceforge.net/viewvc/nekohtml/                                                                     | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      89 | `org.apache.maven.wagon:wagon-http@1.0-beta-6`                       | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-providers/wagon-http                                | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      90 | `org.apache.maven.wagon:wagon-webdav-jackrabbit@1.0-beta-6`          | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-providers/wagon-webdav-jackrabbit                   | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      91 | `org.apache.jackrabbit:jackrabbit-webdav@1.5.0`                      | http://svn.apache.org/viewvc/jackrabbit/trunk/jackrabbit-webdav                                                          | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      92 | `org.apache.jackrabbit:jackrabbit-jcr-commons@1.5.0`                 | http://svn.apache.org/viewvc/jackrabbit/trunk/jackrabbit-jcr-commons                                                     | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      93 | `commons-httpclient:commons-httpclient@3.0`                          | http://svn.apache.org/repos/asf/jakarta/commons/proper/${pom.artifactId.substring(8)}/trunk                              | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      94 | `org.slf4j:slf4j-nop@1.5.3`                                          | http://svn.slf4j.org/viewvc/slf4j/trunk/slf4j-nop/                                                                       | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      95 | `org.slf4j:slf4j-jdk14@1.5.6`                                        | http://svn.slf4j.org/viewvc/slf4j/trunk/slf4j-jdk14/                                                                     | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      96 | `org.slf4j:slf4j-api@1.5.6`                                          | http://svn.slf4j.org/viewvc/slf4j/trunk/slf4j-api/                                                                       | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      97 | `org.slf4j:jcl-over-slf4j@1.5.6`                                     | http://svn.slf4j.org/viewvc/slf4j/trunk/jcl-over-slf4j/                                                                  | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      98 | `org.apache.maven.reporting:maven-reporting-api@2.2.1`               | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-reporting/maven-reporting-api                          | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|      99 | `org.apache.maven.doxia:doxia-sink-api@1.1`                          | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.1/doxia-sink-api                                        | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     100 | `org.apache.maven.doxia:doxia-logging-api@1.1`                       | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.1/doxia-logging-api                                     | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     101 | `org.apache.maven:maven-profile@2.2.1`                               | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-profile                                                | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     102 | `org.apache.maven.wagon:wagon-provider-api@1.0-beta-6`               | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-provider-api                                        | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     103 | `org.apache.maven:maven-repository-metadata@2.2.1`                   | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-repository-metadata                                    | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     104 | `org.apache.maven:maven-error-diagnostics@2.2.1`                     | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-error-diagnostics                                      | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     105 | `commons-cli:commons-cli@1.2`                                        | http://svn.apache.org/viewvc/commons/proper/cli/branches/cli-1.x/                                                        | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     106 | `org.apache.maven.wagon:wagon-ssh-external@1.0-beta-6`               | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-providers/wagon-ssh-external                        | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     107 | `org.apache.maven.wagon:wagon-ssh-common@1.0-beta-6`                 | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-providers/wagon-ssh-common                          | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     108 | `org.apache.maven:maven-plugin-descriptor@2.2.1`                     | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-plugin-descriptor                                      | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     109 | `org.apache.maven:maven-artifact-manager@2.2.1`                      | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-artifact-manager                                       | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     110 | `backport-util-concurrent:backport-util-concurrent@3.1`              | svn://dcl.mathcs.emory.edu/software/harness2/trunk/util/backport-util-concurrent/                                        | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     111 | `org.apache.maven:maven-monitor@2.2.1`                               | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-monitor                                                | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     112 | `org.apache.maven.wagon:wagon-ssh@1.0-beta-6`                        | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-providers/wagon-ssh                                 | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     113 | `com.jcraft:jsch@0.1.38`                                             | http://www.jcraft.com/jsch/                                                                                              | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     114 | `org.apache.maven:maven-project@2.2.1`                               | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-project                                                | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     115 | `org.apache.maven:maven-plugin-registry@2.2.1`                       | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-plugin-registry                                        | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     116 | `org.codehaus.plexus:plexus-interpolation@1.11`                      | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-interpolation-1.11                               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     117 | `org.apache.maven:maven-artifact@2.2.1`                              | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-artifact                                               | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     118 | `org.apache.maven:maven-toolchain@2.2.1`                             | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-toolchain                                              | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
|     119 | `org.apache.maven.shared:maven-common-artifact-filters@1.4`          | http://svn.apache.org/viewvc/maven/shared/tags/maven-common-artifact-filters-1.4                                         | `org.codehaus.mojo:animal-sniffer-maven-plugin@1.18`     | `resolve-plugins` |
|     120 | `commons-beanutils:commons-beanutils@1.9.4`                          | http://svn.apache.org/viewvc/commons/proper/beanutils/tags/BEANUTILS_1_9_3_RC3                                           | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
|     121 | `commons-logging:commons-logging@1.2`                                | http://svn.apache.org/repos/asf/commons/proper/logging/trunk                                                             | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
|     122 | `commons-collections:commons-collections@3.2.2`                      | http://svn.apache.org/viewvc/commons/proper/collections/trunk                                                            | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
|     123 | `org.apache.commons:commons-digester3@3.2`                           | http://svn.apache.org/viewvc/commons/proper/digester/tags/DIGESTER3_3_2_RC2                                              | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
|     124 | `org.tukaani:xz@1.9`                                                 | https://git.tukaani.org/?p=xz-java.git                                                                                   | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
|     125 | `org.eclipse.sisu:org.eclipse.sisu.plexus@0.3.4`                     | http://git.eclipse.org/c/sisu/org.eclipse.sisu.plexus.git/tree/org.eclipse.sisu.plexus/                                  | `org.codehaus.mojo:versions-maven-plugin@2.18.0`         | `resolve-plugins` |
|     126 | `javax.enterprise:cdi-api@1.0`                                       | http://fisheye.jboss.org/browse/Weld/api/tags/1.0/build/tags/weld-parent-6/weld-api-bom/weld-api-parent/cdi-api          | `org.codehaus.mojo:versions-maven-plugin@2.18.0`         | `resolve-plugins` |
|     127 | `javax.annotation:jsr250-api@1.0`                                    | http://jcp.org/aboutJava/communityprocess/final/jsr250/index.html                                                        | `org.codehaus.mojo:versions-maven-plugin@2.18.0`         | `resolve-plugins` |
|     128 | `org.eclipse.sisu:org.eclipse.sisu.inject@0.3.4`                     | http://git.eclipse.org/c/sisu/org.eclipse.sisu.inject.git/tree/org.eclipse.sisu.inject/                                  | `org.codehaus.mojo:versions-maven-plugin@2.18.0`         | `resolve-plugins` |
|     129 | `org.codehaus.plexus:plexus-i18n@1.0-beta-10`                        | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10                                 | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
|     130 | `org.apache.maven.plugins:maven-clean-plugin@2.5`                    | http://svn.apache.org/viewvc/maven/plugins/tags/maven-clean-plugin-2.5                                                   | `org.apache.maven.plugins:maven-clean-plugin@2.5`        | `resolve-plugins` |
|     131 | `org.apache.maven.plugins:maven-resources-plugin@2.6`                | http://svn.apache.org/viewvc/maven/plugins/tags/maven-resources-plugin-2.6                                               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|     132 | `org.codehaus.plexus:plexus-utils@2.0.5`                             | http://fisheye.codehaus.org/browse/plexus/plexus-utils/tags/plexus-utils-2.0.5                                           | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|     133 | `org.apache.maven.shared:maven-filtering@1.1`                        | http://svn.apache.org/viewvc/maven/shared/tags/maven-filtering-1.1                                                       | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|     134 | `org.codehaus.plexus:plexus-interpolation@1.13`                      | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-interpolation-1.13                               | `org.apache.maven.plugins:maven-resources-plugin@2.6`    | `resolve-plugins` |
|     135 | `commons-codec:commons-codec@1.11`                                   | http://svn.apache.org/viewvc/commons/proper/codec/trunk                                                                  | `org.apache.maven.plugins:maven-javadoc-plugin@3.11.2`   | `resolve-plugins` |
|     136 | `org.ow2.asm:asm@9.7`                                                | https://gitlab.ow2.org/asm/asm/                                                                                          | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
|     137 | `org.apache.maven.plugins:maven-install-plugin@2.4`                  | http://svn.apache.org/viewvc/maven/plugins/tags/maven-install-plugin-2.4                                                 | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|     138 | `org.codehaus.plexus:plexus-digest@1.0`                              | https://svn.codehaus.org/plexus/tags/plexus-digest-1.0                                                                   | `org.apache.maven.plugins:maven-install-plugin@2.4`      | `resolve-plugins` |
|     139 | `org.sonatype.plexus:plexus-build-api@0.0.7`                         | http://svn.sonatype.org/spice/tags/plexus-build-api-0.0.7                                                                | `org.apache.maven.plugins:maven-dependency-plugin@3.8.1` | `resolve-plugins` |
|     140 | `org.apache.maven.plugins:maven-site-plugin@3.3`                     | http://svn.apache.org/viewvc/maven/plugins/tags/maven-site-plugin-3.3                                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     141 | `org.apache.maven.reporting:maven-reporting-exec@1.1`                | http://svn.apache.org/viewvc/maven/shared/tags/maven-reporting-exec-1.1                                                  | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     142 | `org.apache.maven.reporting:maven-reporting-api@3.0`                 | http://svn.apache.org/viewvc/maven/shared/tags/maven-reporting-api-3.0                                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     143 | `org.apache.maven:maven-artifact@3.0`                                | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-artifact                                                 | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     144 | `org.apache.maven.shared:maven-shared-utils@0.3`                     | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-utils-0.3                                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     145 | `com.google.code.findbugs:jsr305@2.0.1`                              | http://findbugs.googlecode.com/svn/trunk/                                                                                | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     146 | `org.eclipse.aether:aether-util@0.9.0.M2`                            | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-util/                                                        | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     147 | `org.apache.maven:maven-core@3.0`                                    | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-core                                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     148 | `org.apache.maven:maven-repository-metadata@3.0`                     | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-repository-metadata                                      | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     149 | `org.apache.maven:maven-model-builder@3.0`                           | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-model-builder                                            | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     150 | `org.apache.maven:maven-aether-provider@3.0`                         | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-aether-provider                                          | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     151 | `org.codehaus.plexus:plexus-interpolation@1.14`                      | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-interpolation-1.14                               | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     152 | `org.apache.maven:maven-settings@3.0`                                | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-settings                                                 | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     153 | `org.apache.maven:maven-settings-builder@3.0`                        | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-settings-builder                                         | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     154 | `org.apache.maven:maven-archiver@2.4.2`                              | http://svn.apache.org/viewvc/maven/shared/tags/maven-archiver-2.4.2                                                      | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     155 | `org.apache.maven.doxia:doxia-sink-api@1.4`                          | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-sink-api                                        | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     156 | `org.apache.maven.doxia:doxia-logging-api@1.4`                       | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-logging-api                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     157 | `org.codehaus.plexus:plexus-container-default@1.0-alpha-30`          | http://fisheye.codehaus.org/browse/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-30/plexus-container-default | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     158 | `org.apache.maven.doxia:doxia-core@1.4`                              | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-core                                            | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     159 | `xerces:xercesImpl@2.9.1`                                            | http://svn.apache.org/viewvc/maven/pom/tags/apache-4/xercesImpl                                                          | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     160 | `xml-apis:xml-apis@1.3.04`                                           | http://svn.apache.org/viewvc/xml/commons/tags/xml-commons-external-1_3_04/                                               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     161 | `org.apache.httpcomponents:httpclient@4.0.2`                         | https://svn.apache.org/repos/asf/httpcomponents/httpclient/tags/4.0.2/httpclient                                         | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     162 | `commons-logging:commons-logging@1.1.1`                              | http://svn.apache.org/repos/asf/commons/proper/logging/tags/commons-logging-1.1.1                                        | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     163 | `commons-codec:commons-codec@1.3`                                    | http://cvs.apache.org/viewcvs/jakarta-commons/codec/                                                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     164 | `org.apache.httpcomponents:httpcore@4.0.1`                           | http://svn.apache.org/repos/asf/httpcomponents/httpcore/tags/4.0.1/httpcore                                              | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     165 | `org.apache.maven.doxia:doxia-module-xhtml@1.4`                      | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-xhtml                      | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     166 | `org.apache.maven.doxia:doxia-module-apt@1.4`                        | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-apt                        | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     167 | `org.apache.maven.doxia:doxia-module-xdoc@1.4`                       | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-xdoc                       | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     168 | `org.apache.maven.doxia:doxia-module-fml@1.4`                        | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-fml                        | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     169 | `org.apache.maven.doxia:doxia-module-markdown@1.4`                   | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-markdown                   | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     170 | `org.ow2.asm:asm@4.1`                                                | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm/                                                        | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     171 | `org.ow2.asm:asm-tree@4.1`                                           | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm-tree/                                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     172 | `org.ow2.asm:asm-analysis@4.1`                                       | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm-analysis/                                               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     173 | `org.ow2.asm:asm-util@4.1`                                           | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm-util/                                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     174 | `org.apache.maven.doxia:doxia-decoration-model@1.4`                  | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia-sitetools/tags/doxia-sitetools-1.4/doxia-decoration-model            | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     175 | `org.apache.maven.doxia:doxia-site-renderer@1.4`                     | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia-sitetools/tags/doxia-sitetools-1.4/doxia-site-renderer               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     176 | `org.apache.velocity:velocity-tools@2.0`                             | http://svn.apache.org/repos/asf/velocity/tools/trunk                                                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     177 | `commons-digester:commons-digester@1.8`                              | http://svn.apache.org/repos/asf/jakarta/commons/proper/digester/trunk                                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     178 | `commons-chain:commons-chain@1.1`                                    | http://svn.apache.org/viewcvs.cgi                                                                                        | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     179 | `commons-validator:commons-validator@1.3.1`                          | http://svn.apache.org/viewvc                                                                                             | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     180 | `org.apache.struts:struts-core@1.3.8`                                | http://svn.apache.org/repos/asf/struts/struts1/trunk/core                                                                | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     181 | `org.apache.struts:struts-taglib@1.3.8`                              | http://svn.apache.org/repos/asf/struts/struts1/trunk/taglib/                                                             | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     182 | `org.apache.struts:struts-tiles@1.3.8`                               | http://svn.apache.org/repos/asf/struts/struts1/trunk/tiles/                                                              | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     183 | `commons-collections:commons-collections@3.2.1`                      | http://svn.apache.org/viewvc/commons/proper/collections/trunk                                                            | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     184 | `org.apache.maven.doxia:doxia-integration-tools@1.5`                 | http://svn.apache.org/viewvc/maven/doxia/doxia-tools/tags/doxia-integration-tools-1.5                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     185 | `org.apache.maven.wagon:wagon-provider-api@1.0`                      | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0/wagon-provider-api                                               | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     186 | `org.codehaus.plexus:plexus-archiver@1.0`                            | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-archiver-1.0                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     187 | `org.codehaus.plexus:plexus-io@1.0`                                  | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-io-1.0                                           | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     188 | `org.codehaus.plexus:plexus-i18n@1.0-beta-7`                         | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-i18n-1.0-beta-7                                  | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     189 | `org.apache.velocity:velocity@1.5`                                   | http://svn.apache.org/viewvc/velocity/engine/tags/Velocity_1.5                                                           | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     190 | `org.codehaus.plexus:plexus-velocity@1.1.8`                          | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-velocity-1.1.8                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     191 | `org.codehaus.plexus:plexus-utils@1.5.10`                            | http://fisheye.codehaus.org/browse/plexus/plexus-utils/tags/plexus-utils-1.5.10                                          | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     192 | `org.mortbay.jetty:jetty@6.1.25`                                     | http://fisheye.codehaus.org/viewrep/jetty/modules/jetty/                                                                 | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     193 | `org.mortbay.jetty:servlet-api@2.5-20081211`                         | scm:svn:https://svn.codehaus.org/jetty/servlet-api/tags/servlet-api-2.5-20081211                                         | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     194 | `org.mortbay.jetty:jetty-util@6.1.25`                                | http://fisheye.codehaus.org/viewrep/jetty/jetty-util/                                                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     195 | `commons-lang:commons-lang@2.5`                                      | http://svn.apache.org/viewvc/commons/proper/lang/trunk                                                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     196 | `commons-io:commons-io@1.4`                                          | http://svn.apache.org/viewvc/commons/proper/io/trunk                                                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`         | `resolve-plugins` |
|     197 | `org.apache.maven.shared:maven-shared-incremental@1.1`               | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-incremental-1.1                                              | `org.apache.maven.plugins:maven-compiler-plugin@3.14.0`  | `resolve-plugins` |
|     198 | `org.ow2.asm:asm@9.7.1`                                              | https://gitlab.ow2.org/asm/asm/                                                                                          | `org.apache.maven.plugins:maven-compiler-plugin@3.14.0`  | `resolve-plugins` |
|     199 | `org.apache.maven:maven-plugin-api@3.0.1`                            | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.1/maven-plugin-api                                             | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     200 | `org.apache.maven:maven-artifact@3.0.1`                              | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.1/maven-artifact                                               | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     201 | `org.apache.maven:maven-model@3.0.1`                                 | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.1/maven-model                                                  | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     202 | `org.codehaus.plexus:plexus-utils@2.0.4`                             | http://fisheye.codehaus.org/browse/plexus/plexus-utils/tags/plexus-utils-2.0.4                                           | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     203 | `org.apache.maven:maven-core@3.0.1`                                  | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.1/maven-core                                                   | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     204 | `org.apache.maven:maven-settings@3.0.1`                              | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.1/maven-settings                                               | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     205 | `org.apache.maven:maven-settings-builder@3.0.1`                      | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.1/maven-settings-builder                                       | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     206 | `org.apache.maven:maven-repository-metadata@3.0.1`                   | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.1/maven-repository-metadata                                    | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     207 | `org.apache.maven:maven-model-builder@3.0.1`                         | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.1/maven-model-builder                                          | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     208 | `org.apache.maven:maven-aether-provider@3.0.1`                       | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.1/maven-aether-provider                                        | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     209 | `org.apache.maven.shared:file-management@3.0.0`                      | http://svn.apache.org/viewvc/maven/shared/tags/file-management-3.0.0                                                     | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     210 | `org.apache.maven.shared:maven-shared-io@3.0.0`                      | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-io-3.0.0                                                     | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     211 | `org.apache.maven:maven-compat@3.0`                                  | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-compat                                                   | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     212 | `org.apache.maven.shared:maven-shared-utils@3.0.0`                   | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-utils-3.0.0                                                  | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     213 | `commons-io:commons-io@2.4`                                          | http://svn.apache.org/viewvc/commons/proper/io/trunk                                                                     | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     214 | `org.apache.maven:maven-archiver@2.6`                                | http://svn.apache.org/viewvc/maven/shared/tags/maven-archiver-2.6                                                        | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     215 | `org.apache.commons:commons-compress@1.9`                            | http://svn.apache.org/repos/asf/commons/proper/compress/tags/COMPRESS-1.9                                                | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     216 | `org.apache.ant:ant@1.10.5`                                          | https://git-wip-us.apache.org/repos/asf/ant.git/ant                                                                      | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     217 | `org.apache.ant:ant-launcher@1.10.5`                                 | https://git-wip-us.apache.org/repos/asf/ant.git/ant-launcher                                                             | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     218 | `org.apache.ivy:ivy@2.4.0`                                           | http://svn.apache.org/repos/asf/ant/ivy/core/trunk                                                                       | `org.codehaus.gmavenplus:gmavenplus-plugin@1.7.1`        | `resolve-plugins` |
|     219 | `org.apache.maven.plugins:maven-help-plugin@2.2`                     | http://svn.apache.org/viewvc/maven/plugins/tags/maven-help-plugin-2.2                                                    | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     220 | `org.apache.maven:maven-model@2.2.1`                                 | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-model                                                  | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     221 | `org.apache.maven:maven-plugin-api@2.2.1`                            | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-plugin-api                                             | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     222 | `org.apache.maven.plugin-tools:maven-plugin-tools-api@2.4.3`         | http://svn.apache.org/viewvc/maven/plugin-tools/tags/maven-plugin-tools-2.4.3/maven-plugin-tools-api                     | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     223 | `org.codehaus.plexus:plexus-container-default@1.0-alpha-9`           | scm:svn:svn://svn.codehaus.org/plexus/scm/trunk/plexus-containers/plexus-container-default/                              | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     224 | `org.codehaus.plexus:plexus-utils@1.5.7`                             | http://fisheye.codehaus.org/browse/plexus/plexus-utils/tags/plexus-utils-1.5.7                                           | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     225 | `com.thoughtworks.xstream:xstream@1.4.3`                             | http://fisheye.codehaus.org/browse/xstream/tags/XSTREAM_1_4_3/xstream                                                    | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     226 | `xmlpull:xmlpull@1.1.3.1`                                            | http://www.xmlpull.org                                                                                                   | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     227 | `xpp3:xpp3_min@1.1.4c`                                               | http://www.extreme.indiana.edu/viewcvs/~checkout~/XPP3/java/                                                             | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
|     228 | `commons-lang:commons-lang@2.4`                                      | http://svn.apache.org/viewvc/commons/proper/lang/trunk                                                                   | `org.apache.maven.plugins:maven-help-plugin@2.2`         | `resolve-plugins` |
</details>


---

Report created by [dirty-waters](https://github.com/chains-project/dirty-waters/).

Report created on 2025-05-13 09:27:03
- Tool version: 1dfb5543
- Project Name: awaitility/awaitility
- Project Version: awaitility-4.3.0
- Package Manager: maven
