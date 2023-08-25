# def murat():
#     print("Geeks")
# murat()

# #set frosent - int, str, float, bool, list, tuple, set, frozenset
# nums1 = [1,2,3,4,5]
# nums2 = [3,4,5,6,7]
# nums3 = nums1 + nums2
# print(set(nums3))

# names = {'Nurbolot', 'Kurmanbek', 'Murat', 'Bayastan', 'Nurbolot'}
# print(names)

# numbers = {10, 20, 30, 40, 50, 60, 70, 70}
# print(numbers)

# cars = {'BMW', 'Tesla', 'Mercedes'}
# print(cars)
# cars.add('Honda')
# print(cars)
# cars.add('BMW')
# cars.remove('Tesla')
# print(cars)
# cars.pop()
# print(cars)

# st = {1, 1.0, True, "1"}
# print(st)


# frosenset
# frzn = frozenset({1, 2, 3, 3, 3, 4, 5, 5, 6})
# print(frzn)
# frzn.add(100)
# print(frzn)
# Dictionary - словари
# student = {'name':'Askhat', 'age':20}
# print(student)
# print(student['name'])
# print(student['age'])
# student.setdefault('language', 'Python')
# print(student)
# student.pop('age')
# print(student)
# student['language'] = 'JavaScript'
# print(student)

# tesla_modex_x = {'brand':'Tesla', 'Model':'Model X', 'year':2023, 'color':'white'}
# print(tesla_modex_x)
# print(tesla_modex_x.keys())
# print(tesla_modex_x.values())
# print(tesla_modex_x.items())

# for key, value in tesla_modex_x.items():
#     print(key, value)

# contact = {'MCHS':'112'}
# while True:
#     command = input("1 - посмотреть, 2 - добавить, 3 - удалить, 4 - обновить: ")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("Имя: ")
#         add_number = input("Номер: ")
#         contact.setdefault(add_name, "успешно добавлен")
#     elif command == "3":
#         delete_name = input("Кого добавить")
#         contact.pop("delete_name")
#         print(delete_name, "успешно удален")
#     elif command == "4":
#         update_name = input("Кого обновить: ")
#         new_number = input("Новый номер: ")
#         contact[update_name] = new_number
#         print("Контакт", update_name, "Успешно обновлен")
#     else:
#         print("Такой команды нету")