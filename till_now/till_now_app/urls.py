from django.conf.urls import url
from till_now_app import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^formpage/$', views.form_view, name="formpage")
]
