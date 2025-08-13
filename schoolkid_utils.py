from datacenter.models import Schoolkid


def get_schoolkid_by_name(schoolkid_name):
    """Находит ученика по имени или части имени.
    Returns:
        - объект ученика, если найден ровно один
        - None, если не найден или найдено несколько
    При этом выводит соответствующие сообщения
    """
    try:
        return Schoolkid.objects.get(full_name__icontains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print(
            f"Учеников с именем '{schoolkid_name}' не найдено\n"
            "   Проверьте правильность ввода имени"
        )
    except Schoolkid.MultipleObjectsReturned:
        students = Schoolkid.objects.filter(full_name__icontains=schoolkid_name)
        print(
            f"Найдено {students.count()} учеников с именем содержащим '{schoolkid_name}':\n"
            "----------------------------------------"
        )
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.full_name} (класс {student.year_of_study}{student.group_letter})")
        print("Пожалуйста, уточните полное имя ученика из списка выше")
    return None
