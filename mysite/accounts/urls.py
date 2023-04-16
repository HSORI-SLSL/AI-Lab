from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup2/', signup2, name='signup2'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('home/signup/', signup, name='signup'),
]