from django.db import models

class Message(models.Model):
    content = models.TextField()
    alias = models.CharField(max_length=50)  # New field for alias
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} ({self.alias}): {self.content}"
