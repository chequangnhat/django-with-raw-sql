from django.urls import path
from create_table_app import views

urlpatterns = [
    path('add_table/', views.add_table),

]