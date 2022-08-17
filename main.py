#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, redirect, request
import pandas as pd
import numpy as np
import dask.dataframe as dd
import cookpad
import twi


def main():
    food = "卵"
    #辞書を要素に持つリストが帰る
    ingredients = cookpad.crawler(food)

    calorie = pd.read_csv("calorie.csv")
    # print(calorie.dtypes)


    searched = calorie[calorie['food_name'].str.contains(food)]
    print(searched)

if __name__ == "__main__":
    main()
# @route('/hello')
# def hello():
#     return "Hello World!"

# run(host='localhost', port=8080, debug=True)