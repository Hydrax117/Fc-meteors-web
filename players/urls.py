from unicodedata import name
from django.urls import URLPattern, path,include
from django.views import View
from . import views
app_name = 'player'
urlpatterns = [
    path('', views.index, name='index'),
    path('players', views.players,name='players'),
    path('matches',views.matches,name='matches'),
    path('login', views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('profile/<str:username>',views.profile,name='profile'),
    path('match/results', views.Results,name='results'),
    path('players/<str:id>/profile',views.player_detail, name='player-details'),
    path('officials/<str:id>/profile',views.officialsDetails,name='officials-details')

    
    
]