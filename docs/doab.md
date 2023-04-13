DOAB provides multiple file options, but they are not all the same. TSV only have `first_author` and CSV requires additional parsing for array fields such as authors. ONIX provides separate `keynames` and `forenames` with much more readable fields.

Resources
- [DOAB | Metadata for Libraries and Aggregators](https://www.doabooks.org/en/resources/metadata-harvesting-and-content-dissemination)
- [ONIX 3.0 for Google Play Books](https://support.google.com/books/partner/answer/6374180?hl=en&ref_topic=3273107&sjid=5388543654964950561-NA#)
- [ONIX codelist](http://www.onix-codelists.io/codelist)

Sample
```xml
<Product>
<RecordReference>OAPEN-ID_83a4d350-9332-418a-813e-093e5eb97a84</RecordReference>
<NotificationType>03</NotificationType>
<RecordSourceType>00</RecordSourceType>
<ProductIdentifier>
<ProductIDType>01</ProductIDType>
<IDTypeName>DOAB Library ID</IDTypeName>
<IDValue>1000320</IDValue>
</ProductIdentifier>
<ProductIdentifier>
<ProductIDType>15</ProductIDType>
<IDValue>9780190685515</IDValue>
</ProductIdentifier>
<ProductIdentifier>
<ProductIDType>06</ProductIDType>
<IDValue>10.1093/oso/9780190685515.001.0001</IDValue>
</ProductIdentifier>
<DescriptiveDetail>
<ProductComposition>00</ProductComposition>
<ProductForm>EB</ProductForm>
<ProductFormDetail>E100</ProductFormDetail>
<PrimaryContentType>10</PrimaryContentType>
<EpubLicense>
<EpubLicenseName>Open license</EpubLicenseName>
<EpubLicenseExpression>
<EpubLicenseExpressionType>02</EpubLicenseExpressionType>
<EpubLicenseExpressionLink>http://creativecommons.org/licenses/by-nc-nd/4.0/</EpubLicenseExpressionLink>
</EpubLicenseExpression>
</EpubLicense>
<TitleDetail>
<TitleType>01</TitleType>
<TitleElement>
<TitleElementLevel>01</TitleElementLevel>
<TitleText>Bulk Collection</TitleText>
<Subtitle>Systematic Government Access to Private-Sector Data</Subtitle>
</TitleElement>
</TitleDetail>
<Contributor>
<SequenceNumber>1</SequenceNumber>
<ContributorRole>B01</ContributorRole>
<NamesBeforeKey>Fred H.</NamesBeforeKey>
<KeyNames>Cate</KeyNames>
</Contributor>
<Contributor>
<SequenceNumber>2</SequenceNumber>
<ContributorRole>B01</ContributorRole>
<NamesBeforeKey>James X.</NamesBeforeKey>
<KeyNames>Dempsey</KeyNames>
</Contributor>
<Language>
<LanguageRole>01</LanguageRole>
<LanguageCode>eng</LanguageCode>
</Language>
<Extent>
<ExtentType>00</ExtentType>
<ExtentValue>504</ExtentValue>
<ExtentUnit>03</ExtentUnit>
</Extent>
<Subject>
<SubjectSchemeIdentifier>12</SubjectSchemeIdentifier>
<SubjectCode>JPQ</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>12</SubjectSchemeIdentifier>
<SubjectCode>LB</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>20</SubjectSchemeIdentifier>
<SubjectCode>government surveillance</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>20</SubjectSchemeIdentifier>
<SubjectCode>national security</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>20</SubjectSchemeIdentifier>
<SubjectCode>privacy</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>20</SubjectSchemeIdentifier>
<SubjectCode>human rights</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>20</SubjectSchemeIdentifier>
<SubjectCode>oversight</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>20</SubjectSchemeIdentifier>
<SubjectCode>international law</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>20</SubjectSchemeIdentifier>
<SubjectCode>corporate responsibility</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>20</SubjectSchemeIdentifier>
<SubjectCode>Personal data</SubjectCode>
</Subject>
<Subject>
<SubjectSchemeIdentifier>20</SubjectSchemeIdentifier>
<SubjectCode>United States</SubjectCode>
</Subject>
<Audience>
<AudienceCodeType>01</AudienceCodeType>
<AudienceCodeValue>06</AudienceCodeValue>
</Audience>
</DescriptiveDetail>
<CollateralDetail>
<TextContent>
<TextType>03</TextType>
<ContentAudience>03</ContentAudience>
<Text>In June 2013, Edward Snowden revealed a secret US government program that collected records on every phone call made in the country. Further disclosures followed, detailing mass surveillance by the UK as well. Journalists and policymakers soon began discussing large-scale programs in other countries. Over two years before the Snowden leaks began, Cate and Dempsey had started researching systematic collection. Leading an initiative sponsored by The Privacy Projects, they commissioned a series of country reports, asking national experts to uncover what they could about government demands that telecommunications providers and other private-sector companies disclose information about their customers in bulk. Their initial research found disturbing indications of systematic access in countries around the world. These programs, often undertaken in the name of national security, were cloaked in secrecy and largely immune from oversight, posing serious threats to personal privacy. After the Snowden leaks, the project morphed into something more ambitious: an effort to explore what should be the rules for government access to data and how companies should respond to those demands within the framework of corporate responsibility. This volume concludes the nearly six-year project. It assembles 12 country reports, updated to reflect recent developments. One chapter presents both descriptive and normative frameworks for analyzing national surveillance laws. Others examine international law, human rights law, and oversight mechanisms. Still others explore the concept of accountability and the role of encryption in shaping the surveillance debate. In their conclusion, Cate and Dempsey offer recommendations for both government and industry.</Text>
</TextContent>
<SupportingResource>
<ResourceContentType>01</ResourceContentType>
<ContentAudience>00</ContentAudience>
<ResourceMode>03</ResourceMode>
<ResourceVersion>
<ResourceForm>01</ResourceForm>
<ResourceLink>https://directory.doabooks.org/bitstream/handle/20.500.12854/29877/bulkcollection.pdf.jpg?sequence=1</ResourceLink>
</ResourceVersion>
</SupportingResource>
</CollateralDetail>
<PublishingDetail>
<Publisher>
<PublishingRole>01</PublishingRole>
<PublisherName>Oxford University Press</PublisherName>
</Publisher>
<Publisher>
<PublishingRole>16</PublishingRole>
<PublisherName>NOT AVAILABLE</PublisherName>
<Funding>
<FundingIdentifier>
<FundingIDType>01</FundingIDType>
<IDTypeName>programname</IDTypeName>
<IDValue>NOT AVAILABLE</IDValue>
</FundingIdentifier>
<FundingIdentifier>
<FundingIDType>01</FundingIDType>
<IDTypeName>projectname</IDTypeName>
<IDValue>NOT AVAILABLE</IDValue>
</FundingIdentifier>
<FundingIdentifier>
<FundingIDType>01</FundingIDType>
<IDTypeName>grantnumber</IDTypeName>
<IDValue>NOT AVAILABLE</IDValue>
</FundingIdentifier>
</Funding>
</Publisher>
<CityOfPublication>Oxford, UK</CityOfPublication>
<PublishingStatus>00</PublishingStatus>
<PublishingDate>
<PublishingDateRole>01</PublishingDateRole>
<Date dateformat="05">2017</Date>
</PublishingDate>
</PublishingDetail>
<RelatedMaterial>
<RelatedProduct>
<ProductRelationCode>06</ProductRelationCode>
<ProductIdentifier>
<ProductIDType>15</ProductIDType>
<IDValue>9780190685515</IDValue>
</ProductIdentifier>
</RelatedProduct>
</RelatedMaterial>
<ProductSupply>
<SupplyDetail>
<Supplier>
<SupplierRole>11</SupplierRole>
<SupplierName>DOAB Library</SupplierName>
<Website>
<WebsiteRole>05</WebsiteRole>
<WebsiteDescription>DOAB Library: download the title</WebsiteDescription>
<WebsiteLink>https://library.oapen.org/bitstream/20.500.12657/29614/1/bulkcollection.pdf</WebsiteLink>
</Website>
</Supplier>
<ProductAvailability>99</ProductAvailability>
<UnpricedItemType>04</UnpricedItemType>
</SupplyDetail>
<SupplyDetail>
<Supplier>
<SupplierRole>09</SupplierRole>
<SupplierName>Oxford University Press</SupplierName>
<Website>
<WebsiteRole>01</WebsiteRole>
<WebsiteDescription>Publisher's website: web shop</WebsiteDescription>
<WebsiteLink>NOT AVAILABLE</WebsiteLink>
</Website>
</Supplier>
<ProductAvailability>99</ProductAvailability>
<UnpricedItemType>04</UnpricedItemType>
</SupplyDetail>
</ProductSupply>
</Product>
```