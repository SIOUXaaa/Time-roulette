"""backEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login/', views.login),
    path('user/register/', views.register),
    path('schedule/get/<int:user_id>', views.get_schedule),
    path('schedule/add/', views.add_schedule),
    path('schedule/update/<int:schedule_id>', views.update_schedule),
    path('schedule/delete/<int:schedule_id>', views.delete_schedule),
    path('schedule/deleteAll/<int:user_id>', views.delete_all_schedule),
    path('memo/get/<int:user_id>', views.get_memo),
    path('memo/add/', views.add_memo),
    path('memo/update/<int:memo_id>', views.update_memo),
    path('memo/delete/<int:memo_id>', views.delete_memo),
    path('memo/deleteAll/<int:user_id>', views.delete_all_memo),

]
