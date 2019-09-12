import enum


class OrderStatus(enum.Enum):

 created = "CREATED"
 pending = "PENDING"
 delivered = "DELIVERED"
 closed = "CLOSED"
