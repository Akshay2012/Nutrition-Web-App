from rest_framework import serializers

from .models import NutritionPlan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionPlan
        fields = ['user','plan','meal','meal_items','description']
    
    