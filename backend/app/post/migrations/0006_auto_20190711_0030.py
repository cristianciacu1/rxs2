# Generated by Django 2.2.3 on 2019-07-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20190711_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tools',
            field=models.CharField(choices=[('Adobe Illustrator, Django, React JS', 'Adobe Illustrator, Django, React JS'), ('Django', 'Django'), ('React JS', 'React JS')], max_length=300),
        ),
    ]