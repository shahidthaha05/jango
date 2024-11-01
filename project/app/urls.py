from django.urls import path
from.import views

urlpatterns=[
    path('',views.shop_login),
    path('shop_logout',views.shop_logout),
    



    #----------------------------------shop----------------------------



    path('shop_home',views.shop_home),
    path('add_product',views.add_product)




    #----------------------user--------------------------------
]