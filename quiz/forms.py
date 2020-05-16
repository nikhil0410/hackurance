from django import forms
from django.forms.widgets import RadioSelect


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        # print(question.get_answers_list())
        choice_list = [x for x in question.get_answers_list()]
        print(choice_list)
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number'}), required=False)