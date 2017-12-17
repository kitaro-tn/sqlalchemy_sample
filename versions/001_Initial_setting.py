from sqlalchemy import MetaData, Table, Column, String, Float, Date, DateTime, ForeignKey, text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER
from migrate import *
# from app.model.person import Person
# from app.model.shop import Shop
# from app.model.character_voice import CharacterVoice
# from app.model.voice_actor import VoiceActor
# from app.model.office import Office
# from app import Model


meta = MetaData()

shop = Table(
    'shop', meta,
    Column('id', INTEGER(unsigned=True), primary_key=True),
    Column('address', String(256)),
    Column('created_at', DateTime, nullable=False, server_default=current_timestamp()),
    Column('updated_at', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
)

office = Table(
    'office', meta,
    Column('id', INTEGER(unsigned=True), primary_key=True),
    Column('address', String(256)),
    Column('created_at', DateTime, nullable=False, server_default=current_timestamp()),
    Column('updated_at', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
)

person = Table(
    'person', meta,
    Column('id', INTEGER(unsigned=True), primary_key=True),
    Column('name', String(256)),
    Column('nickname', String(256)),
    Column('age', INTEGER),
    Column('height', Float),
    Column('birthday', String(16)),
    Column('blood_type', String(2)),
    Column('shop_id', INTEGER(unsigned=True), ForeignKey('shop.id')),
    Column('created_at', DateTime, nullable=False, server_default=current_timestamp()),
    Column('updated_at', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    # Column('updated_at', DateTime, nullable=False, server_onupdate=current_timestamp(), server_default=current_timestamp()),
)

voice_actor = Table(
    'voice_actor', meta,
    Column('id', INTEGER(unsigned=True), primary_key=True),
    Column('name', String(256)),
    Column('height', Float),
    Column('birthday', Date),
    Column('office_id', INTEGER(unsigned=True), ForeignKey('office.id')),
    Column('created_at', DateTime, nullable=False, server_default=current_timestamp()),
    Column('updated_at', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
)

character_voice = Table(
    'character_voice', meta,
    Column('id', INTEGER(unsigned=True), primary_key=True),
    Column('voice_actor_id', INTEGER(unsigned=True), ForeignKey('voice_actor.id')),
    Column('person_id', INTEGER(unsigned=True), ForeignKey('person.id')),
    Column('created_at', DateTime, nullable=False, server_default=current_timestamp()),
    Column('updated_at', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
)

def upgrade(migrate_engine):
    # Person.metadata.bind = migrate_engine
    # Person.__table__.create_all()
    # Shop.metadata.bind = migrate_engine
    # Shop.metadata.create_all(migrate_engine)
    # Offiece.metadata.bind = migrate_engine
    # Offiece.metadata.create_all(migrate_engine)
    # Person.metadata.bind = migrate_engine
    # Person.metadata.create_all(migrate_engine)
    # VoiceActor.metadata.bind = migrate_engine
    # VoiceActor.metadata.create_all(migrate_engine)
    # CharacterVoice.metadata.bind = migrate_engine
    # CharacterVoice.metadata.create_all(migrate_engine)
    # Model.metadata.create_all(migrate_engine)
    meta.create_all(migrate_engine)

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    # Person.metadata.bind = migrate_engine
    # Person.__table__.drop()
    # Shop.metadata.bind = migrate_engine
    # Shop.metadata.drop_all()
    # Offiece.metadata.bind = migrate_engine
    # Offiece.metadata.drop_all()
    # Person.metadata.bind = migrate_engine
    # Person.metadata.drop_all()
    # VoiceActor.metadata.bind = migrate_engine
    # VoiceActor.metadata.drop_all()
    # CharacterVoice.metadata.bind = migrate_engine
    # CharacterVoice.metadata.drop_all()
    # Model.metadata.drop_all(migrate_engine)
    meta.drop_all(migrate_engine)
