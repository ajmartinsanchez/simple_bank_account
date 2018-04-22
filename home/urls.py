from django.conf.urls import url
from home import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.Home.as_view())),
    url(r'^client/add', login_required(views.AddClient.as_view()), name='add_client'),
    url(r'^client/update/(?P<user_id>\d+)/', login_required(views.UpdateClient.as_view()), name='update_client'),
    url(r'^client/remove/(?P<user_id>\d+)', login_required(views.RemoveClient.as_view()), name='remove_client'),
    url(r'^account/logout/$', views.Logout.as_view()),
]