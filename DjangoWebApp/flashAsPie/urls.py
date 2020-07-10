from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path

from .views import  home, order, employee
from enviro import settings

urlpatterns = [
    path('', home, name='home'),
    path('order/', order, name='order'),
    path('employee/', employee, name='employee'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
