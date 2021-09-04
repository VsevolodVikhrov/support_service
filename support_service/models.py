from django.contrib.auth.models import User
from django.db import models


class Theme(models.Model):
    scope_name = models.CharField(max_length=50)

    def __str__(self):
        return self.scope_name


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    theme = models.OneToOneField(Theme, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=300)
    date_created = models.TimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_frozen = models.BooleanField(default=False)
    is_in_processing = models.BooleanField(default=False)
    is_answered = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Staff(models.Model):
    specialist = models.ForeignKey(User, on_delete=models.CASCADE)
    responsibility_scope = models.ManyToManyField(Theme)

    def __str__(self):
        return self.specialist.username


class Processing(models.Model):
    specialist = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ticket = models.ManyToManyField(Ticket)


class Message(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)
    date_answered = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ticket.title
