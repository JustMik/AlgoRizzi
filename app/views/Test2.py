from flask_admin import BaseView, expose

class Test2(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/test2.html')

