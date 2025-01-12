import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy

from .models import Post


class LatestPostsFeed(Feed):
    # The title, link, and description attributes correspond to the
    # <title>, <link>, and <description> RSS elements, respectively.
    title = "My blog"
    # The reverse() method allows you to build URLs by their name and pass optional parameters.
    # The reverse_lazy() utility function is a lazily evaluated version of reverse(). It allows you
    # to use a URL reversal before the project’s URL configuration is loaded.
    link = reverse_lazy("blog:post_list")
    description = "New posts of my blog."

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish
