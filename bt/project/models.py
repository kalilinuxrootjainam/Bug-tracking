from django.db import models
# from django.contrib.auth.models import AbstractUser
from user.models import User

class Project(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=500)
    technology = models.CharField(max_length=100)
    estimatedHours = models.PositiveIntegerField()
    startDate = models.DateField()
    completionDate = models.DateField()

    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Project'

class ProjectTeam(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Project_team'

class Status(models.Model):
    statusName = models.CharField(max_length=20, null=False, unique=True)

    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.statusName

    class Meta:
        db_table = 'status'

class ProjectModule(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    moduleName = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=30)
    estimatedHours = models.PositiveIntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    startDate = models.DateField(null=True)
    endedDate = models.DateField(null=True)

    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.moduleName

    class Meta:
        db_table = 'Project_module'

priorityChoice =  (("High" ,"High") ,("Low" ,"Low") ,("Normal" ,"Normal"))

class Task(models.Model):
    module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    priority = models.CharField(choices=priorityChoice ,max_length=30)
    description = models.CharField(max_length=500, null=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    totalMinutes = models.PositiveIntegerField()

    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_task'


# class ProjectModule(models.Model):
#      project = models.ForeignKey(Project, on_delete=models.CASCADE)
#      moduleName = models.CharField(max_length=100)
#      description = models.TextField()
#      estimeted_hours = models.IntegerField()
#      status = models.CharField(max_length=100)
#      startDate = models.DateField()
#      created_at = models.DateTimeField(auto_now_add=True)
#      updated_at = models.DateTimeField(auto_now=True)
    
#      class Meta:
#          db_table = 'project_module'
    
#      def __str__(self):
#          return self.moduleName
