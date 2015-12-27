from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #empty string i.e "http://127.0.0.1:8000/" will be direced to post_list view
	# The last part name='post_list' is the name of the URL that will be used to identify the view    
]