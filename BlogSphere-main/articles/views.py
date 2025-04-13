from datetime import datetime
from django.shortcuts import render

from .forms import RegistrationForm, LoginForm, ArticleForm, CommentForm, LikeOrDisLikeForm
from .models import RegistrationModel, ArticleModel, CommentModel, LikeOrDisLikeModel, SearchHistoryModel
from .service import getAllArticles

def registration(request):
    status = False

    if request.method == "POST":
        # Get the posted form
        registrationForm = RegistrationForm(request.POST)

        if registrationForm.is_valid():

            regModel = RegistrationModel()
            regModel.name = registrationForm.cleaned_data["name"]
            regModel.email = registrationForm.cleaned_data["email"]
            regModel.mobile = registrationForm.cleaned_data["mobile"]
            regModel.username = registrationForm.cleaned_data["username"]
            regModel.password = registrationForm.cleaned_data["password"]

            user = RegistrationModel.objects.filter(username=regModel.username).first()

            if user is not None:
                status = False
            else:
                try:
                    regModel.save()
                    status = True
                except:
                    status = False
    if status:
        return render(request, 'login.html', locals())
    else:
        response = render(request, 'registration.html', {"message": "User All Ready Exist"})

    return response

def login(request):
    uname = ""
    upass = ""
    if request.method == "GET":
        # Get the posted form
        loginForm = LoginForm(request.GET)

        if loginForm.is_valid():

            uname = loginForm.cleaned_data["username"]
            upass = loginForm.cleaned_data["password"]

            if uname == "admin" and upass == "admin":
                request.session['username'] = "admin"
                request.session['role'] = "admin"

                return render(request, "articles.html", {"articles": getAllArticles()})

        user = RegistrationModel.objects.filter(username=uname, password=upass).first()

        if user is not None:
            request.session['username'] = uname
            request.session['role'] = "user"
            return render(request, "articles.html", {"articles":getAllArticles()})
        else:
            response = render(request, 'index.html', {"message": "Invalid Credentials"})

    return response

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})


def postArticle(request):

    status = False

    articleForm = ArticleForm(request.POST, request.FILES)

    if articleForm.is_valid():

        print("valid")
        new_article = ArticleModel(
            title =articleForm.cleaned_data['title'],
            description = articleForm.cleaned_data['description'],
            date =datetime.now(),
            userid = request.session['username'],
            category = articleForm.cleaned_data['category'],
            banner_image = articleForm.cleaned_data['banner_image'],
            resource_link = articleForm.cleaned_data['resource_link'],
        )

        try:
            print("saving")
            new_article.save()
            status = True
        except:
            status = False
    else:
        print("in valid")

    if status:
        print("of")
        return render(request, "articles.html", {"articles":getAllArticles()})
    else:
        print("else")
        response = render(request, 'postarticle.html', {"message": "Article Upload Failed"})

    return response

def getArticles(request):
    return render(request, "articles.html", {"articles":getAllArticles()})

def search(request):

    str = request.GET["query"]

    resultArticles=[]

    if str!="":
        for articleBean in getAllArticles():
            if str in articleBean.article.title or str in articleBean.article.description or str in articleBean.article.category:
                resultArticles.append(articleBean)

        history=SearchHistoryModel(keyword=str,user=request.session['username'])
        history.save()

    return render(request, 'articles.html', {'articles': resultArticles})

def postComment(request):

    form = CommentForm(request.POST)

    if form.is_valid():

        text = form.cleaned_data['text']
        article_id = request.POST['article']

        new_comment = CommentModel(text=text, user=request.session['username'], article=article_id)
        new_comment.save()

        return render(request, "articles.html", {"articles":getAllArticles()})

    return render(request, "articles.html", {"articles": getAllArticles()})

def likeOrDisLike(request):

    form = LikeOrDisLikeForm(request.GET)

    if form.is_valid():

        ld = form.cleaned_data['likeOrDislike']
        article_id = form.cleaned_data['article']

        islikedOrDisLiked = LikeOrDisLikeModel.objects.filter(user=request.session['username'],
                                                              article=article_id).count()

        if islikedOrDisLiked == 1:
            LikeOrDisLikeModel.objects.filter(user=request.session['username'],
                                              article=article_id).update(status=ld)
        else:
            new_likeOrDisLike = LikeOrDisLikeModel(status=ld, user=request.session['username'], article=article_id)
            new_likeOrDisLike.save()

        return render(request, "articles.html", {"articles": getAllArticles()})

def getRecomendedArticles(request):

    searches=SearchHistoryModel.objects.filter(user=request.session['username'])

    resultArticles = set()

    for search in searches:

        for articleBean in getAllArticles():

            if search.keyword in articleBean.article.name or search.keyword in articleBean.article.description:

                resultArticles.add(articleBean)

    return render(request, 'articles.html', {'articles': resultArticles})

def getRecentArticles(request):

    resultArticles = []

    most_recent_articles = ArticleModel.objects.order_by('-datetime')[:8]

    recentList=[]

    for recent in most_recent_articles:
        recentList.append(recent.id)

    for articleBean in getAllArticles():
        if articleBean.article.id in recentList:
            resultArticles.append(articleBean)

    return render(request, 'articles.html', {'articles': resultArticles})

def deleteArticle(request):

    article_id= request.GET['article']

    ArticleModel.objects.filter(id=article_id).delete()

    for comment in CommentModel.objects.filter(article=article_id):
        CommentModel.objects.filter(id=comment.id).delete()

    for likedislike in LikeOrDisLikeModel.objects.filter(article=article_id):
        LikeOrDisLikeModel.objects.filter(id=likedislike.id).delete()

    return render(request, 'articles.html', {'articles': getAllArticles()})