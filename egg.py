"""
@Author: Bluemangoo
@Date: 2022.05
@Copyright: 2022 Bluemangoo. All rights reserved.
@Description: A game
@version: 1.1.3 alpha
"""
import math
import os
import random

VERSION = "1.1.3 alpha"
VERSION_DATE = "2022.6.4"
DATA_COMPATIBLE_LATEST = [1, 1, 3]

DEBUG = False

PATH = './egg/'

FILE_DATA_FILENAME = 'egg.data'
FILE_VERSION_FILENAME = 'egg.version'
FILE_EDB_FILENAME = 'egg.edb'
FILE_LEADERBOARD_FILENAME = 'egg.leaderboard'

FILE_DATA = PATH + FILE_DATA_FILENAME
FILE_VERSION = PATH + FILE_VERSION_FILENAME
FILE_EDB = PATH + FILE_EDB_FILENAME
FILE_LEADERBOARD = PATH + FILE_LEADERBOARD_FILENAME

EN = {"lang.name": "EN", "lang.set.tip": "Choose a language：\n[1] English\n[2] 简体中文\n[3] 繁體中文\n",
      "error.file.no_permission": "\033[31mERROR: no file permission, please check file path, or set 'PATH' as "
                                  "'D:/'\033[0m\n",
      "error.bad_input": "Invalid input\n", "error.game.floor.too_low": "Then better go to hell\n",
      "error.game.floor.one_to_one": "You dropped the egg from the 1st floor, the egg landed on the 1st floor, "
                                     "the gravitational potential energy decreased by 0 J\n",
      "error.game.floor.too_high": "It's better to go to heaven\n",
      "error.game.score_too_high": "\033[31mERROR: score too high! Please hand on an issue at Github\033[0m\n",
      "egg.hello": "Egg Throwing Game\nAuthor: Bluemangoo\nVersion: " + VERSION + " (" + VERSION_DATE + ")\n",
      "egg.help": "h | help -- help\ns | start -- start game\nr | query -- query data (in-game)\na | analyse -- query "
                  "statistics\nc | cls -- clear screen\nq | quit -- quit\nl | language -- language\n"
                  "b | about -- about\n",
      "egg.help.short": "\ns | start -- start game\nh | help -- help\n", "analyse.game": "Win %d/%d games in total",
      "analyse.egg": "Total %d/%d eggs lost", "analyse.step": "Average performed %.2f steps",
      "egg.leaderboard": "High Score Leaderboard: ", "egg.leaderboard.item": "%d %.2f %s",
      "egg.about": "Egg Throwing Game\nAuthor: Bluemangoo\nGithub: https://github.com/Bluemangoo/egg\n"
                   "Version: " + VERSION + "\nRelease Date: " + VERSION_DATE + "\n",
      "analyse.score": "Average score %.2f\n",
      "game.intro": "There is a building of %d floor, and you have %d identical eggs in your hands.\nThese eggs are "
                    "so tough that they can withstand relatively large shocks.\n "
                    "It won't break if you fall from a low level, but it will when you have a certain number of "
                    "levels.\nPlease find out the number of levels just enough to break the egg through "
                    "experiments\n\n "
                    "Suppose this egg won't break if it falls on level 49, but it will on level 50.\n"
                    "At this point you need to try on both the 49th and 50th floors to prove that the critical floor "
                    "for it to break is 50\nLet's start\n\n",
      "game.get_floor": "Please enter the guessed floor number (2~%d): ",
      "game.result.broken": "The egg is broken, you still have %d eggs, please cherish it\n",
      "game.result.unbroken": "Egg is not broken\n",
      "game.query": "Total floor height: %d\nRemaining eggs: %d / %d\nCurrent floor interval: %d ~ %d\n",
      "game.win": "Congratulations on winning the game\n", "game.fail": "The egg is gone, the game is over\n",
      "game.score": "Game Score: %.2f(%s)\nAverage Score: %.2f\nTried %d times\nBreak %d/%d eggs\n\n",
      "game.high": "High score! Input your name: "}
ZH_CN = {"lang.name": "ZH_CN", "lang.set.tip": "请选择语言：\n[1] English\n[2] 简体中文\n[3] 繁體中文\n",
         "error.file.no_permission": "\033[31m无文件权限, 请检查文件位置, 或将 'PATH' 的值修改为'D:/'\033[0m\n",
         "error.bad_input": "无效的输入\n", "error.game.floor.too_low": "那最好是下地狱去\n",
         "error.game.floor.one_to_one": "你从 1 楼丢下了鸡蛋, 鸡蛋落在了 1 楼, 重力势能减少了 0 J\n",
         "error.game.floor.too_high": "那最好是上天堂去\n",
         "error.game.score_too_high": "\033[31mERROR: 过高的分数, 请联系开发者\033[0m\n",
         "egg.hello": "丢鸡蛋游戏\n作者: Bluemangoo\n版本: " + VERSION + " (" + VERSION_DATE + ")\n",
         "egg.help": "h | help -- 帮助\ns | start -- 开始游戏\nr | query -- 查询数据(游戏内)\na | analyse -- 查询统计数据\n"
                     "c | cls -- 清屏\nq | quit -- 退出\nl | language -- 语言\nb | about -- 关于\n",
         "egg.help.short": "\ns | start -- 开始游戏\nh | help -- 帮助\n", "analyse.game": "共赢得 %d/%d 盘游戏",
         "analyse.egg": "共损失 %d/%d 个鸡蛋", "analyse.step": "平均执行 %.2f 步", "analyse.score": "平均得分 %.2f\n",
         "egg.leaderboard": "高分排行榜: ", "egg.leaderboard.item": "%d %.2f %s",
         "egg.about": "丢鸡蛋游戏\n作者: Bluemangoo\nGithub: https://github.com/Bluemangoo/egg\n版本: "
                      + VERSION + "\n发布日期: " + VERSION_DATE + "\n",
         "game.intro": "有一座 %d 层高的大楼, 你手上有 %d 个一模一样的鸡蛋.\n这些鸡蛋非常坚韧, 以致于可以承受比较大的冲击.\n"
                       "从低层落下去不会摔破, 但在一定层数以上会.\n请你通过实验找出这个刚好能使鸡蛋摔破的层数\n\n"
                       "假设这个鸡蛋在49层摔下去不会破, 但是在50层就会.\n"
                       "这时你需要在49层和50层都尝试过以证明它摔破的临界楼层为50\n接下来就开始吧\n\n",
         "game.get_floor": "请输入猜测的层数(2~%d): ", "game.result.broken": "鸡蛋碎了, 你还有 %d 个蛋, 请你珍惜\n",
         "game.result.unbroken": "鸡蛋没碎\n", "game.query": "楼层总高: %d\n剩余鸡蛋: %d / %d\n当前楼层区间: %d ~ %d\n",
         "game.win": "恭喜你赢得了游戏\n", "game.fail": "鸡蛋没了, 游戏结束\n",
         "game.score": "游戏得分: %.2f(%s)\n平均得分: %.2f\n尝试了 %d 次\n摔破了 %d/%d 个鸡蛋\n\n",
         "game.high": "高分! 请输入名字: "}
ZH_HK = {"lang.name": "ZH_HK", "lang.set.tip": "請選擇語言：\n[1] English\n[2] 简体中文\n[3] 繁體中文\n",
         "error.file.no_permission": "\033[31m無文件權限, 請檢查文件位置, 或將 'PATH' 的值修改為'D:/'\033[0m\n",
         "error.bad_input": "無效的輸入\n", "error.game.floor.too_low": "那最好是下地獄去\n",
         "error.game.floor.one_to_one": "你從 1 樓丟下了雞蛋, 雞蛋落在了 1 樓, 重力勢能減少了 0 J\n",
         "error.game.floor.too_high": "那最好是上天堂去\n",
         "error.game.score_too_high": "\033[31mERROR: 過高的分數, 請聯繫開發者\033[0m\n",
         "egg.hello": "丟雞蛋遊戲\n作者: Bluemangoo\n版本: " + VERSION + " (" + VERSION_DATE + ")\n",
         "egg.help": "h | help -- 幫助\ns | start -- 開始遊戲\nr | query -- 查詢數據(遊戲內)\na | analyse -- 查詢統計數據\n"
                     "c | cls -- 清屏\nq | quit -- 退出\nl|language 語言\nb | about -- 關於\n",
         "egg.help.short": "\ns | start -- 開始遊戲\nh | help -- 幫助\n", "analyse.game": "共贏得 %d/%d 盤遊戲",
         "analyse.egg": "共損失 %d/%d 個雞蛋", "analyse.step": "平均執行 %.2f 步", "analyse.score": "平均得分 %.2f\n",
         "egg.leaderboard": "高分排行榜: ", "egg.leaderboard.item": "%d %.2f %s",
         "egg.about": "丟雞蛋遊戲\n作者: Bluemangoo\nGithub: https://github.com/Bluemangoo/egg\n版本: "
                      + VERSION + "\n發布日期: " + VERSION_DATE + "\n",
         "game.intro": "有一座 %d 層高的大樓, 你手上有 %d 個一模一樣的雞蛋.\n這些雞蛋非常堅韌, 以致於可以承受比較大的衝擊.\n"
                       "從低層落下去不會摔破, 但在一定層數以上會.\n請你通過實驗找出這個剛好能使雞蛋摔破的層數\n\n"
                       "假設這個雞蛋在49層摔下去不會破, 但是在50層就會.\n"
                       "這時你需要在49層和50層都嘗試過以證明它摔破的臨界樓層為50\n接下來就開始吧\n\n",
         "game.get_floor": "請輸入猜測的層數(2~%d): ", "game.result.broken": "雞蛋碎了, 你還有 %d 個蛋, 請你珍惜\n",
         "game.result.unbroken": "雞蛋沒碎\n", "game.query": "樓層總高: %d\n剩餘雞蛋: %d / %d\n當前樓層區間: %d ~ %d\n",
         "game.win": "恭喜你贏得了遊戲\n", "game.fail": "雞蛋沒了, 遊戲結束\n",
         "game.score": "遊戲得分: %.2f(%s)\n平均得分: %.2f\n嘗試了 %d 次\n摔破了 %d/%d 個雞蛋\n\n",
         "game.high": "高分! 請輸入名字: "}

lang = EN

SCORE_K: float = 1.87822326638464

game_count_global: int
game_win_global: int
egg_all_global: int
egg_remain_global: int
step_used_global: int
score_global: float


def print_window(*args, sep=' ', end='\n', file=None):
    print(*args, sep=sep, end=end, file=file)


def input_window(*args, **kwargs):
    return input(*args, **kwargs)


def print_debug(line, *args, start='', sep=' ', end='\n', file=None):
    if DEBUG:
        print(start, "DEBUG#{}: ".format(line), *args, sep=sep, end=end, file=file)


def cls():
    os.system('cls')


def get_lang(force):
    global lang
    flag = True
    while flag:
        input_get_lang = input_window(lang["lang.set.tip"])
        if input_get_lang == '1':
            lang = EN
            flag = False
        elif input_get_lang == '2':
            lang = ZH_CN
            flag = False
        elif input_get_lang == '3':
            lang = ZH_HK
            flag = False
        else:
            if force:
                cls()
                print_window(lang["error.bad_input"])
            else:
                flag = False
                cls()


def initialize_data():
    global lang
    if not os.path.exists(FILE_DATA):
        get_lang(True)
        with open(FILE_DATA, mode='w', encoding='utf-8') as file_data_stream:
            file_data_stream.write(lang["lang.name"] + '\n')
            file_data_stream.write('0\n0\n0\n0\n0\n0.00\n')
    with open(FILE_DATA, mode='r', encoding='utf-8') as file_data_stream:
        try:
            lang = globals()[file_data_stream.readline()[:-1]]
        except KeyError:
            get_lang(True)
            with open(FILE_DATA, mode='w', encoding='utf-8') as file_data_stream2:
                file_data_stream2.write(lang["lang.name"] + '\n')
                file_data_stream2.write('0\n0\n0\n0\n0\n0.00\n')


def initialize_version():
    if not os.path.exists(FILE_VERSION):
        with open(FILE_VERSION, mode='w', encoding='utf-8') as file_version_stream:
            file_version_stream.write(VERSION + '\n')
    with open(FILE_VERSION, mode='r', encoding='utf-8') as file_version_stream:
        try:
            ver_in_file_str = file_version_stream.readline()[:-1]
            ver_in_file = []
            tmp = ''
            for bite in ver_in_file_str:
                if bite == '.' or bite == ' ':
                    ver_in_file.append(int(tmp))
                    tmp = ''
                else:
                    tmp += bite
            compatible = True
            for i in range(0, 3):
                if ver_in_file[i] < DATA_COMPATIBLE_LATEST[i]:
                    compatible = False
                    break
                if ver_in_file[i] > DATA_COMPATIBLE_LATEST[i]:
                    break
                print()
            if not compatible:
                backup_path = PATH + 'backup/' + ver_in_file_str + '/'
                try:
                    os.remove(backup_path + FILE_DATA_FILENAME)
                except FileNotFoundError:
                    pass
                try:
                    os.remove(backup_path + FILE_EDB_FILENAME)
                except FileNotFoundError:
                    pass
                try:
                    os.remove(backup_path + FILE_LEADERBOARD_FILENAME)
                except FileNotFoundError:
                    pass
                try:
                    os.replace(FILE_DATA, backup_path + FILE_DATA_FILENAME)
                except FileNotFoundError:
                    pass
                try:
                    os.replace(FILE_EDB, backup_path + FILE_EDB_FILENAME)
                except FileNotFoundError:
                    pass
                try:
                    os.replace(FILE_LEADERBOARD, backup_path + FILE_LEADERBOARD_FILENAME)
                except FileNotFoundError:
                    pass
                with open(FILE_DATA, mode='w', encoding='utf-8') as file_data_stream:
                    file_data_stream.write(lang["lang.name"] + '\n')
                    file_data_stream.write('0\n0\n0\n0\n0\n0.00\n')
            with open(FILE_VERSION, mode='w', encoding='utf-8') as file_version_stream2:
                file_version_stream2.write(VERSION + '\n')
        except KeyError:
            with open(FILE_DATA, mode='w', encoding='utf-8') as file_version_stream2:
                file_version_stream2.write(VERSION + '\n')


def initialize_edb():
    if not os.path.exists(FILE_EDB):
        with open(FILE_EDB, mode='w', encoding='utf-8') as file_edb_stream:
            file_edb_stream.write('')


def initialize_leaderboard():
    if not os.path.exists(FILE_LEADERBOARD):
        with open(FILE_LEADERBOARD, mode='w', encoding='utf-8') as file_leaderboard_stream:
            file_leaderboard_stream.write('')


def initialize():
    try:
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        initialize_data()
        initialize_version()
        initialize_edb()
        initialize_leaderboard()
    except PermissionError:
        print_window(lang["error.file.no_permission"])


def get_data():
    with open(FILE_DATA, mode='r', encoding='utf-8') as file_data_stream:
        file_data_stream.readline()
        global game_count_global
        global game_win_global
        global egg_all_global
        global egg_remain_global
        global step_used_global
        global score_global
        game_count_global = int(file_data_stream.readline()[:-1])
        game_win_global = int(file_data_stream.readline()[:-1])
        egg_all_global = int(file_data_stream.readline()[:-1])
        egg_remain_global = int(file_data_stream.readline()[:-1])
        step_used_global = int(file_data_stream.readline()[:-1])
        score_global = float(file_data_stream.readline()[:-1])


def set_data(game_count, game_win, egg_all, egg_remain, step_used, score):
    with open(FILE_DATA, mode='w', encoding='utf-8') as file_data_stream:
        try:
            file_data_stream.write(lang["lang.name"] + '\n')
            file_data_stream.write(
                '%d\n%d\n%d\n%d\n%d\n%.2f\n' % (game_count, game_win, egg_all, egg_remain, step_used, score))
        except PermissionError:
            print_window(lang["error.file.no_permission"])


def set_db(score):
    with open(FILE_EDB, mode='a', encoding='utf-8') as file_db_stream:
        try:
            file_db_stream.write('%.2f\n' % score)
        except PermissionError:
            print_window(lang["error.file.no_permission"])


def get_high_five():
    high_five = []
    with open(FILE_LEADERBOARD, mode='r', encoding='utf-8') as file_leaderboard_stream:
        try:
            for i in range(5):
                high_five.append(
                    [float(file_leaderboard_stream.readline()[:-1]), file_leaderboard_stream.readline()[:-1]])
        except KeyError:
            return high_five_sort(high_five)
        except ValueError:
            return high_five_sort(high_five)
    return high_five_sort(high_five)


def set_high_five(high_five):
    high_five = high_five_sort(high_five)
    with open(FILE_LEADERBOARD, mode='w', encoding='utf-8') as file_high_score_stream:
        try:
            for line in high_five:
                file_high_score_stream.write("%.2f\n%s\n" % (line[0], line[1]))
        except PermissionError:
            print_window(lang["error.file.no_permission"])


def high_five_sort(high_five):
    high_five_sorted = []
    for i in range(len(high_five)):
        max_count = -1
        max_score = -1
        for j in range(len(high_five)):
            if high_five[j][0] > max_score:
                max_score = high_five[j][0]
                max_count = j
        high_five_sorted.append(high_five[max_count])
        high_five[max_count] = [-1, '']
    return high_five_sorted


def egg_hello():
    print_window(lang["egg.hello"])
    print_window(lang["egg.help.short"])


def egg_help():
    print_window(lang["egg.help"])


def egg_analyse():
    get_data()
    print_window(lang["analyse.game"] % (game_win_global, game_count_global))
    print_window(lang["analyse.egg"] % (egg_remain_global, egg_all_global))
    if game_count_global > 0:
        print_window(lang["analyse.step"] % (step_used_global / game_count_global))
    else:
        print_window(lang["analyse.step"] % 0)
    if game_win_global > 0:
        print_window(lang["analyse.score"] % (score_global / game_win_global))
    else:
        print_window(lang["analyse.score"] % 0)
    print(lang["egg.leaderboard"])
    high_five = get_high_five()
    for i in range(len(high_five)):
        print(lang["egg.leaderboard.item"] % (i+1, high_five[i][0], high_five[i][1]))
    print()


def egg_about():
    print_window(lang["egg.about"])


def game():
    cls()
    floor_all: int = random.randint(10, 500)
    floor_break: int = int(random.randint(2, floor_all))
    floor_now: int = 1
    floor_high: int = floor_all
    floor_low: int = 1
    egg_all: int = random.randint(2, 10)
    egg_now: int = egg_all
    step_now: int = 0
    distance: int = 0
    win: bool = False
    high: bool = False

    print_window(lang["game.intro"] % (floor_all, egg_all))
    print_debug(floor_break, end='\n\n')
    while True:
        guess = input_window(lang["game.get_floor"] % floor_all)
        if guess == "h" or guess == "help":
            egg_help()
        elif guess == "c" or guess == "cls":
            cls()
        elif guess == "r" or guess == "query":
            print_window(lang["game.query"] % (floor_all, egg_now, egg_all, floor_low, floor_high))
        else:
            guess = ''.join(filter(str.isdigit, guess))
            if guess == '':
                print_window(lang["error.bad_input"])
            else:
                guess = int(guess)
                if guess == 1:
                    print_window(lang["error.game.floor.one_to_one"])
                    distance += abs(floor_now - 1)
                    floor_now = 1
                elif guess < 1:
                    print_window(lang["error.game.floor.too_low"])
                    distance += abs(floor_now - 1)
                    floor_now = 1
                elif guess > floor_all:
                    print_window(lang["error.game.floor.too_high"])
                    distance += abs(floor_now - floor_all)
                    floor_now = floor_all
                else:
                    distance += abs(floor_now - guess)
                    floor_now = guess
                    if guess >= floor_break:
                        egg_now -= 1
                        print_window(lang["game.result.broken"] % egg_now)
                        floor_high = min(guess, floor_high)
                    else:
                        print_window(lang["game.result.unbroken"])
                        floor_low = max(guess, floor_low)
                step_now += 1

        if floor_high - floor_low == 1:
            win = True
            break
        if egg_now == 0:
            break

    score: float
    if win:
        score_egg: int = (egg_now + 1) * 3
        score_floor_all: float = (100 - 3 * egg_all) * 0.8
        score_floor_tmp: float = (1 + (SCORE_K / (egg_all * (pow(floor_all, 1 / egg_all) - 1) - 1)) * (step_now - 2))
        score_floor: float = (math.e - pow(1 + 1 / score_floor_tmp, score_floor_tmp)) * (score_floor_all / (math.e - 2))
        score_distance_all: float = (100 - 3 * egg_all) * 0.2
        score_distance: float = score_distance_all
        if distance > floor_all:
            score_distance -= (distance - floor_all) // (floor_all * 0.05)
        if score_distance < 0:
            score_distance = 0
        score = score_egg + score_floor + score_distance
        score = round(score, 2)
        print_window(lang["game.win"])

        high_five = get_high_five()
        print_debug(436, high_five, end='\n\n')
        high_five = high_five_sort(high_five)
        if len(high_five) < 5:
            high = True
        for line in high_five:
            if score > line[0]:
                high = True
    else:
        score = 0
        print_window(lang["game.fail"])
    get_data()
    set_data(game_count_global + 1, game_win_global + win, egg_all_global + egg_all, egg_remain_global + egg_now,
             step_used_global + step_now, score_global + score)
    set_db(score)
    grade: str
    if score > 100:
        grade = 'E'
        print_window(lang["error.game.score_too_high"])
        input_window()
        exit(-1)
    elif score == 100:
        grade = 'V'
    elif score >= 95:
        grade = 'S'
    elif score >= 90:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    else:
        grade = 'F'
    get_data()
    if game_win_global == 0:
        print_window(lang["game.score"] % (score, grade, 0, step_now, egg_all - egg_now, egg_all))
    else:
        print_window(lang["game.score"] %
                     (score, grade, score_global / game_win_global, step_now, egg_all - egg_now, egg_all))
    if high:
        name = input_window(lang["game.high"])
        high_five = get_high_five()
        if len(high_five) < 5:
            high_five.append([score, name])
        else:
            low_score = 101
            low = -1
            for i in range(4):
                if high_five[i][0] < low_score:
                    low_score = high_five[i][0]
                    low = i
            high_five[low] = [score, name]
        set_high_five(high_five)


def main():
    initialize()
    egg_hello()
    while True:
        inp = input_window(">")
        if inp == "h" or inp == "help":
            egg_help()
        elif inp == "a" or inp == "analyse":
            egg_analyse()
        elif inp == "s" or inp == "start":
            game()
            print_window(lang["egg.help.short"])
        elif inp == "c" or inp == "cls":
            cls()
        elif inp == "l" or inp == "language":
            get_lang(False)
            get_data()
            set_data(game_count_global, game_win_global, egg_all_global, egg_remain_global, step_used_global,
                     score_global)
        elif inp == "b" or inp == "about":
            egg_about()
        elif inp == "q" or inp == "quit":
            break
        else:
            print_window(lang["error.bad_input"])


if __name__ == '__main__':
    main()
