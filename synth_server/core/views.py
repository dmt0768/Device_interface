from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.models import Lines


def show_main_page(request):
    content = Lines.objects.all()
    return render(request, 'core/Main_page.html', {'Lines':content})

def create_line(request):

    #  Добваление id вручную
    if len(Lines.objects.all()) != 0:
        max_id = max([i.id for i in Lines.objects.all()]) + 1
    else: max_id = 0
    Lines.objects.create(id=max_id).save()
    return redirect('show_main_page')

def delete_line(request):
    victim = Lines.objects.filter(id=int(request.GET['delete']))[0]
    victim.delete()
    return redirect('show_main_page')

def edit_line(request):
    #print('\n\n\n\n\n' + str(request.GET) + '\n\n\n\n\n')
    edit = Lines.objects.filter(id=int(request.GET['edit']))[0]
    temp = request.GET

    if (temp['number'] == 'None') or (temp['freq'] == 'None'):
        edit.status = 'Ошибка ввода'
        edit.save()

    else:
        edit.number = int(temp['number'])
        edit.freq = int(temp['freq'])
        edit.status = 'Активно'
        edit.save()

    #content = Lines.objects.all()
    return redirect('show_main_page')

def stop_line(request):
    stopped = Lines.objects.filter(id=int(request.GET['stop']))[0]
    stopped.status = 'Остановлено'
    stopped.save()
    return redirect('show_main_page')