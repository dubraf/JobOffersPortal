from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from restApi import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('tags/', views.TagsList.as_view()),
    path('jobs/', views.JobAvertisementList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)