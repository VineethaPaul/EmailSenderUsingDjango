from django import forms
from .models import Users
from .tasks import send_email_task

forEvery    = [
    ('15', '15 Days'),
    ('30', '30 Days'),
    ('45', '45 Days'),
    ]

class EmailForm(forms.Form):
    to = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget = forms.Textarea)
    forEvery= forms.CharField(label='forEvery', widget=forms.Select(choices=forEvery))
    scheduled_time = forms.DateTimeField(input_formats=['%H:%M'])

    # def send_email(self, files):
    #     # emails = [email.email for email in Users.objects.all()]
    #     try:
    #         emails = self.cleaned_data['to'].split(',')
    #     except:
    #         emails = [self.cleaned_data['to']]
       
        # send_email_task(
        #     self.cleaned_data['subject'],
        #     self.cleaned_data['message'],
        #     emails,
        #     files
        # )
        