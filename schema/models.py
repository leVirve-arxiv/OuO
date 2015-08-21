from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User)

    uuid = models.CharField('UID', max_length=100)

    def __str__(self):
        return self.user.get_username()

    def __unicode__(self):
        return self.user.get_username()


class Field(models.Model):
    FTYPE_CHOICES = (
        ('NUMBER', 'Number'),
        ('STRING', 'String'),
        ('BOOLEAN', 'Boolean'),
    )
    fname = models.CharField(max_length=50, default='')
    ftype = models.CharField(max_length=50, choices=FTYPE_CHOICES, default=FTYPE_CHOICES[0][0])  # noqa

    def __unicode__(self):
        return '%d - %s(%s)' % (self.id, self.fname, self.ftype)


class Template(models.Model):
    tname = models.CharField(max_length=50, default='')
    # Owner to be constructed
    #owner = models.ForeignKey(User)
    description = models.TextField(blank=True)
    sample = models.TextField(blank=True)
    data_src = models.CharField(max_length=150, default='')
    thumbnail_src = models.CharField(max_length=150, default='')
    # Store the struct of the template
    fields = models.ManyToManyField(Field, blank=True, null=True)

    def __unicode__(self):
        return '%d - %s' % (self.id, self.tname)
