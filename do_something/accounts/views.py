from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import Group
from .forms import SignUpFormPriv, SignUpFormOrg
from page.models import OrgUser, Activity
from django.contrib.auth.decorators import login_required


# For privatperson
class SignUpViewPriv(generic.CreateView):
    form_class = SignUpFormPriv
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        pass
        form = SignUpFormPriv(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Legger til i gruppe
            user_group = Group.objects.get(name='Privatperson')
            user.groups.add(user_group)

            return redirect('/accounts/login')
        else:
            return render(request, self.template_name, {'form' : form })

# For organisasjon
class SignUpViewOrg(generic.CreateView):
    form_class = SignUpFormOrg
    success_url = reverse_lazy('login')
    template_name = 'registration/signupOrg.html'

    def post(self, request, *args, **kwargs):
        pass
        form = SignUpFormOrg(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # Legger til i gruppe
            user_group = Group.objects.get(name='Organisasjon')
            user.groups.add(user_group)

            # Oppretter OrgUser som linker til organisasjonsnavn
            org_name = form.cleaned_data['org_name']
            orguser = OrgUser.objects.create(user=user, org_name=org_name)
            

            return redirect('/accounts/login')
        else:
            return render(request, self.template_name, {'form' : form })


def log(request):
    new = Activity.objects.filter(favourites=request.user)
    newReg = Activity.objects.filter(registrations=request.user)
    return render(request,
                  'page/log.html',
                  {'new': new, 'newReg': newReg})



def favourite_add(request, id):
    post = get_object_or_404(Activity, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])