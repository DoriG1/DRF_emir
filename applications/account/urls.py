from django.urls import path
from applications.account.views import RegisterApiView, ActivationApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view())
]