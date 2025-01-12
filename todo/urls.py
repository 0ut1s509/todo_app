from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('tasks/',views.Tasklist.as_view(),name='tasks')

]