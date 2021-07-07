from django import forms  
from .models import Contactcarrers,Contactservices,Contactprojects

class ContactcarrersForm(forms.ModelForm):
	class Meta:
		model=Contactcarrers
		fields=['Name','PhoneNumber','Email','Message']

class ContactservicesForm(forms.ModelForm):
	class Meta:
		model=Contactservices
		fields=['Name','PhoneNumber','Email','Message']

class ContactprojectsForm(forms.ModelForm):
	class Meta:
		model=Contactprojects
		fields=['Name','PhoneNumber','Email','Message']