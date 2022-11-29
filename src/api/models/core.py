import datetime
from django.db import models


class CommonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Common(models.Model):
    created_ts = models.DateTimeField(auto_now=True)
    name = models.CharField(help_text='Наименование', max_length=250)
    is_deleted =  models.BooleanField(default=False, blank=False, null=False)
    objects = CommonManager()
    native_objects = models.Manager()



    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def native_delete(self, *args, **kwargs):
        super().delete()

    def __str__(self):
        return ("Id: %s; Name: %s;"  % (self.id, self.name))

    class Meta:
        abstract = True
        base_manager_name = 'objects' # Заменяем менеджер для обратных связей (p.versions etc.)


class LivenessReport(Common):
    """
    Записи liveness отчетов
    """
    code = models.PositiveBigIntegerField(help_text='Код', blank=False, default=0)