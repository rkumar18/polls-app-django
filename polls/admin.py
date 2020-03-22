from django.contrib import admin

# Register your models here.
from .models import Question, Choice
admin.site.site_header ="Photo Admin"
admin.site.site_title ="Photo Admin Area"
admin.site.index_title ="welcome to Photoo Admin"
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
                 ('Data Information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines = [ChoiceInline]
#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)