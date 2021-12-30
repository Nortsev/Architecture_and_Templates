from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Test website ginicorn']


with make_server('', 8000, application) as httpd:
    try:
        print("Запущенно на 8000 порту.....")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Вы принудительно остановили сервер......")
