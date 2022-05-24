from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse, reverse_lazy


# TODO: change the 'work_time' field 
class Constructor(models.Model):
    inn = models.IntegerField(verbose_name='ИНН', validators=[MinValueValidator(10)])
    ogrn = models.IntegerField(verbose_name='ОГРН', validators=[MinValueValidator(13)])
    title = models.CharField(max_length=100, verbose_name='Название')
    country = models.CharField(max_length=100, verbose_name='Страна')
    region = models.CharField(max_length=100, verbose_name='Регион')
    city = models.CharField(max_length=100, verbose_name='Населенный пункт')
    index = models.IntegerField(verbose_name='Индекс', validators=[MinValueValidator(6)])
    adress = models.CharField(max_length=100, verbose_name='Адрес')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Раздел')
    sub_category = models.ForeignKey('SubCategory', on_delete=models.PROTECT, verbose_name='Подраздел')
    heading = models.CharField(max_length=100, verbose_name='Рубрика')
    keywords = models.CharField(max_length=100,blank=True, verbose_name='Ключевые слова')
    phone = models.IntegerField(verbose_name='Телефон', validators=[MinValueValidator(11)])
    cell_phone = models.IntegerField(verbose_name='Сотовый телефон', validators=[MinValueValidator(11)])
    metro = models.CharField(max_length=100, blank=True, verbose_name='Метро(остановка)')
    email = models.EmailField(max_length=254, verbose_name='Email')
    site = models.CharField(max_length=100, verbose_name='Сайт')
    vk = models.CharField(max_length=100, verbose_name='Vk')
    twtr = models.CharField(max_length=100, verbose_name='Twitter')
    fb = models.CharField(max_length=100, verbose_name='Facebook')
    inst = models.CharField(max_length=100, verbose_name='Instagram')
    x = models.FloatField(help_text='xx.xxxxxx', max_length=8, verbose_name='X', validators=[MinValueValidator(8)])
    y = models.FloatField(help_text='xx.xxxxxx', max_length=8, verbose_name='Y', validators=[MinValueValidator(8)])
    additional = models.TextField(help_text='Дополнительная информация', blank=True, verbose_name='Дополнительно')
    work_time = models.CharField(max_length=50, verbose_name='Время работы')

    def get_absolute_url(self):
        return reverse('inn', kwargs={'pk' : self.pk})

    def __str__(self):
        return f'{self.inn}'

    class Meta:
        verbose_name = 'Конструктор'
        verbose_name_plural = 'Конструкторы'

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Раздел')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class SubCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='Подраздел')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подраздел'
        verbose_name_plural = 'Подразделы'


class Shortcode(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Раздел')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name='Подраздел')
    title = models.CharField(max_length=100, default='default.html' , verbose_name='Шорткод')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Шорткод'
        verbose_name_plural = 'Шорткоды'


#class Template(models.Model):
#     category = models.CharField(max_length=100, unique=True, verbose_name="Раздел", db_column="Раздел")
#     sub_category = models.CharField(max_length=100, unique=True, verbose_name="Подраздел", db_column="Подраздел")
#     title = models.CharField(max_length=100, default="default.html", verbose_name="Темплейт")

#     def __str__(self):
#         return self.title
     

# class ShortCodes(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Название компании")
#     inn = models.IntegerField(verbose_name="ИНН")
#     adress = models.CharField(max_length=100, verbose_name="Адрес")

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = 'Шорткод'   