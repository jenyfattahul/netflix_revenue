from django.urls import path
from .views import login_view, home_view, report_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('report/', report_view, name='report'),
    path('logout/', logout_view, name='logout'),
]
