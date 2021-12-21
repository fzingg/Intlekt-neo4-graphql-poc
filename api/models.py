from neomodel import (
    config,
    StructuredNode,
    StructuredRel,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
)


class Item(StructuredNode):
    __primarykey__ = "name"
    name = StringProperty(unique_index=True)


class isComposition(StructuredRel):
    attributes = StringProperty()


class IemlOntology(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_name = StringProperty()
    ontologies_nodes = RelationshipTo("IemlNode", "HAS_NODE")
    ontologies_components = RelationshipTo("IemlComponent", "HAS_COMPONENT")


class IemlNode(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_names = StringProperty()
    composition_tonodes = RelationshipTo(
        "IemlNode", "IS_COMPOSITION", model=isComposition
    )
    composition_tocomponents = RelationshipTo(
        "IemlComponent", "IS_COMPOSITION", model=isComposition
    )


class IemlComponent(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_names = StringProperty()
    composition_tonodes = RelationshipTo(
        "IemlNode", "IS_COMPOSITION", model=isComposition
    )
    composition_tocomponents = RelationshipTo(
        "IemlComponent", "IS_COMPOSITION", model=isComposition
    )
