"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from data.views import DashboardView, HomeView, PerformenceView, SchemaView, TrendingView, KeteranganView

from manage_user.views.login import ChangePasswordAdminView, UserLoginView, UserLogoutView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("", include('manage_user.urls'), name="manage_users"),
    path('auth/', include([
        path("login", UserLoginView.as_view(), name="login"),
        path("logout", UserLogoutView.as_view(), name="logout"),
        path('change-password/<int:user_id>/', ChangePasswordAdminView.as_view(), name="change-password"),
    ])),
    
    path('admin/', admin.site.urls),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("trending", TrendingView.as_view(), name="trending"),
    path("performance", PerformenceView.as_view(), name="performance"),
    path("schema", SchemaView.as_view(), name="schema"),
    path("keterangan", KeteranganView.as_view(), name="keterangan"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)