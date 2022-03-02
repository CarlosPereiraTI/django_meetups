from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    # dictionary containing meetups information
    meetups = [
        { 'title': '1st meetup' },
        { 'title': '2nd meetup' }
    ]

    return render(request, "meetups/index.html", {
        'show_meetups': True,
        'meetups': meetups
    })