from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label='Benutzername:')
    password = forms.CharField(max_length=35, label='Password:', widget=forms.PasswordInput)





class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='Benutzername:')
    password = forms.CharField(max_length=35, label='Password:', widget=forms.PasswordInput)
