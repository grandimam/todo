from .models import Poll
from .models import Question
from .models import Choice
from django.contrib import admin

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Choice)
