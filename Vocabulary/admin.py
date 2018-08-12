from django.contrib import admin

# Register your models here.
from Vocabulary.models import Vocab

class VocabAdmin(admin.ModelAdmin):
    fields = ('word', 'meaning')
    list_display = ['word', 'meaning', 'id']
    class Meta:
        model = Vocab


admin.site.register(Vocab, VocabAdmin)