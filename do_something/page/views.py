from django.shortcuts import render, get_object_or_404
from .models import Activity
from django import forms
from .forms import FilterForm
from .forms import ActivityForm, PrivateActivityForm
from django.contrib.auth.models import User
from .models import OrgUser
from django.contrib import messages
from django.shortcuts import redirect, HttpResponseRedirect
from datetime import date
import datetime
from django.db.models import Count
from django.db.models import Q

# Hjemmesiden viser aktiviteter
def home(request):
    # Sorterer på dato midlertidig
    # posts = Activity.objects.order_by("publishingDate")
    posts = Activity.objects.order_by("date")
    end = datetime.datetime.now().strftime('%H:%M')
    begin = datetime.datetime.strptime('00:00', '%H:%M').time()
    # Filtrerer bort utgåtte aktiviteter
    posts = posts.exclude(date__lt=date.today().isoformat())
    posts = posts.exclude(Q(date=date.today()) & Q(time__range=(begin, end)))

    # Henter data, eller setter begge valg til alle
    form = FilterForm(request.GET)
    if not form.is_valid():
        form = FilterForm(
            {'inneute': 'alle', 'gratisbetaling': 'alle', 'brukerInput': 'alle'})

    # Filtrer på ute eller inne
    if request.GET.get('inneute') == "inne":
        posts = posts.filter(place='I')
    if request.GET.get('inneute') == "ute":
        posts = posts.filter(place='U')

    # Filtrere på gratis eller betalt
    if request.GET.get('gratisbetaling') == "gratis":
        posts = posts.filter(paid='G')
    if request.GET.get('gratisbetaling') == "betaling":
        posts = posts.filter(paid='B')

    # Filtrerer på bruker
    if request.GET.get('brukerInput') == "privatperson":
        posts = posts.filter(user__groups__name="Privatperson")
    if request.GET.get('brukerInput') == "organisasjon":
        posts = posts.filter(user__groups__name="Organisasjon")

    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'page/home.html', context)


def about(request):
    return render(request, 'page/about.html', {'title': 'About'})


def login(request):
    return render(request, 'registration/login.html', {'title': 'Log in'})


def user(request):
    # Henter alle aktiviteter og filtrerer frem de som er lagt ut av brukeren
    posts = Activity.objects.order_by("date")

    currentUser = (request.user)
    posts = posts.filter(user=currentUser)
    context = {
        'posts': posts,
        'title': 'Profil'
    }
    return render(request, 'page/user.html', context)


def admin(request):
    return render(request, '/admin', {'title': 'Admin'})

# def log(reguest):
#    return render(reguest, 'page/log.html', {'title': 'log'})


def addActivity(request):
    currentUser = request.user

    # Viser riktig form basert på brukertype
    if (currentUser.groups.filter(name='Privatperson').exists()):
        form = PrivateActivityForm()
    else:
        form = ActivityForm()

    context = {
        'title': 'addActivity',
        'form': form,
    }
    if (request.method == "POST"):
        # Får et form for nye aktiviteter fra siden
        f = ActivityForm(request.POST)
        if f.is_valid():
            # Sjekker om aktiviteter fra organisasjoner har dato
            if (currentUser.groups.filter(name='Organisasjon').exists()):
                dateinput = f.cleaned_data.get('date')
                if ((dateinput == None)):
                    messages.error(request, 'Du må legge inn dato')
                    return render(request, 'page/addActivity.html', {"form": f})

                paid_input = request.POST.get('paid')
                if ((paid_input == '')):
                	messages.error(request, 'Betaling kan ikke være blank')
                	return render(request, 'page/addActivity.html', {"form": f})
                input_time = f.cleaned_data.get('time')
                if (dateinput < datetime.date.today()):
                    messages.error(request, 'Datoen kan ikke være i fortiden')
                    return render(request, 'page/addActivity.html', {"form": f})
                if (dateinput == datetime.date.today() and input_time.strftime('%H:%M') < datetime.datetime.now().strftime('%H:%M')):
                    messages.error(request, 'Dagens tidspunkt har vært')
                    return render(request, 'page/addActivity.html', {"form": f})





            # Lager en ny aktivitet fra formet
            newActivity = f.save(commit=False)
            # Legger brukeren som lager formet som foreign key på aktiviteten
            currentUser = request.user
            newActivity.user = currentUser
            # Lagrer aktiviteten i databasen
            newActivity.save()
            messages.success(request, "Din aktivitetet er lagret!")
        else:
            messages.error(request, 'Du må fylle inn alle feltene')
            return render(request, 'page/addActivity.html', {"form": f})

    return render(request, 'page/addActivity.html', context)


def userOrOrg(request):
    return render(request, 'registration/userOrOrg.html', {'title': 'UserOrOrg'})


def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)  # Get your current activity

    if request.method == 'POST':         # If method is POST,
        activity.delete()                     # delete the activity.
        # Finally, redirect to the userpage.
        return redirect('page-user')

    return render(request, 'page/user.html', {'activity': activity})
    # If method is not POST, render the default template.


def registration_and_removefav(request, id):
    post = get_object_or_404(Activity, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return registration_add(request, id)


def registration_add(request, id):
    post = get_object_or_404(Activity, id=id)
    if post.registrations.filter(id=request.user.id).exists():
        post.registrations.remove(request.user)
    else:
        post.registrations.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    

def statistics(request):
	posts = Activity.objects.all()
	number_of_activitys = posts.count()
	users = User.objects.all()
	users.filter()
	number_of_users = users.count()

	number_of_org_users = users.filter(groups__name='Organisasjon').count()
	number_of_private_users = users.filter(groups__name='Privatperson').count()

	posts = Activity.objects.annotate(number_of_regs=Count('registrations')).order_by("number_of_regs").reverse()[:10]
	

		#number_of_registrations_list.append(number_of_registrations)

	amount_of_user_and_activity = {
		'activitys': number_of_activitys,
		'users': number_of_users, 
		'number_of_org_users': number_of_org_users,
		'number_of_private_users': number_of_private_users,
		'posts': posts,

    	}



	return render(request, 'page/statistics.html', amount_of_user_and_activity)
