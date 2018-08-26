from django.shortcuts import render
from .models import Article, Comment, HashTag

# Create your views here.
def index(request):
    # 쿼리 사용해서 카테고리 분류하기
    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtag_list = HashTag.objects.all()
    if not category and not hashtag:
        article_list = Article.objects.all()
    elif category:
        article_list = Article.objects.filter(category=category)
    else:
        article_list = Article.objects.filter(hashtag__name=hashtag)

    # 해시태그
    hashtag_list = HashTag.objects.all()

    # category_list = set([])
    # for article in article_list:
    #     category_list.add(article.get_category_display())
    #     category_list.add(article.category)
    # print(category_list)

    # Lambda로 위의 코드를 짧게표현
    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
        ])

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article" : article,
        "hashtag_list" : hashtag_list
    }
    return render(request, "detail.html", ctx)

# def about(request):
#     pass
