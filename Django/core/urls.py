from django.contrib import admin
from django.urls import path, include
from r_agrocablebot.views import DataDownloadView,DataAllDownloadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('', include('imacuna.urls')),
    # path('', include('r_agrocablebot.urls')),
    path('download-data/', DataDownloadView.as_view(), name='download-data'),
    path('download-all-data/', DataAllDownloadView.as_view(), name='download-all-data'),

]

