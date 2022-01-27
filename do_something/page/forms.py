from django import forms
from .models import Activity
from django.forms.widgets import SelectDateWidget, Select


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = "__all__"
        exclude = ['user']

        # Lager meny med valg for hvert hele klokkeslett
        time_choices = []
        for h in range(24):
            if h < 10:
                time_choices.append(('0'+str(h)+':00', '0'+str(h)+':00'))
            else:
                time_choices.append((str(h)+':00', str(h)+':00'))
        
        # Norske navn i menyen for måneder
        MONTHS = {
            1: 'Januar', 2: 'Februar', 3: 'Mars', 4: 'April',
            5: 'Mai', 6: 'Juni', 7: 'Juli', 8: 'August',
            9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
        }

        widgets = {
            'date': SelectDateWidget(months=MONTHS, empty_label=("År", "Måned", "Dag")),
            'time': Select(choices=time_choices),
        }

class PrivateActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = "__all__"
        exclude = ['user', 'date', 'time', 'paid']
        

class FilterForm(forms.Form):
        
    place_choices = [
        ('alle', 'Vis alle'),
        ('inne', 'Innendørs'),
        ('ute', 'Utendørs'),
    ]
    inneute = forms.CharField(label='Sted ', 
    widget=forms.RadioSelect(choices=place_choices))

        
    paid_choices = [
        ('alle', 'Vis alle'),
        ('gratis', 'Gratis'),
        ('betaling', 'Betaling'),
    ]
    gratisbetaling = forms.CharField(label='Betalt ', 
    widget=forms.RadioSelect(choices=paid_choices))


    user_choices = [
        ('alle', 'Vis alle'),
        ('privatperson', 'Privatperson'),
        ('organisasjon', 'Organisasjon'),
    ]
    brukerInput = forms.CharField(label='Bruker ', 
    widget=forms.RadioSelect(choices=user_choices))
