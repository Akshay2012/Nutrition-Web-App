from django.contrib import admin
from .models import food,profile,exercise

# Register your models here.
admin.site.register(food)
admin.site.register(profile)
admin.site.register(exercise)

# admin.site.register(nutrition_values)