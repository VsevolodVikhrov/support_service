from rest_framework import serializers

from support_service.models import Theme, Staff, Ticket, Message


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'
        read_only_fields = ('id',)


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        read_only_fields = ('id',)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('id', 'user')

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id', 'user')

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
