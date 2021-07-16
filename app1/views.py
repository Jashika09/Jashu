from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth import login,authenticate
from app1.models import Register
from app1.forms import RegisterForm,SignForm
from app1.models import Contact
from app1.forms import ContactForm
from django.contrib.auth.models import User

# Create your views here.

class HomepageView(TemplateView):
    template_name="Home.html"
    def post(self,request):
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            text=form.cleaned_data['name']
            text=form.cleaned_data['lastname']
            text=form.cleaned_data['emailid']
            text=form.cleaned_data['password']

            form=RegisterForm()
            return redirect('/')
        args={'form':form,'text':text}
        return render(request, self.template_name,args)

class AboutpageView(TemplateView):
    template_name="about.html"

class WeeklypageView(TemplateView):
    template_name="weekly.html"

class ServicespageView(TemplateView):
    template_name="services.html"
class UserspageView(ListView):
    template_name="users.html"
    def get_queryset(self):
        return User.objects.all()

class FeedbackpageView(ListView):
    template_name="feeback.html"
    def get_queryset(self):
        return Contact.objects.all()


class ContactpageView(TemplateView):
    template_name="contact.html"
    def post(self,request):
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            text=form.cleaned_data['name']
            text=form.cleaned_data['lastname']
            text=form.cleaned_data['emailid']
            text=form.cleaned_data['feedback']

            form=ContactForm()
            return redirect('/contact/')
        args={'form':form,'text':text}
        return render(request, self.template_name,args)

def sign(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignForm()
    return render(request, 'registration/sign.html', {'form': form})
