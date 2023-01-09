from django.contrib.auth import User

User.objects.create_superuser('admin', 'makarov.da@phystech.edu', 'admin')