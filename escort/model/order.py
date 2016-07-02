from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship

from model.base import Base


class Order(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    describe = Column()
    send_time = Column()
    money = Column()
    location = Column()
    is_complete = Column()
    is_abandon = Column()
    is_running = Column()
    is_deleted = Column(Boolean)
    def __init__(self, title=None, image=None):
        self.title = title
        self.image = image

    def __repr__(self):
        return '<Item %r>' % (self.title)
