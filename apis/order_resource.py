from flask_restplus import Resource, Namespace

from entity.order_entity import OrderEntity
from entity.address_entity import AddressEntity
from domain.order import Order

api = Namespace('orders', description='Orders')
order = Order()

@api.route("/orders")
class OrderResource(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Internal Server Error'})
    def get(self):
        pass

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Internal Server Error'})
    def post(self):
        pass
