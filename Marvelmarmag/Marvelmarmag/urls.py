"""Marvelmarmag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Marvelapp import views 
 
urlpatterns = [ 
    url(r'^admin/', admin.site.urls), 
    url(r'^contactcarrers/', views.contactcarrers_view),
    url(r'^$',views.home_view,name='marmag'),
    url(r'^service/',views.service_view),
    url(r'^project/',views.project_view),
    url(r'^aboutus/',views.aboutus_view),
    url(r'^archieture/',views.archieture_view),
    url(r'^drafting/',views.drafting_view),
    url(r'^engineering/',views.engineering_view),
    url(r'^valueadded/',views.valueadded_view),
    url(r'^contactprojects/', views.contactprojects_view),
    url(r'^contactservices/', views.contactservices_view),
    url(r'^commercialp/',views.commercialp_view),
    url(r'^industrialp/',views.industrialp_view),
    url(r'^infrastructurep/',views.infrastructurep_view),
    url(r'^oilgasp/',views.oilgasp_view),
    url(r'^powerp/',views.powerp_view),
    url(r'^specialp/',views.specialp_view),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
