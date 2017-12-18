from sqlalchemy import *
from migrate import *
from sqlalchemy.orm import sessionmaker
from app.model.person import Person
from app.model.shop import Shop
from app.model.character_voice import CharacterVoice
from app.model.voice_actor import VoiceActor
from app.model.office import Office
from app import Model


def upgrade(migrate_engine):
    Session = sessionmaker(bind=migrate_engine)
    session = Session()
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    objects = [
        Shop(id=1, name='ラビットハウス'),
        Shop(id=2, name='フルール・ド・ラパン'),
        Shop(id=3, name='甘兎庵'),
    ]
    session.bulk_save_objects(objects)
    session.commit()

    objects = [
        Office(id=1, name='アイムエンタープライズ'),
        Office(id=2, name='アクセルワン'),
        Office(id=3, name='大沢事務所'),
        Office(id=4, name='青二プロダクション'),
        Office(id=5, name='響'),
        Office(id=6, name='東京俳優生活協同組合'),
        Office(id=7, name='Rush Style'),
    ]
    session.bulk_save_objects(objects)
    session.commit()

    objects = [
        Person(id=1, name='保登 心愛', nickname='ココア', age=15, height=154, birthday='04-10', blood_type='B', shop_id=1),
        Person(id=2, name='香風 智乃', nickname='チノ', age=13, height=144, birthday='12-04', blood_type='AB', shop_id=1),
        Person(id=3, name='天々座 理世', nickname='リゼ', age=16, height=160, birthday='02-14', blood_type='A', shop_id=1),
        Person(id=4, name='宇治松 千夜', nickname='千夜', age=15, height=157, birthday='09-19', blood_type='O', shop_id=3),
        Person(id=5, name='桐間 紗路', nickname='シャロ', age=15, height=151, birthday='07-15', blood_type='A', shop_id=2),
        Person(id=6, name='ティッピーゴールデンフラワリーオレンジペコ', nickname='ティッピー', age=None, height=None, birthday=None, blood_type=None, shop_id=1),
        Person(id=7, name='香風 タカヒロ', nickname='タカヒロ', age=None, height=None, birthday=None, blood_type=None, shop_id=1),
        Person(id=8, name='保登 モカ', nickname='モカ', age=None, height=None, birthday='03-13', blood_type=None, shop_id=None),
        Person(id=9, name='条河 麻耶', nickname='マヤ', age=13, height=140, birthday='08-08', blood_type='O', shop_id=None),
        Person(id=10, name='奈津 恵', nickname='メグ', age=13, height=145, birthday='11-02', blood_type='A', shop_id=None),
        Person(id=11, name='青山 翠', nickname='青山 ブルーマウンテン', age=None, height=163, birthday='10-27', blood_type='B', shop_id=None),
        Person(id=12, name='真手 凛', nickname='', age=None, height=None, birthday=None, blood_type=None, shop_id=None),
    ]
    session.bulk_save_objects(objects)
    session.commit()

    objects = [
        VoiceActor(id=1, name='佐倉 綾音', height=157, birthday='1994-01-29', office_id=1),
        VoiceActor(id=2, name='水瀬 いのり', height=154, birthday='1995-12-02', office_id=2),
        VoiceActor(id=3, name='種田 梨沙', height=153, birthday='1988-07-12', office_id=3),
        VoiceActor(id=4, name='佐藤 聡美', height=153, birthday='1986-05-08', office_id=4),
        VoiceActor(id=5, name='内田 真礼', height=155, birthday='1989-12-27', office_id=1),
        VoiceActor(id=6, name='清川 元夢', height=182, birthday='1935-04-09', office_id=6),
        VoiceActor(id=7, name='速水 奨', height=174, birthday='1958-08-02', office_id=7),
        VoiceActor(id=8, name='茅野 愛衣', height=153, birthday='1987-09-13', office_id=3),
        VoiceActor(id=9, name='徳井 青空', height=159, birthday='1989-12-26', office_id=5),
        VoiceActor(id=10, name='村川 梨衣', height=152, birthday='1990-06-01', office_id=6),
        VoiceActor(id=11, name='早見 沙織', height=164, birthday='1991-05-29', office_id=1),
        VoiceActor(id=12, name='木村 珠莉', height=150.5, birthday='1987-06-07', office_id=6),
    ]
    session.bulk_save_objects(objects)
    session.commit()

    objects = [
        CharacterVoice(voice_actor_id=1, person_id=1),
        CharacterVoice(voice_actor_id=2, person_id=2),
        CharacterVoice(voice_actor_id=3, person_id=3),
        CharacterVoice(voice_actor_id=4, person_id=4),
        CharacterVoice(voice_actor_id=5, person_id=5),
        CharacterVoice(voice_actor_id=6, person_id=6),
        CharacterVoice(voice_actor_id=7, person_id=7),
        CharacterVoice(voice_actor_id=8, person_id=8),
        CharacterVoice(voice_actor_id=9, person_id=9),
        CharacterVoice(voice_actor_id=10, person_id=10),
        CharacterVoice(voice_actor_id=11, person_id=11),
        CharacterVoice(voice_actor_id=12, person_id=12),
    ]
    session.bulk_save_objects(objects)
    session.commit()

def downgrade(migrate_engine):
    Session = sessionmaker(bind=migrate_engine)
    session = Session()
    session.execute("TRUNCATE TABLE character_voice")
    session.execute("TRUNCATE TABLE voice_actor")
    session.execute("TRUNCATE TABLE person")
    session.execute("TRUNCATE TABLE office")
    session.execute("TRUNCATE TABLE shop")
