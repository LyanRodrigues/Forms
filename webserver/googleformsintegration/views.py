from django.shortcuts import render, redirect
from .forms import ParticipantResponseForm
from .models import ParticipantResponse

def form_view(request):
    if request.method == 'POST':
        form = ParticipantResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('responses')
        else:
            print(form.errors)  # Add this line to print form validation errors
    else:
        form = ParticipantResponseForm()

    return render(request, 'form.html', {'form': form})


def show_responses(request):
    responses = ParticipantResponse.objects.all()
    print(responses)
    return render(request, 'responses.html', {'responses': responses})