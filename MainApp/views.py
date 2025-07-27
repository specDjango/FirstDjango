from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
 #   text = """
  #  <h1>"Изучаем django"</h1>
#<strong>Автор</strong>: <i>Луганцев М.В.</i>
 #   """
  #  return HttpResponse(text)

    template = "index.html" 
    return render(request,template)

# Create your views he

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

    for item in items:
            if item['id']==id:
                 result = f"""
        <h2> имя: {item["name"]}</h2>
        <p>количество: {item["quantity"]}</p>

        <p><a href="/getallitems">Назад к списку товаров</a></p>
       
                 """
                 return HttpResponse(result)

    return HttpResponseNotFound('<p> Item not found with id {0}</p>'.format(id))

def getallitems(request):
    result ="<h1> список товаров</h1><ol>"
    for item in items:
            result +=f""" <li><a href='/item/{item["id"]}'> {item["name"]} </a></li>"""
    result +="</ol"

    return HttpResponse(result)