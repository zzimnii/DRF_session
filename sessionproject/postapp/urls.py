from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CommentViewSet
from django.conf import settings
from django.conf.urls.static import static


post_router = SimpleRouter(trailing_slash=False) # 왜 False?!?!    /는 계층관계를 나타내는것
post_router.register('posts', PostViewSet, basename='post')

comment_router = SimpleRouter(trailing_slash=False)
comment_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(post_router.urls)),
    path('posts/<int:post_id>/', include(comment_router.urls)),
    path('comments/<int:comment_id>/',include(comment_router.urls)),    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)