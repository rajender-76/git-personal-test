
from django.db import models

class students(models.Models):
    name = models.CharField(max_length = 200)
    age = models.CharField()
    section = models.CharField()
    department = models.CharField()
    id = models.CharField()



class department(models.Models):   
    section = models.CharField()
    department = models.CharField()
    id = models.CharField()


<<<<<<< HEAD
=======
class Newdepartment(models.Models):   
    section = models.CharField()
    department = models.CharField()
    id = models.CharField()


class Newdepartment(models.Models):   
    section = models.CharField()
    department = models.CharField()
    id = models.CharField()

>>>>>>> dev



