from sqlalchemy import Column, Integer, String, Text, Boolean, Float, DateTime
from sqlalchemy.orm import relationship

from model.base import Base


class Order(Base):
    __tablename__ = 'Order'
    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    describe = Column(String(800))
    money = Column(Float)
    send_time = Column(DateTime)
    paid_at = Column(DateTime)
    location_x = Column(Float)
    location_y = Column(Float)
    is_complete = Column(Boolean)
    is_paid = Column(Boolean)
    is_abandon = Column(Boolean)
    is_running = Column(Boolean)
    is_deleted = Column(Boolean)

    def __init__(self, title=None, image=None):
        self.title = title
        self.image = image

    def __repr__(self):
        return '<Item %r>' % (self.title)
