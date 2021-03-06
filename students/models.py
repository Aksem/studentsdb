from django.db import models

# Create your models here.
class Student(models.Model):
    """Створюємо модель студента"""
    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"

    first_name = models.CharField(
        max_length = 256,
        blank = False,
        verbose_name =u"Ім'я"
    )
    last_name = models.CharField(
        max_length = 256,
        blank = True,
        verbose_name = u"Прізвище"
    )
    middle_name = models.CharField(
        max_length = 256,
        blank = True,
        verbose_name = u"По-батькові",
        default = ''
    )
    birthday = models.DateField(
        blank = False,
        verbose_name = u"Дата народження",
        null = True
    )
    photo = models.ImageField(
        blank = True,
        verbose_name = u"Фото",
        null = True
    )
    ticket = models.CharField(
        max_length = 256,
        blank = False,
        verbose_name = u"Білет"
    )
    notes = models.TextField(
        blank = True,
        verbose_name = u"Додаткові нотатки"
    )
    student_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Group(models.Model):
    """Модель групи створена по типу моделі студента!"""
    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва"
        )
    leader = models.OneToOneField(
        'Student',
        verbose_name=u"Староста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
        )
    notes = models.TextField(
    blank=True,
    verbose_name=u"Додаткові нотатки"
        )
    def __str__(self):
        return self.title
