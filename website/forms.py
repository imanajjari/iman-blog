from django import forms
from .models import Contact
from captcha.fields import CaptchaField

class contactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

