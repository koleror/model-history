from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Sample
from .forms import SampleForm

def list_samples(request):
    samples = Sample.objects.all()
    return render(request, 'list_samples.html', {'samples': samples})

def one_sample(request, id):
    s = get_object_or_404(Sample, id=id)
    if request.method == "POST":
        form = SettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = SampleForm(instance=s)
    return render(request, 'one_sample.html', {'form': form})
