from app import Model
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


class Person(Model):
    __tablename__ = 'person'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(256))
    nickname = Column(String(256))
    age = Column(INTEGER)
    height = Column(Float)
    birthday = Column(String(16))
    blood_type = Column(String(2))
    shop_id = Column(INTEGER(unsigned=True), ForeignKey('shop.id'))
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    shop = relationship("Shop", back_populates="person")

    def __repr__(self):
        return "<Person(id = %d, name = '%s')>" % (self.id, self.name)
