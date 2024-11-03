# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, n=','):
    first_group = set(str1.split(n))
    second_group = str2.split(n)
    common_set = first_group.intersection(second_group)
    common_list = []
    for i in common_set:
        common_list.append(i)
    common_list.sort()
    return common_list
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, '|')