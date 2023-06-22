#! usr/bin/env python
# -*- coding: utf-8 -*-
"""
Денормализация таблиц и создание сводной таблицы
pandas version 2.0.0
Автор: Отливан Дмитрий
"""
import pandas as pd

df_AboutVacancy = pd.read_csv("/work/data/овакансии1.csv", delimiter=";", encoding="utf-8")

df_Cities = pd.read_csv("/work/data/города.csv", delimiter=";", encoding="utf-8")

df_Dolzh = pd.read_csv("/work/data/должности.csv", delimiter=";", encoding="utf-8")

def denormalization(df_AboutVacancy, df_Cities, df_Dolzh):
    '''
    Денормализует таблицы Города, О вакансии, Должности в одну общую
    Вохвращает общую таблицу SUMMARY
    '''
    SUMMARY = pd.merge(df_Dolzh, df_Cities, on = "КОМП")
    SUMMARY = pd.concat([SUMMARY, df_AboutVacancy], axis=1, join="inner")
    return SUMMARY
def report(df_AboutVacancy, df_Cities, df_Dolzh):
    '''
    Составляет сводную таблицу по средним зарплатам в различных городах по должностям
    Возвращает эту таблицу NUMREP
    '''
    SUMMARY = pd.merge(df_Dolzh, df_Cities, on = "КОМП")
    SUMMARY = pd.concat([SUMMARY, df_AboutVacancy], axis=1, join="inner")
    NUMREP = pd.pivot_table(SUMMARY, index="ДОЛЖН", columns="ГОР", values="ЗАР_ПЛАТ", aggfunc=["mean"])
    return NUMREP