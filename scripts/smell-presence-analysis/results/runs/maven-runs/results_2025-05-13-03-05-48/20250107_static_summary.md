
# Software Supply Chain Report of douglascrockford/JSON-java - 20250107

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
        

 ### Total packages in the supply chain: 307


:wrench: Packages with inaccessible commit SHA/tag (⚠️⚠️⚠️⚠️): 18

:heavy_exclamation_mark: Packages with no source code URL (⚠️⚠️⚠️): 11

:no_entry: Packages with repo URL that is 404 (⚠️⚠️⚠️): 7

:unlock: Packages with invalid code signature (⚠️⚠️⚠️): 0

:lock: Packages without code signature (⚠️⚠️): 41


### Fine grained information

:dolphin: For further information about software supply chain smells in your project, take a look at the following tables.

<details>
<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags(18)</summary>
    


| package_name                                                | sha_exists   | tag_version   | is_sha   | sha   | tag_url   | message                            |   status_code_for_sha | parent                                                  | command           |
|:------------------------------------------------------------|:-------------|:--------------|:---------|:------|:----------|:-----------------------------------|----------------------:|:--------------------------------------------------------|:------------------|
| `commons-io:commons-io@2.11.0`                              | False        | `2.11.0`      | False    |       |           | Tag 2.11.0 not found in the repo   |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.23.0`                | False        | `1.23.0`      | False    |       |           | Tag 1.23.0 not found in the repo   |                   404 | `org.apache.maven.plugins:maven-source-plugin@3.3.0`    | `resolve-plugins` |
| `org.osgi:org.osgi.util.tracker@1.5.4`                      | False        | `1.5.4`       | False    |       |           | Tag 1.5.4 not found in the repo    |                   404 | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `org.osgi:osgi.annotation@8.0.1`                            | False        | `8.0.1`       | False    |       |           | Tag 8.0.1 not found in the repo    |                   404 | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `org.osgi:org.osgi.util.function@1.2.0`                     | False        | `1.2.0`       | False    |       |           | Tag 1.2.0 not found in the repo    |                   404 | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `org.osgi:org.osgi.util.promise@1.2.0`                      | False        | `1.2.0`       | False    |       |           | Tag 1.2.0 not found in the repo    |                   404 | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.20`                  | False        | `1.20`        | False    |       |           | Tag 1.20 not found in the repo     |                   404 | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `org.apache.commons:commons-compress@1.21`                  | False        | `1.21`        | False    |       |           | Tag 1.21 not found in the repo     |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.sonatype.nexus:nexus-client-core@2.7.2-01`             | False        | `2.7.2-01`    | False    |       |           | Tag 2.7.2-01 not found in the repo |                   404 | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `org.sonatype.nexus.plugins:nexus-restlet1x-model@2.7.2-01` | False        | `2.7.2-01`    | False    |       |           | Tag 2.7.2-01 not found in the repo |                   404 | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-site-renderer@1.11.1`         | False        | `1.11.1`      | False    |       |           | Tag 1.11.1 not found in the repo   |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-decoration-model@1.11.1`      | False        | `1.11.1`      | False    |       |           | Tag 1.11.1 not found in the repo   |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.apache.maven.doxia:doxia-skin-model@1.11.1`            | False        | `1.11.1`      | False    |       |           | Tag 1.11.1 not found in the repo   |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.apache.commons:commons-lang3@3.12.0`                   | False        | `3.12.0`      | False    |       |           | Tag 3.12.0 not found in the repo   |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.apache.commons:commons-text@1.10.0`                    | False        | `1.10.0`      | False    |       |           | Tag 1.10.0 not found in the repo   |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.apache.httpcomponents:httpclient@4.5.14`               | False        | `4.5.14`      | False    |       |           | Tag 4.5.14 not found in the repo   |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.apache.httpcomponents:httpcore@4.4.16`                 | False        | `4.4.16`      | False    |       |           | Tag 4.4.16 not found in the repo   |                   404 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.hamcrest:hamcrest-core@1.3`                            | False        | `1.3`         | False    |       |           | Tag 1.3 not found in the repo      |                   404 | `junit:junit@4.13.2`                                    | `tree`            |
</details>

<details>
<summary>Source code links that could not be found(18)</summary>
    


|   index | package_name                                          | github_url                               | github_exists   | parent                                                  | command           |
|--------:|:------------------------------------------------------|:-----------------------------------------|:----------------|:--------------------------------------------------------|:------------------|
|       1 | `org.osgi:org.osgi.compendium@4.2.0`                  | No_repo_info_found                       |                 | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
|       2 | `org.sonatype.plexus:plexus-sec-dispatcher@1.3`       | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
|       3 | `org.sonatype.plexus:plexus-cipher@1.4`               | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
|       4 | `oro:oro@2.0.8`                                       | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
|       5 | `org.sonatype.plexus:plexus-sec-dispatcher@1.4`       | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-gpg-plugin@1.6`         | `resolve-plugins` |
|       6 | `javax.servlet:servlet-api@2.5`                       | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
|       7 | `commons-beanutils:commons-beanutils@1.7.0`           | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
|       8 | `dom4j:dom4j@1.1`                                     | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
|       9 | `sslext:sslext@1.2-0`                                 | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
|      10 | `antlr:antlr@2.7.2`                                   | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
|      11 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0` | No_repo_info_found                       |                 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
|      12 | `org.iq80.snappy:snappy@0.4`                          | https://github.com/dain/snapy            | False           | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
|      13 | `org.eclipse.aether:aether-util@1.1.0`                | https://github.com/jvanzyl/aether-core   | False           | `org.moditect:moditect-maven-plugin@1.0.0.Final`        | `resolve-plugins` |
|      14 | `org.eclipse.aether:aether-api@1.1.0`                 | https://github.com/jvanzyl/aether-core   | False           | `org.moditect:moditect-maven-plugin@1.0.0.Final`        | `resolve-plugins` |
|      15 | `org.slf4j:slf4j-api@1.7.5`                           | https://github.com/ceki/slf4j            | False           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
|      16 | `org.slf4j:jcl-over-slf4j@1.7.5`                      | https://github.com/ceki/slf4j            | False           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
|      17 | `org.sonatype.sisu:sisu-charger@1.1`                  | https://github.com/sonatype/sisu-charger | False           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
|      18 | `org.slf4j:slf4j-simple@1.7.5`                        | https://github.com/ceki/slf4j            | False           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
</details>

The package manager (maven) does not support checking for provenance.

All packages have valid code signature.

<details>
<summary>List of packages without code signature(41)</summary>
    


| package_name                                                        | signature_present   | parent                                                  | command           |
|:--------------------------------------------------------------------|:--------------------|:--------------------------------------------------------|:------------------|
| `javax.inject:javax.inject@1`                                       | False               | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.osgi:org.osgi.compendium@4.2.0`                                | False               | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `javax.annotation:jsr250-api@1.0`                                   | False               | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `com.google.code.findbugs:jsr305@1.3.9`                             | False               | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `aopalliance:aopalliance@1.0`                                       | False               | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `org.codehaus.plexus:plexus-i18n@1.0-beta-7`                        | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `org.codehaus.plexus:plexus-container-default@1.0-alpha-30`         | False               | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `junit:junit@3.8.1`                                                 | False               | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `org.codehaus.plexus:plexus-velocity@1.1.7`                         | False               | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `org.apache.velocity:velocity@1.5`                                  | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `commons-lang:commons-lang@2.1`                                     | False               | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `oro:oro@2.0.8`                                                     | False               | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `commons-collections:commons-collections@3.2`                       | False               | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `org.jdom:jdom@1.1`                                                 | False               | `org.apache.felix:maven-bundle-plugin@5.1.9`            | `resolve-plugins` |
| `com.google.code.findbugs:jsr305@2.0.1`                             | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `xmlpull:xmlpull@1.1.3.1`                                           | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `xpp3:xpp3_min@1.1.4c`                                              | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `javax.ws.rs:jsr311-api@1.1.1`                                      | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `javax.validation:validation-api@1.1.0.Final`                       | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `org.codehaus.jackson:jackson-core-asl@1.9.2`                       | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `org.codehaus.jackson:jackson-mapper-asl@1.9.2`                     | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `org.codehaus.jackson:jackson-jaxrs@1.9.2`                          | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `org.codehaus.jackson:jackson-xc@1.9.2`                             | False               | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3` | `resolve-plugins` |
| `xerces:xercesImpl@2.9.1`                                           | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `xml-apis:xml-apis@1.3.04`                                          | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `commons-codec:commons-codec@1.3`                                   | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `javax.servlet:servlet-api@2.5`                                     | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `commons-beanutils:commons-beanutils@1.7.0`                         | False               | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `commons-digester:commons-digester@1.8`                             | False               | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `commons-chain:commons-chain@1.1`                                   | False               | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `dom4j:dom4j@1.1`                                                   | False               | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
| `sslext:sslext@1.2-0`                                               | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `antlr:antlr@2.7.2`                                                 | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `org.codehaus.plexus:plexus-velocity@1.1.8`                         | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `org.codehaus.plexus:plexus-utils@1.5.10`                           | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `org.mortbay.jetty:servlet-api@2.5-20081211`                        | False               | `org.apache.maven.plugins:maven-site-plugin@3.3`        | `resolve-plugins` |
| `backport-util-concurrent:backport-util-concurrent@3.1`             | False               | `org.apache.maven.plugins:maven-gpg-plugin@1.6`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-interpolation@1.11`                     | False               | `org.apache.maven.plugins:maven-gpg-plugin@1.6`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-container-default@1.0-alpha-9-stable-1` | False               | `org.apache.maven.plugins:maven-gpg-plugin@1.6`         | `resolve-plugins` |
| `classworlds:classworlds@1.1-alpha-2`                               | False               | `org.apache.maven.plugins:maven-gpg-plugin@1.6`         | `resolve-plugins` |
| `org.codehaus.plexus:plexus-i18n@1.0-beta-10`                       | False               | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`   | `resolve-plugins` |
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
    
- Source code repo is not hosted on GitHub:  152

    This could be due, for example, to the package being hosted on a different platform.

    This does not mean that the source code URL is invalid.

    However, for non-GitHub repositories, not all checks can currently be performed.

|   index | package_name                                                        | github_url                                                                                                               | parent                                                         | command           |
|--------:|:--------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:------------------|
|       1 | `javax.inject:javax.inject@1`                                       | http://code.google.com/p/atinject/source/checkout                                                                        | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|       2 | `org.tukaani:xz@1.9`                                                | https://git.tukaani.org/?p=xz-java.git                                                                                   | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|       3 | `org.osgi:org.osgi.core@6.0.0`                                      | private                                                                                                                  | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|       4 | `org.osgi:org.osgi.dto@1.0.0`                                       | https://osgi.org/git/build.git                                                                                           | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|       5 | `org.osgi:org.osgi.resource@1.0.0`                                  | https://osgi.org/git/build.git                                                                                           | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|       6 | `org.osgi:org.osgi.framework@1.8.0`                                 | https://osgi.org/git/build.git                                                                                           | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|       7 | `org.osgi:org.osgi.service.log@1.3.0`                               | https://osgi.org/git/build.git                                                                                           | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|       8 | `org.osgi:org.osgi.service.repository@1.1.0`                        | https://osgi.org/git/build.git                                                                                           | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|       9 | `org.apache.felix:org.apache.felix.bundlerepository@1.6.6`          | http://svn.apache.org/repos/asf/felix/releases/org.apache.felix.bundlerepository-1.6.6                                   | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      10 | `org.easymock:easymock@2.4`                                         | http://easymock.cvs.sourceforge.net/easymock/                                                                            | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      11 | `org.apache.felix:org.apache.felix.utils@1.6.0`                     | scm:svn:https://svn.apache.org/repos/asf/felix/releases/org.apache.felix.utils-1.6.0                                     | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      12 | `org.apache.maven.reporting:maven-reporting-api@3.0`                | http://svn.apache.org/viewvc/maven/shared/tags/maven-reporting-api-3.0                                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      13 | `org.eclipse.aether:aether-spi@0.9.0.M2`                            | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-spi/                                                         | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|      14 | `org.eclipse.aether:aether-impl@0.9.0.M2`                           | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-impl/                                                        | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      15 | `org.eclipse.aether:aether-api@0.9.0.M2`                            | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-api/                                                         | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      16 | `org.eclipse.sisu:org.eclipse.sisu.plexus@0.0.0.M5`                 | http://git.eclipse.org/c/sisu/org.eclipse.sisu.plexus.git/tree/org.eclipse.sisu.plexus/                                  | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      17 | `javax.enterprise:cdi-api@1.0`                                      | http://fisheye.jboss.org/browse/Weld/api/tags/1.0/build/tags/weld-parent-6/weld-api-bom/weld-api-parent/cdi-api          | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      18 | `javax.annotation:jsr250-api@1.0`                                   | http://jcp.org/aboutJava/communityprocess/final/jsr250/index.html                                                        | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      19 | `com.google.guava:guava@10.0.1`                                     | http://code.google.com/p/guava-libraries/source/browse/guava                                                             | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      20 | `com.google.code.findbugs:jsr305@1.3.9`                             | http://findbugs.googlecode.com/svn/trunk/                                                                                | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      21 | `aopalliance:aopalliance@1.0`                                       | http://aopalliance.sourceforge.net                                                                                       | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      22 | `org.eclipse.sisu:org.eclipse.sisu.inject@0.0.0.M5`                 | http://git.eclipse.org/c/sisu/org.eclipse.sisu.inject.git/tree/org.eclipse.sisu.inject/                                  | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      23 | `org.apache.maven.shared:maven-dependency-tree@3.0`                 | http://svn.apache.org/viewvc/maven/shared/tags/maven-dependency-tree-3.0                                                 | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      24 | `org.eclipse.aether:aether-util@0.9.0.M2`                           | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-util/                                                        | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      25 | `org.sonatype.plexus:plexus-build-api@0.0.7`                        | http://svn.sonatype.org/spice/tags/plexus-build-api-0.0.7                                                                | `org.apache.maven.plugins:maven-resources-plugin@4.0.0-beta-1` | `resolve-plugins` |
|      26 | `org.apache.maven.doxia:doxia-sink-api@1.0`                         | https://svn.apache.org/viewvc/maven/doxia/doxia/tags/doxia-1.0/doxia-sink-api                                            | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      27 | `org.apache.maven.doxia:doxia-site-renderer@1.0`                    | https://svn.apache.org/viewvc/maven/doxia/doxia-sitetools/tags/doxia-sitetools-1.0/doxia-site-renderer                   | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      28 | `org.apache.maven.doxia:doxia-core@1.0`                             | https://svn.apache.org/viewvc/maven/doxia/doxia/tags/doxia-1.0/doxia-core                                                | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      29 | `org.codehaus.plexus:plexus-i18n@1.0-beta-7`                        | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-i18n-1.0-beta-7                                  | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      30 | `org.codehaus.plexus:plexus-container-default@1.0-alpha-30`         | http://fisheye.codehaus.org/browse/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-30/plexus-container-default | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|      31 | `junit:junit@3.8.1`                                                 | http://junit.cvs.sourceforge.net/junit/                                                                                  | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|      32 | `org.codehaus.plexus:plexus-velocity@1.1.7`                         | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-velocity-1.1.7                                   | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      33 | `org.apache.velocity:velocity@1.5`                                  | http://svn.apache.org/viewvc/velocity/engine/tags/Velocity_1.5                                                           | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      34 | `commons-lang:commons-lang@2.1`                                     | http://svn.apache.org/viewcvs/jakarta/commons/proper/${pom.artifactId.substring(8)}/trunk                                | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      35 | `org.apache.maven.doxia:doxia-decoration-model@1.0`                 | https://svn.apache.org/viewvc/maven/doxia/doxia-sitetools/tags/doxia-sitetools-1.0/doxia-decoration-model                | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      36 | `commons-collections:commons-collections@3.2`                       | http://svn.apache.org/repos/asf/jakarta/commons/proper/collections/trunk                                                 | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      37 | `org.apache.maven.doxia:doxia-module-apt@1.0`                       | https://svn.apache.org/viewvc/maven/doxia/doxia/tags/doxia-1.0/doxia-modules/doxia-module-apt                            | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      38 | `org.apache.maven.doxia:doxia-module-fml@1.0`                       | https://svn.apache.org/viewvc/maven/doxia/doxia/tags/doxia-1.0/doxia-modules/doxia-module-fml                            | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      39 | `org.apache.maven.doxia:doxia-module-xdoc@1.0`                      | https://svn.apache.org/viewvc/maven/doxia/doxia/tags/doxia-1.0/doxia-modules/doxia-module-xdoc                           | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      40 | `org.apache.maven.doxia:doxia-module-xhtml@1.0`                     | https://svn.apache.org/viewvc/maven/doxia/doxia/tags/doxia-1.0/doxia-modules/doxia-module-xhtml                          | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      41 | `org.jdom:jdom@1.1`                                                 | scm:cvs:pserver:anonymous@cvs.jdom.org:/home/cvspublic:jdom                                                              | `org.apache.felix:maven-bundle-plugin@5.1.9`                   | `resolve-plugins` |
|      42 | `org.apache.maven.shared:maven-shared-incremental@1.1`              | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-incremental-1.1                                              | `org.apache.maven.plugins:maven-compiler-plugin@3.11.0`        | `resolve-plugins` |
|      43 | `org.codehaus.plexus:plexus-component-annotations@1.5.5`            | http://fisheye.codehaus.org/browse/plexus/plexus-containers/tags/plexus-containers-1.5.5/plexus-component-annotations    | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      44 | `org.ow2.asm:asm@9.4`                                               | https://gitlab.ow2.org/asm/asm/                                                                                          | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|      45 | `org.apache.maven.plugins:maven-clean-plugin@2.5`                   | http://svn.apache.org/viewvc/maven/plugins/tags/maven-clean-plugin-2.5                                                   | `org.apache.maven.plugins:maven-clean-plugin@2.5`              | `resolve-plugins` |
|      46 | `org.apache.maven:maven-plugin-api@2.0.6`                           | https://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.6/maven-plugin-api                                      | `org.apache.maven.plugins:maven-clean-plugin@2.5`              | `resolve-plugins` |
|      47 | `com.google.guava:guava@14.0.1`                                     | http://code.google.com/p/guava-libraries/source/browse/guava                                                             | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      48 | `org.apache.maven:maven-model@3.0.4`                                | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0.4/maven-model                                                  | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      49 | `com.google.code.findbugs:jsr305@2.0.1`                             | http://findbugs.googlecode.com/svn/trunk/                                                                                | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      50 | `com.intellij:annotations@9.0.4`                                    | http://git.jetbrains.org/idea/community.git                                                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      51 | `com.thoughtworks.xstream:xstream@1.4.5`                            | http://fisheye.codehaus.org/browse/xstream/tags/XSTREAM_1_4_5/xstream                                                    | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      52 | `xmlpull:xmlpull@1.1.3.1`                                           | http://www.xmlpull.org                                                                                                   | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      53 | `xpp3:xpp3_min@1.1.4c`                                              | http://www.extreme.indiana.edu/viewcvs/~checkout~/XPP3/java/                                                             | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      54 | `commons-lang:commons-lang@2.6`                                     | http://svn.apache.org/viewvc/commons/proper/lang/branches/LANG_2_X                                                       | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      55 | `commons-beanutils:commons-beanutils-core@1.8.3`                    | http://svn.apache.org/viewvc/maven/pom/tags/apache-4/commons-beanutils-core                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      56 | `javax.ws.rs:jsr311-api@1.1.1`                                      | https://jsr311.dev.java.net                                                                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      57 | `com.sun.jersey:jersey-core@1.17.1`                                 | http://java.net/projects/jersey/sources/svn/show/trunk/jersey/jersey-core                                                | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      58 | `com.sun.jersey:jersey-client@1.17.1`                               | http://java.net/projects/jersey/sources/svn/show/trunk/jersey/jersey-client                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      59 | `com.sun.jersey:jersey-json@1.17.1`                                 | http://java.net/projects/jersey/sources/svn/show/trunk/jersey/jersey-json                                                | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      60 | `com.sun.xml.bind:jaxb-impl@2.2.3-1`                                | https://svn.java.net/svn/jaxb~version2/jaxb-ri                                                                           | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      61 | `org.codehaus.jackson:jackson-core-asl@1.9.2`                       | http://jackson.codehaus.org                                                                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      62 | `org.codehaus.jackson:jackson-mapper-asl@1.9.2`                     | http://jackson.codehaus.org                                                                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      63 | `org.codehaus.jackson:jackson-jaxrs@1.9.2`                          | http://jackson.codehaus.org                                                                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      64 | `org.codehaus.jackson:jackson-xc@1.9.2`                             | http://jackson.codehaus.org                                                                                              | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      65 | `com.sun.jersey.contribs:jersey-apache-client4@1.17.1`              | http://java.net/projects/jersey/sources/svn/show/trunk/jersey/jersey-contribs/jersey-apache-client4                      | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      66 | `org.apache.httpcomponents:httpclient@4.3.5`                        | https://svn.apache.org/repos/asf/httpcomponents/httpclient/tags/4.3.5/httpclient                                         | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      67 | `commons-codec:commons-codec@1.6`                                   | http://svn.apache.org/viewvc/commons/proper/codec/trunk                                                                  | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      68 | `org.apache.httpcomponents:httpcore@4.3.2`                          | https://svn.apache.org/repos/asf/httpcomponents/httpcore/tags/4.3.2/httpcore                                             | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      69 | `com.google.protobuf:protobuf-java@2.4.1`                           | http://code.google.com/p/protobuf/source/browse                                                                          | `org.sonatype.plugins:nexus-staging-maven-plugin@1.6.3`        | `resolve-plugins` |
|      70 | `org.apache.maven.plugins:maven-site-plugin@3.3`                    | http://svn.apache.org/viewvc/maven/plugins/tags/maven-site-plugin-3.3                                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      71 | `org.apache.maven.reporting:maven-reporting-exec@1.1`               | http://svn.apache.org/viewvc/maven/shared/tags/maven-reporting-exec-1.1                                                  | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      72 | `org.apache.maven:maven-artifact@3.0`                               | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-artifact                                                 | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      73 | `org.apache.maven.shared:maven-shared-utils@0.3`                    | http://svn.apache.org/viewvc/maven/shared/tags/maven-shared-utils-0.3                                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      74 | `org.apache.maven:maven-core@3.0`                                   | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-core                                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      75 | `org.apache.maven:maven-repository-metadata@3.0`                    | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-repository-metadata                                      | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      76 | `org.apache.maven:maven-model-builder@3.0`                          | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-model-builder                                            | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      77 | `org.apache.maven:maven-aether-provider@3.0`                        | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-aether-provider                                          | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      78 | `org.codehaus.plexus:plexus-interpolation@1.14`                     | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-interpolation-1.14                               | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      79 | `org.codehaus.plexus:plexus-classworlds@2.2.3`                      | http://fisheye.codehaus.org/browse/plexus/plexus-classworlds/tags/plexus-classworlds-2.2.3                               | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      80 | `org.apache.maven:maven-model@3.0`                                  | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-model                                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      81 | `org.apache.maven:maven-plugin-api@3.0`                             | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-plugin-api                                               | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      82 | `org.apache.maven:maven-settings@3.0`                               | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-settings                                                 | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      83 | `org.apache.maven:maven-settings-builder@3.0`                       | http://svn.apache.org/viewvc/maven/maven-3/tags/maven-3.0/maven-settings-builder                                         | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      84 | `org.apache.maven:maven-archiver@2.4.2`                             | http://svn.apache.org/viewvc/maven/shared/tags/maven-archiver-2.4.2                                                      | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      85 | `org.apache.maven.doxia:doxia-sink-api@1.4`                         | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-sink-api                                        | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      86 | `org.apache.maven.doxia:doxia-logging-api@1.4`                      | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-logging-api                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      87 | `org.apache.maven.doxia:doxia-core@1.4`                             | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-core                                            | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      88 | `xerces:xercesImpl@2.9.1`                                           | http://svn.apache.org/viewvc/maven/pom/tags/apache-4/xercesImpl                                                          | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      89 | `xml-apis:xml-apis@1.3.04`                                          | http://svn.apache.org/viewvc/xml/commons/tags/xml-commons-external-1_3_04/                                               | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      90 | `org.apache.httpcomponents:httpclient@4.0.2`                        | https://svn.apache.org/repos/asf/httpcomponents/httpclient/tags/4.0.2/httpclient                                         | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      91 | `commons-logging:commons-logging@1.1.1`                             | http://svn.apache.org/repos/asf/commons/proper/logging/tags/commons-logging-1.1.1                                        | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      92 | `commons-codec:commons-codec@1.3`                                   | http://cvs.apache.org/viewcvs/jakarta-commons/codec/                                                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      93 | `org.apache.httpcomponents:httpcore@4.0.1`                          | http://svn.apache.org/repos/asf/httpcomponents/httpcore/tags/4.0.1/httpcore                                              | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      94 | `org.apache.maven.doxia:doxia-module-xhtml@1.4`                     | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-xhtml                      | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      95 | `org.apache.maven.doxia:doxia-module-apt@1.4`                       | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-apt                        | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      96 | `org.apache.maven.doxia:doxia-module-xdoc@1.4`                      | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-xdoc                       | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      97 | `org.apache.maven.doxia:doxia-module-fml@1.4`                       | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-fml                        | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      98 | `org.apache.maven.doxia:doxia-module-markdown@1.4`                  | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia/tags/doxia-1.4/doxia-modules/doxia-module-markdown                   | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|      99 | `org.ow2.asm:asm@4.1`                                               | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm/                                                        | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     100 | `org.ow2.asm:asm-tree@4.1`                                          | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm-tree/                                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     101 | `org.ow2.asm:asm-analysis@4.1`                                      | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm-analysis/                                               | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     102 | `org.ow2.asm:asm-util@4.1`                                          | http://svn.forge.objectweb.org/cgi-bin/viewcvs.cgi/asm/trunk/asm-util/                                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     103 | `org.apache.maven.doxia:doxia-decoration-model@1.4`                 | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia-sitetools/tags/doxia-sitetools-1.4/doxia-decoration-model            | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     104 | `org.apache.maven.doxia:doxia-site-renderer@1.4`                    | http://svn.apache.org/viewcvs.cgi/maven/doxia/doxia-sitetools/tags/doxia-sitetools-1.4/doxia-site-renderer               | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     105 | `org.apache.velocity:velocity-tools@2.0`                            | http://svn.apache.org/repos/asf/velocity/tools/trunk                                                                     | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     106 | `commons-digester:commons-digester@1.8`                             | http://svn.apache.org/repos/asf/jakarta/commons/proper/digester/trunk                                                    | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     107 | `commons-chain:commons-chain@1.1`                                   | http://svn.apache.org/viewcvs.cgi                                                                                        | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     108 | `commons-validator:commons-validator@1.3.1`                         | http://svn.apache.org/viewvc                                                                                             | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     109 | `org.apache.struts:struts-core@1.3.8`                               | http://svn.apache.org/repos/asf/struts/struts1/trunk/core                                                                | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     110 | `org.apache.struts:struts-taglib@1.3.8`                             | http://svn.apache.org/repos/asf/struts/struts1/trunk/taglib/                                                             | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     111 | `org.apache.struts:struts-tiles@1.3.8`                              | http://svn.apache.org/repos/asf/struts/struts1/trunk/tiles/                                                              | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     112 | `commons-collections:commons-collections@3.2.1`                     | http://svn.apache.org/viewvc/commons/proper/collections/trunk                                                            | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     113 | `org.apache.maven.doxia:doxia-integration-tools@1.5`                | http://svn.apache.org/viewvc/maven/doxia/doxia-tools/tags/doxia-integration-tools-1.5                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     114 | `org.apache.maven.wagon:wagon-provider-api@1.0`                     | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0/wagon-provider-api                                               | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     115 | `org.codehaus.plexus:plexus-archiver@1.0`                           | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-archiver-1.0                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     116 | `org.codehaus.plexus:plexus-io@1.0`                                 | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-io-1.0                                           | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     117 | `org.codehaus.plexus:plexus-velocity@1.1.8`                         | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-velocity-1.1.8                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     118 | `org.codehaus.plexus:plexus-utils@1.5.10`                           | http://fisheye.codehaus.org/browse/plexus/plexus-utils/tags/plexus-utils-1.5.10                                          | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     119 | `org.mortbay.jetty:jetty@6.1.25`                                    | http://fisheye.codehaus.org/viewrep/jetty/modules/jetty/                                                                 | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     120 | `org.mortbay.jetty:servlet-api@2.5-20081211`                        | scm:svn:https://svn.codehaus.org/jetty/servlet-api/tags/servlet-api-2.5-20081211                                         | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     121 | `org.mortbay.jetty:jetty-util@6.1.25`                               | http://fisheye.codehaus.org/viewrep/jetty/jetty-util/                                                                    | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     122 | `commons-lang:commons-lang@2.5`                                     | http://svn.apache.org/viewvc/commons/proper/lang/trunk                                                                   | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     123 | `commons-io:commons-io@1.4`                                         | http://svn.apache.org/viewvc/commons/proper/io/trunk                                                                     | `org.apache.maven.plugins:maven-site-plugin@3.3`               | `resolve-plugins` |
|     124 | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                     | http://svn.apache.org/viewvc/maven/plugins/tags/maven-gpg-plugin-1.6                                                     | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     125 | `org.apache.maven:maven-plugin-api@2.2.1`                           | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-plugin-api                                             | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     126 | `org.apache.maven:maven-project@2.2.1`                              | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-project                                                | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     127 | `org.apache.maven:maven-settings@2.2.1`                             | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-settings                                               | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     128 | `org.apache.maven:maven-profile@2.2.1`                              | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-profile                                                | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     129 | `org.apache.maven:maven-artifact-manager@2.2.1`                     | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-artifact-manager                                       | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     130 | `org.apache.maven.wagon:wagon-provider-api@1.0-beta-6`              | http://svn.apache.org/viewvc/maven/wagon/tags/wagon-1.0-beta-6/wagon-provider-api                                        | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     131 | `backport-util-concurrent:backport-util-concurrent@3.1`             | svn://dcl.mathcs.emory.edu/software/harness2/trunk/util/backport-util-concurrent/                                        | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     132 | `org.apache.maven:maven-plugin-registry@2.2.1`                      | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-plugin-registry                                        | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     133 | `org.codehaus.plexus:plexus-interpolation@1.11`                     | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-interpolation-1.11                               | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     134 | `org.codehaus.plexus:plexus-container-default@1.0-alpha-9-stable-1` | scm:svn:svn://svn.codehaus.org/plexus/scm/trunk/plexus-containers/plexus-container-default/                              | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     135 | `classworlds:classworlds@1.1-alpha-2`                               | http://cvs.classworlds.codehaus.org/                                                                                     | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     136 | `org.apache.maven:maven-artifact@2.2.1`                             | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-artifact                                               | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     137 | `org.apache.maven:maven-repository-metadata@2.2.1`                  | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-repository-metadata                                    | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     138 | `org.apache.maven:maven-model@2.2.1`                                | http://svn.apache.org/viewvc/maven/maven-2/tags/maven-2.2.1/maven-model                                                  | `org.apache.maven.plugins:maven-gpg-plugin@1.6`                | `resolve-plugins` |
|     139 | `org.eclipse.aether:aether-impl@1.0.0.v20140518`                    | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-impl/                                                        | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     140 | `org.eclipse.aether:aether-api@1.0.0.v20140518`                     | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-api/                                                         | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     141 | `org.eclipse.aether:aether-util@1.0.0.v20140518`                    | http://git.eclipse.org/c/aether/aether-core.git/tree/aether-util/                                                        | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     142 | `org.eclipse.sisu:org.eclipse.sisu.plexus@0.3.5`                    | http://git.eclipse.org/c/sisu/org.eclipse.sisu.plexus.git/tree/org.eclipse.sisu.plexus/                                  | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     143 | `javax.annotation:javax.annotation-api@1.2`                         | http://java.net/projects/glassfish/sources/svn/show/tags/javax.annotation-api-1.2                                        | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     144 | `org.eclipse.sisu:org.eclipse.sisu.inject@0.3.5`                    | http://git.eclipse.org/c/sisu/org.eclipse.sisu.inject.git/tree/org.eclipse.sisu.inject/                                  | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     145 | `org.codehaus.plexus:plexus-i18n@1.0-beta-10`                       | http://fisheye.codehaus.org/browse/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10                                 | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     146 | `org.apache.velocity:velocity@1.7`                                  | http://svn.apache.org/viewvc/velocity/engine/trunk                                                                       | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     147 | `commons-lang:commons-lang@2.4`                                     | http://svn.apache.org/viewvc/commons/proper/lang/trunk                                                                   | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     148 | `commons-collections:commons-collections@3.2.2`                     | http://svn.apache.org/viewvc/commons/proper/collections/trunk                                                            | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     149 | `commons-logging:commons-logging@1.2`                               | http://svn.apache.org/repos/asf/commons/proper/logging/trunk                                                             | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     150 | `commons-codec:commons-codec@1.11`                                  | http://svn.apache.org/viewvc/commons/proper/codec/trunk                                                                  | `org.apache.maven.plugins:maven-javadoc-plugin@3.5.0`          | `resolve-plugins` |
|     151 | `org.ow2.asm:asm@9.7.1`                                             | https://gitlab.ow2.org/asm/asm/                                                                                          | `org.apache.maven.plugins:maven-surefire-plugin@3.5.3`         | `resolve-plugins` |
|     152 | `org.ow2.asm:asm@9.3`                                               | https://gitlab.ow2.org/asm/asm/                                                                                          | `net.minidev:accessors-smart@2.5.0`                            | `resolve-plugins` |
</details>


---

Report created by [dirty-waters](https://github.com/chains-project/dirty-waters/).

Report created on 2025-05-13 03:21:18
- Tool version: 1dfb5543
- Project Name: douglascrockford/JSON-java
- Project Version: 20250107
- Package Manager: maven
