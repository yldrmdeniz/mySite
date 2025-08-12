from django.db import models
from django.urls import reverse


class Task(models.Model):
    DO = 'do'
    PLAN = 'plan'
    DELEGATE = 'delegate'
    FORGET = 'forget'
    CATEGORY_CHOICES = [
        (DO, 'Do'),
        (PLAN, 'Plan'),
        (DELEGATE, 'Delegate'),
        (FORGET, 'Forget'),
    ]

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    action = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    importance = models.IntegerField(choices=[(1, 'High'), (0, 'Low')])
    urgence = models.IntegerField(choices=[(1, 'High'), (0, 'Low')])
    is_two_mins = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    domain = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('tasks:board')

    def __str__(self):
        return self.description[:50]
