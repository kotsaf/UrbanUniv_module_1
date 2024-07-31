immutable_var = 5, False, 'Горы', [1, 2, 3]
print(immutable_var)

#immutable_var [0] = 4
#print(immutable_var)        #ошибка выходит пот причине того, что мы пытаемся изменить кортеж, хотя он постоянен и неизменяем

mutable_list = [1, 2, 3, 4, 5, 6]
mutable_list[0] = 6
mutable_list[5] = 1
print(mutable_list)