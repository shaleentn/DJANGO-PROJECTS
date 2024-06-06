from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, index, signup, resource_list, upload_resource





urlpatterns = [
  path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('resources/', resource_list, name='resource_list'),
    path('upload/', upload_resource, name='upload_resource'),
]
