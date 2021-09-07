from django.urls import path

from support_service.views import TicketView

urlpatterns = [
    path('ticket/', TicketView.as_view(), name='ticket'),
]