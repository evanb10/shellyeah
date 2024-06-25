# Generated by Django 4.2.13 on 2024-06-24 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottery_sim', '0002_manager_unique_manager_in_league'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='manager',
            name='unique_manager_in_league',
        ),
        migrations.AddField(
            model_name='leaguemembership',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottery_sim.league'),
        ),
        migrations.AddField(
            model_name='leaguemembership',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottery_sim.manager'),
        ),
        migrations.AlterUniqueTogether(
            name='leaguemembership',
            unique_together={('manager', 'league')},
        ),
    ]