from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router_ver_1 = DefaultRouter()
router_ver_1.register(r'posts', PostViewSet, basename='posts')
router_ver_1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_ver_1.register(r'groups', GroupViewSet, basename='groups')
router_ver_1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_ver_1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
