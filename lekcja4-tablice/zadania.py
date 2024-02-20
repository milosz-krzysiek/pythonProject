#poczytac o tablicach/listach w pythonie i
# sprobowac samemu odniesc sie do elementow listy

'''
funkcje append oraz extend oraz + na liscie
'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
vegetables = ['carrot','potato','tomato','cucumber']
shopping_list_milosz = []
shopping_list_mateusz = []

print(fruits)

fruits.append('strawberry')

print(fruits)

fruit = 'blueberry'

fruits.append(fruit)

print(fruits)

shopping_list_milosz = fruits + vegetables

print("lista milosz: ")
print(shopping_list_milosz)

shopping_list_mateusz.extend(fruits)
shopping_list_mateusz.extend(vegetables)

print("lista mateusz: ")
print(shopping_list_mateusz)