from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import Group
from page.models import OrgUser

#Endrer UserCreationForm til å inneholde flere felter enn default (username, password).
#Nå får vi også fornavn, etternavn og mail i tillegg
class SignUpFormPriv(UserCreationForm):
    email = forms.EmailField()
    first_name  = forms.CharField(max_length=40)
    last_name  = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        help_texts = {
            'username': '<br>Bare tall, bokstaver og @/./+/-/_.',
        }
        labels = {
            'username': 'Brukernavn',
        }
    def __init__(self, *args, **kwargs):
        super(SignUpFormPriv, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = '<br> Passordet kan ikke være for likt annen personlig info. <br> Passordet må være minst 8 langt. <br>Passordet kan ikke bare være tall. <br>Passordet kan ikke være for vanlig.'                                                
        self.fields['password2'].help_text = ''
        self.fields['password1'].label = 'Passord'
        self.fields['password2'].label = 'Gjenta passord'
        self.fields['first_name'].label = 'Fornavn'
        self.fields['last_name'].label = 'Etternavn'


#Lager ny form for organisasjon. Bare endret felt som org skal fylle ut.
class SignUpFormOrg(UserCreationForm):
    email = forms.EmailField()
    org_name  = forms.CharField(max_length=40)

    
    class Meta:
        model = User
        fields = ('username', 'org_name', 'email', 'password1', 'password2')
        help_texts = {
            'username': '<br>Bare tall, bokstaver og @/./+/-/_.',
        }
        labels = {
            'username': 'Brukernavn',
        }
    
    def __init__(self, *args, **kwargs):
        super(SignUpFormOrg, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = '<br> Passordet kan ikke være for likt annen personlig info. <br> Passordet må være minst 8 langt. <br>Passordet kan ikke bare være tall. <br>Passordet kan ikke være for vanlig.'                                                
        self.fields['password2'].help_text = ''
        self.fields['password1'].label = 'Passord'
        self.fields['password2'].label = 'Gjenta passord'
        self.fields['org_name'].label = 'Organisasjonnavn'
        