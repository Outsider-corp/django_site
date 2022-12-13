from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', index, name="index"),
    # path('', cache_page(60)(ClassNew.as_view()), name="index"),
    path('', ClassNew.as_view(), name="index"),
    path('category/<int:cat_id>/', ClassCategory.as_view(), name="cats"),
    path('news/<int:news_id>/', ClassView.as_view(), name="view_post"),
    path('add_post/', ClassCreate.as_view(), name="add_post"),
    path('registration/', registration, name="registration"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('mail/', mail_send, name="mail"),
]
