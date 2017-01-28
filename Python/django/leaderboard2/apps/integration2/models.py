from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# Create your models here.

class LeaderManager(models.Manager):
    # def leaders(self):
    #     leader_list = Leaderboard.objects.filter(total_gold_earned__user_first_name)[:25]
    #     # leader_list = Leaderboard.objects.all()
    #     return(leader_list)

    def curr_gold(self, id):
        user_curr_gold = self.objects.get(id=id)
        return (user_curr_gold)

    def save_gold(self, new_gold):
        print new_gold
        try:
            user_earned_more_gold = self.get(user__id=int(new_gold['id']))
            user_earned_more_gold.total_gold_earned += new_gold['add_gold_to_total_gold']
            print user_earned_more_gold.total_gold_earned
            user_earned_more_gold.games_played += new_gold['num_games']
            print user_earned_more_gold.games_played

            if user_earned_more_gold.top_score < new_gold['new_top_score']:
                user_earned_more_gold.top_score += new_gold['new_top_score']
            else:
                pass
                user_earned_more_gold.save()
        except Leaderboard.DoesNotExist:
            u = User.objects.get(id=new_gold['id'])
            user_earned_more_gold = self.create(user=u, top_score=new_gold['new_top_score'], games_played=new_gold['num_games'], total_gold_earned=new_gold['add_gold_to_total_gold'])
        return (user_earned_more_gold)

class Leaderboard(models.Model):
    user = models.OneToOneField(User)
    top_score = models.IntegerField()
    games_played = models.IntegerField()
    total_gold_earned = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = LeaderManager()
