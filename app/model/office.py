from app import Model
from sqlalchemy import Column, String, DateTime, text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


class Office(Model):
    __tablename__ = 'office'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(256))
    address = Column(String(256))
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    voice_actor = relationship("VoiceActor", back_populates="office")

    def __repr__(self):
        return "<Office(id = %d, name = '%s')>" % (self.id, self.name)
