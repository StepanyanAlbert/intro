from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from .forms import ContactForm

def home(request):
		form=ContactForm()
		return render(request,'home/index.html',{'form':form})

def sendmail(request):
		if request.method=='POST':
				form=ContactForm(request.POST)
				if form.is_valid():
						name=form.cleaned_data['firstname']+form.cleaned_data['lastname']
						message=form.cleaned_data['message']
						sender=form.cleaned_data['email']
						recipients=['1felisidad1@mail.ru']
						send_mail(name,message,sender,recipients)
						return HttpResponseRedirect(reverse('home:home'),{'message':'sadasd'}) 
						#return render(request,'home/index.html',{'message':'Your message has been sent successfully \n Thanks for email'})
		else:
				form=ContactForm()
		return render(request,'home/index.html',{'form':form})

