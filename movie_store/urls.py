from django.urls import path

from . import views

urlpatterns = [
    # start
    path('', views.Start.as_view(), name='start'),
    path('subscription/', views.SubscriptionListView.as_view(), name='subscription_list'),
]
