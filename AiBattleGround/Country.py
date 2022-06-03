import player


class Guild:
    def team_power(self):
        total_power = 0
        for i in self.players:
            total_power += i.get_power()

        self.total_power = total_power
        return total_power

    def new_leader(self):
        leader_power = self.leader.hp+self.leader.atk

        for i in self.players:
            power = i.hp+i.atk
            if leader_power < power:
                self.leader = i

    def __init__(self, leader, name: str):
        self.leader = leader
        self.players = []
        self.players.append(leader)
        leader.guild = self
        self.name: str = name
        self.total_power = self.team_power()

    def join_guild(self, player):
        self.players.append(player)
        player.guild = self

    def leave_guild(self, player):
        self.players.remove(player)
        if self.leader == player:
            self.new_leader()
        player.guild = None

    def is_player_exists(self, player):
        return self.players.count(player) > 0

    def print_info(self):
        print(f'{self.name} 길드-플레이어 수:{len(self.players)}, 길드장:{self.leader.id}, 길드 총 전투력:{self.total_power}', end='')


def organize_guild(guilds):
    if len(guilds) <= 1:
        return guilds
    pivot = guilds[0]
    lessor_list, equal_list, greater_list = [], [], []

    pivot_power = pivot.team_power()
    for i in guilds:
        power = i.team_power()
        if power < pivot_power:
            lessor_list.append(i)
        elif power > pivot_power:
            greater_list.append(i)
        else:
            equal_list.append(i)
    return organize_guild(lessor_list)+equal_list+organize_guild(greater_list)

