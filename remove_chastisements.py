from datacenter.models import Chastisement
from schoolkid_utils import get_schoolkid_by_name


def remove_chastisements(schoolkid_name):
    """Удаляет все замечания для указанного ученика"""
    child = get_schoolkid_by_name(schoolkid_name)
    chastisements = Chastisement.objects.filter(schoolkid=child)
    deleted_count, _ = chastisements.delete()
    print(f"\nДля {child.full_name} удалено {deleted_count} замечаний")
    return deleted_count


if __name__ == "__main__":
    remove_chastisements("Иван")
