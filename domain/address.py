from schema import schema
from entity.address_entity import AddressEntity


class Address(schema.ModelSchema):
    class Meta:
        model = AddressEntity
        load_only = ("deleted",)
        dump_only = ("id",)
