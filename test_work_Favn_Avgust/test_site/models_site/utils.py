from models_site.models import *

def load_data():
    # Load categories
    category_data = """
    1:Товары для дома:None
    2:Посуда для кухни:1
    3:Тарелки:2
    4:Велосипеды:None
    5:Кастрюли:2"""
    for line in category_data.split('\n'):
        fields = line.strip().split(':')
        print(fields[0])
        try:
            category = Category(id=int(fields[0]), title=fields[1])
        except:
            continue
        if fields[2] != 'None':
            category.parent_id = int(fields[2])
        category.save()

    # Load products
    product_data = """
    1:Велосипед:4:100:100.50
    2:Кастрюля 1,5л:5:50:1200
    3:Тарелка 25см:3:1000:25
    4:Кастрюля 3л:5:300.78"""
    for line in product_data.split('\n'):
        fields = line.strip().split(':')
        try:
            product = Product(id=int(fields[0]), title=fields[1], category_id=int(fields[2]), quantity=int(fields[3]), price=float(fields[4]))
        except:
            continue
        product.save()

    print('Data loaded successfully.')