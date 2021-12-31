from wsgiref.simple_server import make_server
from geekbrains_framework.main import Framework
from urls import routes, fronts


application = Framework(routes, fronts)




with make_server('', 8000, application) as httpd:
    try:
        print("Запущенно на 8000 порту.....")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Вы принудительно остановили сервер......")
