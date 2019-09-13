from flask_restplus import Api
from flask_restplus import fields

from .order_restful import OrderRestful

api = Api(version='0.1', title='Order API', description='A simple Order microservice to manage lifecycle',)

api.model('Paginate', {
    'page': fields.Integer(min=0, required=True),
    'size': fields.Integer(min=0, max=50, required=True),
})

api.model('Order', {
    'id': fields.Integer(required=False),
    'name': fields.String(max_length=100, required=True),
    'latitude': fields.Float(min=-90, max=90, required=True),
    'longitude': fields.Float(min=-180, max=180, required=True),
    'status': fields.String(enum=['CREATED', 'PENDING', 'DELIVERED', 'CLOSED'], required=False),
    'time_zone': fields.String(max_length=150, required=False),
    'comments': fields.String(max_length=100, required=True),
    'total': fields.Float(min=0, required=False),
    'updated_at': fields.DateTime(required=False),
    'scheduled_at': fields.DateTime(required=False),
    'finished_at': fields.DateTime(required=False)
})

api.add_resource(OrderRestful, "/orders")
