from django.contrib import admin
from .models import User, Tag, Relation, Worker, Profession, Retrain

# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Relation)
admin.site.register(Worker)
admin.site.register(Profession)
admin.site.register(Retrain)
