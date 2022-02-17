from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=4)


class Document(models.Model):
    uploaded_file = models.FileField(upload_to='images/')
    expiration_date = models.DateField()
    expired = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
