from django.contrib import admin

# In that form, the "Question" field is a select box containing every question in the database.
from .models import Question
admin.site.register(Question)
