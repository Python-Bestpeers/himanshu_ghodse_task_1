# Generated by Django 4.2.17 on 2024-12-17 12:35

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_comment_created_at_remove_comment_updated_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubTask",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("InProcessing", "InProcessing"),
                            ("Completed", "Completed"),
                        ],
                        default="InProcessing",
                        max_length=50,
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub_task",
                        to="app.task",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
