from django.shortcuts import render
from django.contrib import messages


def home(request):
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'go', 'html',
                 'java', 'javascript', 'julia', 'markup', 'php', 'python']
    if request.method == 'POST':
        code = request.POST['code']
        lang = request.POST['lang']

        if lang == "Select Programming Language":
            messages.success(request,"You Forgot To Pick A Programming Language...")
            return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
        return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
    
    return render(request, 'home.html', {'lang_list': lang_list})

