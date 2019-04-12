from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.httpserver import HTTPServer

define('port', default=8000, help='port to listen on')

def main():
    app = Application()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print(f'listening on {options.port}')
    IOLoop.current().start()

if __name__ == "__main__":
    main()