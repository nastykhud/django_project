from django.http import HttpResponse
from django.shortcuts import render

user_f = 'Худякова'
user_i = 'Анастасия'
user_o = 'Дмитриевна'
user_t = '8-111-111-11-11'
user_e = 'hudyakova@bmstu.ru'

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

#Домашняя страница
def home(request):
    user_fio = user_f + ' ' + user_i[0] + '.' + user_o[0] + '.'
    text = f"""<h1>"Изучаем django"</h1>
            <strong>Автор</strong>: <i>{user_fio}</i>"""
    return HttpResponse(text)

#О проекте
def about(request):
    text = f""" Имя: <strong>{user_i}</strong> <br>
    Отчество: <strong>{user_o}</strong> <br>
    Фамилия: <strong>{user_f}</strong> <br>
    телефон: <strong>{user_t}</strong> <br>
    email: <strong>{user_e}</strong>
    """
    return HttpResponse(text)

#Страница товара
def item_info(request, num):
    
    #собираю в лист все id
    ids = []
    for i in items:
        ids.append(i['id'])

    if (num in ids): #если нужный id в списке
        text = f"""id: <strong>{num}</strong> <br>
        Наименование: <strong>{items[ids.index(num)]['name']}</strong> <br>
        Количество: <strong>{items[ids.index(num)]['quantity']}</strong> <br>"""
    else: #если нужный id не в списке
        text = f"""Товар с id = {num} не найден"""
    
    #Гиперссылка на список товаров
    text += """<a href = "/items">Назад к списку товаров</a>"""
    
    return HttpResponse(text)

#Список товаров
def items_info(request):
    text = """<h2>Список товаров</h2><ol>"""
    for i in items:
        text += f"""<li><a href = "item/{i['id']}">{i['name']}</a></li>"""
    text += """</ol>"""
    return HttpResponse(text)
