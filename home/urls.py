

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

app_name="home"

urlpatterns = [
    path("",views.index,name="home-page"),
    path("search/",views.food_search_view.as_view(),name="search_food"),
    # path("info/<slug:urll>",views.allinfo,name="recipe"),
    path("register/",views.register,name="register-user"),
    path("profile/",views.profile,name="profile"),
    re_path(r'info/(?P<urll>[a-zA-Z0-9_#:./]+)$',views.allinfo,name="recipe"),#FDFUFUFUFUCKCKKC YESS
    
    path("login/",auth_views.LoginView.as_view(template_name="home/login.html"),name="login"),

    path("logout/",auth_views.LogoutView.as_view(template_name="home/logout.html"),name="logout"),

    path("add_to_cart/<int:upk>/<int:fpk>",views.add_to_cart,name="add-cart"),

    path('workout/',views.workout,name="workout"),
    
    path("cart",views.foodlistview.as_view(),name="cart"),
    path("nutrition/<int:plan>",views.nutrition,name = "nutrition"),
    path("overview/",views.nutrition_overview,name = "overview"),
    path('add_plan/',views.add_to_nutrition,name='add-plan'),
    path('edit/',views.edit,name='edit'),
    # path('change_plan/',views.change_plan,name='change-plan'),
    path('add_meal_item/<int:plan>/',views.add_meal_item,name='add-meal-item'),
    
]
urlpatterns+=staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)