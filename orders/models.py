from django.contrib.auth import get_user_model
from django.db import models

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Owner: {self.user.email}. Created at:{str(self.created_at)}"

    class Meta:
        ordering = ["-created_at"]

