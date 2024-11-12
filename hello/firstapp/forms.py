from django import forms
class UserForm(forms.Form):
     email = forms.EmailField(label="Электронный адрес", help_text="Обязательный символ - @")