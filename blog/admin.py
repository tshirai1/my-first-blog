## memo
## Django管理画面で、モデルを追加できる。
## admin.pyは、Django管理画面の設定・オプション？
## https://python.keicode.com/django/admin-site-how-to-use.php

from django.contrib import admin
from .models import Post

admin.site.register(Post)
