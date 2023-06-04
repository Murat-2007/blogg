from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_image',
        ),
    ]