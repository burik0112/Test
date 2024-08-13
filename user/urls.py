from django.urls import path

from user.views import TimeSheetAPIView

urlpatterns = [
    path('list/', TimeSheetAPIView.as_view()),
    path('list/<int:pk>/', TimeSheetAPIView.as_view())
]