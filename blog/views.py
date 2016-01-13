from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import CommentForm
from blog.models import Article, Comment
from core.utils import Paginator


def template(tpl_name):
    def _wrapper(func):
        def _wrapped_view(request, *args, **kwargs):
            return render(request, tpl_name, func(request, *args, **kwargs))

        return _wrapped_view

    return _wrapper


@template('blog/home.html')
def home(request):
    paginator = Paginator(list(Article.objects.all()) * 20, 4, request.GET.get('page', 1))
    return {
        'paginator': paginator,
    }


@template('blog/about.html')
def about(request):
    return


#
# def show_article(request, article_id):
#     return render(request, 'blog/article.html', {'article': Article.objects.get(id=article_id)})

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()#.filter(parent__isnull=True)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            if request.user.is_authenticated():
                comment.user = request.user
            comment.article = article
            comment.save()
        return redirect('article', article_id)
    return render(request, 'blog/article.html', {
        'article': article,
        'comments': comments,
        'form': comment_form,
    })


def regis(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/registration.html', {'form': form})