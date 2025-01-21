from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title