from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import LogRecordViewSetCreate, LogRecordViewSetGet, LogRecordViewSetDelete, LogRecordViewSetList,\
    LogRecordViewSetUpdate, ask

urlpatterns = [
    path('log/get/<int:pk>/', LogRecordViewSetGet.as_view()),
    path('log/delete/<int:pk>/', LogRecordViewSetDelete.as_view()),
    path('log/list', LogRecordViewSetList.as_view()),
    path('log/create', LogRecordViewSetCreate.as_view()),
    path('log/update/<int:pk>/', LogRecordViewSetUpdate.as_view()),
    path('ask/', ask)
]
