from django.shortcuts import redirect, render
from django.contrib import messages
import openai
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def home(request):

    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'go', 'html',
                 'java', 'javascript', 'julia', 'markup', 'php', 'python']
    if request.method == 'POST':
        code = request.POST['code']
        lang = request.POST['lang']

        if lang == "Select Programming Language":
            messages.success(request,"You Forgot To Pick A Programming Language...")
            return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
        
        else:
            openai.api_key=""
            openai.Model.list()
            try:
                response=openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Respond only with code. Fix this lang: {lang} code:{code}",
                temperature=0,
                max_tokens=2000,
                top_p=1.0,
                frequency_penalty=0.0)
                response= (response["choices"][0]["text"]).strip()
                return render(request, 'home.html', {'lang_list': lang_list, 'response': response, 'lang': lang})
            except Exception as err:
                return render(request, 'home.html', {'lang_list': lang_list, 'code':err, 'lang': lang})

    return render(request, 'home.html', {'lang_list': lang_list})

def suggest(request):

    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'go', 'html',
                 'java', 'javascript', 'julia', 'markup', 'php', 'python']
    
    if request.method == 'POST':
        code = request.POST['code']
        lang = request.POST['lang']

        if lang == "Select Programming Language":
            messages.success(request,"You Forgot To Pick A Programming Language...")
            return render(request, 'suggest.html', {'lang_list': lang_list, 'code': code, 'lang': lang})

        else:
            openai.api_key=""
            openai.Model.list()
            try:
                response=openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Respond only with code. lang:{lang} code:{code}",
                temperature=0,
                max_tokens=2000,
                top_p=1.0,
                frequency_penalty=0.0)
                response= (response["choices"][0]["text"]).strip()
                return render(request, 'suggest.html', {'lang_list': lang_list, 'response': response, 'lang': lang})
          
            except Exception as err:
                return render(request, 'suggest.html', {'lang_list': lang_list, 'code':err, 'lang': lang})

    return render(request, 'suggest.html', {'lang_list': lang_list})
    

def login_user(request):
    if request.method =="POST":
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request,username=username, password=password)  
        if user is not None:
            login(request, user, messages.success(request, "You Have Been Login In"))  
            return redirect('home')
        else:
            messages.succes(request,"Error Loggin In Please try Again")
            return redirect('home')
    else:
        return render(request,'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method =="POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user= authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"You Have Registred... congratulations!!")
            return redirect('home')
        else:
            form=SignUpForm()
        return render(request, 'register.html',{"form":form})
    