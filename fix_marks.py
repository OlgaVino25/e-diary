from datacenter.models import Mark
from schoolkid_utils import get_schoolkid_by_name


def fix_marks(schoolkid_name):
    """Исправляет плохие оценки (2 и 3) на 5 для указанного ученика"""
    child = get_schoolkid_by_name(schoolkid_name)
    
    if not child:
        return 0
        
    bad_marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    updated_count = bad_marks.update(points=5)
    print(f"Для {child.full_name} исправлено {updated_count} плохих оценок")
    return updated_count


if __name__ == "__main__":
    fix_marks("Иван")
