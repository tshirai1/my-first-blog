## memo
## models.py ... DBテーブルを定義
## 👇モデルフィールド設定テンプレート
## https://qiita.com/okoppe8/items/a1149b2be54441951de1

from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
	# 著者
    author = models.ForeignKey(
		# models.ForeignKey ... 1対多となる関係（記述は子）
		# この場合、１ユーザーに対して幾つかの著者を使い分けることが可能
		settings.AUTH_USER_MODEL,# 親となるモデルを指定
		on_delete=models.CASCADE,# 削除する際の依存関係
		)
	# タイトル
    title = models.CharField(
		max_length=200
		)
	# 本文
    text = models.TextField()
	# 作成日
    created_date = models.DateTimeField(
		default=timezone.now
		)
	# 公開日
    published_date = models.DateTimeField(
		blank=True,
		null=True,
	)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
