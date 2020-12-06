from django.db import models

"""my Todo app"""

class Todo(models.Model):
    context = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.context
