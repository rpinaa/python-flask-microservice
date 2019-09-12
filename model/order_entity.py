from data_source import dataSource
from domain.order_status import OrderStatus


class OrderEntity(dataSource.Model):
    __tablename__ = "order"

    id: dataSource.Column(dataSource.Integer, primary_key=True)
    name: dataSource.Column(dataSource.String(100), nullable=False, unique=True)
    latitude: dataSource.Column(dataSource.Float, nullable=False)
    longitude: dataSource.Column(dataSource.Float, nullable=False)
    status: dataSource.Column(dataSource.Enum(OrderStatus), nullable=False)
    time_zone: dataSource.Column(dataSource.String, nullable=False)
    comments: dataSource.Column(dataSource.String, nullable=True)
    total: dataSource.Column(dataSource.BigInteger, nullable=True)
    created_at: dataSource.Column(dataSource.DateTime, nullable=True, server_default=dataSource.func.current_timestamp())
    updated_at: dataSource.Column(dataSource.DateTime, nullable=True, server_onupdate=dataSource.func.current_timestamp())
    scheduled_at: dataSource.Column(dataSource.DateTime, nullable=True)
    finished_at: dataSource.Column(dataSource.DateTime, nullable=True)
    deleted: dataSource.Column(dataSource.DateTime, nullable=False, default=False)

    @classmethod
    def save(cls) -> None:
        dataSource.session.add(cls)
        dataSource.session.add(cls.address)
        dataSource.session.commit()

    @classmethod   
    def delete(cls) -> None:
        dataSource.session.delete(cls)
        dataSource.session.commit()
