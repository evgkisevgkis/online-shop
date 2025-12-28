from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from string import ascii_letters,digits
from random import choices


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid:
            new_user = form.save()
            send_mail(
                subject='Поздравляем с регистрацией!',
                message=f'''Спасибо за регистрацию на нашем сайте! Перейдите по этой ссылке 
                для подтверждения почты: http://127.0.0.1:8000/users/verification/?code={new_user.code}''',
                from_email=EMAIL_HOST_USER,
                recipient_list = [new_user.email]
            )
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

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


def email_verification(request):
    u_code = request.GET.get('code')
    all_users = User.objects.filter(is_active=False)
    for u in all_users:
        if u_code == u.code:
            u.is_active = True
            u.save()
            return HttpResponse('<h1>Пользователь успешно верифицирован</h1>')
    return HttpResponse('<h1>Верификация не пройдена</h1>')
