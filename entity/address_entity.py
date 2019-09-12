from db import db


class AddressEntity(db.Model):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True)
    int_number = db.Column(db.String(15), nullable=False)
    ext_number = db.Column(db.String(15), nullable=False)
    block = db.Column(db.String(15), nullable=False)
    number = db.Column(db.String(15), nullable=False)
    street = db.Column(db.String(75), nullable=False)
    colony = db.Column(db.String(75), nullable=False)
    municipality = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True, server_onupdate=db.func.current_timestamp())
    deleted = db.Column(db.DateTime, nullable=False, default=False)
