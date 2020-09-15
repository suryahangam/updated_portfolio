from django.db import models
from django.contrib.auth.models import User


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    in_date = models.DateField(null=True)
    out_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exp_title = models.CharField(max_length=255)
    in_date = models.DateField()
    out_date = models.DateField(null=True)
    company_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.exp_title


class RecentWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_cover_image = models.ImageField()
    work_title = models.CharField(max_length=100)
    work_description = models.TextField()
    work_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Recent Works"


SKILL_LEVEL =[
    (1, 'Fundamental Awarness (basic knowledge)'),
    (2, 'Novice (limited experience)'),
    (3, 'Intermediate (practical application)'),
    (4, 'Advanced (applied theory)'),
    (5, 'Expert (recognized authority)'),
]

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_title = models.CharField(max_length=100)
    skill_level = models.IntegerField(choices=SKILL_LEVEL)
    skill_description = models.TextField()

    def __str__(self):
        return self.skill_title


class Experties(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experties_title = models.CharField(max_length=100)
    experties_description = models.TextField()

    def __str__(self):
        return self.experties_title


class Numbers(models.Model):
    cups_of_coffee = models.IntegerField()
    projects = models.IntegerField()
    clients = models.IntegerField()
    partners = models.IntegerField()

    def __str__(self):
        return str(self.id)


class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv_file = models.FileField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.created_date)

    class Meta:
        verbose_name_plural = 'CV'


class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    contact_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contacts'
        managed = False
    