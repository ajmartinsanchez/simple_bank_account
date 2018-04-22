from django.conf.urls import url
from home import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.Home.as_view())),
    # url(r'^profile/$', views.update_profile),
    url(r'^account/logout/$', views.Logout.as_view()),
]