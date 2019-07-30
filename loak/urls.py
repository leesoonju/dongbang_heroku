from django.contrib import admin
from django.urls import path
import jaksung.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jaksung.views.home, name="home"),
    path('submit/', jaksung.views.submit, name="submit"),
    path('reple/', jaksung.views.reple, name="reple"),
]