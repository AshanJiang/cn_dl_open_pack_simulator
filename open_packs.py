from random import randint

ur_list = []
sr_list = []
r_list = []
n_list = []
packs_list = []


def init_cards_list_big():
    global ur_list, sr_list, r_list, n_list
    ur_list = ["UR" + str(i) for i in range(1, 11)]
    sr_list = ["SR" + str(i) for i in range(1, 13)] * 2
    r_list = ["R" + str(i) for i in range(1, 37)] * 6
    n_list = ["N" + str(i) for i in range(1, 43)] * 8
    r_list.extend(["R1", "R2"] * 2)
    n_list.extend(["N1", "N2", "N3", "N4", "N5"] * 2)


def print_all_cards():
    global ur_list, sr_list, r_list, n_list
    print('ur:{}\nsr:{}\nr:{}\nn:{}'
          .format(ur_list, sr_list, r_list, n_list))
    print('The number of\nur:{}\nsr:{}\nr:{}\nn:{}'
          .format(len(ur_list), len(sr_list), len(r_list), len(n_list)))


def init_packs():
    # print("init_packs")
    global packs_list
    packs_list.clear()
    from random import randint
    global ur_list, sr_list, r_list, n_list
    import copy
    ur = copy.deepcopy(ur_list)
    sr = copy.deepcopy(sr_list)
    r = copy.deepcopy(r_list)
    n = copy.deepcopy(n_list)
    remaining_n = len(n_list)
    remaining_r = len(r_list)
    remaining_sr = len(sr_list)
    remaining_ur = len(ur_list)
    for count in range(200):
        # print(count)
        # print("remaining n: {}\nremaining r: {}\nremaining sr: {}\nremaining ur:{}".format(
        #     remaining_n, remaining_r, remaining_sr, remaining_ur))
        pack = []
        for dummy_i in range(2):
            if (remaining_r + remaining_sr + remaining_ur) * 2 - 4 >= remaining_n:
                card1 = randint(0, remaining_n + remaining_r - 1)
            else:
                card1 = randint(0, remaining_n - 1)
            if card1 < remaining_n:
                pack.append(n[card1])
                del n[card1]
                remaining_n -= 1
            else:
                pack.append(r[card1 - remaining_n])
                del r[card1 - remaining_n]
                remaining_r -= 1
        card2 = randint(0, remaining_r + remaining_sr + remaining_ur - 1)
        if card2 < remaining_r:
            pack.append(r[card2])
            del r[card2]
            remaining_r -= 1
        elif card2 < remaining_r + remaining_sr:
            pack.append(sr[card2 - remaining_r])
            del sr[card2 - remaining_r]
            remaining_sr -= 1
        else:
            pack.append(ur[card2 - remaining_r - remaining_sr])
            del ur[card2 - remaining_r - remaining_sr]
            remaining_ur -= 1
        packs_list.append(pack)
    # print(packs_list)


def open_pack():
    global packs_list
    pack_id = randint(0, len(packs_list) - 1)
    pack = packs_list[pack_id]
    del packs_list[pack_id]
    return pack


def draw_ninja():
    total_open_packs = 0
    card_dict = {
        "UR1": 3,
        "SR1": 2,
        "R3": 1,
        "R4": 3,
        "R5": 1,
        "SR2": 1,
        "SR3": 2,
        "R6": 3,
        "UR2": 3,
        "N6": 1
    }
    ur_count = 0
    init_count = 0
    while not all(v == 0 for v in card_dict.values()):
        pack = open_pack()
        for card in pack:
            if card in card_dict:
                if card_dict[card] != 0:
                    card_dict[card] -= 1
                if card == "UR1" or card == "UR2":
                    ur_count += 1
        if ur_count >= 2 and init_count < 2:
            init_packs()
            ur_count = 0
            init_count += 1
        total_open_packs += 1
    # print("总计开包数:{}".format(total_open_packs))
    return total_open_packs


def open_1000_times():
    res_list = []
    init_cards_list_big()
    for dummy_i in range(1000):
        init_packs()
        res_list.append(draw_ninja())
    return res_list


def main():
    init_cards_list_big()
    # print_all_cards()
    for dummy_i in range(10):
        total = 0
        max_packs = 0
        min_packs = 200
        for dummy_j in range(1000):
            init_packs()
            total_open_packs = draw_ninja()
            total += total_open_packs
            max_packs = max(max_packs, total_open_packs)
            min_packs = min(min_packs, total_open_packs)
        print("抽齐忍者，模拟1000次，总计开包数:{}, 平均开包数:{}, 最少开包数:{}, 最多开包数:{}".format(total, total / 1000, min_packs, max_packs))


if __name__ == '__main__':
    main()
