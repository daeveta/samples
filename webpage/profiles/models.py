from django.db import models


class Students(models.Model):
    name = models.CharField('Name', max_length=20)
    surname = models.CharField('Surname', max_length=20)
    grade = models.CharField('Grade', max_length=10)

    def __str__(self):
        return self.name
        #f'[{self.id}] {self.name} {self.surname} {self.grade}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
