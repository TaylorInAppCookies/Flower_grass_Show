# coding: utf-8
from sqlalchemy import Column, Integer, String, Text, Boolean, Float, DateTime, Enum
from sqlalchemy.orm import relationship

from model.base import Base


class Order(Base):
    __tablename__ = 'Order'
    progress_set = {'on', 'off', 'completed'}

    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    describe = Column(String(800))
    money = Column(Float)
    send_time = Column(DateTime)
    paid_at = Column(DateTime)
    location_x = Column(Float)
    location_y = Column(Float)
    progress = Column(Enum(progress_set, name='progress'))
    is_complete = Column(Boolean)
    is_paid = Column(Boolean)
    is_abandon = Column(Boolean)
    is_running = Column(Boolean)
    is_deleted = Column(Boolean)

    def __init__(self, title=None, describe=None, money=None, send_time=None,
                 paid_at=None, location_x=None, location_y=None, is_complete=None,
                 is_paid=None, is_abandon=None, is_running=None, is_deleted=None):
        self.title = title
        self.describe = describe
        self.money = money
        self.send_time = send_time
        self.paid_at = paid_at
        self.location_x = location_x
        self.location_y = location_y
        self.is_complete = is_complete
        self.is_paid = is_paid
        self.is_abandon = is_abandon
        self.is_running = is_running
        self.is_deleted = is_deleted

    def json(self):
        pass
        # TODO add return messages of Order using json
