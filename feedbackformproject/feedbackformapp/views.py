from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
# Create your views here.

import datetime
date1 = datetime.datetime.now()

def feedback_view(request):

    if request.method == 'POST':
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

        data = FeedbackData(
            name = name,
            rating = rating,
            feedback = feedback,
            date =date1
        )
        data.save()
        fform = FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        context = {'form':fform,'feedbacks':feedbacks}
        return render(request,'feedback.html',context)

    else:
        fform = FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        context = {'form':fform,'feedbacks':feedbacks}
        return render(request,'feedback.html',context)