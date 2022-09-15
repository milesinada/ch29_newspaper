from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm
from django.views.generic.edit import CreateView, FormView
# from django.contrib.auth.views import PasswordResetView
# from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(CreateView):
    form_class =  CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordChangeView(FormView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'
    

# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'users/password_reset.html'
#     email_template_name = 'users/password_reset_email.html'
#     subject_template_name = 'users/password_reset_subject'
#     success_message = "We've emailed you instructions for setting your password, " \
#                     "if an account exists with the email you entered. You should receive them shortly." \
#                     " If you don't receive an email, " \
#                     "please make sure you've entered the address you registered with, and check your spam folder."
#     success_url = reverse_lazy('password_change_done')