from django.contrib import admin
from .models import TopPost, Posts


# Register your models here.
@admin.register(Posts)
class TopPostAdmin(admin.ModelAdmin):
    class Meta:
        model = Posts


@admin.register(TopPost)
class TopPostAdmin(admin.ModelAdmin):
    class Meta:
        model = TopPost
