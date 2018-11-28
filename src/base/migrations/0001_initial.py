# Generated by Django 2.1.3 on 2018-11-28 06:53

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.core.fields.StreamField([('section_blocks', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.TextBlock()), ('heading', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.TextBlock()), ('link', wagtail.core.blocks.TextBlock(required=False))])), ('link', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('icon', wagtail.core.blocks.TextBlock())]))], verbose_name='Body')),
            ],
            options={
                'verbose_name_plural': 'Footer Text',
            },
        ),
    ]
