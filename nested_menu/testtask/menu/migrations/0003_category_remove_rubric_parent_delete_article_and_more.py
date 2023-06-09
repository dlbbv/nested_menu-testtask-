# Generated by Django 4.2 on 2023-04-13 12:45

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='category name')),
                ('slug', models.SlugField(unique=True)),
                ('views', models.PositiveIntegerField(default=0, verbose_name='number of page views')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='menu.category', verbose_name='parent category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='rubric',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Rubric',
        ),
    ]
