# Generated by Django 4.0.5 on 2022-06-09 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'db_table': 'actors',
            },
        ),
        migrations.CreateModel(
            name='ActorsMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actor')),
            ],
            options={
                'db_table': 'actors_movies',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('relase_date', models.DateField()),
                ('running_time', models.IntegerField()),
                ('actors', models.ManyToManyField(related_name='actors', through='movies.ActorsMovies', to='movies.actor')),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.AddField(
            model_name='actorsmovies',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]