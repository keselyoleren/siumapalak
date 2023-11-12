# myapp/urls.py
from django.urls import path, include
from manage_user.views.user_views import *

urlpatterns = [
    path("user/", include([
        path('', AccountUserListView.as_view(), name='user-list'),
        path('create/', AccountUserCreateView.as_view(), name='user-create'),
        path('update/<int:pk>/', AccountUserUpdateView.as_view(), name='user-update'),
        path('delete/<int:pk>/', AccountUserDeleteView.as_view(), name='user-delete'),
    ])),
]
