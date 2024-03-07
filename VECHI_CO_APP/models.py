from django.db import models


# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    usertype = models.CharField(max_length=200)


class serviceprovider(models.Model):
    service_name = models.CharField(max_length=200)
    contactnumber = models.BigIntegerField()
    lattitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)


class user(models.Model):
    username = models.CharField(max_length=200)
    contact = models.BigIntegerField()
    Email = models.CharField(max_length=200)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)


class feedback(models.Model):
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)
    date = models.CharField(max_length=200)


class service(models.Model):
    service_name = models.CharField(max_length=200)



class ownservice(models.Model):
    SERVICE = models.ForeignKey(service, default=1, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200, default=1)
    SERVICEPROVIDER = models.ForeignKey(serviceprovider, default=1, on_delete=models.CASCADE)

class booking(models.Model):
    OWNSERVICE = models.ForeignKey(ownservice, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    lattitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    paymentstatus = models.CharField(max_length=200)
    note = models.CharField(max_length=200, default=1)
    completionstatus = models.CharField(max_length=200, default=1)
    status=models.CharField(max_length=200,default=1)
    amount=models.CharField(max_length=200,default=1)


class rating(models.Model):
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    rating = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    SERVICE = models.ForeignKey(service, default=1, on_delete=models.CASCADE)

class bank(models.Model):
    bank_name = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    IFSC_code = models.CharField(max_length=100)
    amount = models.IntegerField()
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)



class complaint(models.Model):
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    SERVICEPROVIDER = models.ForeignKey(serviceprovider, default=1, on_delete=models.CASCADE)
    reply = models.CharField(max_length=200, default=1)
    replydate = models.CharField(max_length=200, default=1)



class payment(models.Model):
    BOOKING = models.ForeignKey(booking,default=1,on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user,default=1,on_delete=models.CASCADE)