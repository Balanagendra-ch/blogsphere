from django.forms import Form, CharField, PasswordInput, FileField

class RegistrationForm(Form):
    username =CharField(max_length=50)
    name = CharField(max_length=50)
    password =CharField(max_length=50)
    email =CharField(max_length=50)
    mobile =CharField(max_length=50)

class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())

class ArticleForm(Form):
    title = CharField(max_length=5000)
    description = CharField(max_length=5000)
    category = CharField(max_length=5000)
    banner_image = FileField()
    resource_link = CharField(max_length=5000)

class CommentForm(Form):
    text = CharField(max_length=300)
    article = CharField(max_length=60)

class SearchHistoryForm(Form):
    keyord = CharField(max_length=300)

class LikeOrDisLikeForm(Form):
    likeOrDislike = CharField(max_length=100)
    article = CharField(max_length=60)