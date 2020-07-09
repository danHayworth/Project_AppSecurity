from django.urls import path

from .views import employee, home, order
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('order/', order, name='order'),
    path('<int:user_id>', employee, name='employee')
]
urlpatterns += staticfiles_urlpatterns()
