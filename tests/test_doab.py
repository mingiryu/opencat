from lxml import etree

from opencat.doab import NAMESPACES, Product


PATH = "tests/data/doab.xml"


def test_product():
    tree = etree.parse(PATH)
    root = tree.getroot()
    products = root.findall(".//onix:Product", namespaces=NAMESPACES)

    product = Product(products[0])
    data = product.to_dict()

    assert data == {
        "id": "OAPEN-ID_83a4d350-9332-418a-813e-093e5eb97a84",
        "doab": "1000320",
        "isbn": "9780190685515",
        "doi": "10.1093/oso/9780190685515.001.0001",
        "title": "Bulk Collection",
        "subtitle": "Systematic Government Access to Private-Sector Data",
        "contributors": [
            {
                "position": "1",
                "role": "editor",
                "keynames": "Cate",
                "forenames": "Fred H.",
            },
            {
                "position": "2",
                "role": "editor",
                "keynames": "Dempsey",
                "forenames": "James X.",
            },
        ],
        "description": "In June 2013, Edward Snowden revealed a secret US government program that collected records on every phone call made in the country. Further disclosures followed, detailing mass surveillance by the UK as well. Journalists and policymakers soon began discussing large-scale programs in other countries. Over two years before the Snowden leaks began, Cate and Dempsey had started researching systematic collection. Leading an initiative sponsored by The Privacy Projects, they commissioned a series of country reports, asking national experts to uncover what they could about government demands that telecommunications providers and other private-sector companies disclose information about their customers in bulk. Their initial research found disturbing indications of systematic access in countries around the world. These programs, often undertaken in the name of national security, were cloaked in secrecy and largely immune from oversight, posing serious threats to personal privacy. After the Snowden leaks, the project morphed into something more ambitious: an effort to explore what should be the rules for government access to data and how companies should respond to those demands within the framework of corporate responsibility. This volume concludes the nearly six-year project. It assembles 12 country reports, updated to reflect recent developments. One chapter presents both descriptive and normative frameworks for analyzing national surveillance laws. Others examine international law, human rights law, and oversight mechanisms. Still others explore the concept of accountability and the role of encryption in shaping the surveillance debate. In their conclusion, Cate and Dempsey offer recommendations for both government and industry.",
        "thumbnail": "https://directory.doabooks.org/bitstream/handle/20.500.12854/29877/bulkcollection.pdf.jpg?sequence=1",
        "publisher": "Oxford University Press",
        "year": "2017",
        "url": "https://library.oapen.org/bitstream/20.500.12657/29614/1/bulkcollection.pdf",
    }
