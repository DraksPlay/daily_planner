from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('auth/', include('django.contrib.auth.urls')),
    path("signup/", SignUp.as_view(), name="signup"),
    path("create_task/", create, name="create"),
    path("delete_tasks/", delete_tasks, name="delete_tasks"),
    path("edit_task/", edit_task, name="edit_task"),
    path("set_session/", set_session, name="set_session"),
]
