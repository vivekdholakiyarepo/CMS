from django.urls import path
from cms.views import(
    UserListCreateView,
    UserUpdateRetriveDestroy,

    PostListCreateView,
    PostRetrieveUpdateDestroyView,

    LikeListCreateView,
    LikeRetrieveUpdateDestroyView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view()),
    path('users/<int:pk>', UserUpdateRetriveDestroy.as_view()),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>', PostRetrieveUpdateDestroyView.as_view()),
    path('likes', LikeListCreateView.as_view()),
    path('likes/<int:pk>', LikeRetrieveUpdateDestroyView.as_view()),
]
