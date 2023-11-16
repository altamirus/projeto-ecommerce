from typing import Any, Dict
from django.contrib.auth.models import User
from django import forms
from . import models


class Perfilfrorms(forms.ModelsForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_nome', 'last_name', 'username', 'password', 'email')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.changed_data
