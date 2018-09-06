from django.db import models
from math import floor


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

    def attack(self, monster):
        enemy_hp = monster.hp
        monster.hp = monster.hp - self.damage
        dealed_damage = enemy_hp - monster.hp
        return f'{monster.name} a subit {dealed_damage}'
    @property
    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def maudire(self):
        self.level -= 1

    FIRST_LEVEL_EXP = 0
    SECOND_LEVEL_EXP = 100

    @property
    def level(self):
        return floor((self.exp / self.SECOND_LEVEL_EXP) ** .5 + 1)

    @level.setter
    def level(self, new_level):
        self.exp = max(self.FIRST_LEVEL_EXP, ((new_level - 1) * self.SECOND_LEVEL_EXP) ** 2)

    def __str__(self):
        return f'{self.name} niv {self.level} de {self.summoner}'


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

    FIRST_LEVEL_EXP = 0
    SECOND_LEVEL_EXP = 100

    @property
    def level_attack_one(self):
        return floor((self.exp_one / self.SECOND_LEVEL_EXP) ** .5 + 1)

    @level_attack_one.setter
    def level_attack_one(self, new_level):
        self.exp_one = max(self.FIRST_LEVEL_EXP, ((new_level - 1) * self.SECOND_LEVEL_EXP) ** 2)

    @property
    def level_attack_two(self):
        return floor((self.exp_two / self.SECOND_LEVEL_EXP) ** .5 + 1)

    @level_attack_two.setter
    def level_attack_two(self, new_level):
        self.exp_two = max(self.FIRST_LEVEL_EXP, ((new_level - 1) * self.SECOND_LEVEL_EXP) ** 2)

    @property
    def level_attack_three(self):
        return floor((self.exp_three / self.SECOND_LEVEL_EXP) ** .5 + 1)

    @level_attack_three.setter
    def level_attack_three(self, new_level):
        self.exp_three = max(self.FIRST_LEVEL_EXP, ((new_level - 1) * self.SECOND_LEVEL_EXP) ** 2)

    @property
    def level_attack_four(self):
        return floor((self.exp_four / self.SECOND_LEVEL_EXP) ** .5 + 1)

    @level_attack_four.setter
    def level_attack_four(self, new_level):
        self.exp_four = max(self.FIRST_LEVEL_EXP, ((new_level - 1) * self.SECOND_LEVEL_EXP) ** 2)
    def __str__(self):
        return f'Attaques de {self.Clickmon}'

