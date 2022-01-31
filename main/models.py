from django.db import models


class FeedBack(models.Model):
    data = models.TextField('Отзыв')
    category = models.Value("Категория отзыва")

    def __str__(self):
        return self.data
        
