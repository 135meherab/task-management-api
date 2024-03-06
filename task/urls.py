from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('list', views.TaskViewSets)


urlpatterns = [
    path('', include(router.urls)),
    path('complete/<int:pk>', views.TaskCompleteViewSets.as_view({'put': 'update'}), name="task_complete"),
    path('delete/<int:pk>', views.DeleteTask.as_view(), name="delete_task"),
]
