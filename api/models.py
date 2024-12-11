from django.db import models

from django.contrib.auth.models import User

from django.db.models import Sum



class Customer(models.Model):

    name=models.CharField(max_length=200)

    email=models.CharField(max_length=200)

    phone=models.CharField(max_length=200)

    vehicle_number=models.CharField(max_length=200)

    running_km=models.PositiveIntegerField()

    technician=models.ForeignKey(User,on_delete=models.CASCADE)

    options=(

        ("pending","pending"),

        ("in-progress","in-progress"),

        ("completed","completed")
    )

    status=models.CharField(max_length=200,choices=options,default="pending")

    created_date=models.DateTimeField(auto_now_add=True)

    update_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)


    @property
    def work_count(self):
                                                    # to display total count of works while listing customer
        return Work.objects.filter(customer=self).count()        # return self.work_set().all().counr()   self--parent (here cuatomer)    
    
    @property
    def work_total(self):                                          
                                                    # to display total amount of works while listing customer
        return Work.objects.filter(customer=self).values('amount').aggregate(total=Sum('amount'))['total']   

    @property
    def works(self):

        return Work.objects.filter(customer=self)



    def __str__(self) -> str:

        return self.name


class Work(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()

    amount=models.PositiveIntegerField()

    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    update_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)



    def __str__(self) -> str:

        return self.title



