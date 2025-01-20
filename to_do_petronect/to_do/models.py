from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    pub_date = models.DateField(auto_now=True)
    due_date = models.DateField()

    def __str__(self):
        return self.title

class Task_list(models.Model):
    title = models.CharField(max_length=100)
    tasks = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title