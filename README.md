# Django Custom User Auth

A powerful and flexible Django custom user authentication system with support for custom fields, admin-ready integration, and email-based authentication.

---

## ✨ Features

- ✅ Admin-ready interface
- 🔧 Custom fields support (extend the user model easily)
- 📧 Email-based authentication with custom user manager
- 🛡️ Pre-built authentication forms
- 🚀 Easy installation and configuration

---

## 📦 Installation

```bash
copy/paste custom_user folder to your project root folder.
```

---

## ⚙️ Configuration

### 1. `settings.py`

```python
INSTALLED_APPS = [
    # ...
    'custom_user',
]

AUTH_USER_MODEL = 'custom_user.CustomUser'
```

### 2. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🛠️ Extending the Model

You can easily add custom fields by extending the `AbstractCustomUser` class.

```python
# models.py
from django.db import models
from custom_user.models import AbstractCustomUser

class CustomUser(AbstractCustomUser):
    # Custom fields
    bio = models.TextField(blank=True)
    company = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
```

---

## 👨‍💻 Admin Integration

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Custom Fields', {'fields': ('bio', 'company', 'birth_date')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
```

---

## 💻 Usage Examples

### Create a User via Shell

```python
from custom_user.models import CustomUser

user = CustomUser.objects.create_user(
    email='user@example.com',
    password='SecurePass123!',
    first_name='John',
    last_name='Doe',
    company='Tech Corp'
)
```

### Authenticate a User

```python
from django.contrib.auth import authenticate

user = authenticate(
    request, 
    email='user@example.com', 
    password='SecurePass123!'
)
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contributing

Feel free to submit issues, fork the repository and send pull requests. Contributions are always welcome!

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out or open an issue.
