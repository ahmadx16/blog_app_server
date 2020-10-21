from rest_framework.routers import DefaultRouter

from .views import BlogView

blog_router = DefaultRouter()
blog_router.register('', BlogView, basename='blog')

urlpatterns = blog_router.urls
