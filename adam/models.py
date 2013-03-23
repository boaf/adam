import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from adam.db import Base


class Skill(Base):

    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    groupID = Column(Integer, unique=True)

    def __init__(self, id, name, groupID):
        self.id = id
        self.name = name
        self.groupID = groupID

    def __repr__(self):
        return '<Skill "%s">' % self.name


class SkillGroup(Base):

    __tablename__ = 'skill_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<SkillGroup "%s">' % self.name

class User(Base):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    email = Column(String(200))
    openid = Column(String(200))

    api_keys = relationship("APIKey")

    def __init__(self, name, email, openid):
        self.name = name
        self.email = email
        self.openid = openid

class APIKey(Base):

    __tablename__ = 'api_keys'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    key_id = Column(Integer, nullable=False)
    key_code = Column(String(100), nullable=False)

    def __init__(self, user_id, key_id, key_code):
        self.user_id = user_id
        self.key_id = key_id
        self.key_code = key_code
