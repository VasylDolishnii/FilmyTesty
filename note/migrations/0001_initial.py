# Generated by Django 3.1.4 on 2020-12-06 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200)),
                ('rok', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Wydawca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rola', models.CharField(max_length=200)),
                ('aktor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='note.osoba')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wystapili', to='note.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='rezyser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wyrezyserowal', to='note.osoba'),
        ),
        migrations.AddField(
            model_name='film',
            name='scenarzysta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filmy_scenariusze', to='note.osoba'),
        ),
    ]
