from schema import schema
from model.address_entity import AddressEntity


class Address(schema.ModelSchema):
    class Meta:
        model = AddressEntity
        load_only = ('deleted',)
        dump_only = ('id',)

    __instance = None

    def __init__(self):
        if Address.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Address.__instance = self

    @staticmethod
    def get_instance() -> "Address":
        if Address.__instance is None:
            Address()
        return Address.__instance
