from rest_framework import generics
from rest_framework import permissions

from support_service.filters import TicketFilter
from support_service.models import Theme, Ticket
from support_service.serializers import ThemeSerializer, TicketSerializer


class TicketView(generics.ListAPIView):
    model = Ticket
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_class = TicketFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Ticket.objects.all()
        else:
            print(self.request.user)
            return Ticket.objects.filter(user=user)
