grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(set(students))                                                  #перевод множества в список и расположение в алфавитном порядке
aver_mark = {'Aaron': sum(grades[0]) / len(grades[0]),
             'Bilbo': sum(grades[1]) / len(grades[1]),
             'Johnny': sum(grades[2]) / len(grades[2]),
             'Khendrik': sum(grades[3]) / len(grades[3]),
             'Steve': sum(grades[4]) / len(grades[4])}                             #присвоение каждому студенту средней оценки
print(aver_mark)



#sum - простая сумма
#len - кол-во объектов
