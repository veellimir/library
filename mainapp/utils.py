from django.utils.safestring import mark_safe


def html_image(img):
    if img:
        return mark_safe(f'<img src="{img.url}" width="50">')
    return 'Нет изображения'
