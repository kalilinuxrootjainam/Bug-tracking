from django.contrib import admin
from django.urls import path
from .views import ManagerRegisterView, DeveloperRegisterView, TeamLeaderRegisterView, TesterRegisterView, UserLoginView, UserLogoutView, indexView,ManagerDashboardView,DeveloperDashboardView,ProjectTaskList
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('managerregister/', ManagerRegisterView.as_view(), name='managerregister'),
    path('developerregister/', DeveloperRegisterView.as_view(), name='developerregister'),
    path('teamleaderregister/', TeamLeaderRegisterView.as_view(), name='teamleaderregister'),
    path('testerregister/', TesterRegisterView.as_view(), name='testerregister'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/',LogoutView.as_view(), name='logout'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('index/', indexView, name='index'),

    path('managerdashboard/',ManagerDashboardView.as_view(),name="managerdashboard"),
    path('developerdashboard/',DeveloperDashboardView.as_view(),name="developerdashboard"),
    path('developerdashboard/projecttasklist/',ProjectTaskList.as_view(),name='projecttasklist'),
    #path('adminpage/',AdminPage.as_view(),name="adminpage"),
    #path('userprofile/',UserProfileView.as_view(),name="userprofile"),
    #path('userprofileupdate/<int:pk>',UserProfileUpdateView.as_view(),name="userprofileupdate"),
]