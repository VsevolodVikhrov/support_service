from django_filters import rest_framework as filters

from support_service.models import Ticket


class TicketFilter(filters.FilterSet):
    id = filters.CharFilter(field_name="id", lookup_expr='exact')

    class Meta:
        model = Ticket
        fields = ['id']