from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_note$', views.add_note),
    url(r'^add_note/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)$', views.add_note_from_view),
    url(r'^add_note_from_view/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)$', views.add_note_from_view),
    url(r'^append_note/(?P<id>\d+)$', views.append_note),
    url(r'^add_category$', views.add_category),
    url(r'^add_category_from_view/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)$', views.add_category_from_view),
    url(r'^delete_category/(?P<id>\d+)$', views.delete_category),
    url(r'^delete_sub_category/(?P<id>\d+)$', views.delete_sub_category),
    url(r'^delete_subcontent/(?P<id>\d+)$', views.delete_subcontent),
    url(r'^delete_subcontent_from_view/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)/(?P<id>\d+)$', views.delete_subcontent_from_view),
    url(r'^delete_note/(?P<id>\d+)$', views.delete_note),
    url(r'^delete_note_from_view/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)/(?P<id>\d+)$', views.delete_note_from_view),
    url(r'^create_sub_category/(?P<id>\d+)$', views.create_sub_category),
    url(r'^create_subcategory_from_view/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)/(?P<id>\d+)$', views.create_subcategory_from_view),
    url(r'^append_note_from_view/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)/(?P<id>\d+)$', views.append_note_from_view),
    url(r'^append_note_from_view(?P<id>\d+)$', views.append_note_from_view),
    url(r'^view/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)$', views.view_sub_category),
    url(r'^logout$', views.logout),
]