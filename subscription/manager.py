from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required!")
        
        email=self.normalize_email(email)
        # extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        # if not username:
        #     raise ValueError("Name is required!")
        
        # user = self.model(
        #     email=self.normalize_email(email)
        # )
        # # extra_fields['email'] = self.normalize_email(extra_fields['email'])
        # user = self.model(name = name, **extra_fields)
        # user.set_password(password)
        # user.save(using = self._db)
        # return user
        return self.create_user(email, password, **extra_fields)