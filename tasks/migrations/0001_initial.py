from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('action', models.CharField(max_length=200)),
                ('is_completed', models.BooleanField(default=False)),
                ('importance', models.IntegerField(choices=[(1, 'High'), (0, 'Low')])),
                ('urgence', models.IntegerField(choices=[(1, 'High'), (0, 'Low')])),
                ('is_two_mins', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=20, choices=[('do', 'Do'), ('plan', 'Plan'), ('delegate', 'Delegate'), ('forget', 'Forget')])),
                ('domain', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
