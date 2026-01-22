from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('root/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('',include('lisa.urls')),
    path('api/',include('api.urls'))
]
