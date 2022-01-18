from datetime import date
from views import Index, Contact, Examples, Another_page, Page, CopyCourse, CreateCourse, CreateCategory, \
    CategoryList, CoursesList


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/contact/': Contact(),
    '/examples/': Examples(),
    '/another_page/': Another_page(),
    '/page/': Page(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse()
}
