# Generated by Django 5.0.6 on 2024-05-22 03:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('league_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('num_of_teams', models.IntegerField()),
                ('sport', models.CharField(max_length=25)),
                ('league_name', models.CharField(max_length=255)),
                ('previous_league_id', models.BigIntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('team', models.CharField(blank=True, max_length=255, null=True)),
                ('player_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=255, null=True)),
                ('display_name', models.CharField(max_length=255)),
                ('record', models.CharField(max_length=255, null=True)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('points_for', models.IntegerField(default=0)),
                ('points_against', models.IntegerField(default=0)),
                ('league_id', models.ForeignKey(db_column='league_id', on_delete=django.db.models.deletion.CASCADE, to='lottery_sim.league')),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.ForeignKey(db_column='manager_id', on_delete=django.db.models.deletion.CASCADE, to='lottery_sim.manager')),
                ('player_id', models.ForeignKey(db_column='player_id', on_delete=django.db.models.deletion.CASCADE, to='lottery_sim.player')),
            ],
        ),
    ]
