from django.db import models

# Create your models here.
class Gym(models.Model):
    title = models.CharField(max_length=255)
    description_first = models.TextField()
    image=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title


class Gym_d(models.Model):
    name = models.CharField(max_length=255)
    description_second = models.TextField()
    image=models.URLField(blank=True,null=True)
    slug = models.SlugField()
    def __str__(self):
        return self.name


class Gym_r(models.Model):
    name = models.CharField(max_length=255)
    description_second = models.TextField()
    image=models.URLField(blank=True,null=True)
    slug = models.SlugField()
    def __str__(self):
        return self.name



class Gym_S(models.Model):
    title = models.CharField(max_length=255)
    description_first = models.TextField()
    image=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    image=models.URLField(blank=True,null=True)
    description_first = models.TextField()
    def __str__(self):
            return self.name

class Comment(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    comment = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name

class Classes(models.Model):
    name = models.CharField(max_length=255)
    tabs=models.CharField(max_length=255)
    description_second = models.TextField()
    image=models.URLField(blank=True,null=True)
    slug = models.SlugField()
    def __str__(self):
        return self.name
class Classes_tabs(models.Model):
    name = models.CharField(max_length=255)
    image=models.URLField(blank=True,null=True)
    tabs = models.CharField(max_length=255)
    slug = models.SlugField()
    def __str__(self):
        return self.name