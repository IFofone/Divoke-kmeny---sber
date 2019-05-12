import tkinter as tk
import math
from tkinter import messagebox

window = tk.Tk()

window.title("Divoké kmeny - sběr surovin")


class Unit:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


spear = Unit("spear", 25)
sword = Unit("sword", 15)
axe = Unit("axe", 10)
bow = Unit("bow", 10)
light_horse = Unit("light horse", 80)
bow_horse = Unit("bow horse", 50)
heavy_horse = Unit("heavy horse", 50)

unit_list = [spear, sword, axe, bow, light_horse, bow_horse, heavy_horse]


def calculate():
    lazy, common, clever, great = entry11.get(), entry12.get(), entry13.get(), entry14.get()

    spear_num, sword_num, axe_num, bow_num, light_horse_num, bow_horse_num, heavy_horse_num = entry17.get(), entry18.get(), entry19.get(), entry110.get(), entry111.get(), entry112.get(), entry113.get()
    unit_num_list = [spear_num, sword_num, axe_num, bow_num, light_horse_num, bow_horse_num, heavy_horse_num]

    try:  # zkontroluje hodnoty
        for i in unit_num_list:
            if len(i) > 0:
                i = int(i)
    except ValueError:
        messagebox.showerror("Error", "Zadej číslo!")
        return ["", 0]

    for i in range(len(unit_num_list)):  # nastavi prazdne hodnoty na 0
        if unit_num_list[i] == "":
            unit_num_list[i] = 0

    if lazy == "1" and common == "1" and clever == "1" and great == "1":
        result = combo4(unit_num_list)
        return result, 4

    elif lazy == "1" and common == "1" and clever == "1":
        result = combo3(unit_num_list)
        return result, 3

    elif lazy == "1" and common == "1":
        result = combo2(unit_num_list)
        return result, 2

    elif lazy == "1":
        return [unit_num_list], 1

    else:
        messagebox.showerror("Error", "Vyber sběrače!")
        return ["", 0]


coefficient = {"lazy": 0.1, "common": 0.25, "clever": 0.5, "great": 0.75}


def gain_calculate(unit_number, unit_order, coeff):
    gain = unit_number * unit_list[unit_order].capacity * coeff / (((math.pow(
        (math.pow((coeff * unit_number * unit_list[unit_order].capacity), 2) * 100), 0.45) + 1800) * 0.7237692407)
                                                                   / 3600)
    # print(gain)
    return gain


def combo2(unit_num_list):
    lazy_result = []
    common_result = []

    for i in range(len(unit_list)):  # 7
        max_gain = 0
        best_number = []

        if int(unit_num_list[i]) == 0:
            lazy_result.append(0)
            common_result.append(0)
            continue

        for j in range(0, int(unit_num_list[i]) + 1):
            rate1 = int(unit_num_list[i]) - j
            rate2 = j
            # print(rate1, rate2)
            combo_gain = gain_calculate(rate1, i, coefficient["lazy"]) + gain_calculate(rate2, i, coefficient["common"])

            if combo_gain > max_gain:
                max_gain = combo_gain
                best_number = [rate1, rate2]

        lazy_result.append(best_number[0])
        common_result.append(best_number[1])

    return lazy_result, common_result


def combo3(unit_num_list):
    lazy_result = []
    common_result = []
    clever_result = []

    for i in range(len(unit_list)):  # 7
        max_gain = 0
        best_number = []

        if int(unit_num_list[i]) == 0:
            lazy_result.append(0)
            common_result.append(0)
            clever_result.append(0)
            continue

        for k in range(0, int(unit_num_list[i]) + 1):
            for j in range(0, int(unit_num_list[i]) + 1):
                rate1 = int(unit_num_list[i]) - k - j
                rate2 = k
                rate3 = j

                if rate1 >= 0:
                    # print(rate1, rate2, rate3)
                    combo_gain = gain_calculate(rate1, i, coefficient["lazy"]) \
                                 + gain_calculate(rate2, i, coefficient["common"]) \
                                 + gain_calculate(rate3, i, coefficient["clever"])

                if combo_gain > max_gain:
                    max_gain = combo_gain
                    best_number = [rate1, rate2, rate3]

        lazy_result.append(best_number[0])
        common_result.append(best_number[1])
        clever_result.append(best_number[2])

    return lazy_result, common_result, clever_result


def combo4(unit_num_list):
    lazy_result = []
    common_result = []
    clever_result = []
    great_result = []

    for i in range(len(unit_list)):  # 7
        max_gain = 0
        best_number = []

        if int(unit_num_list[i]) == 0:
            lazy_result.append(0)
            common_result.append(0)
            clever_result.append(0)
            great_result.append(0)
            continue

        for m in range(0, int(unit_num_list[i]) + 1):
            for k in range(0, int(unit_num_list[i]) + 1):
                for j in range(0, int(unit_num_list[i]) + 1):
                    rate1 = int(unit_num_list[i]) - m - k - j
                    rate2 = m
                    rate3 = k
                    rate4 = j

                    if rate1 >= 0:
                        # print(rate1, rate2, rate3, rate4)
                        combo_gain = gain_calculate(rate1, i, coefficient["lazy"]) \
                                     + gain_calculate(rate2, i, coefficient["common"]) \
                                     + gain_calculate(rate3, i, coefficient["clever"]) \
                                     + gain_calculate(rate4, i, coefficient["great"])

                    if combo_gain > max_gain:
                        max_gain = combo_gain
                        best_number = [rate1, rate2, rate3, rate4]

        lazy_result.append(best_number[0])
        common_result.append(best_number[1])
        clever_result.append(best_number[2])
        great_result.append(best_number[3])

    return lazy_result, common_result, clever_result, great_result


def result_display():
    result = calculate()
    # print(result)
    if result[1] >= 1:
        title26 = tk.Label(text="Líní sběrači")
        title26.grid(column=2, row=6)

        entry27 = tk.Entry(width=10)
        entry27.grid(column=2, row=7)
        entry27.insert(tk.END, result[0][0][0])

        entry28 = tk.Entry(width=10)
        entry28.grid(column=2, row=8)
        entry28.insert(tk.END, result[0][0][1])

        entry29 = tk.Entry(width=10)
        entry29.grid(column=2, row=9)
        entry29.insert(tk.END, result[0][0][2])

        entry210 = tk.Entry(width=10)
        entry210.grid(column=2, row=10)
        entry210.insert(tk.END, result[0][0][3])

        entry211 = tk.Entry(width=10)
        entry211.grid(column=2, row=11)
        entry211.insert(tk.END, result[0][0][4])

        entry212 = tk.Entry(width=10)
        entry212.grid(column=2, row=12)
        entry212.insert(tk.END, result[0][0][5])

        entry213 = tk.Entry(width=10)
        entry213.grid(column=2, row=13)
        entry213.insert(tk.END, result[0][0][6])

        if result[1] >= 2:
            title36 = tk.Label(text="Běžní sběrači")
            title36.grid(column=3, row=6)

            entry37 = tk.Entry(width=10)
            entry37.grid(column=3, row=7)
            entry37.insert(tk.END, result[0][1][0])

            entry38 = tk.Entry(width=10)
            entry38.grid(column=3, row=8)
            entry38.insert(tk.END, result[0][1][1])

            entry39 = tk.Entry(width=10)
            entry39.grid(column=3, row=9)
            entry39.insert(tk.END, result[0][1][2])

            entry310 = tk.Entry(width=10)
            entry310.grid(column=3, row=10)
            entry310.insert(tk.END, result[0][1][3])

            entry311 = tk.Entry(width=10)
            entry311.grid(column=3, row=11)
            entry311.insert(tk.END, result[0][1][4])

            entry312 = tk.Entry(width=10)
            entry312.grid(column=3, row=12)
            entry312.insert(tk.END, result[0][1][5])

            entry313 = tk.Entry(width=10)
            entry313.grid(column=3, row=13)
            entry313.insert(tk.END, result[0][1][6])

            if result[1] >= 3:
                title46 = tk.Label(text="Chytří sběrači")
                title46.grid(column=4, row=6)

                entry47 = tk.Entry(width=10)
                entry47.grid(column=4, row=7)
                entry47.insert(tk.END, result[0][2][0])

                entry48 = tk.Entry(width=10)
                entry48.grid(column=4, row=8)
                entry48.insert(tk.END, result[0][2][1])

                entry49 = tk.Entry(width=10)
                entry49.grid(column=4, row=9)
                entry49.insert(tk.END, result[0][2][2])

                entry410 = tk.Entry(width=10)
                entry410.grid(column=4, row=10)
                entry410.insert(tk.END, result[0][2][3])

                entry411 = tk.Entry(width=10)
                entry411.grid(column=4, row=11)
                entry411.insert(tk.END, result[0][2][4])

                entry412 = tk.Entry(width=10)
                entry412.grid(column=4, row=12)
                entry412.insert(tk.END, result[0][2][5])

                entry413 = tk.Entry(width=10)
                entry413.grid(column=4, row=13)
                entry413.insert(tk.END, result[0][2][6])

                if result[1] >= 4:
                    title56 = tk.Label(text="Velcí sběrači")
                    title56.grid(column=5, row=6)

                    entry57 = tk.Entry(width=10)
                    entry57.grid(column=5, row=7)
                    entry57.insert(tk.END, result[0][3][0])

                    entry58 = tk.Entry(width=10)
                    entry58.grid(column=5, row=8)
                    entry58.insert(tk.END, result[0][3][1])

                    entry59 = tk.Entry(width=10)
                    entry59.grid(column=5, row=9)
                    entry59.insert(tk.END, result[0][3][2])

                    entry510 = tk.Entry(width=10)
                    entry510.grid(column=5, row=10)
                    entry510.insert(tk.END, result[0][3][3])

                    entry511 = tk.Entry(width=10)
                    entry511.grid(column=5, row=11)
                    entry511.insert(tk.END, result[0][3][4])

                    entry512 = tk.Entry(width=10)
                    entry512.grid(column=5, row=12)
                    entry512.insert(tk.END, result[0][3][5])

                    entry513 = tk.Entry(width=10)
                    entry513.grid(column=5, row=13)
                    entry513.insert(tk.END, result[0][3][6])


title10 = tk.Label(text="ANO = 1, NE = cokoli jiného")
title10.grid(column=1, row=0)

title01 = tk.Label(text="Líní sběrači")
title01.grid(column=0, row=1)

entry11 = tk.Entry(width=10)
entry11.grid(column=1, row=1)

title02 = tk.Label(text="Běžní sběrači")
title02.grid(column=0, row=2)

entry12 = tk.Entry(width=10)
entry12.grid(column=1, row=2)

title03 = tk.Label(text="Chytří sběrači")
title03.grid(column=0, row=3)

entry13 = tk.Entry(width=10)
entry13.grid(column=1, row=3)

title04 = tk.Label(text="Velcí sběrači")
title04.grid(column=0, row=4)

entry14 = tk.Entry(width=10)
entry14.grid(column=1, row=4)

title05 = tk.Label(text="")  # SPACE
title05.grid(column=0, row=5)

title16 = tk.Label(text="Počet jednotek")
title16.grid(column=1, row=6)

title07 = tk.Label(text="Kopiník")
title07.grid(column=0, row=7)

entry17 = tk.Entry(width=10)
entry17.grid(column=1, row=7)

title08 = tk.Label(text="Šermíř")
title08.grid(column=0, row=8)

entry18 = tk.Entry(width=10)
entry18.grid(column=1, row=8)

title09 = tk.Label(text="Sekerník")
title09.grid(column=0, row=9)

entry19 = tk.Entry(width=10)
entry19.grid(column=1, row=9)

title010 = tk.Label(text="Lučištník")
title010.grid(column=0, row=10)

entry110 = tk.Entry(width=10)
entry110.grid(column=1, row=10)

title011 = tk.Label(text="Lehká kavalerie")
title011.grid(column=0, row=11)

entry111 = tk.Entry(width=10)
entry111.grid(column=1, row=11)

title012 = tk.Label(text="Lučištník na koni")
title012.grid(column=0, row=12)

entry112 = tk.Entry(width=10)
entry112.grid(column=1, row=12)

title013 = tk.Label(text="Těžká kavalerie")
title013.grid(column=0, row=13)

entry113 = tk.Entry(width=10)
entry113.grid(column=1, row=13)

button114 = tk.Button(text="Ok", bg="light gray", height=1, width=8, command=result_display)
button114.grid(column=1, row=14)

title014 = tk.Label(text="©Tomáš_Fojt", font=("Helvetica", 8, "italic"))
title014.grid(column=0, row=14)

window.mainloop()
