# Generated by Django 4.0.6 on 2022-10-06 07:28

from django.db import migrations, models
import players.models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('role', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=players.models.Officials.upload_location)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Results',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='assist',
            new_name='assists',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='other_names',
            new_name='nick_name',
        ),
        migrations.AddField(
            model_name='match',
            name='match_type',
            field=models.CharField(default='Friendly', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='meteors_logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='match',
            name='oponent_logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='match',
            name='played',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='DEF',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='DRI',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='PAC',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='PAS',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='PHY',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='SHO',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='contract',
            field=models.CharField(default=2023, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='player',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='player',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='strong_foot',
            field=models.CharField(choices=[('Left', 'Left'), ('Right', 'Right'), ('Both', 'Both')], default='Right', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='year_joined',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.RemoveField(
            model_name='match',
            name='goal_scorers',
        ),
        migrations.AddField(
            model_name='match',
            name='goal_scorers',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
