from django.shortcuts import render, redirect
from .forms import ParticipantResponseForm
from .models import ParticipantResponse

from django.contrib import messages

def form_view(request):
    if request.method == 'POST':
        form = ParticipantResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)

            # Check if absences_count is not empty before saving
            absences_count_value = form.cleaned_data['absences_count']
            response.absences_count = int(absences_count_value) if absences_count_value else 0

            response.save()

            # Add a success message
            messages.success(request, 'Form submitted successfully!')

            # Redirect to a different URL after successful form submission
            

    else:
        form = ParticipantResponseForm()

    return render(request, 'form.html', {'form': form})

def show_responses(request):
    responses = ParticipantResponse.objects.all()
    print(responses)
    return render(request, 'responses.html', {'responses': responses})
