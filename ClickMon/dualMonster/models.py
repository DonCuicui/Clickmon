from django.db import models

class Attack(models.Model):
    name = models.CharField(max_length=20)
    stamina_cost = models.IntegerField(default=0)
    img =models.ImageField(max_length=100)
    damage = models.IntegerField(default=0)
    element = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name} attaque type : {self.element}'

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
        return f'{self.name}'

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
    stamina_max = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.name} de {self.summoner}'

class AttackPack(models.Model):
    Clickmon = models.ForeignKey(Clickmon, related_name='clickmon_attack', on_delete=models.CASCADE)
    attack_one = models.ForeignKey(Attack, related_name='attack_one_rn', on_delete=models.CASCADE)
    exp_one = models.IntegerField(default=0)
    attack_two = models.ForeignKey(Attack, related_name='attack_two_rn', on_delete=models.CASCADE)
    exp_two = models.IntegerField(default=0)
    attack_three = models.ForeignKey(Attack, related_name='attack_three_rn', on_delete=models.CASCADE)
    exp_three = models.IntegerField(default=0)
    attack_four = models.ForeignKey(Attack, related_name='attack_four_rn', on_delete=models.CASCADE)
    exp_four = models.IntegerField(default=0)
    def __str__(self):
        return f'Attaques de {self.Clickmon}'

