#!/bin/bash
EXEC='python manage.py'
$EXEC makemigrations
$EXEC migrate
