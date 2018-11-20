from django.urls import reverse


def perfil(request):
    return render(request, 'usuario/perfil.html')


from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from django.views.generic import FormView, RedirectView

# Authentication imports
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from apps.usuario.models import Donador
import random
import string


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("terreno_seguimiento")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'user_login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('user_login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


## Método que obtiene el detalle de usuario logueado
def perfil(request):
    usuario = User.objects.filter(username=request.user).first()
    return render(request, "usuario/perfil.html", {"usuario": usuario})


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'existe': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def recover_password(request):
    email_to = request.GET.get('email', None)
    user = User.objects.get(email=email_to)
    new_password = id_generator()
    user.set_password(new_password)
    user.save()

    subject = 'Recuperación de contraseña'
    message = 'Su nueva contraseña es: ' + new_password
    from_email = 'obaquerog@gmail.com'

    if subject and message and from_email:
        response = send_email(subject, message, from_email, email_to)
        if response:
            data = {
                'error': "no",
                'message': "Se envió una nueva contraseña al correo electrónico " + email_to
            }
        else:
            data = {
                'error': "si",
                'message': "Se produjo un error durante el envío del correo electrónico."
            }
    else:
        data = {
            'error': "si",
            'message': "Por favor verifique el correo electrónico ingresado e intentelo nuevamente."
        }

    return JsonResponse(data)


def send_email(from_email, email_to, subject, message):
    try:
        send_mail(subject, message, from_email, [email_to])
        response = True
    except BadHeaderError:
        response = False

    return response


def get_user_donor_by_donation(donation_id):
    user_donator = Donador.objects.raw('''
    select usuario_donador.* from usuario_donador join financiacion_donacion on donador_id = usuario_donador.id
    where financiacion_donacion.id = %s
    ''', [donation_id])[0]

    return user_donator
