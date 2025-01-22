from django.db import models
from datetime import date, timedelta

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    done = models.BooleanField(default=False)
    
    def expire(self):
        today = date.today()
        yestarday = today - timedelta(days=1)
        if self.due_date < yestarday and self.done == False:
            return True
        return False

    def __str__(self):
        return self.title