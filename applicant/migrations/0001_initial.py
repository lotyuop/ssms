# Generated by Django 2.1.4 on 2019-01-14 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('result', models.IntegerField()),
                ('admission_status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Appstudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appno', models.CharField(max_length=12, unique=True)),
                ('surname', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('other_name', models.CharField(max_length=50)),
                ('sex', models.IntegerField()),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=16)),
                ('home_address', models.TextField()),
                ('raddress', models.TextField()),
                ('country', models.CharField(default='Nigeria', max_length=40)),
                ('parent_name', models.CharField(max_length=120)),
                ('parent_phone', models.CharField(max_length=16)),
                ('parent_phone2', models.CharField(max_length=16)),
                ('parent_email', models.CharField(max_length=40)),
                ('parent_occupation', models.CharField(max_length=120)),
                ('health_condition', models.TextField()),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Bloodgroup')),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Lga')),
                ('sclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.SchoolClass')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.State')),
            ],
        ),
        migrations.AddField(
            model_name='admission',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.Appstudent'),
        ),
    ]
