from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from register.forms import *
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.core.mail.message import BadHeaderError
from django.http.response import HttpResponse
from mysite import settings

# Create your views here.
class Home(TemplateView):
    template_name="index.html"


class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "-login.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = '/register/user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)


def anonymous_required(func):
    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL )
        if request.user.is_authenticated():
            return redirect(redirect_to)
        response = func(request, *args, **kwargs)
        return response
    return as_view
