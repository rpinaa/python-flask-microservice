from flask_restplus import Api

from .order_resource import OrderResource

api = Api(version='0.1', title='Order API', description='A simple Order microservice to manage lifecycle',)

api.add_resource(OrderResource, "/orders")
