# -*- coding: utf-8 -*-
"""
Графический анализ данных
pandas version 2.0.0
numpy version 1.24.2
tkinter version 0.3.1
"""
import tkinter as tki
from tkinter import ttk
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

directory = '\\'.join(os.getcwd().split('\\')[:-1])
sys.path.insert(1, directory+'\\library')
os.chdir(directory)

DB = pd.DataFrame()

def rgb_hack(rgb):
    """
    Использование RGB формата для цветов
    https://docs.python.org/3/library/stdtypes.html#old-string-formatting
    """
    return "#%02x%02x%02x" % rgb
class Loads:
    """
    Class for loading tables
    """
    def load_city():
        """
        Загрузка данных

        Returns
        -------
        DB - фрейм с данными

        """
        global DB
        DB = pd.read_csv("/work/data/города.csv", delimiter=";", encoding='utf-8')
        DB = DB.head(25)
        return 0

    def load_dolzh():
        """
        Загрузка данных

        Returns
        -------
        DB - фрейм с данными

        """
        global DB
        DB = pd.read_csv("/work/data/должности.csv", delimiter=";", encoding='utf-8')
        DB = DB.head(25)
        return 0

    def load_vac():
        """
        Загрузка данных

        Returns
        -------
        DB - фрейм с данными

        """
        global DB
        DB = pd.read_csv("/work/data/овакансии1.csv", delimiter=";", encoding='utf-8')
        DB = DB.head(25)
        return 0

def hst():
    """
    Создание гистограммы

    Returns
    -------
    None.

    """
    global DB
    if len(DB) == 0:
        error = tki.Text(width=30, height=5, bg="black", font=('Times', 18),
            fg='white', wrap = tki.WORD)
        error.insert(tki.END, "ОШИБКА: Не загружена таблица или загружена пустая таблица")
        error.pack(expand=True)
        error.after(3000, lambda: error.destroy()) #исчезнет через 3 секунды
        return
    def clck():
        """
        Обработка нажатия кнопки
        """
        t_1 = DB[[cmb.get()]]
        x_1 = t_1[t_1.columns[0]].unique()
        y_1 = [len(DB[DB[t_1.columns[0]] == i]) for i in x_1]

        fig, ax_1 = plt.subplots()

        ax_1.bar(x_1, y_1)
        plt.title("График зависимостей")
        plt.xlabel(t_1.columns[0])
        plt.ylabel("Количество")
        ax_1.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')
        fig.set_figwidth(8)
        fig.set_figheight(4)


        plt.show()
        lbl.destroy()
        cmb.destroy()
        btn.destroy()
        btn2.destroy()

    lbl = tki.Label(text='Выбор показателя >', font=('Arial', 12, 'italic'),
                    bg='blue',fg='yellow')
    lbl.grid(column=0, row=0)
    cmb = ttk.Combobox(root)
    cmb['values'] = tuple(DB.columns)
    cmb.current(0) #Значение по умолчанию
    cmb.focus()
    cmb.grid(column=1, row=0)
    btn = tki.Button(root, text='Построить', font=('Arial', 12, 'italic'),
                    bg='blue',fg='red', command=clck)
    btn.grid(column=2, row=0)

    def destroy1():
        lbl.destroy()
        cmb.destroy()
        btn.destroy()
        btn2.destroy()

    btn2 = tki.Button(root, text='Очистить поле', font=('Arial', 12, 'italic'),
                    bg='black',fg='yellow', command=destroy1)
    btn2.grid(column=3, row=0)
    return 0

def sct():
    """
    Создание диаграммы рассеивания

    Returns
    -------
    None.

    """
    global DB
    if len(DB) == 0:
        error = tki.Text(width=30, height=5, bg="black", font=('Times', 18),
            fg='white', wrap = tki.WORD)
        error.insert(tki.END, "ОШИБКА: Не загружена таблица или загружена пустая таблица")
        error.pack(expand=True)
        error.after(3000, lambda: error.destroy()) #исчезнет через 3 секунды
        return
    def clck():
        """
        Обработка нажатия кнопки
        """
        from matplotlib.pyplot import scatter, show
        w_1 = lb_1.curselection()
        args = [lst[k] for k in w_1]
        global DB
        if DB.dtypes[args[0]] != np.int64 or DB.dtypes[args[1]] != np.int64: #выбраны нечисловые данные для диаграммы
            print("Неверные данные")
            return
        scatter(DB[[args[0]]], DB[[args[1]]])
        show()
        lbl.destroy()
        lb_1.destroy()
        btn.destroy()
        btn2.destroy()
    lbl = tki.Label(text='Выберите два показателя (x,y) >', font=('Arial', 12, 'italic'),
                    bg='blue',fg='yellow')
    lbl.grid(column=0, row=0)
    lst = list(DB.columns)
    nln = len(lst)
    lb_1 = tki.Listbox(root, selectmode=tki.EXTENDED, height=nln, font="Times 14")
    for i in lst:
        lb_1.insert(tki.END, i)
    lb_1.grid(column=1, row=0)
    btn = tki.Button(root, text='Построить', font=('Arial', 12, 'italic'),
                    bg='blue',fg='red', command=clck)
    btn.grid(column=2, row=0)

    def destroy1():
        lbl.destroy()
        lb_1.destroy()
        btn.destroy()
        btn2.destroy()

    btn2 = tki.Button(root, text='Очистить поле', font=('Arial', 12, 'italic'),
                    bg='black',fg='yellow', command=destroy1)
    btn2.grid(column=3, row=0)
    return 0

def cercle():
    """

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    global DB
    if len(DB) == 0:
        error = tki.Text(width=30, height=5, bg="black", font=('Times', 18),
            fg='white', wrap = tki.WORD)
        error.insert(tki.END, "ОШИБКА: Не загружена таблица или загружена пустая таблица")
        error.pack(expand=True)
        error.after(3000, lambda: error.destroy()) #исчезнет через 3 секунды
        return
    if DB.columns[1] != "ЗАР_ПЛАТ":
        return 0
    # данные
    skills = DB["ТРЕБ_НАВ"].unique()
    data = [len(DB[DB["ТРЕБ_НАВ"] == i]) for i in skills]
    print(data)

    # Расстояние м/у дольками
    explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.1, 0.0, 0.2)

    # Цвета долек
    colors = ( "orange", "cyan", "brown",
            "grey", "indigo", "blue", "black", "red", "yellow")

    # Свойства "долек"
    wp_1 = { 'linewidth' : 1, 'edgecolor' : "green" }

    # Создание аргументов autocpt
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    # Создание графика
    fig, ax_1 = plt.subplots(figsize =(6, 5))
    wedges, texts, autotexts = ax_1.pie(data,
                                    autopct = lambda pct: func(pct, data),
                                    explode = explode,
                                    labels = skills,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    wedgeprops = wp_1,
                                    textprops = dict(color ="magenta"))

    # Легенда
    ax_1.legend(wedges, skills,
            title ="Навыки",
            loc ="center left",
            bbox_to_anchor =(1, 0, 0.5, 1))

    plt.setp(autotexts, size = 7, weight ="bold")
    ax_1.set_title("Ключевые навыки")

    plt.show()

def box_plt():
    """
    Создание гистограммы

    Returns
    -------
    None.

    """
    global DB
    if len(DB) == 0:
        error = tki.Text(width=30, height=5, bg="black", font=('Times', 18),
            fg='white', wrap = tki.WORD)
        error.insert(tki.END, "ОШИБКА: Не загружена таблица или загружена пустая таблица")
        error.pack(expand=True)
        error.after(3000, lambda: error.destroy()) #исчезнет через 3 секунды
        return
    def clck():
        """
        Обработка нажатия кнопки
        """
        import matplotlib.pyplot as plt
        #from sklearn import preprocessing
        t_1 = DB[[cmb.get()]]
        x_1 = t_1[t_1.columns[0]].unique()
        # Предобработка данных
        data_1 = []
        data_2 = []
        for i in x_1:
            data_1.append(i)
            data_2.append(len(t_1[t_1[t_1.columns[0]] == i]))
        #строим boxplot по количеству
        if cmb.get() == "ЗАР_ПЛАТ":
            DB[cmb.get()].astype('int32')
            data_2 = DB[[cmb.get()]]
            plt.boxplot(data_2, labels=['Зарплата'])
        else:
            plt.boxplot(data_2, labels=['Количество'])
        plt.title("box plot")

        plt.show()

    lbl = tki.Label(text='Выбор показателя >', font=('Arial', 12, 'italic'),
                    bg='blue',fg='yellow')
    lbl.grid(column=0, row=0)
    cmb = ttk.Combobox(root)
    cmb['values'] = tuple(DB.columns)
    cmb.current(0) #Значение по умолчанию
    cmb.focus()
    cmb.grid(column=1, row=0)
    btn = tki.Button(root, text='Построить', font=('Arial', 12, 'italic'),
                    bg='blue',fg='red', command=clck)
    btn.grid(column=2, row=0)

    def destroy1():
        lbl.destroy()
        cmb.destroy()
        btn.destroy()
        btn2.destroy()

    btn2 = tki.Button(root, text='Очистить поле', font=('Arial', 12, 'italic'),
                    bg='black',fg='yellow', command=destroy1)
    btn2.grid(column=3, row=0)
    return 0


F_DESTROYING = False
def vak_excel():
    """

    Returns
    -------
    None.

    """
    TMP.to_excel("/work/output/new_data.xlsx", encoding='utf-8')
    TOP.destroy()
    BOTTOM.destroy()

def vak_csv():
    """
    Function for csv-file
    """
    TMP.to_csv("/work/output/new_data.csv", encoding='utf-8')
    TOP.destroy()
    BOTTOM.destroy()
def add_data():
    """
    Function for message
    """
    def message():
        values = entry.get().split(";")
        DB.loc[len(DB.index)] = values
        DB.to_csv("/work/output/after_changes.csv", encoding='utf-8')
        title.destroy()
        cols.destroy()
        f_btn.destroy()
        form.destroy()
        TOP.destroy()
        BOTTOM.destroy()
        global F_DESTROYING
        F_DESTROYING = True
    #форма для добавления строки в таблице
    form = tki.LabelFrame(root, bg='black', fg="yellow", font=('Arial', 14, 'bold'))
    form.grid(column=2, row=0)
    title = tki.Label(form, text='Введи данные через ;', font=('Arial', 14, 'bold'),
                    bg='black',fg='yellow')
    title.grid(column=0,row=0)
    atrib = " | ".join(DB.columns)
    cols = tki.Label(form, text=atrib, font=('Arial', 12),
                    bg='black',fg='yellow')
    cols.grid(column=0,row=1)

    entry = tki.Entry(form, bg="black", fg="yellow", font=('Arial', 10))
    entry.grid(column=0, row=2)
    f_btn = tki.Button(form, text='OK',
                    font=('Arial', 12, 'bold'), bg='yellow', fg='black',
                    command=message)
    f_btn.grid(column=0, row=3)
    def destroy1():
            BOTTOM.destroy()
            TOP.destroy()
            btn_d.destroy()
            form.destroy()

    btn_d = tki.Button(form, text='Очистить поле', font=('Arial', 12, 'italic'),
                        bg='black',fg='yellow', command=destroy1)
    btn_d.grid(column=0, row=4)

def del_data():
    """
    Function for message
    """
    global DB
    def message():
        global DB
        values = set(map(int, entry.get().split(",")))
        print(values)
        for i in values:
            if i < 0 or i >= len(DB):
                print("Неверное значение")
                return
        DB = DB.drop(labels = list(values), axis = 0)
        DB.to_csv("/work/output/after_changes.csv", encoding='utf-8')
        title.destroy()
        cols.destroy()
        f_btn.destroy()
        form.destroy()
        TOP.destroy()
        BOTTOM.destroy()
        global F_DESTROYING
        F_DESTROYING = True
    #форма для удаления строк в таблице
    form = tki.LabelFrame(root, bg='black', fg="yellow", font=('Arial', 14, 'bold'))
    form.grid(column=3, row=0)
    title = tki.Label(form, text='Введи номера строк через запятую от 0 до ' + str(len(DB) - 1), font=('Arial', 14, 'bold'),
                    bg='black',fg='yellow')
    title.grid(column=0,row=0)
    atrib = " | ".join(DB.columns)
    cols = tki.Label(form, text=atrib, font=('Arial', 12),
                    bg='black',fg='yellow')
    cols.grid(column=0,row=1)

    entry = tki.Entry(form, bg="black", fg="yellow", font=('Arial', 10))
    entry.grid(column=0, row=2)
    f_btn = tki.Button(form, text='OK',
                    font=('Arial', 12, 'bold'), bg='yellow', fg='black',
                    command=message)
    f_btn.grid(column=0, row=3)
    def destroy1():
            BOTTOM.destroy()
            TOP.destroy()
            btn_d.destroy()
            form.destroy()

    btn_d = tki.Button(form, text='Очистить поле', font=('Arial', 12, 'italic'),
                        bg='black',fg='yellow', command=destroy1)
    btn_d.grid(column=0, row=4)

def change_data():
    """
    Function for message
    """
    global DB
    def message():
        global DB
        string = int(entry1.get())
        if string not in range(len(DB)):
            print("Неверное значение")
            return
        values = entry2.get().split(";")
        if len(values) != DB.shape[1]:
            print("Неверное значение")
            return
        DB.iloc[string] = values
        DB.to_csv("/work/output/after_changes.csv", encoding='utf-8')
        title.destroy()
        cols.destroy()
        f_btn.destroy()
        form.destroy()
        TOP.destroy()
        BOTTOM.destroy()
        global F_DESTROYING
        F_DESTROYING = True
    #форма для изменения строки в таблице
    form = tki.LabelFrame(BOTTOM, bg='black', fg="yellow", font=('Arial', 14, 'bold'))
    form.grid(column=0, row=5)
    title = tki.Label(form, text='Введи номер строки от 0 до ' + str(len(DB) - 1), font=('Arial', 14, 'bold'),
                    bg='black',fg='yellow')
    title.grid(column=0,row=0)
    
    entry1 = tki.Entry(form, bg="black", fg="yellow", font=('Arial', 10))
    entry1.grid(column=0, row=1)

    title2 = tki.Label(form, text='Введи данные через ;', font=('Arial', 14, 'bold'),
                    bg='black',fg='yellow')
    title2.grid(column=0, row=2)

    atrib = " | ".join(DB.columns)
    cols = tki.Label(form, text=atrib, font=('Arial', 12),
                    bg='black',fg='yellow')
    cols.grid(column=0, row=3)

    entry2 = tki.Entry(form, bg="black", fg="yellow", font=('Arial', 10))
    entry2.grid(column=0, row=4)

    f_btn = tki.Button(form, text='OK',
                    font=('Arial', 12, 'bold'), bg='yellow', fg='black',
                    command=message)
    f_btn.grid(column=0, row=5)
    def destroy1():
            BOTTOM.destroy()
            TOP.destroy()
            btn_d.destroy()
            form.destroy()

    btn_d = tki.Button(form, text='Очистить поле', font=('Arial', 12, 'italic'),
                        bg='black',fg='yellow', command=destroy1)
    btn_d.grid(column=0, row=6)

def show():
    """
    Показывает таблицу с вычеркиванием колонок
    """
    if len(DB) == 0:
        error = tki.Text(width=30, height=5, bg="black", font=('Times', 18),
            fg='white', wrap = tki.WORD)
        error.insert(tki.END, "ОШИБКА: Не загружена таблица или загружена пустая таблица")
        error.pack(expand=True)
        error.after(3000, lambda: error.destroy()) #исчезнет через 3 секунды
        return
    def clck():
        """
        Обработка нажатия кнопки
        """
        w_1 = lb_1.curselection()
        args = [lst[k] for k in w_1]
        lbl.destroy()
        lb_1.destroy()
        btn.destroy()
        btnd.destroy()
        global TMP
        TMP = DB[args]
        height = TMP.shape[0]
        width = TMP.shape[1]
        # Формируем массив указателей на виджеты Entry
        pnt = np.empty(shape=(height, width), dtype="O")
        # Формируем массив указателей на текстовые буферы для передачи данных Tcl/Tk
        vrs = np.empty(shape=(height, width), dtype="O")
        # Построение изображения
        # До любых обращений к tkinter
        # Создаем фрейм (контейнер) в котором будет размещена таблица
        # https://www.tutorialspoint.com/python/tk_labelframe.htm
        global TOP
        TOP = tki.LabelFrame(root, text="Справочник",
                            bg=rgb_hack((0, 255, 255)))
        TOP.grid(column=0, row=0)
        global BOTTOM
        BOTTOM = tki.LabelFrame(root, text="Управление",
                            bg=rgb_hack((0, 255, 125)))
        BOTTOM.grid(column=1, row=0, sticky="w")
        # Инициализация указателей на буферы
        for i in range(height):
            for j in range(width):
                vrs[i, j] = tki.StringVar()
        # Построение таблицы
        for i in range(height):
            for j in range(width):
                pnt[i, j] = tki.Entry(TOP, textvariable = vrs[i, j])
                pnt[i, j].grid(row=i, column=j)
        # Заполнение таблицы значениями
        for i in range(height):
            for j in range(width):
                cnt = TMP.iloc[i, j]
                vrs[i, j].set(str(cnt))
        # ----------------------------------------------------------------
        btn_1 = tki.Button(BOTTOM, text='Сохранить в Excel',
                        font=('Arial', 12, 'italic'), bg='purple', fg='white',
                        command=vak_excel)
        btn_1.grid(column=0, row=0, sticky="w")
        btn_2 = tki.Button(BOTTOM, text='Сохранить в CSV',
                        font=('Arial', 12, 'italic'), bg='blue', fg='black',
                        command=vak_csv)
        btn_2.grid(column=0, row=1, sticky="w")
        btn_3 = tki.Button(BOTTOM, text='Добавить запись',
                        font=('Arial', 12, 'italic'), bg='yellow', fg='blue',
                        command=add_data)
        btn_3.grid(column=0, row=2, sticky="w")
        btn_4 = tki.Button(BOTTOM, text='Удалить запись',
                        font=('Arial', 12, 'italic'), bg='yellow', fg='blue',
                        command=del_data)
        btn_4.grid(column=0, row=3, sticky="w")
        btn_5 = tki.Button(BOTTOM, text='Изменить запись',
                        font=('Arial', 12, 'italic'), bg='yellow', fg='blue',
                        command=change_data)
        btn_5.grid(column=0, row=4, sticky="w")
        def destroy1():
            btn_1.destroy()
            btn_2.destroy()
            btn_3.destroy()
            BOTTOM.destroy()
            TOP.destroy()
            lbl.destroy()
            lb_1.destroy()
            btn.destroy()
            btn_d.destroy()

        btn_d = tki.Button(BOTTOM, text='Очистить поле', font=('Arial', 12, 'italic'),
                        bg='black',fg='yellow', command=destroy1)
        btn_d.grid(column=0, row=5)

    lbl = tki.Label(text='Выберите столбцы >', font=('Arial', 14, 'italic'),
                    bg='black',fg='yellow')
    lbl.grid(column=0, row=0)
    lst = list(DB.columns)
    nln = len(lst)
    lb_1 = tki.Listbox(root, selectmode=tki.EXTENDED, height=nln, font="Times 14")
    for i in lst:
        lb_1.insert(tki.END, i)
    lb_1.grid(column=1, row=0)
    btn = tki.Button(root, text='Показать', font=('Arial', 12, 'italic'),
                    bg='blue',fg='red', command=clck)
    btn.grid(column=2, row=0)
    def destroy1():
        lbl.destroy()
        lb_1.destroy()
        btn.destroy()
        btnd.destroy()

    btnd = tki.Button(root, text='Очистить поле', font=('Arial', 12, 'italic'),
                    bg='black',fg='yellow', command=destroy1)
    btnd.grid(column=4, row=0)



class Colors():
    """
    Class with functions for colors
    """
    def red():
        """
        Makes window red
        """
        root["bg"] = "red"
    def white():
        """
        Makes window white
        """
        root["bg"] = "white"
    def black():
        """
        Makes window black
        """
        root["bg"] = "black"

def hlp():
    """
    Помощь

    Returns
    -------
    None.

    """
    def clck():
        """
        Обработка нажатия кнопки
        """
        text.destroy()
        scrolly.destroy()
        scrollx.destroy()
        btn.destroy()
    text = tki.Text(width=55, height=15, bg="black", font=('Times', 13),
            fg='white', wrap = tki.WORD)
    text.grid(row = 0, column = 0) 
    scrolly = tki.Scrollbar(command=text.yview)
    scrolly.grid(row = 0, column = 1)     
    scrollx = tki.Scrollbar(orient=tki.HORIZONTAL, command=text.xview)
    scrollx.grid(row = 1, column = 0)     
    text.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    with open("/work/data/text_h.txt", "r", encoding='utf-8') as fln:
        txt = fln.read()
    text.insert(tki.END, txt)
    btn = tki.Button(root, text='Ок', font=('Times', 14),
                    bg='black',fg='white', command=clck)
    btn.grid(row = 2, column = 0) 

def stat():
    TMP = pd.read_csv("/work/data/должности.csv", delimiter=";", encoding="utf-8")
    dct = {'ДОЛЖН': [], "Количество": []}
    for dolzh in TMP['ДОЛЖН'].unique():
        if dolzh not in dct:
            dct['ДОЛЖН'].append(dolzh)
            dct['Количество'].append(len(TMP[TMP['ДОЛЖН'] == dolzh]))
    TMP = pd.DataFrame(dct)
    height = TMP.shape[0]
    width = TMP.shape[1]
    # Формируем массив указателей на виджеты Entry
    pnt = np.empty(shape=(height, width), dtype="O")
    # Формируем массив указателей на текстовые буферы для передачи данных Tcl/Tk
    vrs = np.empty(shape=(height, width), dtype="O")
    # Построение изображения
    # До любых обращений к tkinter
    # Создаем фрейм (контейнер) в котором будет размещена таблица
    # https://www.tutorialspoint.com/python/tk_labelframe.htm
    global TOP
    TOP = tki.LabelFrame(root, text="Статистика профессии/количество",
                        bg=rgb_hack((0, 255, 255)))
    TOP.grid(column=0, row=0)
    # Инициализация указателей на буферы
    for i in range(height):
        for j in range(width):
            vrs[i, j] = tki.StringVar()
    # Построение таблицы
    for i in range(height):
        for j in range(width):
            pnt[i, j] = tki.Entry(TOP, textvariable = vrs[i, j])
            pnt[i, j].grid(row=i, column=j)
    # Заполнение таблицы значениями
    for i in range(height):
        for j in range(width):
            cnt = TMP.iloc[i, j]
            vrs[i, j].set(str(cnt))
    # ----------------------------------------------------------------
    def destroy1():
        btn_d.destroy()
        TOP.destroy()
        btngr.destroy()
        
    def graph():
        """
        Обработка нажатия кнопки
        """
        x_1 = TMP[TMP.columns[0]].to_list()
        y_1 = TMP[TMP.columns[1]].to_list()

        fig, ax_1 = plt.subplots()

        ax_1.bar(x_1, y_1)
        plt.title("График количества профессий")
        plt.ylabel("Количество")
        ax_1.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')
        fig.set_figwidth(8)
        fig.set_figheight(4)


        plt.show()

    btngr = tki.Button(root, text='График', font=('Arial', 12, 'italic'),
                    bg='black',fg='yellow', command=graph)
    btngr.grid(column=0, row=1)

    btn_d = tki.Button(root, text='Очистить поле', font=('Arial', 12, 'italic'),
                        bg='black',fg='yellow', command=destroy1)
    btn_d.grid(column=0, row=2)

root = tki.Tk()
root.geometry('950x550+30+30')
root.title("Анализ рынка вакансий IT")

# Создание меню
mainmenu = tki.Menu(root, tearoff=0)

dan = tki.Menu(mainmenu, tearoff=0)
dan.add_command(label="Гистограмма", command = hst)
dan.add_command(label="Диаграмма рассеивания", command = sct)
dan.add_command(label="Круговая диаграмма", command = cercle)
dan.add_command(label="Ящик с усамми", command = box_plt)
dan.add_command(label="Статистика", command = stat)
dan.add_command(label="Показать таблицу", command = show)

tables = tki.Menu(mainmenu, tearoff=0)
tables.add_command(label="Города", command = Loads.load_city)
tables.add_command(label="Должности", command = Loads.load_dolzh)
tables.add_command(label="О вакансии", command = Loads.load_vac)

working = tki.Menu(mainmenu, tearoff=0)
working.add_cascade(label="Загрузка таблицы", menu=tables)
working.add_command(label="Завершить", command = root.destroy)

colors = tki.Menu(mainmenu, tearoff=0)
colors.add_command(label="Красный", command = Colors.red)
colors.add_command(label="Белый", command = Colors.white)
colors.add_command(label="Черный", command = Colors.black)

# Размещение пунктов в меню
mainmenu.add_cascade(label="Файл", menu=working)
mainmenu.add_cascade(label="Анализ данных", menu = dan)
mainmenu.add_cascade(label="Фон", menu=colors)
mainmenu.add_command(label="Помощь", command = hlp)
mainmenu.add_command(label="Выход", command = root.destroy)

root.config(menu=mainmenu)

root.mainloop()
