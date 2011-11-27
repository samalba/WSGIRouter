
from webob import Request, Response, exc
import wsgirouter


class Hello(wsgirouter.Root):

    def get(self, environ):
        req = Request(environ)
        name = req.path_info.split('/').pop()
        resp = Response('Hello ' + name)
        return resp


class Yo(wsgirouter.Root):

    def get(self, environ):
        req = Request(environ)
        name = req.path_info.split('/').pop()
        return Response('Yo ' + name)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    urls = wsgirouter.Router()
    urls['*'] = (
            '^/.*', Hello()
            )
    urls['toto.com'] = (
            '^/.*', Yo()
            )
    print 'http://localhost:4242/'
    make_server('localhost', 4242, urls).serve_forever()
