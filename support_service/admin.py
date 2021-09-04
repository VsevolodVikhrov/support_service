from django.contrib import admin

from support_service.models import Ticket, Theme, Staff, Message, Processing


@admin.register(Ticket)
class Ticket(admin.ModelAdmin):
    fields = ('title', 'theme', 'description', 'date_created', 'is_active',
              'is_frozen', 'is_in_processing', 'is_answered', 'user')
    readonly_fields = ('date_created',)


@admin.register(Theme)
class Theme(admin.ModelAdmin):
    fields = ('scope_name',)


@admin.register(Staff)
class Staff(admin.ModelAdmin):
    fields = ('specialist', 'responsibility_scope')


@admin.register(Processing)
class Processing(admin.ModelAdmin):
    fields = ('specialist', 'ticket')


@admin.register(Message)
class Message(admin.ModelAdmin):
    fields = ('ticket', 'answer', 'date_answered', 'user')
    readonly_fields = ('date_answered',)









