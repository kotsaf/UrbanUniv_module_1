my_dict = {'Safar': 2002, 'Misha': 2000, 'Sasha': 2001}
print(my_dict)
print(my_dict['Safar'])
print(my_dict.get('Sonya'))
my_dict.update({'Inal': 1999,
                'Alex': 1998})
del my_dict['Misha']
print(my_dict)

my_set = {1, 2, 3, 4, 5, 1}
print(my_set)
my_set = {1, 2, 3, 4, 5, 1, (1, 2, 3), 'Tall'}
my_set.discard((1, 2, 3))
print(my_set)