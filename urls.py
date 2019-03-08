from django.urls import path

import views

urlpatterns=[
    path('', views.index),
    path('about', views.about),
    path('resume', views.resume),
    path('education', views.education),
    path('interests', views.interests),
    path('blog', views.blog), 
     
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

