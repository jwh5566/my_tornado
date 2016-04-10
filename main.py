#coding=utf-8
__author__ = 'root'

import os.path
import random

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define('port', default=8000, type=int)

class IndexHandle(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class MungedPageHandle(tornado.web.RequestHandler):
    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.plit(' ') if len(x) > 0]:
                if word[0] not in mapped: mapped[word[0]]=[]
                mapped[word[0]].append(word)
        return mapped

    def post(self):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map =self.map_by_first_letter(source_text)
        change_lines = text_to_change.split('\r\n')
        self.render('munged.html', source_map=source_map, change_lines=change_lines,choice=random.choice)

if __name__ == '__main__':
    pass