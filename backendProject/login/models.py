from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.db import models


"""
ADMINISTRADOR DE USUARIOS
"""
class UserManager(BaseUserManager):
    def create_superuser(self, name, lastname, username, email, password):
        user = self.model(name = name, lastname = lastname, username = username)
        email = self.normalize_email(email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)

"""
CREDENCIAL
"""
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True, null=False)
    name = models.CharField(max_length=100, unique=False, null=False)
    lastname = models.CharField(max_length=100, unique=False, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    last_modified = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'lastname']

    class Meta:
        verbose_name = ('User')
        verbose_name_plural = ('Users')
        
    objects = UserManager()

    def get_full_name(self):
        return self.name+" "+self.lastname
    def get_short_name(self):
        return self.name
    def __unicode__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_staff
