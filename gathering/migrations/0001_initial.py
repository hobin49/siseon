# Generated by Django 3.2.13 on 2022-11-30 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gathering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('오프라인 모임', '오프라인 모임'), ('온라인 모임', '온라인 모임'), ('오프라인 스터디', '오프라인 스터디'), ('온라인 스터디', '온라인 스터디')], default=None, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('image', models.ImageField(blank=True, upload_to=None)),
                ('like_users', models.ManyToManyField(related_name='like_gathering', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VoteContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('user', models.ManyToManyField(related_name='vote_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.DateTimeField()),
                ('gathering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gathering.gathering')),
            ],
        ),
        migrations.CreateModel(
            name='GatheringComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gathering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='gathering.gathering')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
