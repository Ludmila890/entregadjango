from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from usuarios.models import DatosExtras

class CreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {llave:'' for llave in fields}
        
from django import forms
from .models import DatosExtras

class EditarPerfilForm(forms.ModelForm):
    email = forms.EmailField(label="Editar el email")
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    hobbies = forms.CharField(label='Mis Hobbies')
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = DatosExtras
        fields = ['email', 'first_name', 'last_name', 'hobbies', 'avatar']

    def __init__(self, *args, **kwargs):
        super(EditarPerfilForm, self).__init__(*args, **kwargs)
        usuario = self.instance.user
        datos_extras = self.instance
        self.initial['email'] = usuario.email
        self.initial['first_name'] = usuario.first_name
        self.initial['last_name'] = usuario.last_name
        self.initial['hobbies'] = datos_extras.hobbies
        self.initial['avatar'] = datos_extras.avatar

    def save(self, commit=True):
        usuario = self.instance.user
        usuario.email = self.cleaned_data['email']
        usuario.first_name = self.cleaned_data['first_name']
        usuario.last_name = self.cleaned_data['last_name']
        if commit:
            usuario.save()

        datos_extras = super(EditarPerfilForm, self).save(commit=False)
        datos_extras.hobbies = self.cleaned_data['hobbies']
        datos_extras.avatar = self.cleaned_data['avatar']
        if commit:
            datos_extras.save()
        return datos_extras

