from django.apps import AppConfig


class ConstructorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'constructor'

    class Meta:
        verbose_name = 'Конструктор'
        verbose_name_plural = 'Конструкторы'