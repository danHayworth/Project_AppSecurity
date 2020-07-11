from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path, include

from .views import  home, order, employee
from enviro import settings

urlpatterns = [
    path('', home, name='home'),
    path('order/', order, name='order'),
    path('staff/', employee, name='staff'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
