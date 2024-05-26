from django.db import models

# Create your models here.

class Room(models.Model):
    user1 = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='user2')

    def __str__(self):
        return self.user1.username + ' - ' + self.user2.username
    




