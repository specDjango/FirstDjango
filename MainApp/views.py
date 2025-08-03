from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

items = [
{"id": 0, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 1, "name": "Куртка кожаная" ,"quantity":2},
{"id": 2, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 3, "name": "Картофель фри" ,"quantity":0},
{"id": 4, "name": "Кепка" ,"quantity":124},
]


#def home(request)
 #   text = """
  #  <h1>"Изучаем django"</h1>
#<strong>Автор</strong>: <i>Луганцев М.В.</i>
 #   """
  #  return HttpResponse(text)

 ##  return render(request,template)

def home(request) -> HttpResponse:
    context = { 
    "name": "Ivanov Ivan Ivanovich",
    "email": "ivanov@mail.ru"
    }
    return render(request,"index.html",context)



# Create your views he

def about(request):
    text ="""

      <header>
        <a href="/"> Home </a> <br>
        <a href="/getallitems"> Список товаров</a><br>
        <a href="/about">About</a>
    </header>

<br>Имя: <b>Максим</b></br>
<br>фамилия: <b>Скрыто</b>
<br>Отчество: <b>Викторович</b>
<br>Телефон: <b>8*15******04</b>
<br>e-mail: <b>mlugants@mail.ru</b>



    """
    return HttpResponse(text)

def item_detail(request,id):
    context ={"itemtoreturn":items[id]}
    return render(request,"item.html",context)
    
def getallitems(request):
    result ="<h1> список товаров</h1><ol>"
    for item in items:
            result +=f""" <li><a href='/item/{item["id"]}'> {item["name"]} </a></li>"""
    result +="</ol"

    context ={"products": items}
    
    return render(request,"allproducts.html",context)