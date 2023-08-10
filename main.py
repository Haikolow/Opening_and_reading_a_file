from pprint import pprint


with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        recipe_name = line.strip()
        ing_qty = int(f.readline())
        ing = []
        for _ in range(ing_qty):
            ingredient_name, quantity,  measure = f.readline().strip().split(' | ')
            ing.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        cook_book[recipe_name] = ing
        f.readline()

pprint(cook_book, sort_dicts=False)


def shop_list(cook_book, dishes, person_count):

    list_ = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * int(person_count)
                measure = ingredient['measure']
                # pprint(f' 1 - {result}')
                if name not in list_.keys():
                    list_[name] = {
                        'measure': measure,
                        'quantity': quantity
                    }
                else:
                    list_[name]['quantity'] +=quantity
    return list_


menu_=[]

for dish in cook_book.keys():
    menu_.append(dish)
print('Menu: ')
for i, dish in enumerate(menu_, 1):
    print(f' {i}. {dish}')
print('\nPlease select dishes number(s) from the list: ')
print('To stop the input enter "-" ')
dishes = []


while True:
    menu = input()

    if menu == '-':
        break
    elif not menu.isdigit():
        print('Please try again.')
    elif 1 > int(menu) or int(menu) > len(menu_):
        print('Please try again.')
    else:
        dishes.append(menu_[int(menu)-1])


while True:
    person_count = input('Please enter the number of persons: ')

    if not person_count.isdigit():
        print('Please try again.')
    elif int(person_count) < 1:
        print('Please try again.')
    else:
        break


pprint(shop_list(cook_book, dishes, person_count), sort_dicts=False)