from flask import request
from flask_restplus import Resource, Namespace, fields

from entity.order_entity import OrderEntity
from domain.order import Order
from domain.address import Address
from domain.order_status import OrderStatus

api = Namespace('orders', description='Orders')

api.model('Order', {})
api.model('Paginate', {}) 


@api.route("/orders")
class OrderRestful(Resource):

    @api.doc(responses={201: 'OK', 400: 'Invalid Argument', 500: 'Internal Server Error'})
    @api.expect(
        api
        .parser()
        .add_argument('page', type=int, location='args', required=True)
        .add_argument('size', type=int, location='args', required=True)
    )
    def get(self):
        return Order.get_instance().dump(OrderEntity.query.all())

    @api.doc(responses={201: 'OK', 400: 'Invalid Argument', 500: 'Internal Server Error'})
    @api.expect(api.models.get('Order'))
    def post(self):
        order = Order.get_instance().load(request.get_json())

        order.status = OrderStatus.created
        order.deleted = False
        order.total = 0

        order.address.deleted = False

        address = Address.get_instance().load(order.address)

        order.save()
        address.save()

        return None, 201
