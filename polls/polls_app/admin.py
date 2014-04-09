from django.contrib import admin
from polls_app.models import Poll
from polls_app.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)