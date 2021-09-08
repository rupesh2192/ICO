# Generated by Django 3.2.7 on 2021-09-06 18:50

from django.db import migrations


def generate_tokens(apps, schema_editor):
    Token = apps.get_model('coin_offering', 'Token')
    tokens = []
    for i in range(500):
        tokens.append(Token())

    Token.objects.bulk_create(tokens)


class Migration(migrations.Migration):
    dependencies = [
        ('coin_offering', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_tokens)
    ]
