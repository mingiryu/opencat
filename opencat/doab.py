import polars as pl

from isbnlib import ean13
from enum import Enum
from lxml import etree


NAMESPACES = {"onix": "http://ns.editeur.org/onix/3.0/reference"}

SRC = "../data/doab.xml"
DST = "../data/doab.parquet"


def find_text(root, tag, namespaces=NAMESPACES):
    node = root.find(tag, namespaces=namespaces)
    if node is not None:
        return node.text


class ContributorRole(Enum):
    author = "A01"
    editor = "B01"
    other = "Z99"


class Contributor:
    def __init__(self, root):
        self.root = root

    @property
    def position(self):
        return find_text(self.root, ".//onix:SequenceNumber")

    @property
    def role(self):
        return ContributorRole(find_text(self.root, ".//onix:ContributorRole")).name

    @property
    def keynames(self):
        return find_text(self.root, ".//onix:KeyNames")

    @property
    def forenames(self):
        return find_text(self.root, ".//onix:NamesBeforeKey")

    def to_dict(self):
        # TODO: Split keynames when forenames isn't present.
        return dict(
            position=self.position,
            role=self.role,
            keynames=self.keynames,
            forenames=self.forenames,
        )


class Product:
    def __init__(self, root):
        self.root = root

    @property
    def id(self):
        return find_text(self.root, ".//onix:RecordReference")

    @property
    def doab(self):
        return find_text(
            self.root,
            './/onix:ProductIdentifier[onix:ProductIDType="01"]/onix:IDValue',
        )

    @property
    def isbn(self):
        # TODO: Standardize ISBN (9783937816098, 978-612-5069-6...)
        isbn = find_text(
            self.root,
            './/onix:ProductIdentifier[onix:ProductIDType="15"]/onix:IDValue',
        )
        if isbn is None:
            return None
        if isbn and (isbn := ean13(isbn)):
            return isbn

    @property
    def doi(self):
        doi = find_text(
            self.root,
            './/onix:ProductIdentifier[onix:ProductIDType="06"]/onix:IDValue',
        )
        if doi is None:
            return None
        if doi.startswith("http"):
            # XXX: Parse the URL
            return None
        return doi

    @property
    def title(self):
        return find_text(self.root, ".//onix:TitleText")

    @property
    def subtitle(self):
        return find_text(self.root, ".//onix:Subtitle")

    @property
    def contributors(self):
        return [
            Contributor(node).to_dict()
            for node in self.root.findall(".//onix:Contributor", namespaces=NAMESPACES)
        ]

    @property
    def description(self):
        return find_text(self.root, ".//onix:Text")

    @property
    def thumbnail(self):
        return find_text(self.root, ".//onix:ResourceLink")

    @property
    def publisher(self):
        return find_text(
            self.root,
            './/onix:Publisher[onix:PublishingRole="01"]/onix:PublisherName',
        )

    @property
    def year(self):
        return find_text(
            self.root,
            './/onix:PublishingDate[onix:PublishingDateRole="01"]/onix:Date',
        )

    @property
    def url(self):
        url = find_text(self.root, ".//onix:WebsiteLink")

        if url is None:
            return None
        if url.startswith("http"):
            return url

    def to_dict(self):
        return dict(
            id=self.id,
            doab=self.doab,
            isbn=self.isbn,
            doi=self.doi,
            title=self.title,
            subtitle=self.subtitle,
            contributors=self.contributors,
            description=self.description,
            thumbnail=self.thumbnail,
            publisher=self.publisher,
            year=self.year,
            url=self.url,
        )


def build():
    tree = etree.parse(SRC)
    root = tree.getroot()
    products = root.findall(".//onix:Product", namespaces=NAMESPACES)
    df = pl.DataFrame((Product(product).to_dict() for product in products))
    df.write_parquet(DST)


if __name__ == "__main__":
    build()
