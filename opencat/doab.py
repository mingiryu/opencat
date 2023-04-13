from enum import Enum


NAMESPACES = {"onix": "http://ns.editeur.org/onix/3.0/reference"}


def find_text(root, tag, namespaces=NAMESPACES):
    node = root.find(tag, namespaces=namespaces)
    if node is not None:
        return node.text


class ContributorRole(Enum):
    author = "A01"
    editor = "B01"


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
        return find_text(
            self.root, './/onix:ProductIdentifier[onix:ProductIDType="01"]/onix:IDValue'
        )

    @property
    def isbn(self):
        return find_text(
            self.root, './/onix:ProductIdentifier[onix:ProductIDType="15"]/onix:IDValue'
        )

    @property
    def doi(self):
        return find_text(
            self.root, './/onix:ProductIdentifier[onix:ProductIDType="06"]/onix:IDValue'
        )

    @property
    def title(self):
        return find_text(self.root, ".//onix:TitleText")

    @property
    def subtitle(self):
        return find_text(self.root, ".//onix:Subtitle")

    @property
    def contributors(self):
        for node in self.root.findall(".//onix:Contributor", namespaces=NAMESPACES):
            yield Contributor(node).to_dict()

    @property
    def description(self):
        return find_text(self.root, ".//onix:Text")

    @property
    def thumbnail(self):
        return find_text(self.root, ".//onix:ResourceLink")

    @property
    def publisher(self):
        return find_text(
            self.root, './/onix:Publisher[onix:PublishingRole="01"]/onix:PublisherName'
        )

    @property
    def year(self):
        return find_text(
            self.root, './/onix:PublishingDate[onix:PublishingDateRole="01"]/onix:Date'
        )

    @property
    def url(self):
        return find_text(self.root, ".//onix:WebsiteLink")

    def to_dict(self):
        return dict(
            id=self.id,
            isbn=self.isbn,
            doi=self.doi,
            title=self.title,
            subtitle=self.subtitle,
            contributors=tuple(self.contributors),
            description=self.description,
            publisher=self.publisher,
            year=self.year,
            url=self.url,
        )
