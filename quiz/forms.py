from django import forms
from django.forms.widgets import RadioSelect
from .models import ContactModel, EnrollmentModel, ClaimModel, GetFreeQuote


class ContactForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Last Name'}))
    class Meta:
        model = ContactModel
        fields = ['name', 'email','subject', 'message']


class EnrollmentForm(forms.ModelForm):

    employer_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Employer Name'}))
    group_plan_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Group Plan Number'}))

    ssn = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'SSN'}))
    age = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Age'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Gender'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Date Of Birth'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Address'}))
    work_status = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Work Status'}))
    annual_income = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Annual Income'}))
    profession = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Job Title'}))
    dependent_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Dependent Details'}))

    class Meta:
        model = EnrollmentModel
        fields = ['employer_name', 'group_plan_number', 'ssn', 'age', 'gender', 'date_of_birth', 'address', 'work_status',
        'annual_income', 'profession', 'dependent_details']

class ClaimForm(forms.ModelForm):

    group_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Group ID'}))
    ssn = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Social Security Number'}))
    claim_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Claim Number'}))
    # profession = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Profession'}))
    class Meta:
        model = ClaimModel
        fields = ['group_id', 'ssn','claim_number']


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number'}), required=False)

class GetFreeQuoteForm(forms.ModelForm):
    CHOICES = (
        ('Life Insurance', 'Life Insurance'),
        ('Group Insurance', 'Group Insurance'),
        ('Travel Insurance', 'Travel Insurance'),
        ('Health Insurance', 'Health Insurance'),
        ('Dental insurance', 'Dental insurance'),
        ('Vision insurance', 'Vision insurance'),
        ('Accident insurance', 'Accident insurance'),
        ('Critical illiness insurance', 'Critical illiness insurance'),
        ('Motor Policy', 'Motor Policy'),)

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number'}))
    product = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}))
    class Meta:
        model = GetFreeQuote
        fields = ['name', 'email','phone', 'product', 'message']










