# Generated by Django 4.0.3 on 2022-04-04 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Posts_Tags',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='author_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='category_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.category'),
        ),
    ]
