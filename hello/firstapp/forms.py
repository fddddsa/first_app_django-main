from django import forms
class UserForm(forms.Form):
      combo_text = forms.ComboField(label="Введите URL",
           fields=[forms.URLField(), forms.CharField(max_length=20)])