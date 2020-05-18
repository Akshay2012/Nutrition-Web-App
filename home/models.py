from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#superuser username= akshay
#password- 123
from django.utils import timezone

from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField


class  profile(models.Model):
    active_choice=[('not_active',"Not active"),('light',"Lightly Active"),('active','Active'),('very',"Very Active")]
    goal_choice=[('Gain','Gain Weight'),('maintain','Maintain Weight'),('fat_Loss','Fat loss')]

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jfif',upload_to="profile_pics")
    email=models.EmailField(max_length=244,default="abc@gmail.com")
    height=models.IntegerField(default=0,help_text="In cms")
    weight=models.IntegerField(default=0,help_text="In kgs")
    goalweight=models.IntegerField(default=0,help_text="In kgs")
    goal=models.CharField(max_length=20,default="maintain",choices=goal_choice)
    activity_level=models.CharField(max_length=15,choices=active_choice,default='active')
    # allergies=models.Choices

    def __str__(self):  
        return f'{self.user.username} PROFILE'


class userpost(models.Model):
    post_user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=220)
    post_content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.post_title} - {self.post_user}'

class user_foodlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    user_eat=models.CharField(max_length=250)
    user_calories=models.BigIntegerField(default=0)
    user_protein=models.BigIntegerField(default=0)
    user_carbs=models.BigIntegerField(default=0)
    user_fat=models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.user_eat

    

    


class food(models.Model):
    food_url=models.URLField(max_length=400,default="www.google.com")
    food_name=models.CharField(max_length=200)
    carbs=models.BigIntegerField(default=0)
    servings=models.BigIntegerField(default=0)
    protein=models.BigIntegerField(default=0)
    calories=models.BigIntegerField(default=0)  
    fat=models.BigIntegerField(default=0)
    saturated=models.BigIntegerField(default=0)
    monounsaturated=models.BigIntegerField(default=0)
    trans=models.BigIntegerField(default=0)
    fiber=models.BigIntegerField(default=0)
    cholestrol=models.BigIntegerField(default=0)
    magnesium=models.BigIntegerField(default=0)
    iron=models.BigIntegerField(default=0)
    zinc=models.BigIntegerField(default=0)
    vite=models.BigIntegerField(default=0)
    vitc=models.BigIntegerField(default=0)
    vitk=models.BigIntegerField(default=0)
    vita=models.BigIntegerField(default=0)
    sugar=models.BigIntegerField(default=0)
    dietlabel= ArrayField(models.CharField(max_length=100),default=list)
    healthlabel= ArrayField(models.CharField(max_length=100),default=list)
    steps=ArrayField(models.CharField(max_length=100),default=list)
    
    def __str__(self):
        return self.food_name
    
    def get_absolute_url(self):
        return reverse("home:home-page")

class NutritionPlan(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000,default = '')
    plan = models.IntegerField(blank = True,null = True)
    meal = models.IntegerField(blank = True,null = True)
    meal_items= ArrayField(models.IntegerField(blank=True,null=True),default=list)