from rest_framework import generics, status
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import decorators
from rest_framework.response import Response

from support_service.filters import TicketFilter
from support_service.models import Theme, Ticket
from support_service.serializers import ThemeSerializer, TicketSerializer


class TicketView______(generics.ListAPIView):
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


class TicketView______(generics.ListAPIView):
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


class TicketView(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Ticket.objects.all()

    def perform_create(self, serializer):
        """Implemented for setting creator of ticket behind the scenes"""
        user = self.request.user
        serializer.save(user=user)

    def get_queryset(self):
        """Implemented for users. Allows to see only self-created tickets"""
        user = self.request.user
        return Ticket.objects.filter(user=user)

    @decorators.action(detail=True, methods=['get'], permission_classes=[permissions.IsAdminUser])
    def get_ticket(self, request, pk=None):
        """Implemented for staff only. Allows staff to get any ticket,
        even if it created by another user"""
        ticket = Ticket.objects.filter(id=pk)
        response_data = self.get_serializer(ticket, many=True)
        return Response(response_data.data, status=status.HTTP_200_OK)

    @decorators.action(detail=True, methods=['patch'], permission_classes=[permissions.IsAdminUser])
    def update_ticket(self, request, pk=None):

        return Response(status=status.HTTP_200_OK)

