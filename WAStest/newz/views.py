from django.shortcuts import render
from django.http import HttpResponse
from newz.models import Story


def index(request):
    latest_question_list = Story.objects.order_by('-pub_date')[:5]
    context = {'latest_story_list': latest_question_list}
    return render(request, 'newz/index.py', context)


