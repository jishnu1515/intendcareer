from django.shortcuts import render
from .models import ComingSoon

def comingsoon(request):
    if request.POST:
        email = request.POST['email']

        # checking if email already exists
        if ComingSoon.objects.filter(email=email).exists():
            return render(request, 'comingsoon.html', {'error': True, 'message': 'Already subscribed to our newsletter! Stay tuned!'})
        
        commingsoon = ComingSoon.objects.create(email=email)
        commingsoon.save()

        return render(request, 'comingsoon.html', {'success': True, 'message': 'Thank you for subscribing to our newsletter! Stay tuned!'})

    return render(request, 'comingsoon.html')
