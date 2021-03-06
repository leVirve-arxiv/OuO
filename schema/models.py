from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User)

    uuid = models.CharField('UID', max_length=100)
    name = models.CharField('name', max_length=100)

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


class Mapping(models.Model):
    field = models.ForeignKey(Field)
    onto = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return '%d - [%s -> %s]' % (self.id, self.field.fname, self.onto)


class Template(models.Model):
    tname = models.CharField(max_length=50, default='')
    owner = models.ForeignKey(Member)
    description = models.TextField(blank=True)
    sample = models.TextField(blank=True)
    # html describe that template
    html_src = models.TextField(blank=True)
    thumbnail_src = models.FileField(upload_to='upload_img')
    # Store the struct of the template
    fields = models.ManyToManyField(Field, blank=True, null=True)

    def __unicode__(self):
        return '%d - %s' % (self.id, self.tname)


class Graph(models.Model):
    gname = models.CharField(max_length=50, default='')
    owner = models.ForeignKey(Member)
    template = models.ForeignKey(Template)
    description = models.TextField(blank=True)
    # json file
    data_src = models.TextField()
    mappings = models.ManyToManyField(Mapping, blank=True, null=True)

    def __unicode__(self):
        return '%d - %s' % (self.id, self.gname)
