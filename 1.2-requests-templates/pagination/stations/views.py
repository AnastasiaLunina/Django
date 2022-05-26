from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def read_csv():
    content = []
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        # content.extend(reader)
        for row in reader:
            content.append({
                "Name": row['Name'],
                "Street": row['Street'],
                "District": row['District']
            })
    return content


def bus_stations(request):
    content = read_csv()
    page_range = Paginator(content, 10)
    current_page = request.GET.get('page', 1)
    page = page_range.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
