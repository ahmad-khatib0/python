from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    # changefreq and priority attributes indicate the change frequency of your post
    # pages and their relevance in your website (the maximum value is 1).
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
