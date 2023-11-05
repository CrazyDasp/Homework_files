import pprint
cook_book = {}
with open('recipes.txt', 'r', encoding='UTF-8') as file:
    line = file.readline().strip()
    while line:
        dish_name = line
        ingredient_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_line = file.readline().strip()
            ingredient_parts = ingredient_line.split(' | ')
            ingredient_name = ingredient_parts[0]
            quantity = int(ingredient_parts[1])
            measure = ingredient_parts[2]
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish_name] = ingredients
        line = file.readline().strip()
        line = file.readline().strip()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for name_dish in cook_book[dish]:
            if name_dish['ingredient_name'] not in shop_list:
                shop_list[name_dish['ingredient_name']] = {'measure': name_dish['measure'], 'quantity': name_dish['quantity'] * person_count}
            else:
                shop_list[name_dish['ingredient_name']]['quantity'] += name_dish['quantity'] * person_count
    return shop_list
pprint.pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2))
