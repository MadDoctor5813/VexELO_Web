from django.db import models

# Create your models here.

class Team(models.Model):

    name = models.CharField(max_length=10)
    elo = models.FloatField()

    def __str__(self):
        return self.name


class Match(models.Model):

    redTeam1 = models.ForeignKey(Team, related_name="redTeam1_set")
    redTeam2 = models.ForeignKey(Team, related_name="redTeam2_set")
    blueTeam1 = models.ForeignKey(Team, related_name="blueTeam1_set")
    blueTeam2 = models.ForeignKey(Team, related_name="blueTeam2_set")

    redScore = models.IntegerField()
    blueScore = models.IntegerField()

    match_num = models.IntegerField()

    event_sku = models.CharField(max_length=16)
    event_start_date = models.DateField()

    def __str__(self):
        return "{0} {1} vs. {2} {3}".format(self.redTeam1.name, self.redTeam2.name, self.blueTeam1.name, self.blueTeam2.name)
