from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import connection
from django.apps import apps

import json
import requests
# Create your views here.

def get_table_names_sqlite():
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_names = [row[0] for row in cursor.fetchall()]
    return table_names

def get_table_names_postgres():
    with connection.cursor() as cursor:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE';")
        table_names = [row[0] for row in cursor.fetchall()]
    return table_names

@api_view(['GET'])
@permission_classes([AllowAny])
def add_table(request):
  list_table = get_table_names_sqlite()
  print(list_table)

  table_name = request.data['table_name']
  # print('table_name: ',table_name)
  # models = apps.get_models(include_auto_created=True, include_swapped=True,)

  # # Loop through each model and print its name
  # for model in models:
  #     print(model.__name__)
  #     list_table.append(model.__name__)

  sql_command = f'''
                  CREATE TABLE {table_name} (
                  id serial PRIMARY KEY,
                  name varchar(100) NOT NULL,
                  age integer
                  )
                  '''

  if table_name in list_table:
     print("existing in models")
  else:
    print("not exist")
    with connection.cursor() as cursor:
      cursor.execute(sql_command)
    
  #   for model in models:
  #     # print(model.__name__)
  #     list_table.append(model.__name__)



 
  

  return Response({'result': 'hehehe'})

