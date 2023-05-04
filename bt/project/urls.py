from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('projectcreate/', ProjectCreateView.as_view(), name='projectcreate'),
    path('projectlist/', ProjectListView.as_view(), name='projectlist'),
    path('projectteamcreate/', ProjectTeamCreateView.as_view(), name='projectteamcreate'),
    path('projectteamlist/', ProjectTeamListView.as_view(), name='projectteamlist'),
    path('projectteamdetail/',ProjectTeamDetailView.as_view(),name='projectteamdetail'),
    path('projectteamdelete/',ProjectTeamDeleteView.as_view(), name='projectteamdelete'),
    path('projectteamupdate/', ProjectTeamUpdateView.as_view(), name='projectteamupdate'),
    path('projectupdate/<int:pk>', ProjectUpdateView.as_view(), name='projectupdate'),
    path('projectdetail/<int:pk>', ProjectDetailView.as_view(), name='projectdetail'),
    path('projectdelete/<int:pk>', ProjectDeleteView.as_view(), name='projectdelete'),
    path('createprojectmodule/',CreateProjectModule.as_view(),name='createprojectmodule'),
    path('listprojectmodule/',ProjectModuleListByProject.as_view(),name='listprojectmodule'),
    path('detailprojectmodule/<int:pk>', ProjectDetailView.as_view(), name='detailprojectmodule'),
    path('create_project_task/',CreateProjectTask.as_view(),name='create_project_task'),
    path('project_task_list/',ProjectTaskListByProject.as_view(),name='project_task_list'),
    path('project_task_delete/<int:pk>',ProjectTaskDeleteView.as_view(),name='project_task_delete'),
    path('project_task_update/<int:pk>',ProjectTaskUpdateView.as_view(),name='project_task_update'),
    path('project_task_detail/<int:pk>',ProjectTaskDetailView.as_view(),name='project_task_detail'),
    path('project_task_assign/<int:pk>',ProjectTaskView.as_view(),name='project_task_assign'),
]
