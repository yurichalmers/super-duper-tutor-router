from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(post_data['first_name']) < 2:
            errors['first_name'] = "Please enter a first name longer than 2 characters."   
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Please enter a last name longer than 2 characters."
        if len(post_data['username']) < 8:
            errors['username'] = "Your username must be at least 8 characters."      
        if len(post_data['level']) < 1:
            errors['grade_level'] = "Please choose your level."
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Please enter a valid email."
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors['email2'] = "That email is already in use."
        if len(post_data['password']) < 1:
            errors['password'] = "You need to enter a password."   

        if post_data['password'] != post_data['confirm_password']:
            errors['password'] = "Your password does not match."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    user_type = models.CharField(max_length=64)
    level = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)

    objects = UserManager()


class TutorhelpManager(models.Manager):
    def tutorhelp_validator(self, post_data):
        errors = {}

        if len(post_data['topic']) < 5:
            errors['topic'] = "The topic must be at least 5 characters."
            
        return errors

class Tutorhelp(models.Model):
    subject = models.CharField(max_length=64)
    course = models.CharField(max_length=64)
    topic = models.CharField(max_length=64)
    desc = models.TextField()
    poster = models.ForeignKey(
        User,
        related_name = "tutorhelp",
        on_delete = models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = TutorhelpManager()

class Comment(models.Model):
    comment = models.TextField()
    request = models.ForeignKey(
        Tutorhelp,
        related_name = "comments",
        on_delete = models.CASCADE
    )
    poster = models.ForeignKey(
        User,
        related_name = "comments",
        on_delete = models.CASCADE
    )
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)