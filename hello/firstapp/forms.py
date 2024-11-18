from django import forms
class UserForm(forms.Form):
 reg_text = forms.RegexField(label="Текст", regex="^[0-9][A-F][0-9]$")