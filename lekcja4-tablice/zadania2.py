vegetables = ['carrot','potato','tomato','cucumber', 'potato']

shopping_list = (vegetables)

shopping_list.insert(0, "water")

print(shopping_list)

'''
shopping_list.remove("potato")
shopping_list.remove("potato")
shopping_list.remove("potato")
'''

ilosc_potatoes = shopping_list.count('potato')

print(ilosc_potatoes)

shopping_list.remove("potato")
shopping_list.remove("potato")

print("lista bez zmiorow")
print(shopping_list)

element_do_kupienia = shopping_list.pop(0)
print(element_do_kupienia)
#print('\n')
print(shopping_list)

#print("nie mam pieniedzy")

#shopping_list.clear()

shopping_list.sort()

print(shopping_list)