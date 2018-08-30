
# coding: utf-8

import sys
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
predict_answer = sys.argv[1]

# path = "/home/math/putintostyle/cathay2018/raw_data/"

compare_df = pd.read_csv("y_test.csv")
compare_arr = compare_df.values


input_df = pd.read_csv(predict_answer)
input_arr = input_df.values
input_arr[:,1]

error = 0
Erroe_array = []
length_input = len(input_arr)
length_compare = len(compare_arr)

if length_input == length_compare:
    for i in range(len(input_arr)):
        if input_arr[i][1] != compare_arr[i][1]:
            error += 1
            Erroe_array.append(1)
        else:
            Erroe_array.append(0)
print("Your Score is : " + str(1-(error/len(input_arr))))


Result = pd.DataFrame()
Result.head()
result_cols = ["CUST_ID","True_BUY_TYPE","Predict_BUY_TYPE", "ERROR"]
Result.columes = result_cols
Result["CUST_ID"] = input_arr[:,0]
Result["True_BUY_TYPE"] = input_arr[:,1]
Result["Predict_BUY_TYPE"] = compare_arr[:,1]
Result["ERROR"] = Erroe_array

Result.to_csv("match.csv")

