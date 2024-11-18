from django import forms
class UserForm(forms.Form):
 url_text = forms.URLField(label="Введите URL", help_text="Например http://www.google.com")