import cherrypy
import os

class Root(object):
    @cherrypy.expose
    def index(self):
        message = "Hello World!\n\n"
        for key in os.environ.keys():
            message += '{0}: {1}\n'.format(key, os.environ.get(key))
        return message

if __name__ == '__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(Root(), '/')
