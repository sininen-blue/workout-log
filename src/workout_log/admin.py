from django.contrib import admin
from .models import Exercise, Tag, Set, ExerciseTagMap, Session

admin.site.register(Exercise)
admin.site.register(ExerciseTagMap)
admin.site.register(Tag)
admin.site.register(Session)
admin.site.register(Set)
