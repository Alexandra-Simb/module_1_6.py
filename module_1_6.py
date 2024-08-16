my_dict = {'Sasha': 1993, 'Pasha': 1997}
print(my_dict)
print(my_dict.get('Sasha'))
print(my_dict.get('Masha'))
my_dict.update({'Masha': 1992, 'Dasha': 1998})
print(my_dict.get('Pasha'))
my_dict.pop('Pasha')
print(my_dict)
my_set = {1,1,1, 2,3, 'World', False, True, 5}
print(my_set)
my_set.remove('World')
print(my_set)

