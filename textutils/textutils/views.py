# i have created this file -saloni
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get  the text 
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    fullsmall=request.GET.get('fullsmall','off')
    spacerem=request.GET.get('spacerem','off')
    charcount=request.GET.get('charcount', 'off')
    
    if removepunc =="on":
        punctuations='''.,?!:;'"—-()[].../{ }<>'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'analyzed_text':analyzed}
        djtext=analyzed
        #analyze the text
        #return render(request,'analyze.html',params)
    
    if(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'analyzed_text':analyzed}
        djtext=analyzed
        #analyze the text
        #return render(request,'analyze.html',params)
    
    if(newlineremover == "on"):
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params={'analyzed_text':analyzed}
        djtext=analyzed
        #analyze the text
        #return render(request,'analyze.html',params)

    if(fullsmall == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params={'analyzed_text':analyzed}
        djtext=analyzed
        #analyze the text
        #return render(request,'analyze.html',params)

    if(spacerem == "on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not (index < len(djtext) - 1 and djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params={'analyzed_text':analyzed}
        djtext=analyzed
        #analyze the text
        
    return render(request,'analyze.html',params)
    
    if charcount =="on":
        analyzed=len(djtext)
        analyzed=analyzed
        params={'analyzed_text':analyzed}
        #analyze the text
        return render(request,'analyze.html',params)
    
    
