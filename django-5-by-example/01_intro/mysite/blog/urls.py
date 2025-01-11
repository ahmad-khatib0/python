from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    # post views
    # path("", views.post_list, name="post_list"),
    path("", views.PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path("<int:post_id>/comment/", views.post_comment, name="post_comment"),
    # If using path() and converters isn’t sufficient for you, you can use re_path()
    # instead to define complex URL patterns with Python regular expressions.
]
