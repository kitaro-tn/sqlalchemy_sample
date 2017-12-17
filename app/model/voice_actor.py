from app import Model
from sqlalchemy import Column, String, Date, Float, DateTime, ForeignKey, text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


class VoiceActor(Model):
    __tablename__ = 'voice_actor'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(256))
    height = Column(Float)
    birthday = Column(Date)
    office_id = Column(INTEGER(unsigned=True), ForeignKey('office.id'))
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    office = relationship('Office', back_populates='voice_actor')

    def __repr__(self):
        return "<VoiceActor(id = %s, name = '%s')>" % (self.id, self.name)
