# coding: utf-8
import enum as enum
from sqlalchemy import Column, Integer, String, Text, Boolean, Float, DateTime, Enum
from sqlalchemy.orm import relationship

from model.base import Base


class Order(Base):
    __tablename__ = 'Order'

    class Progeress_Enum(enum.Enum):
        on = 'on'
        attemper = 'attemper'
        run = 'run'
        abandon = 'abandon'
        deleted = 'deleted'
        paid = 'paid'
        arrive = 'arrive'
        sign = 'sign'
        complete = 'complete'
        off = 'off'

    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    describe = Column(String(800))
    money = Column(Float)
    send_time = Column(DateTime)
    paid_at = Column(DateTime)
    location_x = Column(Float)
    location_y = Column(Float)
    progress = Column(Enum(Progeress_Enum, name='progress'))

    def __init__(self, title=None, describe=None, money=None, send_time=None,
                 paid_at=None, location_x=None, location_y=None, progress='off'):
        self.title = title
        self.describe = describe
        self.money = money
        self.send_time = send_time
        self.paid_at = paid_at
        self.location_x = location_x
        self.location_y = location_y
        self.progress = progress
