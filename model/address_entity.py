from data_source import dataSource


class AddressEntity(dataSource.Model):
    __tablename__ = "address"

    id: dataSource.Column(dataSource.Integer, primary_key=True)
    int_number: dataSource.Column(dataSource.String(15), nullable=False)
    ext_number: dataSource.Column(dataSource.String(15), nullable=False)
    block: dataSource.Column(dataSource.String(15), nullable=False)
    number: dataSource.Column(dataSource.String(15), nullable=False)
    street: dataSource.Column(dataSource.String(75), nullable=False)
    colony: dataSource.Column(dataSource.String(75), nullable=False)
    municipality: dataSource.Column(dataSource.String(50), nullable=False)
    state: dataSource.Column(dataSource.String(50), nullable=False)
    country: dataSource.Column(dataSource.String(50), nullable=False)
    created_at: dataSource.Column(dataSource.DateTime, nullable=True, server_default=dataSource.func.current_timestamp())
    updated_at: dataSource.Column(dataSource.DateTime, nullable=True, server_onupdate=dataSource.func.current_timestamp())
    deleted: dataSource.Column(dataSource.DateTime, nullable=False, default=False)
    order_id = dataSource.Column(dataSource.Integer, dataSource.ForeignKey('order.id'), nullable=False)
