from django.http import HttpResponse
from django.shortcuts import render
from MainApp.models import Item

#Глобальные переменные
user_f = 'Худякова'
user_i = 'Анастасия'
user_o = 'Дмитриевна'
user_t = '8-111-111-11-11'
user_e = 'hudyakova@bmstu.ru'

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
    
    try:
        context = {'item': Item.objects.get(id = num)}
        return render(request, "show_page.html", context)
    except: #если нужный id не в списке
        context = {'id': num}
        return render(request, "show_none_page.html", context)

#Список товаров
def items_info(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "list_page.html", context)