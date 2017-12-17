from app import Model
from sqlalchemy import Column, String, DateTime, ForeignKey, text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


class CharacterVoice(Model):
    __tablename__ = 'character_voice'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    voice_actor_id = Column(INTEGER(unsigned=True), ForeignKey('voice_actor.id'))
    person_id = Column(INTEGER(unsigned=True), ForeignKey('person.id'))
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    voice_actor = relationship('VoiceActor', foreign_keys=[voice_actor_id])
    person = relationship('Person', foreign_keys=[person_id])

    def __repr__(self):
        return "<CharacterVoice(id = %d, voice_actor_id = %d, person_id = %d)>" % (self.id, self.voice_actor_id, self.person_id)
