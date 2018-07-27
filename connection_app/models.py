from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def add_user(self, form_data):
        # validate here if necessary!
        user = User.objects.create(name=form_data["name"], email=form_data["email"])
        return (True, user)
    def connect(self, form_data):
        # get the user trying to connect
        connecting_user = User.objects.get(id=form_data["connecting"])
        # get the user they are connecting to
        connected_user = User.objects.get(id=form_data["connected"])
        # connect them together
        # basically append them to the list of connected users
        connecting_user.connections.add(connected_user)
        # in order to remove we do the same thing, just change add to remove
        # connecting_user.connections.remove(connected_user)
        return True


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # connections is like a list of users
    connections = models.ManyToManyField("self", related_name="user_connections")

    objects = UserManager()
