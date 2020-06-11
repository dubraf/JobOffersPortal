from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)