import re
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from info.models import submit_info
from info.serializers import SubmitSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
import socket
socket.getaddrinfo('localhost', 8080)


def mob_validation(mob):
    mob = str(mob)
    pattern = re.match('(0|91)?[6-9][0-9]{9}', mob)
    return pattern


def insert_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        mob = request.POST.get('phone_number')

        if mob_validation(mob) is None:
            print("Enter valid mobile number")
        else:
            try:
                data = submit_info(name=name, dob=dob, email=email, mob=mob)
                data.save()

            except Exception as msg:
                return HttpResponse(msg)
            else:
                return redirect('submitted')

    elif request.method == 'GET':
        return render(request, 'index.html')


@receiver(post_save, sender=submit_info)
def send_submission_notification(sender, instance, created, **kwargs):
    if created:
        name = instance.name
        email = instance.email

        send_mail(
            'Form is submitted successfully',
            f'''Hii! {name},
                your form is submitted successfully''',
            'anirudha.djangotestmail@gmail.com',
            [email],
            fail_silently=False,
        )


def submitted(request):
    users = submit_info.objects.all()
    serializer = SubmitSerializer(users, many=True)
    return render(request, 'submited.html', {'submited': serializer.data})
