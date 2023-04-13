from django.shortcuts import render
from .forms import contactForm


def contact(request):
    if request == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
    else:
        form = contactForm()
    return render(request, 'contact.html', {'form': form})
