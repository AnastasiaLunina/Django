import csv
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for each_phone in phones:
            phone = Phone(each_phone.get('id'), each_phone.get('name'), each_phone.get('price'),
                          each_phone.get('image'), each_phone.get('release_date'), each_phone.get('lte_exists'),
                          slugify(each_phone.get('name'), allow_unicode=True))
            phone.save()
