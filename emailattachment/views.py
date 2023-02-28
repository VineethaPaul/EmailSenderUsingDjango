from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from django.conf import settings
from .forms import EmailForm
from .models import Users
from django.shortcuts import render
from django.utils import timezone
from .tasks import send_email_task
from django_celery_beat.models import PeriodicTask,CrontabSchedule

class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'emailattachment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(form.errors,'eeeeeeee')
        if form.is_valid():
            files = request.FILES.getlist('attach')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            scheduled_time = form.cleaned_data['scheduled_time']
            # scheduled_time = timezone.make_aware(scheduled_time)

            # try:
            # form.send_email(files=files)

            try:
                emails = self.request.POST['to'].split(',')
            except:
                emails = [self.request.POST['to']]
                
            # send_email_task(subject,message,emacils,files)

            # send_email_task.apply_async(
            #     args=[subject, message,emails , files],
            #     eta=scheduled_time
            # )
            # send_email_task.delay()


            schedule, created = CrontabSchedule.objects.get_or_create(hour=21,minute=13)
            task = PeriodicTask.objects.create(crontab=schedule,name='schedule_email'+'5',task='emailattachment.tasks.send_email_task')
            return render(request, self.template_name, {'email_form': form, 'error_message': 'Mail has been successfully sent'})
            # except:
            #     return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})

