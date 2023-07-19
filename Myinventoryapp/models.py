from django.db import models

class Supplier(models.Model):
    Name = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    Country = models.CharField(max_length=300)
    CreatedAt = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def getName(self):
        return self.Name

    def __str__(self):
        return self.Name + ' - ' + self.City + ', ' + self.Country + ' created at: ' + str(self.CreatedAt)

class WaterBottle(models.Model):

    SKU = models.CharField(max_length=300)
    Brand = models.CharField(max_length=300)
    Cost = models.CharField(max_length=300)
    Size = models.CharField(max_length=300)
    Mouth_Size = models.CharField(max_length=300)
    Color = models.CharField(max_length=300)
    Supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Current_Quantity = models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return self.SKU + ': ' + self.Brand + ', ' + self.Mouth_Size + ', ' + self.Size + ', ' + self.Color + ', supplied by ' + str(self.Supplied_by) + ', ' + self.Cost + ' : ' + str(self.Current_Quantity)

class Account(models.Model):
    acc_user = models.CharField(max_length=300)
    acc_pass = models.CharField(max_length = 300)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + self.acc_user + self.acc_pass
    
    def getUsername(self):
        return self.acc_user

    def getPassword(self):
        return self.acc_pass