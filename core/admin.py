from django.contrib import admin

from core.models import Gym, Gym_d, Gym_r, Gym_S, Trainer, Comment, Classes,Classes_tabs


# Register your models here.
class postAdmin(admin.ModelAdmin):
         prepopulated_fields = {'slug': ('name',)}
class CommentAdmin(admin.ModelAdmin):
    list_display = ['first_name','subject','email','comment','date']

admin.site.register(Gym)
admin.site.register(Gym_d,postAdmin)
admin.site.register(Gym_r,postAdmin)
admin.site.register(Gym_S)
admin.site.register(Trainer)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Classes,postAdmin)
admin.site.register(Classes_tabs,postAdmin)

