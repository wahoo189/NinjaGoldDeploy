from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = ''

    return render(request, 'appNinjaGold/index.html')

def process_gold(request):
    choice = request.POST['choice']
    newGold = 0

    if choice == 'farm':
        newGold = random.randrange(10, 21)
    if choice == 'house':
        newGold = random.randrange(2, 6)
    if choice == 'cave':
        newGold = random.randrange(5, 11)
    if choice == 'casino':
        newGold = random.randrange(-50, 51)

    activity = "You have entered the {} and you have received {} gold! ({})"
    activity = activity.format(choice, newGold, datetime.datetime.now())
    request.session['activity'] = activity + request.session['activity']
    request.session['total_gold'] += newGold

    return redirect('/')

def reset(request):
    request.session['total_gold'] = 0
    request.session['activity'] = ''
    return redirect('/')
