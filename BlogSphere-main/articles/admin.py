from django.contrib import admin

# Register your models here.
from .models import RegistrationModel, CommentModel, SearchHistoryModel, LikeOrDisLikeModel, ArticleModel

admin.site.register(RegistrationModel)
admin.site.register(ArticleModel)
admin.site.register(CommentModel)
admin.site.register(SearchHistoryModel)
admin.site.register(LikeOrDisLikeModel)
