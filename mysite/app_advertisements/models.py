from django.db import models

class Advertisements(models.Model):
    title = models.CharField("Заголовок", max_length=60)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    is_auction = models.BooleanField("Уместен ли торг", help_text="Отметьте, если торг по объявлению уместен.")
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        db_table = "advertisements"

    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"