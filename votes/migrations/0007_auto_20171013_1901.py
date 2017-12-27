# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-13 19:01
from __future__ import unicode_literals

from django.db import migrations, models

def convert_book_to_str(apps, schema_editor):
    Election = apps.get_model('votes', 'Election')
    for e in Election.objects.filter(winner__isnull=False):
        e.winner_str = str(e.winner)
        e.save()

def convert_str_to_book(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    Election = apps.get_model('votes', 'Election')
    for e in Election.objects.filter(winner_str__isnull=False):
        book = Book.objects.filter(as_string=e.winner_str).first()
        if book is not None:
            e.winner = book
            e.save()



class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0006_auto_20171013_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='winner_str',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.RunPython(
            convert_book_to_str,
            convert_str_to_book
        ),
        migrations.RemoveField(
            model_name='election',
            name='winner',
        ),
        migrations.RenameField(
            model_name='election',
            old_name='winner_str',
            new_name='winner',
        )
    ]
