from neomodel import (
    config,
    StructuredNode,
    StructuredRel,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
)
from neomodel.relationship_manager import RelationshipFrom


class Item(StructuredNode):
    __primarykey__ = "name"
    name = StringProperty(unique_index=True)


class isComposition(StructuredRel):
    path = StringProperty()
    type = StringProperty()


class IemlOntology(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_name = StringProperty()
    ontologies_files = RelationshipTo("IemlFile", "HAS_FILE")
    ontologies_nodes = RelationshipTo("IemlNode", "HAS_NODE")
    ontologies_components = RelationshipTo("IemlComponent", "HAS_COMPONENT")
    ontologies_categories = RelationshipTo("IemlCategory", "HAS_CATEGORY")
    ontologies_inflections = RelationshipTo("IemlInflection", "HAS_INFLECTION")
    ontologies_auxiliaries = RelationshipTo("IemlAuxiliary", "HAS_AUXILIARY")
    ontologies_junctions = RelationshipTo("IemlJunction", "HAS_JUNCTION")


class IemlFile(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_name = StringProperty()


class IemlNode(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_names = StringProperty()
    file_tonodes = RelationshipFrom("IemlFile", "HAS_OBJECT")
    composition_tonodes = RelationshipTo(
        "IemlNode", "IS_COMPOSITION", model=isComposition
    )
    composition_tocomponents = RelationshipTo(
        "IemlComponent", "IS_COMPOSITION", model=isComposition
    )
    composition_tocategories = RelationshipTo(
        "IemlCategory", "IS_COMPOSITION", model=isComposition
    )
    composition_toinflections = RelationshipTo(
        "IemlInflection", "IS_COMPOSITION", model=isComposition
    )
    composition_toauxiliaries = RelationshipTo(
        "IemlAuxiliary", "IS_COMPOSITION", model=isComposition
    )
    composition_tojunctions = RelationshipTo(
        "IemlJunction", "IS_COMPOSITION", model=isComposition
    )


class IemlComponent(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_names = StringProperty()
    file_tocomponents = RelationshipFrom("IemlFile", "HAS_OBJECT")
    composition_tonodes = RelationshipTo(
        "IemlNode", "IS_COMPOSITION", model=isComposition
    )
    composition_tocomponents = RelationshipTo(
        "IemlComponent", "IS_COMPOSITION", model=isComposition
    )
    composition_tocategories = RelationshipTo(
        "IemlCategory", "IS_COMPOSITION", model=isComposition
    )
    composition_toinflections = RelationshipTo(
        "IemlInflection", "IS_COMPOSITION", model=isComposition
    )
    composition_toauxiliaries = RelationshipTo(
        "IemlAuxiliary", "IS_COMPOSITION", model=isComposition
    )
    composition_tojunctions = RelationshipTo(
        "IemlJunction", "IS_COMPOSITION", model=isComposition
    )


class IemlCategory(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_names = StringProperty()
    file_tocategories = RelationshipFrom("IemlFile", "HAS_OBJECT")
    composition_tonodes = RelationshipTo(
        "IemlNode", "IS_COMPOSITION", model=isComposition
    )
    composition_tocomponents = RelationshipTo(
        "IemlComponent", "IS_COMPOSITION", model=isComposition
    )
    composition_tocategories = RelationshipTo(
        "IemlCategory", "IS_COMPOSITION", model=isComposition
    )
    composition_toinflections = RelationshipTo(
        "IemlInflection", "IS_COMPOSITION", model=isComposition
    )
    composition_toauxiliaries = RelationshipTo(
        "IemlAuxiliary", "IS_COMPOSITION", model=isComposition
    )
    composition_tojunctions = RelationshipTo(
        "IemlJunction", "IS_COMPOSITION", model=isComposition
    )


class IemlInflection(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_names = StringProperty()
    file_toinflections = RelationshipFrom("IemlFile", "HAS_OBJECT")
    composition_tonodes = RelationshipTo(
        "IemlNode", "IS_COMPOSITION", model=isComposition
    )
    composition_tocomponents = RelationshipTo(
        "IemlComponent", "IS_COMPOSITION", model=isComposition
    )
    composition_tocategories = RelationshipTo(
        "IemlCategory", "IS_COMPOSITION", model=isComposition
    )
    composition_toinflections = RelationshipTo(
        "IemlInflection", "IS_COMPOSITION", model=isComposition
    )
    composition_toauxiliaries = RelationshipTo(
        "IemlAuxiliary", "IS_COMPOSITION", model=isComposition
    )
    composition_tojunctions = RelationshipTo(
        "IemlJunction", "IS_COMPOSITION", model=isComposition
    )


class IemlAuxiliary(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_names = StringProperty()
    file_toauxiliaries = RelationshipFrom("IemlFile", "HAS_OBJECT")
    composition_tonodes = RelationshipTo(
        "IemlNode", "IS_COMPOSITION", model=isComposition
    )
    composition_tocomponents = RelationshipTo(
        "IemlComponent", "IS_COMPOSITION", model=isComposition
    )
    composition_tocategories = RelationshipTo(
        "IemlCategory", "IS_COMPOSITION", model=isComposition
    )
    composition_toinflections = RelationshipTo(
        "IemlInflection", "IS_COMPOSITION", model=isComposition
    )
    composition_toauxiliaries = RelationshipTo(
        "IemlAuxiliary", "IS_COMPOSITION", model=isComposition
    )
    composition_tojunctions = RelationshipTo(
        "IemlJunction", "IS_COMPOSITION", model=isComposition
    )


class IemlJunction(StructuredNode):
    __primarykey__ = "uid"
    uid = UniqueIdProperty()
    ieml_id = IntegerProperty()
    ieml_names = StringProperty()
    file_tojunctions = RelationshipFrom("IemlFile", "HAS_OBJECT")
    composition_tonodes = RelationshipTo(
        "IemlNode", "IS_COMPOSITION", model=isComposition
    )
    composition_tocomponents = RelationshipTo(
        "IemlComponent", "IS_COMPOSITION", model=isComposition
    )
    composition_tocategories = RelationshipTo(
        "IemlCategory", "IS_COMPOSITION", model=isComposition
    )
    composition_toinflections = RelationshipTo(
        "IemlInflection", "IS_COMPOSITION", model=isComposition
    )
    composition_toauxiliaries = RelationshipTo(
        "IemlAuxiliary", "IS_COMPOSITION", model=isComposition
    )
    composition_tojunctions = RelationshipTo(
        "IemlJunction", "IS_COMPOSITION", model=isComposition
    )
