from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    # class Meta:
    #     model = Participant
    #     fields = ['email']