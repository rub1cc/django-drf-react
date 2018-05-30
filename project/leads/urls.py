from django.urls import path
from leads import views

urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view())
]
