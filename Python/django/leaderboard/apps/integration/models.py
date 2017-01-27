from __future__ import unicode_literals

from django.db import models
from ..login.models import User, UserManager
# Create your models here.
class LeaderManager(models.Manager):
    def leaders(self):
        leaders_list = self.order_by(total_gold_earned__first_name)[:25]
        return(leaders_list)
    def update_gold(self, new_gold, id):
        gold_up = new_gold.total_gold
        u = self.get(id = id)
        if gold_up > u.total_gold_earned:
            u.total_gold_earned = gold_up
            u.save()

class Leaderboard(models.Model):
    user = models.OneToOneField(User)
    top_score = models.IntegerField()
    games_played = models.IntegerField()
    total_gold_earned = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = LeaderManager()
