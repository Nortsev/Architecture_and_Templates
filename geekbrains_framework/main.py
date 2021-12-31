from templator import render


class PageNotFound404:
    def __call__(self, request):
        try:
            return '200 OK', render('404.html', date=request.get('date', None))
        except FileNotFoundError:
            return '404 WHAT', '404 PAGE Not Found'


class Framework:
    """Основной класс фреймворка"""

    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        request = {}
        for front in self.fronts_lst:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
