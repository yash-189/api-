from djongo import models
import datetime

# Create your models here.


class months(models.Model):
    month_id = models.AutoField(primary_key=True)
    month = models.CharField(max_length=20)

    def __str__(self):
        return self.month


currMonth = datetime.datetime.now().strftime("%B")
monthId = datetime.datetime.now().strftime("%m")

class user(models.Model):
    
    user_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    batch = models.CharField(max_length=5, choices=(('6-7AM','6-7AM'),('7-8AM','7-8AM'),('8-9AM','8-9AM'),('5-6PM','5-6PM')))
    paid = models.BooleanField(default=False)
    amount = models.CharField(editable=False,default=500,max_length=3)
    paid_month = models.CharField(max_length=200,default=currMonth)
    date = models.DateTimeField(auto_now=True)
    month = models.ForeignKey(months,on_delete=models.CASCADE,default=monthId)

