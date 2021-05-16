from djongo import models

# Create your models here.
class Address(models.Model):
    _id = models.ObjectIdField()
    street = models.CharField(max_length=30)
    city = models.CharField( max_length=40)
    zipcode = models.IntegerField()
    country = models.CharField( max_length=40)
    
    class Meta:
        abstract = True

class Employee(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField( max_length=40)
    email = models.EmailField()
    emp_id = models.PositiveIntegerField()
    address = models.EmbeddedField(
        model_container=Address
    )
    # objects = models.DjongoManager()

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name



