from django.db import models

# Create your models here.
# doc cat like pdf , doc , csv etc

#login and signup details
class login(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.IntegerField()
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=8)
    role = models.IntegerField()

    def __str__(self):
        return self.first_name


#security tech name like public , private , privillaged

class document_security_technique(models.Model):
    c_name = models.CharField(max_length=30)

    def __str__(self):
        return self.c_name


# upload doc details will be stored here
class document_detail(models.Model):
    l_id = models.ForeignKey(login,on_delete=models.CASCADE)
    d_name = models.CharField(max_length=30,blank=True)
    d_description = models.TextField(max_length=30)
    d_type = models.CharField(max_length=40)
    security_id = models.ForeignKey(document_security_technique,on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    document = models.FileField(upload_to='docs')
    timestamp = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.d_name

#contact details
class contact_detail(models.Model):
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=15)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,editable=False)


#feedback details
class Feedback_Detail(models.Model):
    l_id = models.ForeignKey(login,on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True,editable=False)

#privillage details
class privillaged_document(models.Model):
    d_id = models.ForeignKey(document_detail, on_delete=models.CASCADE)
    l_id = models.ForeignKey(login,on_delete=models.CASCADE)
    demail = models.EmailField()
    privillage_status = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True,editable=False)