from django.shortcuts import render
from question.models import Questions

# Create your views here.
def question_details(request):
    obj = Questions.objects.all()
    context = {
    "object_list":obj,

    }
    return render(request,"home.html",context)
