from django.shortcuts import render
import datetime

# Create your views here.
def set_info(request):
    template = 'userColor/set_info.html'

    if request.method == 'POST':
        username = request.POST['username'],
        color = request.POST['color']

        if 'visit_count' in request.session:
            request.session['visit_count'] += 1
            
        else:
            request.session['visit_count'] = 1

        request.session['last_visit'] = str(datetime.datetime.now())

        response = render(request, 'userColor/get_info.html', {
            'username': username,
            'color': color,
            'visit_count': request.session['visit_count'],
            'last_visit': request.session['last_visit']

        })

        response.set_cookie('username', username)
        response.set_cookie('color', color)

        return response

    return render(request, template, {})


def get_info(request):
    template = 'userColor/get_info.html'

    username = request.COOKIES.get('username', 'Unknown')
    color = request.COOKIES.get('color', 'ffffff')

    visit_count = request.session.get('visit_count', 0)
    last_visit = request.session.get('last_visit', 'unknown')

    return render(request, template, {
        'username': username,
        'color': color,
        'visit_count': visit_count,
        'last_visit': last_visit
    })