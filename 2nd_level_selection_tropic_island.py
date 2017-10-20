"""
Solution for the task 'Tropic Island'
Full task description in:
The Task_2nd_level_selection_tropic_island.mhtml

Created on 09 oct. 2017.
@author: HYuHY
"""

# island is a list of lists
#  island = [
#      [2, 2, 2],
#      [2, 1, 2],
#      [2, 1, 2],
#      [2, 1, 2]
#  ]

import json
import os
import pprint
import random

def get_water_volume(island):
    def make_map_island(island, land, m, n):
        """подготавливает карту данных острова для обработки"""
        for x in range(0, m):
            for y in range(0, n):
                #       S (south)    W (west)    N (north)   E (east)
                swne = [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]  
                land[(x, y)] = {}
                land[(x, y)].update({"swne": swne,  # координаты соседей обрабатываемой ячейки
                                     "abs_height": island[y][x],
                                     "abs_water": island[y][x],
                                     "watered": None,  # значения - перечень областей-озёрц
                                     "limit": None,    # области-стоки в контакте с клеткой
                                     })
        return land
        
    def island_border(m, n):
        """определяет кортежи координат ячеек на границе прямоугольного острова"""
        a = zip([0] * n, range(0, n))
        b = zip([m-1] * n, range(0, n))
        c = zip(range(1, m-1), [0]*(m-2))
        d = zip(range(1, m-1), [n-1]*(m-2))
        border = [tuple(j) for i in [a, b, c, d] for j in i]
        return border
        
    def get_cells_to_check(land, h, cells_to_check):
        """выдаёт клетки острова с высотой, равной текущему шагу в списке высот"""
        for k in land:
            if land[k]["abs_height"] == h:
                cells_to_check.append(k)
        return cells_to_check
        
    def rain(land, heights, border, water_count):
        """клетки острова по мере повышения высоты h начинают сочиться водой"""
        water_area = 1
        limit_area = 1
        for h in heights:
            cells_to_check = []
            cells_to_check = get_cells_to_check(land, h, cells_to_check)
            for cell in cells_to_check:
                # области удержание воды/сток в которые входит или имеет контакт 
                # новая только что залитая клетка
                areas = {"watered": [], "limit": []}
                for cell_2 in land[cell]["swne"]:
                    if cell_2 in land:
                        if land[cell_2]["watered"]:
                            areas["watered"].append(land[cell_2]["watered"])
                        if land[cell_2]["limit"]:
                            areas["limit"].append(land[cell_2]["limit"])
                # проверка условий для различного окружения текущей клетки
                if cell in border:
                    land[cell]["limit"] = limit_area
                    limit_area += 1
                    land[cell]["abs_water"] = land[cell]["abs_height"]
                    areas["limit"].append(land[cell]["limit"])
                if areas["watered"] and areas["limit"]:
                    land[cell]["abs_water"] = land[cell]["abs_height"]
                    for k in land:
                        if land[k]["watered"] in areas["watered"]:
                            land[k]["watered"] = None
                            land[k]["limit"] = limit_area
                            land[k]["abs_water"] = land[cell]["abs_water"]
                    land[cell]["limit"] = limit_area
                    limit_area += 1
                if areas["limit"] and not areas["watered"]:
                    land[cell]["limit"] = areas["limit"][0]
                    land[cell]["abs_water"] = land[cell]["abs_height"]
                if areas["watered"] and not areas["limit"]:
                    land[cell]["watered"] = areas["watered"][0]
                    for k in land:
                        if land[k]["watered"] in areas["watered"]:
                            land[k]["watered"] = water_area
                    water_area += 1
                if not areas["watered"] and not areas["limit"]:
                    land[cell]["watered"] = water_area
                    water_area += 1
            for k in land:   # обновление уровня воды для клеток без стока
                if land[k]["watered"]:
                    land[k]["abs_water"] = h
        for k in land:
            water_count += land[k]["abs_water"] - land[k]["abs_height"]
        return land, water_count
        
    # (0,0) в левом верхнем углу острова
    m = len(island[0])  # max x
    n = len(island)     # max y
    # создаём структуру данных на базе словаря на все клетки острова для последующих манипуляций
    water_count = 0 
    land = {}       
    land = make_map_island(island, land, m, n)
    # подготавливаем стартовые данные о дренажных клетках
    border = island_border(m, n)
    heights = list({land[k]["abs_height"] for k in land})
    heights.sort()
    land, water_count = rain(land, heights, border, water_count)
    return water_count
        

def generate_island(m_min, m_max, n_min, n_max, h_min, h_max):
    island = []
    for _1 in range(n_min, n_max + 1):
        island.append(['{:4d}'.format(random.randint(h_min, h_max)) for _2 in range(m_min, m_max + 1)])
    return island


def write_island_json(lst, file_name):
    with open(file_name, 'w') as f:
        json.dump(lst, f)


def read_island_json(file_name):
    with open(file_name, 'r') as f:
        lst = json.load(f)
    return lst


def write_island_txt(lst, file_name):
    with open(file_name, 'w') as f:
        for row in lst:
            f.write('{0}\n'.format(row))


def read_island_txt(file_name):
    with open(file_name, 'r') as f:
        lst = [[int(x.strip(' \'')) for x in line.strip('[]\n').split(',')] for line in f]
    return lst


def main(file_name, rewrite_mode):
    if file_name[-5:-1:1] == ".data":  # выбор способа хранения и чтения - txt или json
        write_island = write_island_json
        read_island = read_island_json
    else:
        write_island = write_island_txt
        read_island = read_island_txt
    if rewrite_mode:
        island = generate_island(1, 5, 1, 5, 1, 20)
        write_island(island, file_name)
    else:
        island = read_island(file_name)
    pprint.pprint(island, indent=2)
    water_count = get_water_volume(island)
    print("water_count = ", water_count)


if __name__ == "__main__":
    file_name = 'island_to_input_8.txt'
    storage_path = os.path.join(os.getcwd(), file_name)  # файл острова создаётся в текущей рабочей директории
    if os.path.isfile(storage_path):    # перезаписывать ли файл с данными
         rewrite_mode = False           # острова на сгенерированный случайно
    else:
        rewrite_mode = True
    main(file_name, rewrite_mode)
