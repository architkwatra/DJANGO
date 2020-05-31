from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # return render(request, 'polls/index.html',context)
    return HttpResponse(template.render(context, request))

def getQuestionId(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Either Question not found or it does not exixts")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # return HttpResponse("you are looking at the results of the question %s" %question_id) 

def vote(request, question_id):
    print("hjgsdfhsfdhsfhsfhsfgjf", request) 
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'you did not select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
    return HttpResponse("You are voting on the question %s" % question_id) 


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': 'you did not select a choice',
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
#     return HttpResponse("You are voting on the question %s" % question_id) 
