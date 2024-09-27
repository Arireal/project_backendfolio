from django.contrib import admin
from django.urls import path
from portfolio import views  # Import views from your portfolio app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.portfolio_view, name='portfolio'),  # Direct the root URL to the portfolio view
]
