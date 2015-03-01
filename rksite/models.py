from django.db import models

class Message(models.Model):
    #Name of the person contacting you
    name = models.CharField(max_length=200, unique=True)
    #Email of the person contacting you
    email = models.EmailField(unique=True)
    #Subject of the person contacting you
    subject = models.CharField(max_length=100, unique=True)
    #Message written by person contacting you
    message = models.CharField(max_length=1000, unique=True)

    def __unicode__(self):
        return self.name
