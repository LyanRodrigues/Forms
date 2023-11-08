from django.shortcuts import render, redirect
from .forms import ParticipantResponseForm
from .models import ParticipantResponse
def form_view(request):
    if request.method == 'POST':
        form = ParticipantResponseForm(request.POST)
        if form.is_valid():
            print(request.POST.getlist('participant_disability'))

            form.save()
            return redirect('responses')
        else:
            print(form.errors)
            print(request.POST)
    else:
        form = ParticipantResponseForm()

    return render(request, 'form.html', {'form': form})

def show_responses(request):
    responses = ParticipantResponse.objects.all()
    print(responses)
    return render(request, 'responses.html', {'responses': responses})