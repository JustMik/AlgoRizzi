from flask_admin import BaseView, AdminIndexView, expose
from flask_login import current_user


class AdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    @expose('/')
    def index(self):
        return self.render('/admin/index.html')

    @expose('/post')
    def post(self):
        return self.render('/admin/post.html')