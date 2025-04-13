from .beans import ArticleBean
from .models import LikeOrDisLikeModel, CommentModel, ArticleModel


def getAllArticles():

    articles = []

    for article in ArticleModel.objects.all():

        article.banner_image = str(article.banner_image).split("/")[1]

        comments = CommentModel.objects.filter(article=article.id)

        likes = 0
        dislikes = 0

        for likeordislike in LikeOrDisLikeModel.objects.filter(article=article.id):

            if int(likeordislike.status) == 0:
                dislikes = dislikes + 1
            elif int(likeordislike.status) == 1:
                likes = likes + 1

        bean = ArticleBean(article, comments, likes, dislikes)

        print()
        articles.append(bean)

    return articles

def getArticleByUser(userid):

    articles = []

    for article in ArticleModel.objects.filter(userid=userid):
        article.banner_image = str(article.banner_image).split("/")[1]

        comments = CommentModel.objects.filter(article=article.id)

        likes = 0
        dislikes = 0

        for likeordislike in LikeOrDisLikeModel.objects.filter(article=article.id):

            if int(likeordislike.status) == 0:
                dislikes = dislikes + 1
            elif int(likeordislike.status) == 1:
                likes = likes + 1

        bean = ArticleBean(article, comments, likes, dislikes)
        articles.append(bean)

    return articles