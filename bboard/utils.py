from django.db import models


class DataMixin:
    weight = models.IntegerField(verbose_name="Вес", default=0,)

    def get_extra_context_data(self, **kwargs):
        extra_context = kwargs
        extra_context['weight'] = {
            'weight': 0
        }
        return extra_context