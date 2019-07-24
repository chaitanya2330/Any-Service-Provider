from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    body = models.TextField()
    url = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    prize = models.CharField(max_length=255, null= True)
    video = models.FileField(upload_to="videos",null=True, blank=True)



    def summary(self):
        return self.body[:100]

    def pub_date_preety(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title

class Mobile(models.Model):
        name= models.CharField(max_length=255)
        image1 = models.ImageField(upload_to='images/')
        icon1 = models.ImageField(upload_to='images/')
        body1 = models.TextField()
        prize1 = models.CharField(max_length=255, null= True)
        votes_total1 = models.IntegerField(default=1)


        def __str__(self):
            return self.name

from django.db import models

MALE, FEMALE = range(2)
GENDER = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)

CHINESE, SPANISH, ENGLISH, FRENCH, HINDI, ARABIC, RUSSIAN = range(7)
LANGUAGES = (
    (CHINESE, 'CHINESE'),
    (SPANISH, 'SPANISH'),
    (ENGLISH, 'ENGLISH'),
    (FRENCH, 'FRENCH'),
    (HINDI, 'HINDI'),
    (ARABIC, 'ARABIC'),
    (RUSSIAN, 'RUSSIAN'),
)

class Student(models.Model):
    full_name = models.CharField('Full Name', max_length=50)
    gender = models.PositiveSmallIntegerField('Gender', choices=GENDER, default=MALE)
    language = models.PositiveSmallIntegerField('Language', choices=LANGUAGES, default=ENGLISH)
    grades = models.CharField('Grades', max_length=2)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = ('Student')
