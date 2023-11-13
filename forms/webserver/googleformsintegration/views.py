from django.shortcuts import render, redirect
from .forms import ParticipantResponseForm
from .models import ParticipantResponse
from django.views.decorators.csrf import csrf_protect

def form_view(request):
    if request.method == 'POST':
        form = ParticipantResponseForm(request.POST)
        if form.is_valid():
            # Convert selected disability choices to integers
            form.cleaned_data['participant_disability'] = [int(choice) for choice in form.cleaned_data['participant_disability']]

            # Save the form data without committing to the database
            response = form.save(commit=False)

            # Assign the disability choices to the response object
            response.participant_disability.set(form.cleaned_data['participant_disability'])

            # Save the response object to the database
            response.save()

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
