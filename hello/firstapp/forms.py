from django import forms
class UserForm(forms.Form):
 ip_adres = forms.GenericIPAddressField(label="IP адрес", help_text=" Пример формата 192.0.2.0")