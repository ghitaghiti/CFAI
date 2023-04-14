from django.shortcuts import render

def home(request):
    lang_list=['c', 'clike', 'cpp', 'csharp', 'css', 'go', 'html', 'java', 'javascript', 'julia', 'markup', 'php', 'python']

    return render(request, 'home.html', {'lang_list': lang_list})
