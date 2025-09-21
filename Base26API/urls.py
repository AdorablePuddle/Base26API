from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Base26API.quickstart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base26/', views.base26_post)
]

urlpatterns = format_suffix_patterns(urlpatterns)
