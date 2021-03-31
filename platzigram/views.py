from django.http import HttpResponse
from datetime import datetime
import json


def hello_world(request):

    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse(
        'Hello World, current server time {now}'.format(now=now)
    )


def sorted_numbers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers_ = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sorted_numbers_,
        'message': 'Integers sorted successfully'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def hi(request, name, age):

    if age < 18:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)

    return HttpResponse(message)
