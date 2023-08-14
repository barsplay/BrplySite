from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=60)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    is_auction = models.BooleanField("Уместен ли торг", help_text="Отметьте, если торг по объявлению уместен.")
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="advertisements")

    @admin.display(description="Дата публикации")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M")
            return format_html(
                "<span style='color: green; font-weight: bold'>Сегодня в {}</span>", created_time
            )
        return self.created_at.strftime("%d.%m.%Y - %H:%M ")
    
    @admin.display(description="Обновлено")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M")
            return format_html(
                "<span style='color: orange; font-weight: bold'>Сегодня в {}</span>", updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y - %H:%M ")
    
    @admin.display(description="Файлы")
    def image_display(self):
        if self.image:
            return format_html(
                "<img src='{}' width = '150px' height = '100px'>", self.image.url
            )
        return None
        # return format_html(
        #     "<img src='{}'>'", image
        # )

    
    class Meta:
        db_table = "advertisements"

    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"