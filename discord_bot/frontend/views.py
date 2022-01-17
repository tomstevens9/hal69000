from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Sound
from .forms import SoundForm

@login_required
def index(request):
    if request.method == 'POST':
        form = SoundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    sounds = Sound.objects.all() 
    form = SoundForm()
    context = {
        'sounds': sounds,
        'form': form,
    }
    return render(request, 'frontend/index.html', context)
