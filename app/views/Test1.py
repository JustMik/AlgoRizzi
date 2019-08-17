from flask_admin import BaseView, expose

class Test1(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/test1.html')

