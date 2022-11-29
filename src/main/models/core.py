from django.db import models
from main.utils import get_username_from_call_stack


class CommonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Common(models.Model):
    name = models.CharField(help_text='Наименование', max_length=250)
    is_deleted =  models.BooleanField(default=False, blank=False, null=False)
    objects = CommonManager()
    native_objects = models.Manager()

    def save(self, *args, **kwargs):
        if hasattr(self, 'created_by'):
            if not self.created_by:
                self.created_by = get_username_from_call_stack()
        if hasattr(self, 'changed_by'):
            self.changed_by = get_username_from_call_stack()
        super().save()

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


class Company(Common):
    """
    Компания это вершина иерархии объектов (Компания - Площадка(Area) - Ресурсы)
    Пользователь имеет доступ только к тем ресурсам которые привязаны к его компании.
    """
    short_name = models.CharField(help_text='Короткое наименование',max_length=100)
    full_name = models.CharField(help_text='Полное наименование', max_length=250)
    code = models.PositiveBigIntegerField(help_text='Код ЦФО', blank=False, default=0)
    root_dir = models.CharField(help_text='Каталог со статикой', max_length=100)

    def to_json(self, is_short=True, target_date=None):
        result={
            "id": self.id,
            "name": self.name,
            "short_name": self.short_name,
            "full_name": self.full_name,
            "code": self.code,
            "root_dir": self.root_dir,
            "areas": {} if is_short else self.get_areas_json(is_short=is_short, target_date=target_date)
        }
        return result

    def get_areas_json(self, is_short=True, target_date=None):
        result = []
        for a in self.area_set.all():
            result.append(a.to_json(is_short, target_date))
        return result