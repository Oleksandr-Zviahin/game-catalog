from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = 'catalog/user/login.html'

    success_url = '/catalog/index'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
