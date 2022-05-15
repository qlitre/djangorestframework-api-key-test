# blog/views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated  # 追加


class PostList(generics.ListAPIView):
    permission_classes = [HasAPIKey | IsAuthenticated]  # 変更
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [HasAPIKey | IsAuthenticated]  # 変更
    queryset = Post.objects.all()
    serializer_class = PostSerializer



