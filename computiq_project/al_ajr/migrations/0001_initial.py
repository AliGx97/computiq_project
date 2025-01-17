# Generated by Django 4.0.1 on 2022-02-26 02:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='skill name')),
                ('detail', models.CharField(max_length=2000, verbose_name='detail')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='users')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='price')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('detail', models.CharField(max_length=2000, verbose_name='details')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=2, null=True, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(0.0)], verbose_name='free lancer rating')),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('PROCESSING', 'PROCESSING'), ('DONE', 'DONE'), ('DELETED', 'DELETED')], max_length=255, verbose_name='status')),
                ('receiver_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_id', to=settings.AUTH_USER_MODEL, verbose_name='freelancer_id')),
                ('requester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester_id', to=settings.AUTH_USER_MODEL, verbose_name='custmer_id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=255, verbose_name='message')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='sender')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
