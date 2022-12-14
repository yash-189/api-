
from django.urls import path
from .views import MonthViews,UserViews,CompletePayment

urlpatterns = [
    path('months/', MonthViews.as_view()),
    path('months/<int:id>', MonthViews.as_view()),
    path('user/', UserViews.as_view()),
    path('user/<int:id>', UserViews.as_view()),
     path('payment/', CompletePayment.as_view()),
]