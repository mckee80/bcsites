from django.urls import path

from . import views

app_name = 'bcglacier'
urlpatterns = [
    path('', views.index, name='index'),
	path('<int:id>/', views.detail, name='detail'),
	path('list/', views.list, name='list'),
	path('<int:id>/votecomment/', views.votecomment, name='votecomment'),
	path('<int:id>/addinfo/', views.addinfo, name='addinfo'),
	path('<int:id>/addpicture/', views.addpicture, name='addpicture'),
	path('signup/', views.signup, name='signup'),
	path('processsignup/', views.processsignup, name='processsignup'),
	path('setMarkers/', views.setMarkers, name='setMarkers'),
	path('update_park/', views.update_park, name='update_park'),
    # path('update_park/<slug:park>', views.update_park, name='update_park'),
]
