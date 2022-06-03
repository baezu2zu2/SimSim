import player as p
import ui
import Country as c
import data


data.playernum = input('플레이어 몇 명이서 싸울지 입력 하세요(기본값:100)>>')
data.min_hp = input('최소 hp를 입력 하세요(기본값:10)>>')
data.max_hp = input('최대 hp를 입력 하세요(기본값:100)>>')
data.min_atk = input('최소 공격력을 입력 하세요(기본값:1)>>')
data.max_atk = input('최대 공격력을 입력 하세요(기본값:30)>>')
data.min_left_heal = input('최소 구급상자 개수를 입력 하세요(기본값:0)>>')
data.max_left_heal = input('최대 구급상자 개수를 입력 하세요(기본값:5)>>')
data.guild = input('길드 창립을 허용하시려면 y를 입력하세요(기본값:창립 불가)>>')

try:
    if data.guild.lower() == 'y':
        data.guild = True

    data.playernum, data.min_hp, data.max_hp, data.min_atk, data.max_atk, data.min_left_heal, data.max_left_heal \
        = int(data.playernum), int(data.min_hp), int(data.max_hp), int(data.min_atk), int(data.max_atk), int(data.min_left_heal), int(
        data.max_left_heal)
    data.players = p.randomize_players(data.playernum, data.min_hp, data.max_hp, data.min_atk, data.max_atk, data.min_left_heal, data.max_left_heal)
except ValueError:
    print('잘못된 값이 있습니다. 모든 값을 기본값으로 설정합니다.')
    data.players = p.randomize_players()

before_orged_player = None
before_orged_guilds = None

while True:
    orged_guilds = c.organize_guild(data.guilds)
    orged_players = p.organize_players(data.players)

    ui.print_rank(orged_players, before_orged_player)
    print('-' * 20)
    ui.print_guild(orged_guilds, before_orged_guilds)

    print(f'총 플레이어 명수 : {len(data.players)}, 길드 개수 : {len(data.guilds)}, 길드 창립 허용 여부 : {data.guild}')

    input('다음 턴을 실행 하려면 엔터>>')

    data.kings.append(orged_players[-1].copy())

    before_orged_player = orged_players.copy()
    before_orged_guilds = orged_guilds.copy()

    average_hp = p.get_average(data.players, 'hp')
    average_atk = p.get_average(data.players, 'atk')

    for i in data.players:
        i.select(average_hp, average_atk, data.players, data.guilds, orged_players[-10:],  data.guild)

    if len(data.players) == 1:
        print(f'{data.players[0].id}번 플레이어님이 승리하셨습니다!')
        break
    elif len(data.players) == 0:
        print('아무도 승자가 되지 못했습니다...')
        break

    print('\n')

if input('역대 1등 목록을 보시려면 y를 입력하고, 아니면 그냥 엔터를 눌러주세요>>').lower() == 'y':
    for i in data.kings:
        i.print_info()
        print()
    print(f'최종 승지 : {data.players[0].id}번 플레이어')
    data.players[0].print_info()