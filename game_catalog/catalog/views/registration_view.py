from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


class RegistrationFormView(FormView):
    form_class = UserCreationForm

    success_url = '/catalog/'

    template_name = 'catalog/user/register.html'

    def form_valid(self, form):
        form.save()

        return super(RegistrationFormView, self).form_valid(form)
