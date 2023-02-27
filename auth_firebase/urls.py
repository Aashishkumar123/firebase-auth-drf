from django.urls import path
from auth_firebase import views


urlpatterns = [
    path('',views.StudentAPIView.as_view(),name="test-api"),
]
