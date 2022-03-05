from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    # dictionary containing meetups information
    meetups = [
        { 
            'title': '1st meetup',
            'location': 'New York',
            'slug': 'a-fst-meetup' 
        },
        { 
            'title': '2nd meetup',
            'location': 'Paris',
            'slug': 'a-snd-meetup' 
        }
    ]

    return render(request, "meetups/index.html", {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'First meetup',
        'description': 'This is the first meetup'
        }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
    })