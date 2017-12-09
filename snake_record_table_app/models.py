from django.db import models

class RecordManager(models.Manager):
    def get_new_record(self, player_name, score):
        return self.create(player_name=player_name, score=score)

class Record(models.Model):
    player_name = models.CharField(max_length=30)
    score = models.SmallIntegerField()
    joke_comment = models.CharField(max_length=100)

    objects = RecordManager()

    def __str__(self):
        return "{0}: {1} pts".format(self.player_name, str(self.score))
