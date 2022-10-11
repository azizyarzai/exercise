from django.db import models


class ProductManager(models.Manager):
    # def all(self):
    #     return super().filter(is_available=True)

    def get_availibes(self):
        return self.filter(is_available=True)
