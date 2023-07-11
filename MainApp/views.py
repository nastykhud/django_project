from django.http import HttpResponse
from django.shortcuts import render

#Глобальные переменные
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

#Главная страница
def home(request):
    user_fio = user_f + ' ' + user_i[0] + '.' + user_o[0] + '.'
    context = {'key1': user_fio}
    return render(request, "main_page.html", context)

#О проекте
def about(request):
    context = {'name': user_i, 'midname': user_o, 'surname': user_f,
                'phone': user_t, 'mail': user_e}
    return render(request, "about_page.html", context)

#Страница товара
def item_info(request, num):
    
    #собираю в лист все id
    ids = []
    for i in items:
        ids.append(i['id'])

    if (num in ids): #если нужный id в списке
        context = {'item': items[ids.index(num)]}
        return render(request, "show_page.html", context)

    else: #если нужный id не в списке
        context = {'id': num}
        return render(request, "show_none_page.html", context)

#Список товаров
def items_info(request):
    context = {"items": items}
    return render(request, "list_page.html", context)