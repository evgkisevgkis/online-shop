from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from string import ascii_letters,digits
from random import choices


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    symbols = ascii_letters + digits
    randoms = choices(symbols, k=8)
    new_password = ''.join(randoms)
    subject = 'Смена пароля'
    message = f'Вы запросили новый пароль. Вот он: {new_password}'
    from_email = 'evgeny-kiselev-95@yandex.ru'
    recipient_list = [request.user.email]
    send_mail(subject, message, from_email, recipient_list)
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:profile'))


