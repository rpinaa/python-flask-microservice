from schema import schema
from model.order_entity import OrderEntity
from model.address_entity import AddressEntity


class Order(schema.ModelSchema):
    class Meta:
        model = OrderEntity
        load_only = ('deleted',)
        dump_only = ('id',)
        address = schema.Nested(AddressEntity)

    __instance = None

    def __init__(self):
        if Order.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Order.__instance = self

    @staticmethod
    def get_instance() -> "Order":
        if Order.__instance is None:
            Order()
        return Order.__instance
