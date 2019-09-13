from schema import schema
from entity.order_entity import OrderEntity
from entity.address_entity import AddressEntity


class Order(schema.ModelSchema):
    class Meta:
        model = OrderEntity
        load_only = ("deleted",)
        dump_only = ("id",)
        address = schema.Nested(AddressEntity)

    @staticmethod
    def get_instance() -> "Order":
        return Order()
