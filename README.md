wsgirouter is a tiny web library based on webob. It has been made to write
simple WSGI apps efficiently withoutextra dependency.

It contains two parts so far:

- A Router class which is basically an URL router.
- A Root class from you can inherit to create a cleaner App class.

All you need is to import the file router.py.

Here is a very simple Hello World example:

    from webob import Request, Response, exc
    import router

    class Hello(router.Root):

        def get(self, environ):
            req = Request(environ)
            name = req.path_info.split('/').pop()
            return Response('Hello ' + name)

    if __name__ == '__main__':
        from wsgiref.simple_server import make_server
        urls = router.Router()
        # Here we add an URL on the "default" vhost, like a catch-all.
        urls['*'] = (
                '^/hello/.*$', Hello()
                )
        print 'http://localhost:4242/'
        make_server('localhost', 4242, urls).serve_forever()