from django import forms

class ContactForm(forms.Form):
		firstname=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control'}))	
		lastname=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control'}))	
		email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control emailfield'}))	
		message=forms.CharField(max_length=40,widget=forms.Textarea(attrs={'class':'form-control'}))	

