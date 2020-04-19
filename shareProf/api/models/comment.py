from django.db import models
from .log import Log
from .catalog import CatClassDifficulty
from .catalog import CatClassExperience


class CommentText(models.Model):
    content = models.CharField(max_length=300,
                               null=False,
                               blank=False)


class Ratting(models.Model):
    class_difficulty = models.ForeignKey(CatClassDifficulty,
                                         on_delete=models.PROTECT)

    class_experience = models.ForeignKey(CatClassExperience,
                                         on_delete=models.PROTECT)


class CommentInfo(models.Model):
    id_log_fk = models.ForeignKey(Log, on_delete=models.PROTECT)
    text = models.OneToOneField(CommentText, on_delete=models.PROTECT, null=True)
    ratting = models.OneToOneField(Ratting, on_delete=models.PROTECT, null=True)
