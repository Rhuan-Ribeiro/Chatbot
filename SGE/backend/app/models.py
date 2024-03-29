from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# criando uma classe de usuário customizada para substituir a padrão com atributos desejados:

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email adress", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    registrationNumber = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email" # substituir o login username por e-mail
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class Equipments(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    assigneeFK = models.ForeignKey(CustomUser, related_name='assigneeEquipament', on_delete=models.CASCADE)

    def __str__(self):
        return self.code


BLOCKS = [
        ("A","Bloco A"),
        ("B","Bloco B"),
        ("C","Bloco C"),
]


class Environments(models.Model):
    name = models.CharField(max_length=100)
    block = models.CharField(max_length=30, choices=BLOCKS)

    def __str__(self):
        return self.name

TASK_TYPE = [
        ("MA","Manutenção"),
        ("ME","Melhoria"),
]

TASK_STATUS = [
        ("AB","Aberta"),
        ("EA","Em Andamento"),
        ("CA","Cancelada"),
        ("CO","Concluída"),
        ("EN","Encerrada")
]

class Tasks(models.Model):
    environmentFk = models.ForeignKey(Environments, related_name='taskEnvironments', on_delete = models.CASCADE)
    reporterFk = models.ForeignKey(CustomUser, related_name='taskCustomUser', on_delete = models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=2000)
    diagnostic = models.CharField(max_length=300, null=True, blank=True)
    type = models.CharField(max_length=100, choices=TASK_TYPE)
    status = models.CharField(max_length=100, choices=TASK_STATUS)
    # environmentAlocationFk = models.ForeignKey(EnvironmentsLocation, related_name='taskEnviromentAlocation', on_delte= models.CASCADE)

    def __str__(self):
        return self.title
    
class TaskAssignes(models.Model):
    taskFk = models.ForeignKey(Tasks, related_name="taksAssignesTask", on_delete=models.CASCADE)
    AssignesFk = models.ForeignKey(CustomUser, related_name="taksAssignesCustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.taskFk.title
    
class TaskAssignees(models.Model):
    taskFk = models.ForeignKey(Tasks, related_name='taskAssigneesTask', on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name='taskAssigneesAssignees', on_delete=models.CASCADE)

    def __str__(self):
        return self.str(id)
    
class TaskStatus(models.Model):
    taskFk = models.ForeignKey(Tasks, related_name = "taskAssignesTask", on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=TASK_STATUS)
    creationDate = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.status
    
FILE_TYPE = [
    ("D","Document"),
    ("P","Photo"),
]
    
class FileTaskStatus(models.Model):
    taskStatusFk = models.ForeignKey(TaskStatus, related_name = "fileTaskStatusTaskStatus", on_delete=models.CASCADE)
    link = models.CharField(max_length=300)
    fileType = models.CharField(max_length=100, choices=FILE_TYPE)

    def __srt__(self):
        return self.fileType
    
class TasksEquipaments(models.Model):
    taskFk = models.ForeignKey(Tasks, related_name="tasksEquipamentsTask" , on_delete=models.CASCADE)
    equipmentFk = models.ForeignKey(Equipments, related_name="tasksEquipamentsEquipaments" , on_delete=models.CASCADE)

    def __str__(self):
        return self.taskFk.title