from datacenter.models import Lesson, Commendation
from schoolkid_utils import get_schoolkid_by_name
import random


COMMENDATION_TEXTS = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
]

def create_commendation(schoolkid_name, subject_title):
    """Создает похвалу для ученика по указанному предмету"""
    try:      
        child = get_schoolkid_by_name(schoolkid_name)
        if child is None:
            raise ValueError(f"Ученик '{schoolkid_name}' не найден")

        lesson = Lesson.objects.filter(
            year_of_study=child.year_of_study,
            group_letter=child.group_letter,
            subject__title=subject_title
        ).order_by('-date').first()

        if not lesson:
            print(f"Урок по предмету '{subject_title}' не найден")
            return

        Commendation.objects.create(
            text=random.choice(COMMENDATION_TEXTS),
            created=lesson.date,
            schoolkid=child,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
        print(f"Создана похвала для {child.full_name} по предмету {subject_title}")
        
    except Exception as e:
        print(f"\nОшибка при создании похвалы: {str(e)}")


if __name__ == "__main__":
    create_commendation("Фролов Иван Григорьевич", "Математика")
