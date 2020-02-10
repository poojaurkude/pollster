from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse

from .models import Question, Choice, Vote
from django.contrib.auth.models import User, auth

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def home(request):
    return render(request, 'home.html')


def index(request):
    latest_question_list = Question.objects.all()
    for qstn in latest_question_list:
        print(qstn.question_text)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

# Show specific question and choice


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExits:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})


# get question and display results

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

# vote


def vote(request, question_id):
    # if request.user.is_authenticated:
    #     question = get_object_or_404(Question, pk=question_id)
    #     try:
    #         selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #     except (KeyError, Choice.DoesNotExist):
    #         return render(request, 'detail.html', {'question': question, 'error_message': "You did not select a choice", })
    #     else:
    #         selected_choice.votes += 1
    #         selected_choice.save()
    #         return HttpResponseRedirect(reverse('app:results', args=(question_id,)))
    # else:
    #     print("Please login")
    #     return redirect('app:home')
        
    question = get_object_or_404(Question, pk=question_id)
    
    
    if Vote.objects.filter(question=question,vote=request.user).exists():
        messages.error(request,"Already Voted on this Question")
        return redirect('app:index')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question': question, 'error_message': "you did not select a choice", })
    
    else:
        
        selected_choice.votes += 1
        selected_choice.save()
        v= Vote(question=question,vote=request.user)
        v.save()
        
        return HttpResponseRedirect(reverse('app:results', args=(question_id,)))



# Login


def register(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conformPassword = request.POST.get('conformpassword')
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        print('user created')
        return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        print('login successfull')
        if user is not None:
            auth.login(request, user)
            return redirect('app:index')
        else:
            message.info(request, 'Invalid credentials')
            return redirect('app:login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def voter(request):
    voter = Vote.objects.all()
    return render(request,'showvoter.html',{'voter':voter})

