import csv
import sys
import os

project_dir = "/Users/vladaradchenko/Documents/Rental_Car_WEB/mysite"
sys.path.append(project_dir)

# Переменная DJANGO_SETTINGS_MODULE – это путь Python к файлу с параметрами. Например, если предположить, что каталог mysite включен
# в путь Python, значением переменной DJANGO_SETTINGS_MODULE для нашего текущего примера будет ‘mysite.settings’.
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django

django.setup()

from rentalcar.models import Car
from django.core.files.images import ImageFile


def main():
    with open("data_table.csv", "r") as in_file:
        data = csv.reader(in_file, delimiter='\t')
        next(data)  # skip header line
        for line in data:
            car = Car()
            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, 'media/images/cars_pictures', line[0])
            car.photo = ImageFile(open(filename, "rb"), name=line[0])
            car.name = line[1]
            car.type = line[2]
            car.brand = line[3]
            car.num_of_passengers = line[4]
            car.price_per_day = line[5]
            car.air_conditioning = line[6]
            car.automatic_transmission = line[7]
            car.doors_4 = line[9]

            car.save()


if __name__ == '__main__':
    main()
