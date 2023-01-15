"""famyli URL Configuration

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
from appfamyli import views

urlpatterns = [
    path('item1/', views.item1),
    path('item2/', views.item2),
    path('item3/', views.item3),
    path('', views.index, name='index'),
    # path('parent-child/', parent_child_view, name='parent_child'),
    path('team/<int:town_id>/', views.team, name='team'),
    path('subteam/<int:team_id>/', views.subteam, name='subteam'),
    path('admin/', admin.site.urls),
    path('view_in_browser/<int:parent_id>/', views.view_in_browser),

]
