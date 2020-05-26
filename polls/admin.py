from django.contrib import admin

from .models import choice, Question


class ChoiceInline(admin.TabularInline):
    model = choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('Question_text', 'pub_date', 'was_published_recently')

    list_filter=['pub_date']
    search_fields=['Question_text']

admin.site.register(Question, QuestionAdmin)