# quiz/views.py
import random
from django.shortcuts import render
from .models import Country

def quiz_view(request):
    if request.method == 'POST':
        country_id = int(request.POST['country_id'])
        user_answer = request.POST['answer']
        
        country = Country.objects.get(id=country_id)
        is_correct = (user_answer == country.capital)

        return render(request, 'result.html', {
            'country': country,
            'user_answer': user_answer,
            'is_correct': is_correct
        })

    # GET request – náhodná otázka
    country = random.choice(list(Country.objects.all()))
    
    # vybereme 3 náhodné jiné možnosti
    wrong_options = list(
        Country.objects.exclude(id=country.id).order_by('?')[:3]
    )
    
    options = [country.capital] + [c.capital for c in wrong_options]
    random.shuffle(options)  # zamícháme
    
    return render(request, 'questions.html', {
        'country': country,
        'options': options
    })
