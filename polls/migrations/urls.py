
from django.http import HttpResponse


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^polls/', include('polls.urls')),

]