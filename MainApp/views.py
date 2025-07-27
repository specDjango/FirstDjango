from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
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
<br>Имя: <b>Максим</b></br>
<br>фамилия: <b>Луганцев</b>
<br>Отчество: <b>Викторович</b>
<br>Телефон: <b>89150511104</b>
<br>e-mail: <b>maxim.lugantsev@mail.ru</b>

    """
    return HttpResponse(text)

def item_detail(request,id):

    context ={
        "itemtoreturn":items[id]
            }
   
              
    return render(request,"item.html",context)
    
def getallitems(request):
    result ="<h1> список товаров</h1><ol>"
    for item in items:
            result +=f""" <li><a href='/item/{item["id"]}'> {item["name"]} </a></li>"""
    result +="</ol"

    context ={"products": items}
    
    return render(request,"allproducts.html",context)