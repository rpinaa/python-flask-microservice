from db import db
from domain.order_status import OrderStatus


class OrderEntity(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(OrderStatus), nullable=False)
    time_zone = db.Column(db.String, nullable=False)
    comments = db.Column(db.String, nullable=True)
    total = db.Column(db.BigInteger, nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True, server_onupdate=db.func.current_timestamp())
    scheduled_at = db.Column(db.DateTime, nullable=True)
    finished_at = db.Column(db.DateTime, nullable=True)
    deleted = db.Column(db.DateTime, nullable=False, default=False)

    @classmethod
    def save(cls) -> None:
        db.session.add(cls)
        db.session.commit()

    @classmethod   
    def delete(cls) -> None:
        db.session.delete(cls)
        db.session.commit()
