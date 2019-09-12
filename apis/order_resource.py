from flask_restplus import Resource, Namespace

api = Namespace('orders', description='Orders')


@api.route("/orders")
class OrderResource(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Internal Server Error'})
    def get(self):
        pass

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Internal Server Error'})
    def post(self):
        pass
