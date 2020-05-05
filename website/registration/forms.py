from django import forms


class usernameForm(forms.Form):
    username = forms.CharField(label="Username:", min_length=1, max_length=20,
                               widget=forms.TextInput(attrs={"placeholder":"Username"}))


class passwordForm(forms.Form):
    password = forms.CharField(label="Password:", min_length=6, max_length=20 ,widget=forms.PasswordInput(attrs={
    'class': 'input-text with-border', 'placeholder': 'Password'}))


class repeatPasswordForm(forms.Form):
    repeatPassword = forms.CharField(label="Repeat password:", min_length=1, widget=forms.PasswordInput(attrs={
    'class': 'input-text with-border', 'placeholder': 'Repeat password'}))
