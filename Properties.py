# -*- coding: utf-8 -*-
from configparser import RawConfigParser

class Properties:
    config : RawConfigParser = RawConfigParser().read('application.properties')
    a = config.get('rabbitmq',"rabbitmq.username")

    def __init__(self):
        self.config = RawConfigParser()
        self.config.read('application.properties')