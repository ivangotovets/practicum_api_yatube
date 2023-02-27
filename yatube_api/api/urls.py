from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_1 = DefaultRouter()

router_1.register('posts', PostViewSet)
router_1.register('groups', GroupViewSet)
router_1.register('follow', FollowViewSet, basename='follow'),
router_1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router_1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
