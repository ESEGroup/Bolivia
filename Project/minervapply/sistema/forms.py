from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


def validarDre(dre):
    if len(dre) != 9:
        return False
    soma = 0
    i = 1
    for i in range(1, 9):
        soma = soma + (i * int(dre[i - 1]))
    verify = int(dre[8])
    if soma % 10 == verify:
        return True
    else:
    	return False

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class ProfessorProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('telefone','data_nascimento','registro_ufrj','departamento','url',)

class AlunoProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('telefone','data_nascimento','curso','dre')

    def clean_dre(self):
        dre = self.cleaned_data.get('dre')
        if not validarDre(dre):
            raise ValidationError("Dre não valido")
        return dre

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Password confirmation",
        widget=forms.PasswordInput,
        help_text= "Enter the same password as above, for verification.")

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2



    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
