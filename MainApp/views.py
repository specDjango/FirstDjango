from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    text = """
    <h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>Луганцев М.В.</i>

    """
    return HttpResponse(text)
# Create your views here.

def about(request):
    text ="""
<br>Имя: <b>Максим</b></br>
<br>фамилия: <b>Луганцев</b>
<br>Отчество: <b>Викторович</b>
<br>Телефон: <b>89150511104</b>
<br>e-mail: <b>maxim.lugantsev@mail.ru</b>

    """
    return HttpResponse(text)

def item_detail(request,id):
    return HttpResponse('<p> Item with id {0}</p>'.format(id))
