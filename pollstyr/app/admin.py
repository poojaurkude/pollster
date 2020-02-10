from django.contrib import admin

from .models import Choice, Question,Vote


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]

# admin.site.register(Question, QuestionAdmin)


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)

