from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyse(request):
    analysed = ''
    param = {'purpose': 'Upper Case', 'analyzed_text': analysed}
    eText = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')

    totalChar = request.GET.get('totalChar', 'off')
    if removepunc == "on":
        analysed = ""
        punc = """!@#$%^&*()-_+=/''"":;<>"""
        for char in eText:
            if char not in punc:
                analysed = analysed + char

        param = {'purpose': 'Text Punctualisation', 'analyzed_text': analysed}
        eText = analysed
        # return render(request, 'analyse.html', param)

    if newlineremover == 'on':
        analysed = ""
        for char in eText:
            if char != "\n" and char != "\r":
                analysed = analysed + char
                if char == " ":
                    analysed = analysed + " "

        print(analysed)
        param = {'purpose': 'Line removed', 'analyzed_text': analysed}
        eText = analysed
        # return render(request, 'analyse.html', param)

    # elif extraspaceremover == 'on':
    #     analysed = ""
    #     analysed = ""
    #     for index, char in enumerate(eText):
    #
    #         if eText[index] == " " and eText[index + 1] == " ":
    #             pass
    #         else:
    #             analysed = analysed + char
    #
    #     param = {'purpose': 'Space remover', 'analyzed_text': analysed}
    #     return render(request, 'analyse.html', param)

    if fullcaps == 'on':
        analysed = ""
        for char in eText:
            analysed = analysed + char.upper()

        param = {'purpose': 'Upper Case', 'analyzed_text': analysed}
        eText = analysed

        # return render(request, 'analyse.html', param)

    if totalChar == "on":
        analysed = 0
        for char in eText:
            if char != " ":
                analysed = analysed + 1

        param = {'purpose': 'Total No. of character', 'analyzed_text': analysed}
    if totalChar != 'on' and fullcaps != 'on' and newlineremover != 'on' and removepunc != 'on':
        return HttpResponse('Please select any of the options ')

    return render(request, 'analyse.html', param)

    # elif totalChar == "on" or removepunc == "on":
