from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.models import Lines

import random

#_______________________________________
def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

#_______________________________________



def show_main_page(request):
    content = Lines.objects.all()
    return render(request, 'core/Main_page.html', {'Lines':content})

def refresh_page(request):
    content = Lines.objects.all()
    return render(request, 'core/Create_tmpl.html', {'Lines':content}) #redirect('show_main_page')

def create_line(request):

    #  Добваление id вручную
    if len(Lines.objects.all()) != 0:
        max_id = max([i.id for i in Lines.objects.all()]) + 1
    else: max_id = 0
    Lines.objects.create(id=max_id).save()
    content = Lines.objects.all()

    return render(request, 'core/Create_tmpl.html', {'Lines':content}) #redirect('show_main_page')

def delete_line(request):
    victim = Lines.objects.filter(id=int(request.GET['delete']))[0]
    victim.delete()
    content = Lines.objects.all()
    return render(request, 'core/Create_tmpl.html', {'Lines':content})

def edit_line(request):
    #print('\n\n\n\n\n' + str(request.GET) + '\n\n\n\n\n')
    edit = Lines.objects.filter(id=int(request.GET['edit']))[0]
    temp = request.GET

    if (is_integer(temp['freq']) != True) or (is_integer(temp['number']) != True): #if (temp['number'] == '') or (temp['freq'] == '') or (temp['freq'].is_integer() != True) or (temp['freq'].is_integer() != True):
        edit.status = 'Ошибка ввода'
        edit.save()

    else:
        edit.number = int(temp['number'])
        edit.freq = int(temp['freq'])
        edit.status = 'Активно'
        edit.save()

    content = Lines.objects.all()
    return render(request, 'core/Create_tmpl.html', {'Lines':content}) #redirect('show_main_page')

def stop_line(request):
    stopped = Lines.objects.filter(id=int(request.GET['stop']))[0]
    stopped.status = 'Остановлено'
    stopped.save()
    content = Lines.objects.all()
    return render(request, 'core/Create_tmpl.html', {'Lines':content}) #redirect('show_main_page')

def AJAX_test(request):

    return HttpResponse(str(random.uniform(1,10)) + ' Гц')