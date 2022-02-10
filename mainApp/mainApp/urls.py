from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('rest_api_test/', include('rest_api_test.urls')),

    path('blog', include('blog.urls'), name='blog'),
    path('youtube', include('youtube.urls'), name='youtube'),
    path('bookStore', include('bookStore.urls'), name='bookStore'),
    path('admin', admin.site.urls),
]
