from django.core.exceptions import ValidationError


def get_path_upload_image(instance, file):
    """Путь для хранения аватарок format:(media)/publicate/user_id/photo.jpg"""
    return f"publicate/{instance.id}/{file}"


def validate_size_image(file_object):
    """Проверка размера файла"""
    size_limit = 2
    if file_object.size > size_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер {size_limit}MB")
