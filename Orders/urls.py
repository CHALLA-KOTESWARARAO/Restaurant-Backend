from django.urls import path
from .views import all_orders,get_order,update_order,delete_order,create_order

urlpatterns = [
    path('all_orders/',all_orders,name="all_orders"),
    path('get_order/<int:id>/',get_order,name="get_order"),
    path('update_order/<int:id>/',update_order,name="update_order"),
    path('delete_order/<int:id>/',delete_order,name="delete_order"),
    path('create_order/',create_order,name="create_order"),
]
