from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import *
from .models import *

# Create your views here.
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/project_create.html'
    success_url = '/project/projectlist'

    def form_valid(self, form):
        return super().form_valid(form)
    
class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projectlist'

    def get_queryset(self):
        return super().get_queryset()

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/project_create.html'
    success_url = '/project/projectlist'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'projectdetail'

    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(project_id = self.kwargs['pk'])
        return render(request, self.template_name, {'projectdetail': self.get_object(), 'team':team})
    
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    success_url = '/project/projectlist'
    context_object_name = 'projectdelete'

    # def get(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)
    
    # success_url = 'project/projectlist'
    
class ProjectTeamCreateView(CreateView):
    model = ProjectTeam
    form_class = ProjectTeamCreationForm
    template_name = 'project/projectteam_create.html'
    success_url = '/project/projectteamlist'

    def form_valid(self, form):
        return super().form_valid(form)
    
class ProjectTeamListView(ListView):
    model = ProjectTeam
    template_name = 'project/projectteam_list.html'
    # success_url = '/project/projectteam_list'
    context_object_name = 'projectteamlist'

    def get_queryset(self):
        return super().get_queryset()
    
class ProjectTeamUpdateView(UpdateView):
     model = ProjectTeam
     form_class = ProjectTeamCreationForm
     template_name = 'project/projectteam_create.html'
     success_url = '/project/projectteamcreate'
     
    
class ProjectTeamDetailView(ListView):
    model = ProjectTeam
    template_name = 'projectteam/projectteam_detail.html'
    context_object_name = 'projectteamdetail'
    

    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(project_id = self.kwargs['pk'])
        return render(request, self.template_name, {'projectteamdetail': self.get_object(), 'team':team})
    #  def get_queryset(self):
    #      return super().get_queryset()

class ProjectTeamDeleteView(DeleteView):
    model = ProjectTeam
    template_name = 'project/projectteam_delete.html'
    success_url = '/project/projectteamdelete'
    context_object_name = 'projectteamdelete'
    
    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(project_id = self.kwargs['pk'])
        return render(request, self.template_name, {'projectteamdelete': self.get_object(), 'team':team})



    
class CreateProjectModule(CreateView):
    model = ProjectModule
    form_class = CreateProjectModuleForm
    template_name = 'project/create_project_module.html'
    success_url = '/project/listprojectmodule/'

    def form_valid(self, form):
        user = form.save()
        return redirect('listprojectmodule')
        

class ProjectModuleListByProject(ListView):
    model = ProjectModule
    template_name = 'project/list_project_module.html'
    success_url = '/project/listprojectmodule'
    context_object_name = 'listprojectmodule'
    
class ProjectModuleDetailView(DetailView):
    model = ProjectModule
    template_name = 'project/detail_project_module.html'
    # success_url = '/project/detailprojectmodule'
    context_object_name = 'detailprojectmodule'

    def get(self, request, *args, **kwargs):
         team = ProjectTeam.objects.filter(project_id = self.kwargs['pk'])
         return render(request, self.template_name, {'detailprojectmodule': self.get_object(), 'team':team})
    
    # def get_queryset(self):
    #     return super().get_queryset().filter(project_id=self.kwargs['pk'])


class CreateProjectTask(CreateView):
    model = Task
    form_class = CreateProjectTaskForm
    template_name = 'project/create_project_task.html'
    success_url = '/project/project_task_list/'

class ProjectTaskListByProject(ListView):
    model = Task
    template_name = 'project/project_task_list.html'
    context_object_name = 'project_task_list'

class ProjectTaskDetailView(DetailView):
    model = Task
    template_name = 'project/project_task_detail.html'
    context_object_name = 'project_task_detail'

    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(project_id = self.kwargs['pk'])
        return render(request, self.template_name, {'project_task_detail': self.get_object(), 'team':team})


# class TaskUpdateView(UpdateView):
#     model = Task
#     form_class = CreateProjectModuleForm
#     template_name = 'project/project_task_create.html'
#     success_url = '/project/project_task_list/' 
    
class ProjectTaskDeleteView(DeleteView):
    model = Task
    template_name = 'project/project_task_delete.html'
    success_url = '/project/project_task_list'
    context_object_name = 'project_task_delete'

class ProjectTaskUpdateView(UpdateView):
    model = Task
    form_class = CreateProjectTaskForm
    template_name = 'project/create_project_task.html'
    success_url = '/project/project_task_list'

    # def form_valid(self, form):
    #     return super().form_valid(form)

class ProjectTaskView(UpdateView):
    model = Task
    form_class = CreateProjectTaskForm
    template_name = 'project/assign_task.html'
    success_url = '/project/project_task_list'
    
    # def form_valid(self, form):
    #     return super().form_valid(form)