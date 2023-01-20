from time import strftime
import datetime as dt
import xlwt

from datetime import datetime
from django.contrib import messages, auth
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.safestring import mark_safe
from django.views.generic import UpdateView, DeleteView
from .models import Detect, Category
from .forms import DetectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('gatnasyk')
        else:
            messages.info(request, 'Girizilen maglumat ýalňyş')
            return redirect('/')
    else:
        return render(request, 'base/home.html')


@login_required(login_url='/')
def gatnasyk(request):
    detect = Detect.objects.all()
    categories = Category.objects.all()
    rows = request.GET.get('_export', None)
    context = {
        'detect': detect,
        'name': 'Ady',
        'categories': categories,
        'rows': rows,
    }
    return render(request, 'base/gatnasyk.html', context=context)


@login_required(login_url='/')
def hasaba_almak_sanow(request):
    detect = Detect.objects.all()
    categories = Category.objects.all()
    context = {
        'detect': detect,
        'name': 'Ady',
        'categories': categories,
    }
    return render(request, template_name='base/hasaba_almak_sanow.html', context=context)


@login_required(login_url='/')
def get_category(request, category_id):
    detect = Detect.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'base/gatnasyk.html', {'detect': detect, 'categories': categories, 'category': category})


@login_required(login_url='/')
def add_detect(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = DetectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hasaba_almak_sanow')
    else:
        form = DetectForm()
    return render(request, 'base/add_detect.html', {'form': form, 'categories': categories})


@login_required(login_url='/')
def deleteDetect(request, pk):
    detect = Detect.objects.get(id=pk)
    if request.method == 'POST':
        detect.delete()
        return redirect('hasaba_almak_sanow')
    return render(request, 'base/delete.html', {'obj': detect})



@login_required(login_url='/')
def search(request):
    detect = Detect.objects.all()
    category = Category.objects.all()

    if request.GET.get("q") is not None:
        q = request.GET.get('q')
        detect = Detect.objects.filter(Q(name__icontains=q) | Q(surname__icontains=q))

    return render(request, 'base/search.html', {'detect': detect, 'category': category})


@login_required(login_url='/')
def get_search_category(request, category_id):
    detect = Detect.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'search_by_categories.html',
                  {'detect': detect, 'categories': categories, 'category': category})


class UpdateDetect(LoginRequiredMixin, UpdateView):
    template_name = 'base/detect_form.html'
    model = Detect
    success_url = reverse_lazy('hasaba_almak_sanow')
    fields = ['name', 'surname', 'photo', 'category']

    def get_queryset(self):
        queryset = super(UpdateDetect, self).get_queryset()
        queryset.update()
        return queryset


@login_required(login_url='/')
def export_excel_file(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="gatnasyk.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('base_detect')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'surname', 'category', 'photo', 'time_in', 'time_out']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Detect.objects.all().values_list('name', 'surname', 'category', 'photo', 'time_in', 'time_out')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num], dt.datetime):
                date_time = row[col_num].strftime('%d-%m-%Y %H:%M:%S')
                ws.write(row_num, col_num, date_time, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def logout(request):
    auth.logout(request)
    return redirect('/')

