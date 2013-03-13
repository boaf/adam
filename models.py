import datetime
from app import db

from eve_api import SkillTreeParser, eve_parser

class SkillTreeDocument(db.Document):
    
    def get_skills(self):
        return eve_parser(SkillTreeParser)