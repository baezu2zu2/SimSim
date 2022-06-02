def print_rank(orged_players, before_orged_player):
    for i in range(len(orged_players)):
        print(f'{len(orged_players)-i}위 : ', end='')
        orged_players[i].print_info()
        if before_orged_player is not None and i >= len(orged_players)-10 and len(before_orged_player) >= 10:
            for j in range(len(before_orged_player)-10, len(before_orged_player)):
                if orged_players[i].id == before_orged_player[j].id:
                    change = i-j+len(before_orged_player)-len(orged_players)
                    #100->99 1->2 -1 뒤-앞
                    #99->100 2->1 1 뒤-앞
                    #100->94 1->2 -1 뒤-앞 = -6
                    #                +죽은사람(5) = -1
                    #죽은 사람 = 처음 플레이어 - 나중 플레이어
                    #99->95 2->1 1 뒤-앞 = -4
                    #              +죽은사람(5) = 1

                    #99->93 -6+1 = -5

                    if change == 0:
                        print('(-)')
                        break
                    print(f'({change})')
                    break
            else:
                print('(NEW!)')
        else:
            print()


def print_guild(orged_rank, before_orged_rank):
    for i in range(len(orged_rank)):
        print(f'{len(orged_rank)-i}위 : ', end='')
        orged_rank[i].print_info()
        if before_orged_rank is not None and i >= len(orged_rank)-5 and len(before_orged_rank) >= 5:
            for j in range(len(before_orged_rank)-5, len(before_orged_rank)):
                if orged_rank[i].name == before_orged_rank[j].name:
                    change = i-j+len(before_orged_rank)-len(orged_rank)

                    if change == 0:
                        print('(-)')
                        break
                    print(f'({change})')
                    break
            else:
                print('(NEW!)')
        else:
            print()
