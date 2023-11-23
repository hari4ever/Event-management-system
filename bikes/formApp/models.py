from django.db import models
    
class Mydata(models.Model) :
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 199) 
    email = models.CharField(max_length = 199)
    
    def __str__(self) -> str:
        return self.username
    
class registerdata(models.Model) :
    username = models.CharField(max_length = 100)
    ph_no = models.CharField(max_length = 199) 
    email = models.CharField(max_length = 199)
    address = models.CharField(max_length = 199)
    
    def __str__(self) -> str:
        return self.username
    