#coding=utf-8
__author__ = 'root'
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define('port', default=8000, type=int)

class IndexHandle(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class PoemPageHandle(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb, difference=noun3)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/poem', PoemPageHandle),
                                            (r'/', IndexHandle)],
                                  template_path=os.path.join(os.path.dirname(__file__), 'templates'))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()