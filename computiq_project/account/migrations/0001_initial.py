# Generated by Django 4.0.1 on 2022-02-26 02:47

import account.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('field', models.CharField(max_length=50, verbose_name='field')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10, null=True, verbose_name='rating')),
                ('state', models.CharField(choices=[('دهوك', 'دهوك'), ('اربيل', 'اربيل'), ('نينوى', 'نينوى'), ('السليمانية', 'السليمانية'), ('كركوك', 'كركوك'), ('صلاح الدين', 'صلاح الدين'), ('ديالى', 'ديالى'), ('بغداد', 'بغداد'), ('الانبار', 'الانبار'), ('واسط', 'واسط'), ('بابل', 'بابل'), ('النجف', 'النجف'), ('كربلاء', 'كربلاء'), ('ميسان', 'ميسان'), ('الديوانيه', 'الديوانيه'), ('المثنى', 'المثنى'), ('ذي قار', 'ذي قار'), ('البصره', 'البصره')], max_length=255, verbose_name='states')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', account.models.CustomUserManger()),
            ],
        ),
    ]
