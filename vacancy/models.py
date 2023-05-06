from django.db import models


class Category(models.Model):
    title = models.TextField("Название", unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Region(models.Model):
    state = models.CharField("Область", max_length=55, unique=True)
    city = models.CharField("Город", max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.state


class Vacancy(models.Model):
    title = models.CharField("Название", max_length=50)
    desc = models.TextField("Описание")
    require = models.TextField("Требования")
    company = models.CharField('Компания', max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', to_field='title')
    count = models.IntegerField(default=0, null=True)
    state = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='states', to_field='city')
    contact = models.CharField(max_length=13)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title
