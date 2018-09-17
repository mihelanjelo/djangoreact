from rest_framework.generics import ListAPIView, RetrieveAPIView
from articles.models import Article
from .serializers import ArticleSerilizer

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilizer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilizer