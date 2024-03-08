from django.urls import path
from comments.views import comment_on_post,view_all_comments

urlpatterns = [
    path('post/<int:post_id>/all_comments/',view_all_comments,name='view_all_comments'),
    path('post/<int:post_id>/comment_to_post/',comment_on_post,name='comment_to_post'),

]
