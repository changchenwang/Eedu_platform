# Generated by Django 2.0 on 2021-09-22 06:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20210920_0836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Course'},
        ),
        migrations.AlterModelOptions(
            name='courseresource',
            options={'verbose_name': 'resource file', 'verbose_name_plural': 'resource file'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Chapter', 'verbose_name_plural': 'Chapter'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'video', 'verbose_name_plural': 'video'},
        ),
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Add Time'),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(default='The backend development', max_length=300, verbose_name='Course category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='click_nums',
            field=models.IntegerField(default=0, verbose_name='clicks'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='organizatio'),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', 'primary'), ('zj', 'intermediate'), ('gj', 'senior')], max_length=2, verbose_name='课程难度'),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.CharField(max_length=300, verbose_name='Course description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=models.TextField(verbose_name='Course details'),
        ),
        migrations.AlterField(
            model_name='course',
            name='fav_nums',
            field=models.IntegerField(default=0, verbose_name='The number of collection'),
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(upload_to='courses/%Y/%m', verbose_name='cover'),
        ),
        migrations.AlterField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='is banner'),
        ),
        migrations.AlterField(
            model_name='course',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='Learning Duration(minutes)'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Course name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.IntegerField(default=0, verbose_name='The number of learning'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='Class label'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='lecturer'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='', max_length=300, verbose_name='The teacher tells you'),
        ),
        migrations.AlterField(
            model_name='course',
            name='youneed_know',
            field=models.CharField(default='', max_length=300, verbose_name='Course information'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='add time'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='download',
            field=models.FileField(upload_to='course/resouce/%Y/%m', verbose_name='Resource file'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Add time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Chapter'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Add the time'),
        ),
        migrations.AlterField(
            model_name='video',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='Learning Duration(minutes)'),
        ),
        migrations.AlterField(
            model_name='video',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='Lesson'),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='Access to the address'),
        ),
    ]
