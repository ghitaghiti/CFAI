from django.shortcuts import render
from django.contrib import messages
import openai

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
            openai.api_key="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"
            openai.Model.list()
            try:
                response=openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Respond only with code. Fix this{lang} code:{code}",
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
    return render(request, 'suggest.html', {})
    
