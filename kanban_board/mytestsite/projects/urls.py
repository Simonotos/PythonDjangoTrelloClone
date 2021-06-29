from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('archivio', views.showPageArchivio),
    path('saveTile', views.saveTile, name='saveTile'),
    path('getTiles', views.getTiles, name='getTiles'),
    path('getColumns', views.getColumns, name='getColumns'),
    path('getColumnsArchived', views.getColumnsArchived, name='getColumnsArchived'),
    path('saveColumn', views.saveColumn, name='saveColumn'),
    path('moveTile', views.moveTile, name='moveTile'),
    path('modifyColumn', views.modifyColumn, name='modifyColumn'),
    path('modifyTile', views.modifyTile, name='modifyTile'),
    path('deleteColumn', views.deleteColumn, name='deleteColumn'),
    path('archiveColumn', views.archiveColumn, name='archiveColumn'),
    path('restoreColumn', views.restoreColumn, name='restoreColumn'),
]