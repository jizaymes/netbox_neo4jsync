from django.urls import path

from . import views

urlpatterns  = (
    path('neo4jsync/', views.Neo4jSyncListView, name='neo4jsync_list'),   
)