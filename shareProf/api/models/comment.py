from django.db import models
from .log import Log
from .catalog import CatSubjectDifficulty
from .catalog import CatSubjectExperience
from .user import UserInfo
from .education import Professor
from .education import Subject


class CommentText(models.Model):
    content = models.CharField(max_length=300,
                               null=False,
                               blank=False)


class Rating(models.Model):
    class_difficulty = models.ForeignKey(CatSubjectDifficulty,
                                         on_delete=models.PROTECT)

    class_experience = models.ForeignKey(CatSubjectExperience,
                                         on_delete=models.PROTECT)


class CommentInfo(models.Model):
    log = models.ForeignKey(Log, on_delete=models.PROTECT)
    user = models.ForeignKey(UserInfo, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject,on_delete=models.PROTECT)
    text = models.OneToOneField(CommentText, on_delete=models.PROTECT, null=True)
    rating = models.OneToOneField(Rating, on_delete=models.PROTECT, null=True)
