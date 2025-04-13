
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from articles.views import login, registration, logout, postArticle, getArticles, search, postComment, \
    likeOrDisLike, getRecomendedArticles, getRecentArticles, deleteArticle

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('login/',TemplateView.as_view(template_name = 'login.html'),name='login'),
    path('loginaction/',login,name='loginaction'),

    path('registration/',TemplateView.as_view(template_name = 'registration.html'),name='registration'),
    path('regaction/',registration,name='regaction'),

    path('postarticle/',TemplateView.as_view(template_name = 'postarticle.html'),name='postarticle'),
    path('postarticleaction/',postArticle,name='postarticleaction'),

    path('getarticles/',getArticles,name='articlelist'),
    path('search/',search,name='searcharticles'),
    path('postcomment/',postComment,name='postcomment'),
    path('likedislike/',likeOrDisLike,name='likedislike'),
    path('recomendations/',getRecomendedArticles,name='recomendations'),
    path('recentarticles/',getRecentArticles,name='recentarticles'),

    path('deletearticle/',deleteArticle,name='deletearticles'),

    path('logout/',logout,name='logout'),
]
