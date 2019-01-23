from django.db import models
from django.contrib.auth.models import User

# Tree of things in the platform

# -Subject
# --Course
# ---Module
# ----Content img
# ----Content vid
# ----Content txt
# ---Module 2


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title


class Course(models.Model):
    
    # Instructor that created the course
    owner = models.ForeignKey(User,
                              related_name='courses_created',
                              on_delete=models.CASCADE)

    # Subject that this course is about
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    # Slug will be used in URL later
    slug = models.SlugField(max_length=200, unique=True)

    # Overview of the course
    overview = models.TextField()

    #Setting a field that adds date and time automatically on create
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title