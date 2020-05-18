from django.shortcuts import render,redirect
from django.http import HttpResponse
from fatsecret import Fatsecret
from .models import food,user_foodlist,NutritionPlan
# from .models import food
from .forms import food_form,user_register,update_profile_form,update_user_form
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from django.views.generic import ListView,DetailView,CreateView
from collections import defaultdict
import requests
from urllib.parse import urlencode
from urllib.request import urlretrieve
from rest_framework.decorators import api_view
from .serializers import PlanSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# from django.Http import JsonResponse

def workout(request):
    response=requests.get("https://wger.de/api/v2/exerciseinfo/")
    response=response.json()
    exercise_muscle={}
    #----Name of exercise ---> Muscle trained.
    count=10
    while(count!=0):
        for x in response['results']:

            exercise_muscle[x['name']]=x['category']['name']
            # print(x['name'],"---->",x['category']['name'])
        
        count-=1
        response=requests.get(response['next']).json()

    #---Types of Muscle..
    response2=requests.get('https://wger.de/api/v2/muscle/')
    response2=response2.json()
    muscle_type=[]
    for x in response2["results"]:
        muscle_type.append(x["name"])
    

    
    return render(request,'home/workout.html',context={'exercise_muscle':exercise_muscle,'muscle':muscle_type})







def index(request):



    # for x in foods:
    #     print(x)
    
    if request.method=="POST":
        form=food_form(request.POST)
        if form.is_valid():
            foodname=form.cleaned_data["food_name"]
            # dietlabel=form.cleaned_data["dietlabel"]     
            mydict={'q':foodname,'app_key':'f3d813123b45b823f7c67142633c5541','app_id':'58e8a407'}
            # response2=requests.get('https://api.edamam.com/search?q=paneer-masala&app_key=f3d813123b45b823f7c67142633c5541&app_id=58e8a407&diet=low-carb&health=peanut-free&health=tree-nut-free')
            qstr=urlencode(mydict)
            urlend='https://api.edamam.com/search'
            response2=requests.get(urlend,params=mydict)
            response2j=response2.json()
            # d={}
            # print(type(response2j["hits"]))
            d=defaultdict(list)
            c=0
            for x in response2j["hits"]:
                # if c>15:
                #     break 
                # else:
                    # print(x["recipe"]["label"])
                    # print(x["recipe"]["calories"])
                    # print(x["recipe"]["totalNutrients"]["FAT"]["quantity"])
                    # print(x["recipe"]["totalNutrients"]["PROCNT"]["quantity"])
                try:
                    obj,created=food.objects.get_or_create(food_url=x["recipe"]["uri"],
                                            food_name=x["recipe"]["label"],
                                            carbs=int(x["recipe"]["totalNutrients"]["CHOCDF"]["quantity"]),
                                            servings=int(x["recipe"]["yield"]),
                                            protein=int(x["recipe"]["totalNutrients"]["PROCNT"]["quantity"]),
                                            calories=int(x["recipe"]["calories"]),
                                            fat=int(x["recipe"]["totalNutrients"]["FAT"]["quantity"]),
                                            saturated=int(x["recipe"]["totalNutrients"]["FASAT"]["quantity"]),
                                            monounsaturated=int(x["recipe"]["totalNutrients"]["FAMS"]["quantity"]),
                                            trans=int(x["recipe"]["totalNutrients"]["FATRN"]["quantity"]),
                                            fiber=int(x["recipe"]["totalNutrients"]["FIBTG"]["quantity"]),
                                            cholestrol=int(x["recipe"]["totalNutrients"]["CHOLE"]["quantity"]),
                                            magnesium=int(x["recipe"]["totalNutrients"]["MG"]["quantity"]),
                                            iron=int(x["recipe"]["totalNutrients"]["FE"]["quantity"]),
                                            zinc=int(x["recipe"]["totalNutrients"]["ZN"]["quantity"]),
                                            vite=int(x["recipe"]["totalNutrients"]["TOCPHA"]["quantity"]),
                                            vitc=int(x["recipe"]["totalNutrients"]["VITC"]["quantity"]),
                                            vitk=int(x["recipe"]["totalNutrients"]["VITK1"]["quantity"]),
                                            vita=int(x["recipe"]["totalNutrients"]["VITA_RAE"]["quantity"]),
                                            sugar=int(x["recipe"]["totalNutrients"]["SUGAR"]["quantity"]),
                                            dietlabel=x["recipe"]["dietLabels"],
                                            healthlabel=x["recipe"]["healthLabels"],
                                            steps=x["recipe"]["ingredientLines"]
                                            )
                    # print(j)
                    #j is a tuple which returns  tuple ie (object,created)
                    #created =True when new obj is created
                    #else if obj already exists  return False
                    # print(type(j))

                    if created:
                        obj.save()
                    

                    d["foodname"].append(obj.food_name)
                    d["calories"].append(obj.calories)
                    d["fat"].append(obj.fat)
                    d["protein"].append(obj.protein)
                    d["carbs"].append(obj.carbs)
                    d['dietlabel'].append(obj.dietlabel)
                    d["healthlabel"].append(obj.healthlabel)
                    d["steps"].append(obj.steps)
                    d["image"].append(x["recipe"]["image"])
                    d["servings"].append(obj.servings)
                    d["urll"].append(obj.food_url)
                    # d["foodname"].append(x["recipe"]["label"])
                    # d["calories"].append(int(x["recipe"]["calories"]))
                    # d["fat"].append(int(x["recipe"]["totalNutrients"]["FAT"]["quantity"]))
                    # d["protein"].append(int(x["recipe"]["totalNutrients"]["PROCNT"]["quantity"]))
                    # d["carbs"].append(int(x["recipe"]["totalNutrients"]["CHOCDF"]["quantity"]))
                    # d['dietlabel'].append(x["recipe"]["dietLabels"])
                    # d["healthlabel"].append(x["recipe"]["healthLabels"])
                    # d["steps"].append(x["recipe"]["ingredientLines"])
                    # d["image"].append(x["recipe"]["image"])
                    # d["servings"].append(x["recipe"]["yield"])
                    # d["urll"].append(x["recipe"]["uri"])
                    c+=1
                except KeyError:
                    print("HELLO")
             

            # print(d)
            context={'food':d,'count':range(c)}

            # fs=Fatsecret('f132e781377040bd91ef5a3cf84420c9','a920f6230b8b491ea8eb789128fce893')
            # foods = fs.foods_search(foodname)
            # # form.save()
            # # print(foods)
            # context={'foods':foods}
            return render(request,'home/fooddetails.html',context=context)
    else:
        form=food_form()
        context={'form':form}
    return render(request,"home/homepage.html",context=context)





def allinfo(request,urll):
    #urll is the url of corresponding dish 
    #that is why we used r as  a parameter

    mydict={'r':urll,'app_key':'f3d813123b45b823f7c67142633c5541','app_id':'58e8a407'}
    qstr=urlencode(mydict)
    urlend='https://api.edamam.com/search'
    response2=requests.get(urlend,params=mydict)
    response2j=response2.json()
    d=defaultdict(list)
    for x in response2j:
        # print(x["recipe"]["label"])
        # print(x["recipe"]["calories"])
        # print(x["recipe"]["totalNutrients"]["FAT"]["quantity"])
        # print(x["recipe"]["totalNutrients"]["PROCNT"]["quantity"])

        d["foodname"]=x["label"]
        d["calories"]=int(x["calories"])
        d["fat"]=int(x["totalNutrients"]["FAT"]["quantity"])
        d["saturated"]=int(x["totalNutrients"]["FASAT"]["quantity"])
        d["trans"]=int(x["totalNutrients"]["FATRN"]["quantity"])
        d["monounsaturated"]=int(x["totalNutrients"]["FAMS"]["quantity"])
        d["fiber"]=int(x["totalNutrients"]["FIBTG"]["quantity"])
        d["cholestrol"]=int(x["totalNutrients"]["CHOLE"]["quantity"])
        d["protein"]=int(x["totalNutrients"]["PROCNT"]["quantity"])
        d["carbs"]=int(x["totalNutrients"]["CHOCDF"]["quantity"])
        d["sugar"]=int(x["totalNutrients"]["SUGAR"]["quantity"])
        d["magnesium"]=int(x["totalNutrients"]["MG"]["quantity"])
        d["iron"]=int(x["totalNutrients"]["FE"]["quantity"])
        d["zinc"]=int(x["totalNutrients"]["ZN"]["quantity"])
        d["vita"]=int(x["totalNutrients"]["VITA_RAE"]["quantity"])
        d["vitc"]=int(x["totalNutrients"]["VITC"]["quantity"])
        d["vite"]=int(x["totalNutrients"]["TOCPHA"]["quantity"])
        d["vitk"]=int(x["totalNutrients"]["VITK1"]["quantity"])
        d['dietlabel']=x["dietLabels"]
        d["healthlabel"]=x["healthLabels"]
        d["steps"]=x["ingredientLines"]
        d["image"]=x["image"]
        d["servings"]=x["yield"]

    details=[d["fat"],d["protein"],d["carbs"]]
    metric=["fat","protein","carbs"]
    foodid=food.objects.get(food_url=urll).pk
    context={'food':d,'foodid':foodid,"details":details,"metric":metric}
    return render(request,"home/info.html",context=context)    





class food_search_view(CreateView):
    model=food
    fields=('food_name',)


@login_required
def profile(request):
    
    if request.method=="POST":
        form=update_profile_form(request.POST,request.FILES,instance=request.user.profile)

        if form.is_valid():
            form.save() 
            messages.success(request,f'YOUR ACCOUNT IS UPDATED')
            return redirect('home:profile')
        

    else:
        form=update_profile_form(instance=request.user.profile)
    return render(request,'home/profile.html',context={'form':form})


def register(request):

    if request.method=="POST":
        uform=user_register(request.POST)
        if uform.is_valid():
            uform.save()
            messages.success(request,f'ACCOUNT CREATED!')
            username=uform.cleaned_data["username"]
            
    else:
        uform=user_register()

    return render(request,'home/register.html',context={'form':uform})
            


@login_required
def add_to_cart(request,upk,fpk):
    
    #Querying for data of food which is to be added.
    carbs=food.objects.get(pk=fpk).carbs
    name=food.objects.get(pk=fpk).food_name
    calories=food.objects.get(pk=fpk).calories
    protein=food.objects.get(pk=fpk).protein
    fat=food.objects.get(pk=fpk).fat

    user_item=user_foodlist.objects.create(user=request.user,
                                            user_eat=name,
                                            user_calories=calories,
                                            user_protein=protein,
                                            user_fat=fat,
                                            user_carbs=carbs,
                                            )
    user_item.save()

    return redirect('home:cart')    


class foodlistview(ListView):
    model=user_foodlist
    context_object_name='user_food'
    
    def get_queryset(self):
        return user_foodlist.objects.filter(user=self.request.user)


# class foodlistview(ListView):
#     model=models.food

# class fooddetailview(DetailView):
#     model=models.food
#     template_name='home/food_detailview.html'

def nutrition(request,plan):
    query = NutritionPlan.objects.filter(plan=plan)
    return render(request,'home/nutrition.html',{'plan':query[0]})

def nutrition_overview(request):
    return render(request,'home/nutrition_overview.html')

class PlanView(APIView):
    def post(self,request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['POST'])
def add_to_nutrition(request):
    serializer = PlanSerializer(data=request.data)
    print("serializer",serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
    # print(request)
    # plan = NutritionPlan.objects.create(user=request.user,plan=p)
    # plan.save()

def edit(request):
    return render(request,'home/edit.html')

@api_view(['POST'])
def add_meal_item(request,plan):
    if request.method == 'POST':
        li = []
        print("Request",request)
        query = NutritionPlan.objects.get(plan=plan)
    
        # li.append(request.data['meal_items'][0])
        print("data",request.data['meal_items'][0])
        print("query",query.meal_items)
        query.meal_items.append(request.data['meal_items'][0])
    
        query.save()
        # serializer = PlanSerializer(instance = query,data=request.data)
        # # print("initial data",serializer.initial_data)
        # # serializer.data.meal_items = serializer.data.meal_items.append(data)
        # # print("data",serializer.data)
        # serializer.save()
        # return Response(serializer.data)
        
        # print(request.values)
        # query.meal_items.append()
        return HttpResponse(json.dumps({"success":True}), content_type="application/json")

