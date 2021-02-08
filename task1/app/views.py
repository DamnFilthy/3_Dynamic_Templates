import csv
from django.shortcuts import render
from django.conf import settings

res_dict = {}
res_list = []
csvfile = open(settings.FILE_CSV, encoding='utf-8')
reader = csv.DictReader(csvfile, delimiter=';')
result = [item for item in reader]
for i in range(len(result)):
    # print(result[i]['Год'])
    res_dict['Год'] = result[i]['Год']
    res_dict['Янв'] = result[i]['Янв']
    res_dict['Фев'] = result[i]['Фев']
    res_dict['Мар'] = result[i]['Мар']
    res_dict['Апр'] = result[i]['Апр']
    res_dict['Май'] = result[i]['Май']
    res_dict['Июн'] = result[i]['Июн']
    res_dict['Июл'] = result[i]['Июл']
    res_dict['Авг'] = result[i]['Авг']
    res_dict['Сен'] = result[i]['Сен']
    res_dict['Окт'] = result[i]['Окт']
    res_dict['Ноя'] = result[i]['Ноя']
    res_dict['Дек'] = result[i]['Дек']
    res_dict['Суммарная'] = result[i]['Суммарная']
    res_list.append(res_dict.copy())


def inflation_view(request):
    template_name = 'inflation.html'

    context = {'res_list': res_list}

    return render(request, template_name,
                  context)
