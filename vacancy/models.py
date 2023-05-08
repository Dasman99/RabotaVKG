from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.TextField("Название", unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField("Название", max_length=100)
    desc = models.TextField("Описание", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Region(models.Model):
    state = models.CharField("Область", max_length=55, unique=True)
    city = models.CharField("Город", max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return f'{self.city},{self.state}'


class Vacancy(models.Model):
    title = models.CharField("Название", max_length=50)
    desc = models.TextField("Описание")
    require = models.TextField("Требования")
    salary = models.IntegerField(default=0)
    company = models.ForeignKey(Company, max_length=100, on_delete=models.CASCADE, related_name='company')
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


class TopVacancy(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='top_vacancy')

    class Meta:
        verbose_name = "Топ Вакансии"
        verbose_name_plural = "Топ Вакансии"

    def __str__(self):
        return f'{self.vacancy}'