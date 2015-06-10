from django.db.models import signals
from django_proxy.signals import proxy_save, proxy_delete
from basic.blog.models import Post

signals.post_save.connect(proxy_save, Post, True)
signals.post_delete.connect(proxy_delete, Post)

