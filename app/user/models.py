import uuid
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def user_create(self, username: str, email: str, password: str):
        for val, name in ((username, 'username'), (email, 'email'), (password, 'password')):
            if val is None:
                raise ValueError(f'The given {val} must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def user_delete(self, user_uuid: str):
        try:
            user = self.get(user_uuid=user_uuid)
            user.delete()
            return "The user was deleted"
        except User.DoesNotExist:
            raise ValueError(f'User does not exist')


class User(AbstractBaseUser):
    user_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    username = models.CharField(
        unique=True,
        max_length=40,
        null=False,
        blank=False)
    email = models.EmailField(
        unique=True,
        max_length=255,
        null=True,
        blank=True)
    join_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'user'

    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
