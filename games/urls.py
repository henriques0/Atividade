from django.urls import path
from .views import IndexView

urlpatterns = [
	path('HOME', IndexView.as_view(), name="index"),
]
