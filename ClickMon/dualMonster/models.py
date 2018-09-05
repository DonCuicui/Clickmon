from django.db import models

class Attack(models.Model):
    name = models.CharField(max_length=20)
    samina_cost=models.IntegerField

class Summoner(models.Model):
    name = models.CharField(max_length=20)
    mdp = models.CharField(max_length=20)
    MALE = 'Mr'
    FEMALE = 'Mme'
    GENDER_SELECTION = (
        (MALE, 'Garçon'),
        (FEMALE, 'Fille'),
    )
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION, default=MALE)
    money = models.IntegerField(default=50)
    exp = models.IntegerField(default=0)
    def __str__(self):
        return f'SALUT JE SUIS LE DRESSEUR DE CLICKMON {self.name}'


class Clickmon(models.Model):
    summoner = models.ForeignKey(Summoner, related_name='clickmon',
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    hp_max = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    element = models.CharField(max_length=20)
    img_front = models.ImageField(max_length=100)
    img_back =models.ImageField(max_length=100)
    stamina = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    def __str__(self):
        return f'SALUT JE SUIS LE CLICKMON {self.name}'


