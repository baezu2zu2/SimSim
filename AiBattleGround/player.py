import random as r
import Country
import typing
import data


class Player():
    def __init__(self, id, hp=100, atk=10, left_heal=3):
        self.hp = hp
        self.atk = atk
        self.id = id
        self.left_heal = left_heal
        self.score = 0
        self.guild : Country.Guild or None = None

    def get_power(self):
        return self.hp+self.atk

    def death(self):
        print(f'{self.id}번 플레이어님이 사망하셨습니다.')
        if self.guild is not None:
            last_guild = self.guild
            self.guild.leave_guild(self)
            if len(last_guild.players) == 0:
                data.guilds.remove(last_guild)
        data.players.remove(self)

    def attack(self, target):
        target.hp -= self.atk*int(r.uniform(0.5, 2))
        if target.hp <= 0:
            target.death()

    def print_info(self):
        print(f'{self.id}번 플레이어-체력:{self.hp}, 공격력:{self.atk}, 남은 구급상자 개수:{self.left_heal}, 전투력: {self.atk+self.hp}', end='')
        if self.guild is not None:
            print(f', 길드: {self.guild.name}', end='')

    def farming(self):
        self.atk += r.randint(1, 10)
        self.left_heal += r.randint(1, 3)

    def heal(self):
        if self.left_heal <= 0:
            return
        self.hp *= r.uniform(1.1, 1.9)
        self.hp = int(self.hp)
        self.left_heal -= 1

    def select_action(self, player_list, attack_num, heal_num, farming_num):
        rand = r.randint(1, attack_num+heal_num+farming_num)
        if rand <= attack_num:
            target = r.choice(player_list)
            if self.guild is not None:
                while self.guild.is_player_exists(target) and len(data.guilds) > 1:
                    target = r.choice(player_list)

            self.attack(target)
        elif rand <= heal_num and self.left_heal > 0:
            self.heal()
        else:
            self.farming()

    def guild_interact(self, player_list, guild_list, top_ten):
        if self.guild is not None:
            if (self.get_power() / self.guild.team_power() * 100 >= 5 or self.get_power() / self.guild.team_power() * 100 <= 0.1)\
                    and self.guild.leader != self:
                self.guild.leave_guild(self)
            return None

        if r.randint(1, 2) == 1 and top_ten.count(self) > 0:
            data.guilds.append(Country.Guild(self, str(self.id)))
        elif r.randint(1, 3) == 1 and len(guild_list) >= 1:
            pow_sum = 0
            max_pow = guild_list[0].team_power()
            for i in guild_list[1:]:
                if max_pow < i.team_power():
                    max_pow = i.team_power()

            for i in guild_list:
                pow_sum += max_pow-i.team_power()+10

            rand = r.randint(1, pow_sum)
            dst = 1
            for i in guild_list:
                if rand <= dst:
                    i.join_guild(self)
                    break
                dst += max_pow - i.team_power() + 10



        return None

    def select(self, average_hp, average_atk, player_list, guild_list: typing.List[Country.Guild], top_ten, guild_permitted=False):
        if average_hp < self.hp and average_atk < self.atk:
            self.select_action(player_list, 2, 1, 1)
        elif average_hp - self.hp >= average_atk - self.atk:
            self.select_action(player_list, 1, 2, 1)
        else:
            self.select_action(player_list, 2, 1, 2)

        if guild_permitted:
            self.guild_interact(player_list, guild_list, top_ten)

    def __copy__(self):
        return Player(self.id, self.hp, self.atk, self.left_heal)

    def copy(self):
        return self.__copy__()


def randomize_player(id, min_hp, max_hp, min_atk, max_atk, min_left_heal, max_left_heal):
    return Player(id, hp=r.randint(min_hp, max_hp), atk=r.randint(min_atk, max_atk), left_heal=r.randint(min_left_heal, max_left_heal))


def randomize_players(num=100, min_hp=10, max_hp=100, min_atk=1, max_atk=30, min_left_heal=0, max_left_heal=5):
    players = []

    for i in range(num):
        players.append(randomize_player(i+1, min_hp, max_hp, min_atk, max_atk, min_left_heal, max_left_heal))

    return players


def organize_players(players):
    if len(players) <= 1:
        return players
    pivot = players[0]
    lessor_list, equal_list, greater_list = [], [], []

    pivot_power = pivot.hp+pivot.atk
    for i in players:
        power = i.hp+i.atk
        if power < pivot_power:
            lessor_list.append(i)
        elif power > pivot_power:
            greater_list.append(i)
        else:
            equal_list.append(i)
    return organize_players(lessor_list)+equal_list+organize_players(greater_list)


def get_average(players, str):
    sum = 0
    if str.lower() == 'hp':
        for i in players:
            sum += i.hp
    elif str.lower() == 'atk':
        for i in players:
            sum += i.atk
    elif str.lower() == 'left_heal':
        for i in players:
            sum += i.left_heal

    return sum / len(players)
