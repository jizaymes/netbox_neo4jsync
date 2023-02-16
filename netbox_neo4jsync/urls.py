from django.urls import path

from . import views

urlpatterns  = (
    path('neo4jsync', views.Neo4jSyncListView.as_view(), name='neo4jsync_list'),   
)