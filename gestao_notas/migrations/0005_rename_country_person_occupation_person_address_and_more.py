# Generated by Django 5.0.4 on 2024-04-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestao_notas", "0004_person_remove_nota_categoria_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="person",
            old_name="country",
            new_name="occupation",
        ),
        migrations.AddField(
            model_name="person",
            name="address",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="phone_number",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="state",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
