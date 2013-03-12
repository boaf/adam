import xml.etree.ElementTree as ET

from urllib2 import urlopen

import re

class SkillTreeParser(object):
    feed = 'https://api.eveonline.com/eve/SkillTree.xml.aspx'

    skill_count = 0

    def __init__(self):
        self.tree = {}

    def start(self, tag, attrib):

        if 'groupName' in attrib:
            if attrib['groupID'] not in self.tree:
                self.tree[attrib['groupID']] = {
                    'name': attrib['groupName'],
                    'skills': {},
                    'count': 0
                }

        if 'typeName' in attrib:
            self.tree[attrib['groupID']]['skills'][attrib['typeID']] = attrib['typeName']
            self.skill_count += 1
            self.tree[attrib['groupID']]['count'] += 1

    def close(self):
        return {
            'tree': self.tree,
            'skill_count': self.skill_count,
            'group_count': len(self.tree)
        }

    def data(self, data): pass
    def end(self, tag): pass


def eve_parser(target):
    parser = ET.XMLParser(target=target())
    parser.feed(urlopen(target.feed).read())
    return parser.close()