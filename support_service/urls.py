from django.urls import path
from rest_framework import routers
from support_service.views import TicketView

# urlpatterns = [
#     path('ticket/', TicketView.as_view(), name='ticket'),
# ]

router = routers.SimpleRouter()
router.register(r'ticket', TicketView)
urlpatterns = router.urls