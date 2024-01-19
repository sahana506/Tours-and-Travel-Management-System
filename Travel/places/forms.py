from django import forms
from .models import Details
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class BookForm(forms.Form):
    #name = forms.CharField(label='Name' , max_length=100)
    #phno = forms.CharField(label='PhNo', max_length=10)
    #email = forms.CharField(label='Email', max_length=100)
    #age = forms.IntegerField(label='Age')
    #source =forms.ChoiceField(label='Source',choices=[('place1','place1'),('place2','place2'),('place3','place3'),('place4','place4'),('place5','place5')])
    #dest = forms.ChoiceField(label='Dest',choices=[('place1','place1'),('place2','place2'),('place3','place3'),('place4','place4'),('place5','place5')])
    #'email'

class BookForm(forms.ModelForm):
    email = forms.EmailField()
    methods =(('paypal','PAYPAL'),('AMAZON PAY','AMAZON PAY'),('GOOGLE PAY','GOOGLE PAY'),('PHONEPAY','PHONE PAY'))
    payment = forms.ChoiceField(choices=methods)
    class Meta:
        model=Details
        fields=['name','phno','age','source','dest','departure','return_date']

class MultipleForms(forms.Form):
    number = forms.IntegerField(min_value=2,max_value=20)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']