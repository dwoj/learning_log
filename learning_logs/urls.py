"""Definiuje wzorce adresów URL dla learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #strona główna.
    path('', views.index, name='index'),
    #wyświetlenie wszystkich tematów.
    path('topics/', views.topics, name ='topics'),
    #strona szczegółowa dotycząca pojedynczego tematu.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #strona przeznaczona do dodawania nowego tematu.
    path('new_topic/', views.new_topic, name='new_topic'),
    #strona przeznaczona do dodawania nowego wpisu.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]