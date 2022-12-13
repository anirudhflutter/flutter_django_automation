
"""
Api end points for subscription module
"""

from django.urls import path
from subscription import views


urlpatterns = [
    path('add_subscription/', views.add_subscription, name="add_subscription"),
    path('get_subscription/', views.get_subscription, name="get_subscription"),
    path('get_subscription_by_id/', views.get_subscription_by_id, name="get_subscription_by_id"),
    path('delete_all_subscription/', views.delete_subscription, name="delete_subscription"),
    path('delete_subscription_by_id/', views.delete_subscription_by_id, name="delete_subscription_by_id"),
    path('update_subscription/', views.update_subscription, name="update_subscription"),
]


                  