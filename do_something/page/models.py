from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver

#Aktivitetsklasse med atributter
class Activity(models.Model):
    # Felter for alle aktiviteter
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, verbose_name='tittel')
    description = models.TextField(max_length=1000, verbose_name='beskrivelse')

    PLACE_CHOICES = [        
        ('U', 'Ute'),
        ('I', 'Inne'),
    ]
    place = models.CharField(max_length=1, choices=PLACE_CHOICES, default='U', verbose_name='sted')
    
    # Felter for organiserte aktiviteter
    date = models.DateField(blank=True, null=True, verbose_name='dato')
    time = models.TimeField(blank=True, null=True, verbose_name='tidspunkt')
    PAID_CHOICES = [        
        ('B', 'Betalt'),
        ('G', 'Gratis'),
    ]
    paid = models.CharField(max_length=1, choices=PAID_CHOICES, default='G', blank=True, null=True, verbose_name='betalt')
    

    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)

    registrations = models.ManyToManyField(
        User, related_name='registration', default=None, blank=True)

    def __str__(self):
        return self.title

    #For å skrive riktig på admin-siden (ikke activitys)
    class Meta:
        verbose_name_plural = "activities"


# Modell som inneholder en bruker og organisjonsnavn
# Kan legge til mer info her som ikke er i default User
class OrgUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=40)
    
   
    def __str__(self):
        return str(self.user)

    # Plasseres i Auth på adminsiden
    class Meta:
        app_label = 'auth'
    
