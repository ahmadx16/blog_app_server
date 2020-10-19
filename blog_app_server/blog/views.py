from rest_framework.viewsets import ModelViewSet

from .models import Blog
from .serializers import BlogSerializer


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
