from django.db import models
from django import forms

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20)
    Time = models.DateTimeField()
    created = models.DateField()
    updated = models.DateField()
    deletion = models.BooleanField(default= False)

    def __str__(self):
        return self.title+' - '+self.status
"""
class UserProfile(models.Model):
    # Let us add some simple fields to profile
    todo = models.OneToOneField(Todo,on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20)
    Time = models.DateTimeField()
    created = models.DateField()
    updated = models.DateField()
    deletion = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s" % self.user
<----
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('title', 'description', 'status', 'Time') #Note that we didn't mention user field here.

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile

"""