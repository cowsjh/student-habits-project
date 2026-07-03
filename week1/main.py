from pathlib import Path
import os

import pandas as pd
import numpy as np
import matplotlib
import sklearn


def load_data(file):

    
    if os.path.exists(file) :
        df = pd.read_csv(file, encoding="utf-8-sig")
        print("CSV 파일이 정상적으로 로드 되었습니다.")
        print(df.shape)
        return df
    else :
        raise Exception("csv 파일이 존재 하지 않습니다.")
    

def explore_structure(df):

    print(f"Shape \t:")
    print(f"\t{df.shape}")
    
    print("\nColumns :")
    for c in df.columns :
        print( f"\t{c:<20}{str(df[c].dtype):<10}" )
        
    print( "\nTOP 5\t:" )
    print(f"{df.head(5)}\n" )
    
    df.info()
    

def show_statistics(df):

    # count = non_null 집계
    # mean = 평균
    # std = 표준편차
    # min = 최솟값
    # max = 최댓값
    # 25% = 오름차순 으로 정렬 했을때 25%지점의 값
    # 50% = 오름차순 으로 정렬 했을때 50%지점의 값 - median 중앙값
    # 75% = 오름차순 으로 정렬 했을때 75%지점의 값
    
    des = df.describe()

    print(f" "*20 +"mean")
    for c in df.select_dtypes(include="number") :
        print(f"{c:<20}{des[c]["mean"]}")
    print("\n")
    

def check_missing(df):
    
    r = len(df)

    nullData = {}
    for c in df.columns :

        nullSum = df[c].isnull().sum()
        if nullSum > 0 :
            nullData[c] = {}   
            per = int((nullSum / r)*100)
            if per < 5 :
                severity = "낮음"
            elif 20 > per >= 5 :
                severity = "주의"
            else :
                severity = "높음"

            nullData[c] = { "per" : per, "sev" : severity }

    if nullData :
        print("\n<Warning!!> 해당 columns 에서 결측치를 발견했습니다.\n")
        for c, info in nullData.items() :
            print(f"{c:<20}{info["per"]}%{info["sev"]:>5}")
            
    return nullData
    

def numpy_stats(df,colStr):
    # 기능 5

    colData = df[colStr].dropna().values
    
    max = np.max(colData)
    min = np.min(colData)
    mean = np.mean(colData)
    std = np.std(colData,ddof=1)
    median = np.median(colData)

    des = df[colStr].dropna().describe()
    
    print(f"{str(des["max"] == max):<6} {"max":<8}:  {max}")
    print(f"{str(des["min"] == min):<6} {"min":<8}:  {min}")
    print(f"{str(des["mean"] == mean):<6} {"mean":<8}:  {mean}")
    print(f"{str(des["std"] == std):<6} {"std":<8}:  {std}")
    print(f"{str(des["50%"] == median):<6} {"median":<8}:  {median}")
    

    print("\n6 시간 이상 공부한 학생의 수")
    print(f"{len(colData[colData >= 6])}명")

    return 0

if __name__ == "__main__" :
        
    BASE_DIR = Path(__file__).resolve().parent
    csv_data = BASE_DIR/ "../data/student_habits.csv"

    print("\n")
    print("-"*80)
    print(f"{"="*30}    Function #1    {"="*30}")
    print("-"*80)

    # 기능 1
    df = load_data(csv_data)

    print("\n")
    print("-"*80)
    print(f"{"="*30}    Function #2    {"="*30}")
    print("-"*80)
    print(f"\nFunction #2\n")

    # 기능 2
    explore_structure (df)

    print("-"*80)
    print(f"{"="*30}    Function #3    {"="*30}")
    print("-"*80)

    # 기능 3
    show_statistics(df)

    print("-"*80)
    print(f"{"="*30}    Function #4    {"="*30}")
    print("-"*80)
    
    # 기능 4
    check_missing(df)

    print("-"*80)
    print(f"{"="*30}    Function #5    {"="*30}")
    print("-"*80)

    # 기능 5
    colStr = "study_hours"
    numpy_stats(df,colStr)

