from django import forms
class UserForm(forms.Form):
      file = forms.FileField(label="Файл")