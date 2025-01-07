from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    # post views
    path("", views.post_list, name="post_list"),
    path("<int:id>/", views.post_detail, name="post_detail"),
    # If using path() and converters isn’t sufficient for you, you can use re_path()
    # instead to define complex URL patterns with Python regular expressions.
]
