#-*- coding=utf-8 -*-
import pandas as pd
import numpy as np
import datetime
from feature import * 
import xgboost as xgb
from sklearn.cross_validation import train_test_split
import os


# 读取数据
action_1 = pd.read_csv("JData/JData_Action_201602.csv")
action_2 = pd.read_csv("JData/JData_Action_201603.csv")
action_3 = pd.read_csv("JData/JData_Action_201604.csv")
action_all = pd.concat([action_1,action_2,action_3],axis= 0)
action_all.sort_values(["user_id","time"],inplace=True)
action_all.index =[x for x in range(len(action_all))]
del action_1
del action_2
del action_3
action_all["index_col"] = action_all.index.tolist()



action_cate_8 = action_all.loc[action_all["cate"]==8]
#action_cate_8.sort_values(["user_id","time"],inplace=True)
action_cate_8.index =[x for x in range(len(action_cate_8))]

def hanshu111(df):
    if len(df.loc[df["type"]==4]["days"])>0:
        days_std = list(df.loc[df["type"]==4]["days"])[0]
    else:
        days_std =0
    df = df.loc[:,["days","type"]]
    df = df.drop_duplicates(["days"])
    df = df.loc[df["days"]>=days_std]
    #print(1)
    df.index =[ x for x in range(len(df))]
    #print(df)
    biaoben1 = pd.merge(biaoben,df,how="left",on=["days"])
    biaoben1 = biaoben1.fillna(value=0)
    biaoben1 =biaoben1[biaoben1 <=0]
    #print(biaoben1)
    biaoben1.days = [ x for x in range(1,76)]
    biaoben1 = biaoben1.fillna(value=1)
    if days_std>0:
        biaoben1.iloc[days_std-1:days_std,1:2]=10
    return biaoben1.type.T
biaoben=pd.DataFrame({"days": [x for x in range(1,76)]})
shijian = action_cate_8.groupby(["user_id"]).apply(hanshu111)
shijian.to_csv("shijian.csv")
## 得到每个人的login表格


user_all =pd.read_csv("JData/JData_User.csv",encoding="gbk")
com_all= pd.read_csv("JData/JData_Comment.csv")
sku_all = pd.read_csv("JData/JData_Product.csv")

action_all_buy = action_all.loc[(action_all["type"]==4)&(action_all["cate"]==8)]
action_all_buy.index =[x for x in range(len(action_all_buy))]
sku_num = pd.DataFrame({"sku_id": action_all_buy["sku_id"].value_counts().index.tolist(),"number": action_all_buy["sku_id"].value_counts().tolist()})


com_all.sort_values(["sku_id","dt"],inplace=True )
com_all1 = pd.merge(com_all,sku_all,how="left",on=["sku_id"])
com_all1=com_all1.loc[com_all1["cate"]==8]
com_all1.index =[x for x in range(len(com_all1)) ]
com_all1.loc[com_all1["a1"]==-1]
com_all1.sort_values(["a1","a2","a3","sku_id","dt"])
com_all_deal = com_all1.loc[(com_all1["dt"]=="2016-04-15")]
com_all_deal.index =[x for x  in range(len(com_all_deal))]

com_all_deal1 = com_all_deal.loc[:,["sku_id_x","comment_num","has_bad_comment","bad_comment_rate","a1","a2","a3"]]
zz =com_all_deal1.columns.tolist()
zz[0]="sku_id"
com_all_deal1.columns = zz
com_all_deal1
action_all_buy.time = pd.to_datetime(action_all_buy.time)
std_time1 =pd.to_datetime("2016-04-16 00:00:00")
action_all_buy["time_days"] = action_all_buy.time.apply(lambda x : abs((x-std_time1).days))
action_all_buy = pd.merge(action_all_buy, user_all,how="left",on=["user_id"])
action_all_buy.sort_values(["sku_id","time"],inplace=True)
action_all_buy = pd.merge(action_all_buy, com_all_deal1,how="left",on=["sku_id"] )


all_biaoben =pd.read_csv("shijian.csv")
os.remove("shijian.csv")
buy_biaoben_1 = pd.concat([all_biaoben.iloc[:,:1].copy(),all_biaoben.iloc[:,1: 6  ].copy().sum(1)],axis=1)
buy_biaoben_2 = pd.concat([all_biaoben.iloc[:,:1].copy(),all_biaoben.iloc[:,6: 11 ].copy().sum(1)],axis=1)
buy_biaoben_3 = pd.concat([all_biaoben.iloc[:,:1].copy(),all_biaoben.iloc[:,11: 16].copy().sum(1)],axis=1)
buy_biaoben_1 = buy_biaoben_1.loc[buy_biaoben_1[0]>=10]
buy_biaoben_2 = buy_biaoben_2.loc[buy_biaoben_2[0]>=10]
buy_biaoben_3 = buy_biaoben_3.loc[buy_biaoben_3[0]>=10]
buy_biaoben_1.index =[x for x in range(len(buy_biaoben_1))] 
buy_biaoben_2.index =[x for x in range(len(buy_biaoben_2))] 
buy_biaoben_3.index =[x for x in range(len(buy_biaoben_3))] 


maybe_biaoben_1 = pd.concat([all_biaoben.iloc[:,:1].copy(),all_biaoben.iloc[:,6: ].copy()],axis=1)
maybe_biaoben_1.columns =["user_id"]+[x for x in range(70)]
maybe_biaoben_2 = pd.concat([all_biaoben.iloc[:,:1].copy(),all_biaoben.iloc[:,11: ].copy()],axis=1)
maybe_biaoben_2.columns =["user_id"]+[x for x in range(65)]


all_biaoben1 =all_biaoben.copy()
all_biaoben1["if_buy"] = all_biaoben1.apply(lambda x : sum(x==10),axis=1)
all_biaoben1 = all_biaoben1.loc[all_biaoben1["if_buy"]==0]
all_biaoben1.index =[ x for x in range(len(all_biaoben1))]

#all_biaoben1.iloc[ : , 1:5 ].sum(1),all_biaoben1.iloc[ : , 1:8 ].sum(1),all_biaoben1.iloc[ : , 1:15 ].sum(1),maybe_biaoben_2.iloc[ : , 1:29 ].sum(1),all_biaoben1.iloc[ : , 1: ].sum(1)
 
all_biaoben1 = pd.concat([all_biaoben1,all_biaoben1.iloc[ : , 1:5 ].sum(1),all_biaoben1.iloc[ : , 1:8 ].sum(1),maybe_biaoben_1.iloc[ : , 1:10 ].sum(1),all_biaoben1.iloc[ : , 1:15 ].sum(1),all_biaoben1.iloc[ : , 1:29 ].sum(1),all_biaoben1.iloc[ : , 1: ].sum(1),all_biaoben1.iloc[ : , 32:33 ].sum(1),all_biaoben1.iloc[ : , 33:34 ].sum(1)],axis=1)
all_biaoben1.columns =["user_id"]+[x for x in range(75)]+["if_buy","four_days","seven_days","nine_days","two_weeks","four_weeks","all_days","3-15","3-14"]
all_biaoben1 = all_biaoben1.loc[all_biaoben1["all_days"]!=0]
all_biaoben1.index =[ x for x in range(len(all_biaoben1))]



maybe_biaoben_1["if_buy"] = maybe_biaoben_1.apply(lambda x : sum(x==10),axis=1)
maybe_biaoben_1 = maybe_biaoben_1.loc[maybe_biaoben_1["if_buy"]==0]
maybe_biaoben_1.index =[ x for x in range(len(maybe_biaoben_1))]
maybe_biaoben_1 = pd.concat([maybe_biaoben_1,maybe_biaoben_1.iloc[ : , 1:5 ].sum(1),maybe_biaoben_1.iloc[ : , 1:8 ].sum(1),maybe_biaoben_1.iloc[ : , 1:10 ].sum(1),maybe_biaoben_1.iloc[ : , 1:15 ].sum(1),maybe_biaoben_1.iloc[ : , 1:29 ].sum(1),maybe_biaoben_1.iloc[ : , 1: ].sum(1),all_biaoben1.iloc[ : , 27:28 ].sum(1),all_biaoben1.iloc[ : , 28:29 ].sum(1)],axis=1)
maybe_biaoben_1.columns =["user_id"]+[x for x in range(70)]+["if_buy","four_days","seven_days","nine_days","two_weeks","four_weeks","all_days","3-15","3-14"]
maybe_biaoben_1 = maybe_biaoben_1.loc[maybe_biaoben_1["all_days"]!=0]
maybe_biaoben_1.index =[ x for x in range(len(maybe_biaoben_1))]


maybe_biaoben_2["if_buy"] = maybe_biaoben_2.apply(lambda x : sum(x==10),axis=1)
maybe_biaoben_2 = maybe_biaoben_2.loc[maybe_biaoben_2["if_buy"]==0]
maybe_biaoben_2.index =[ x for x in range(len(maybe_biaoben_2))]
maybe_biaoben_2 = pd.concat([maybe_biaoben_2,maybe_biaoben_2.iloc[ : , 1:5 ].sum(1),maybe_biaoben_2.iloc[ : , 1:8 ].sum(1),maybe_biaoben_2.iloc[ : , 1:10 ].sum(1),maybe_biaoben_2.iloc[ : , 1:15 ].sum(1),maybe_biaoben_2.iloc[ : , 1:29 ].sum(1),maybe_biaoben_2.iloc[ : , 1: ].sum(1),all_biaoben1.iloc[ : , 27:28 ].sum(1),all_biaoben1.iloc[ : , 28:29 ].sum(1)],axis=1)
maybe_biaoben_2.columns =["user_id"]+[x for x in range(65)]+["if_buy","four_days","seven_days","nine_days","two_weeks","four_weeks","all_days","3-15","3-14"]
maybe_biaoben_2 = maybe_biaoben_2.loc[maybe_biaoben_2["all_days"]!=0]
maybe_biaoben_2.index =[ x for x in range(len(maybe_biaoben_2))]


maybe_biaoben_1 = pd.merge(maybe_biaoben_1,user_all,how="left",on=["user_id"])
maybe_biaoben_2 = pd.merge(maybe_biaoben_2,user_all,how="left",on=["user_id"])
maybe_biaoben_4 = pd.merge(all_biaoben1,user_all,how="left",on=["user_id"])

pd1= pd.merge(buy_biaoben_1,action_cate_8.loc[:,["user_id","sku_id","type"]],how="left",on=["user_id"])
pd1 = pd1.loc[pd1.type==4]
pd1.index = [x for x in range(len(pd1))]

pd2= pd.merge(buy_biaoben_2,action_cate_8.loc[:,["user_id","sku_id","type"]],how="left",on=["user_id"])
pd2 = pd2.loc[pd2.type==4]
pd2.index = [x for x in range(len(pd2))]

def jisuandaan(df1,df2):
    df11 = df1.loc[:,["user_id"]]
    df11["if1"] =[1 for x in range(len(df11))]
    df22 = df2.loc[:,["user_id"]]
    df_dd = pd.merge(df22,df11,how="left",on=["user_id"])
    print(len(df_dd.loc[df_dd["if1"]==1]),len(df1),"*****",len(df_dd.loc[df_dd["if1"]==1])/len(df1),"*****",len(df2))


def acq(df):
    a1 = (df[0]==1)
    a2 = (df[1]==1)
    a3 = (df[2]==1)
    a4 = (df[3]==1)
    a5 = (df[4]==1)
    a6 = (df[5]==1)
    a7 = (df[6]==1)
    a8 = (df[7]==1)
    a9 = (df[8]==1)
    b1 = (df["all_days"]>=1)
    b2 = (df["all_days"]>=2)
    b3 = (df["all_days"]==3)
    b4 = (df["all_days"]==4)
    b5 = (df["all_days"]==5)
    c0 = (df["seven_days"]==df["all_days"])
    c00 = (df["nine_days"]==df["all_days"])
    c1 = (df["seven_days"]==1 )
    c2 = (df["seven_days"]==2 )
    c3 = (df["seven_days"]==3 )
    f1 = (df["user_lv_cd"]==1)
    f2 = (df["user_lv_cd"]==2)
    f3 = (df["user_lv_cd"]==3)
    f4 = (df["user_lv_cd"]==4)
    f5 = (df["user_lv_cd"]==5)
    g1 = (df["user_reg_tm"]<"2015-01-26")
    h1 = (df["sex"]==0) 
    h2 = (df["sex"]==1) 
    h3 = (df["sex"]==2) 
    j0 = (df["age"]=="-1")
    j1 = (df["age"]=="15岁以下")
    j2 = (df["age"]=="16-25岁")
    j3 = (df["age"]=="26-35岁")
    j4 = (df["age"]=="36-45岁")
    j5 = (df["age"]=="46-55岁")
    j6 = (df["age"]=="56岁以上")

    df1 = df.loc[((a4&b1&c0)|(a3&b1&c0)|(a2&b1&c0)|(c0&a1&b1)|(c0&a5&b1)|(c0&a6&b1)|(c0&a7&b1)|(c0&b2&(a1&a3))|(c0&b2&(a1&a4))|(c0&b2&(a1&a2))|(c0&b2&(a2&a4)))&(f3|f4|f5)]

    return df1


user_all["user_reg_tm1"] = pd.to_datetime(user_all.user_reg_tm)#.apply(lambda x )
user_all["user_reg_tm2"] = (user_all["user_reg_tm1"]-pd.to_datetime("2016-04-20 00:00:00"))#.days
z = list(user_all["user_reg_tm2"])
t=[]
for j in range(len(z)):
    try:
        t.append(int(str(z[j])[1:-14]))
    except:
        t.append(365)
user_all["zhucedays"] = t
user_all = user_all.loc[:,["user_id","age","sex","user_lv_cd","user_reg_tm","zhucedays"]]

def acq_deal_1(df):
    df = df.loc[:,["user_id"]]
    df1 = pd.merge(df,action_cate_8,how="left",on=["user_id"])
    df1.index = [ x for x in range(len(df1))]
    df1["time0"]=df1.time.apply(lambda x : int(x[5:7])-3)
    df1["time1"]=df1.time.apply(lambda x : int(x[8:10]))
    df1["time2"]=df1.time.apply(lambda x : int(x[11:13]))
    df1["time3"]=df1.time.apply(lambda x : int(x[14:16]))
    df1.time = pd.to_datetime(df1.time)
    df1_time = pd.to_datetime("2016-04-11 00:00:00")
    df1["days"] = df1.time.apply(lambda x : abs((x - df1_time).days))
    return df1

deal_1 = acq_deal_1(acq(maybe_biaoben_1))
deal_1 = deal_1.loc[deal_1["time"]<"2016-04-11 00:00:00"]
deal_1.index =[x for x in range(len(deal_1))]
deal_1_con = pd.merge(deal_1,pd1.loc[:,["user_id","sku_id","type"]],how="left",on=["user_id"])
com_all.sort_values(["sku_id","dt"],inplace=True )
com_all1 = pd.merge(com_all,sku_all,how="left",on=["sku_id"])
com_all1=com_all1.loc[com_all1["cate"]==8]
com_all1.index =[x for x in range(len(com_all1)) ]
com_all1.loc[com_all1["a1"]==-1]
com_all1.sort_values(["a1","a2","a3","sku_id","dt"])
com_all_deal = com_all1.loc[(com_all1["dt"]=="2016-04-15")]
com_all_deal.index =[x for x  in range(len(com_all_deal))]
#com_all_deal.head(5)
com_all_deal.columns = ["dt","sku_id_x","comment_num","has_bad_comment","bad_comment_rate","a1","a2","a3","cate","brand"]
deal_1_last = pd.merge(deal_1_con,com_all_deal.loc[:,["sku_id_x","comment_num","has_bad_comment","bad_comment_rate","a1","a2","a3"]],how="left",on=["sku_id_x"])
deal_1_last["time_sum"] =deal_1_last.time0*31*24*60+ deal_1_last.time1*24*60+deal_1_last.time2*60+1*deal_1_last.time3
deal_1_last = pd.merge(deal_1_last,user_all,how="left",on=["user_id"])

time_time = deal_1_last.groupby(["user_id"]).apply(hanshu_time_time)
type_car_con_1 = deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_1)
type_car_con_6 = deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_6)
type_car_con_2 = deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_2)
type_car_con_3 = deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_3)
type_car_con_5 = deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_5)
type_car_con_1_all = deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_1_all)
type_car_con_6_all = deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_6_all)
type_car_con_2_all = deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_2_all)
type_car_con_3_all= deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_3_all)
type_car_con_5_all= deal_1_last.groupby(["user_id"]).apply(hanshu_type_car_con_5_all)
time_ci = deal_1_last.groupby(["user_id"]).apply(hanshu_time_ci)
sku_number = deal_1_last.groupby(["user_id"]).apply(hanshu_sku_number)
days_number = deal_1_last.groupby(["user_id"]).apply(hanshu_days_number)
if_buy = deal_1_last.groupby(["user_id"]).apply(hanshu_if_buy)
age0 =deal_1_last.groupby(["user_id"]).apply(hanshu_age0)
age1 =deal_1_last.groupby(["user_id"]).apply(hanshu_age1)
age2 =deal_1_last.groupby(["user_id"]).apply(hanshu_age2)
age3 =deal_1_last.groupby(["user_id"]).apply(hanshu_age3)
age4 =deal_1_last.groupby(["user_id"]).apply(hanshu_age4)
age5 =deal_1_last.groupby(["user_id"]).apply(hanshu_age5)
age6 =deal_1_last.groupby(["user_id"]).apply(hanshu_age6)
sex =deal_1_last.groupby(["user_id"]).apply(hanshu_sex)
user_lv_cd = deal_1_last.groupby(["user_id"]).apply(hanshu_user_lv_cd)
day_1 = deal_1_last.groupby(["user_id"]).apply(hanshu_day_1)
day_2 = deal_1_last.groupby(["user_id"]).apply(hanshu_day_2)
day_3 = deal_1_last.groupby(["user_id"]).apply(hanshu_day_3)
day_4 = deal_1_last.groupby(["user_id"]).apply(hanshu_day_4)
day_5 = deal_1_last.groupby(["user_id"]).apply(hanshu_day_5)
day_6 = deal_1_last.groupby(["user_id"]).apply(hanshu_day_6)
day_7 = deal_1_last.groupby(["user_id"]).apply(hanshu_day_7)
qiua1 = deal_1_last.groupby(["user_id"]).apply(hanshu_qiua1)
qiua2 = deal_1_last.groupby(["user_id"]).apply(hanshu_qiua2)
qiua3 = deal_1_last.groupby(["user_id"]).apply(hanshu_qiua3)
time2_1 = deal_1_last.groupby(["user_id"]).apply(hanshu_time2_1)
time2_2 = deal_1_last.groupby(["user_id"]).apply(hanshu_time2_2)
time2_3 = deal_1_last.groupby(["user_id"]).apply(hanshu_time2_3)
time2_4 = deal_1_last.groupby(["user_id"]).apply(hanshu_time2_4)
time2_5 = deal_1_last.groupby(["user_id"]).apply(hanshu_time2_5)
time2_6 = deal_1_last.groupby(["user_id"]).apply(hanshu_time2_6)
user_reg_tm = deal_1_last.groupby(["user_id"]).apply(hanshu_user_reg_tm)
index_col_rate = deal_1_last.groupby(["user_id"]).apply(hanshu_index_col)
sku_only_one = deal_1_last.groupby(["user_id"]).apply(hanshu_sku_only_one)
brand_number = deal_1_last.groupby(["user_id"]).apply(hanshu_brand_number)
brand_only_one = deal_1_last.groupby(["user_id"]).apply(hanshu_brand_only_one)
brand_top_545 = deal_1_last.groupby(["user_id"]).apply(hanshu_brand_top_545)
model_number = deal_1_last.groupby(["user_id"]).apply(hanshu_model_number)
model_216 = deal_1_last.groupby(["user_id"]).apply(hanshu_model_216)
model_217 = deal_1_last.groupby(["user_id"]).apply(hanshu_model_217)
model_26 = deal_1_last.groupby(["user_id"]).apply(hanshu_model_26)
model_27 = deal_1_last.groupby(["user_id"]).apply(hanshu_model_27)


train_x = pd.DataFrame({"user_id": time_time.index.tolist(),"time_time": time_time.tolist(),"time2_1": time2_1.tolist(),"time2_2": time2_2.tolist(),"time2_3": time2_3.tolist(),"time2_4": time2_4.tolist(),"time2_5": time2_5.tolist(),"time2_6": time2_6.tolist(),
              "day_1":day_1.tolist(),"day_2":day_2.tolist(),"day_3":day_3.tolist(),"day_4":day_4.tolist(),"day_5":day_5.tolist(),"day_6":day_6.tolist(),"day_7":day_7.tolist(),"qiua1": qiua1.tolist(),"qiua2": qiua2.tolist(),"qiua3": qiua3.tolist(),
             "user_lv_cd": user_lv_cd.tolist(),
             "age0": age0.tolist(),"age1": age1.tolist(),"age2": age2.tolist(),"age3": age3.tolist(),"age4": age4.tolist(),"age5": age5.tolist(),
             "age6": age6.tolist(),"sex": sex.tolist(),"time_ci": time_ci.tolist(),"type_car_con_1": type_car_con_1.tolist(),"type_car_con_2": type_car_con_2.tolist(),"type_car_con_3": type_car_con_3.tolist(),"type_car_con_5": type_car_con_5.tolist(),
              "type_car_con_6": type_car_con_6.tolist(),"label": if_buy.tolist(),"sku_number": sku_number.tolist(),"days_number": days_number.tolist(),"index_col_rate": index_col_rate.tolist(),
              "type_car_con_1_all": type_car_con_1_all.tolist(),"type_car_con_2_all": type_car_con_2_all.tolist(),"type_car_con_3_all": type_car_con_3_all.tolist(),"type_car_con_5_all": type_car_con_5_all.tolist() ,"type_car_con_6_all": type_car_con_6_all.tolist(),
            "sku_only_one": sku_only_one.tolist(),"brand_number": brand_number.tolist(),"brand_only_one" : brand_only_one.tolist(),"brand_top_545": brand_top_545.tolist(),
                        "model_number": model_number.tolist(),
                "model_216": model_216.tolist(),"model_217": model_217.tolist(),"model_26": model_26.tolist(),"model_27": model_27.tolist()})
############################
#获取训练集
############################



def acq_deal_2(df):
    df = df.loc[:,["user_id"]]
    df1 = pd.merge(df,action_cate_8,how="left",on=["user_id"])
    df1.index = [ x for x in range(len(df1))]
    df1["time0"]=df1.time.apply(lambda x : int(x[5:7])-3)
    df1["time1"]=df1.time.apply(lambda x : int(x[8:10]))
    df1["time2"]=df1.time.apply(lambda x : int(x[11:13]))
    df1["time3"]=df1.time.apply(lambda x : int(x[14:16]))
    df1.time = pd.to_datetime(df1.time)
    df1_time = pd.to_datetime("2016-04-16 00:00:00")
    df1["days"] = df1.time.apply(lambda x : abs((x - df1_time).days))
    return df1
deal_2 = acq_deal_2(acq(maybe_biaoben_4))
deal_2 = deal_2.loc[deal_2["time"]<"2016-04-16 00:00:00"]
deal_2.index =[x for x in range(len(deal_2))]
deal_2_con = pd.merge(deal_2,pd2.loc[:,["user_id","sku_id","type"]],how="left",on=["user_id"])
com_all.sort_values(["sku_id","dt"],inplace=True )
com_all1 = pd.merge(com_all,sku_all,how="left",on=["sku_id"])
com_all1=com_all1.loc[com_all1["cate"]==8]
com_all1.index =[x for x in range(len(com_all1)) ]
com_all1.loc[com_all1["a1"]==-1]
com_all1.sort_values(["a1","a2","a3","sku_id","dt"])
com_all_deal = com_all1.loc[(com_all1["dt"]=="2016-04-15")]
com_all_deal.index =[x for x  in range(len(com_all_deal))]
#com_all_deal.head(5)
com_all_deal.columns = ["dt","sku_id_x","comment_num","has_bad_comment","bad_comment_rate","a1","a2","a3","cate","brand"]
deal_2_last = pd.merge(deal_2_con,com_all_deal.loc[:,["sku_id_x","comment_num","has_bad_comment","bad_comment_rate","a1","a2","a3"]],how="left",on=["sku_id_x"])
deal_2_last["time_sum"] = deal_2_last.time0*31*24*60+ deal_2_last.time1*24*60+deal_2_last.time2*60+1*deal_2_last.time3
deal_2_last = pd.merge(deal_2_last,user_all,how="left",on=["user_id"])

tetime_time = deal_2_last.groupby(["user_id"]).apply(hanshu_time_time)
tetype_car_con_1 = deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_1)
tetype_car_con_6 = deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_6)
tetype_car_con_2 = deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_2)
tetype_car_con_3 = deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_3)
tetype_car_con_5 = deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_5)
tetype_car_con_1_all = deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_1_all)
tetype_car_con_6_all = deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_6_all)
tetype_car_con_2_all = deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_2_all)
tetype_car_con_3_all= deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_3_all)
tetype_car_con_5_all= deal_2_last.groupby(["user_id"]).apply(hanshu_type_car_con_5_all)
tetime_ci = deal_2_last.groupby(["user_id"]).apply(hanshu_time_ci)
tesku_number = deal_2_last.groupby(["user_id"]).apply(hanshu_sku_number)
tedays_number = deal_2_last.groupby(["user_id"]).apply(hanshu_days_number)
teif_buy = deal_2_last.groupby(["user_id"]).apply(hanshu_if_buy)
teage0 =deal_2_last.groupby(["user_id"]).apply(hanshu_age0)
teage1 =deal_2_last.groupby(["user_id"]).apply(hanshu_age1)
teage2 =deal_2_last.groupby(["user_id"]).apply(hanshu_age2)
teage3 =deal_2_last.groupby(["user_id"]).apply(hanshu_age3)
teage4 =deal_2_last.groupby(["user_id"]).apply(hanshu_age4)
teage5 =deal_2_last.groupby(["user_id"]).apply(hanshu_age5)
teage6 =deal_2_last.groupby(["user_id"]).apply(hanshu_age6)

tesex =deal_2_last.groupby(["user_id"]).apply(hanshu_sex)

teuser_lv_cd = deal_2_last.groupby(["user_id"]).apply(hanshu_user_lv_cd)
teday_1 = deal_2_last.groupby(["user_id"]).apply(hanshu_day_1)
teday_2 = deal_2_last.groupby(["user_id"]).apply(hanshu_day_2)
teday_3 = deal_2_last.groupby(["user_id"]).apply(hanshu_day_3)
teday_4 = deal_2_last.groupby(["user_id"]).apply(hanshu_day_4)
teday_5 = deal_2_last.groupby(["user_id"]).apply(hanshu_day_5)
teday_6 = deal_2_last.groupby(["user_id"]).apply(hanshu_day_6)
teday_7 = deal_2_last.groupby(["user_id"]).apply(hanshu_day_7)
teqiua1 = deal_2_last.groupby(["user_id"]).apply(hanshu_qiua1)
teqiua2 = deal_2_last.groupby(["user_id"]).apply(hanshu_qiua2)
teqiua3 = deal_2_last.groupby(["user_id"]).apply(hanshu_qiua3)
tetime2_1 = deal_2_last.groupby(["user_id"]).apply(hanshu_time2_1)
tetime2_2 = deal_2_last.groupby(["user_id"]).apply(hanshu_time2_2)
tetime2_3 = deal_2_last.groupby(["user_id"]).apply(hanshu_time2_3)
tetime2_4 = deal_2_last.groupby(["user_id"]).apply(hanshu_time2_4)
tetime2_5 = deal_2_last.groupby(["user_id"]).apply(hanshu_time2_5)
tetime2_6 = deal_2_last.groupby(["user_id"]).apply(hanshu_time2_6)
teuser_reg_tm = deal_2_last.groupby(["user_id"]).apply(hanshu_user_reg_tm)
teindex_col_rate = deal_2_last.groupby(["user_id"]).apply(hanshu_index_col)
#df_len = deal_2_last.groupby(["user_id"]).apply(hanshu_df_len)
tesku_only_one = deal_2_last.groupby(["user_id"]).apply(hanshu_sku_only_one)
tebrand_number = deal_2_last.groupby(["user_id"]).apply(hanshu_brand_number)
tebrand_only_one = deal_2_last.groupby(["user_id"]).apply(hanshu_brand_only_one)

tebrand_top_545 = deal_2_last.groupby(["user_id"]).apply(hanshu_brand_top_545)

temodel_number = deal_2_last.groupby(["user_id"]).apply(hanshu_model_number)
temodel_216 = deal_2_last.groupby(["user_id"]).apply(hanshu_model_216)
temodel_217 = deal_2_last.groupby(["user_id"]).apply(hanshu_model_217)
temodel_26 = deal_2_last.groupby(["user_id"]).apply(hanshu_model_26)
temodel_27 = deal_2_last.groupby(["user_id"]).apply(hanshu_model_27)

test_x = pd.DataFrame({"user_id": tetime_time.index.tolist(),"time_time": tetime_time.tolist(),"time2_1": tetime2_1.tolist(),"time2_2": tetime2_2.tolist(),"time2_3": tetime2_3.tolist(),"time2_4": tetime2_4.tolist(),"time2_5": tetime2_5.tolist(),"time2_6": tetime2_6.tolist(),
              "day_1": teday_1.tolist(),"day_2": teday_2.tolist(),"day_3": teday_3.tolist(),"day_4": teday_4.tolist(),"day_5": teday_5.tolist(),"day_6": teday_6.tolist(),"day_7": teday_7.tolist(),"qiua1": teqiua1.tolist(),"qiua2": teqiua2.tolist(),"qiua3": teqiua3.tolist(),
             "user_lv_cd": teuser_lv_cd.tolist(),
             "age0": teage0.tolist(),"age1": teage1.tolist(),"age2": teage2.tolist(),"age3": teage3.tolist(),"age4": teage4.tolist(),"age5": teage5.tolist(),
             "age6": teage6.tolist(),"sex": tesex.tolist(),"time_ci": tetime_ci.tolist(),"type_car_con_1": tetype_car_con_1.tolist(),"type_car_con_2": tetype_car_con_2.tolist(),"type_car_con_3": tetype_car_con_3.tolist(),"type_car_con_5": tetype_car_con_5.tolist(),
              "type_car_con_6": tetype_car_con_6.tolist(),"label": teif_buy.tolist(),"sku_number": tesku_number.tolist(),"days_number": tedays_number.tolist(),"index_col_rate": teindex_col_rate.tolist() ,
            "type_car_con_1_all": tetype_car_con_1_all.tolist(),"type_car_con_2_all": tetype_car_con_2_all.tolist(),"type_car_con_3_all": tetype_car_con_3_all.tolist(),"type_car_con_5_all": tetype_car_con_5_all.tolist() ,"type_car_con_6_all": tetype_car_con_6_all.tolist() ,
             "sku_only_one": tesku_only_one.tolist(),"brand_number": tebrand_number.tolist(),"brand_only_one" : tebrand_only_one.tolist(),
            "brand_top_545": tebrand_top_545.tolist(),"model_number": temodel_number.tolist(),
                "model_216": temodel_216.tolist(),"model_217": temodel_217.tolist(),"model_26": temodel_26.tolist(),"model_27": temodel_27.tolist()})
#################################
#获取测试集
#################################





########
#user_id训练模型
########
X_train, X_test, y_train, y_test = train_test_split(train_x, train_x.label.values, test_size=0.2, random_state=1)
dtrain = xgb.DMatrix(X_train.drop(['user_id', 'label'], axis=1), label=y_train)
dtest = xgb.DMatrix(X_test.drop(['user_id', 'label'], axis=1), label=y_test)
dvalid = xgb.DMatrix(test_x.drop(['user_id', 'label'], axis=1))

param = {'learning_rate' : 0.1, 'n_estimators': 500, 'max_depth': 3, 
        'min_child_weight': 5, 'gamma': 0.2, 'subsample': 1, 'colsample_bytree': 0.8,
        'scale_pos_weight': 1, 'eta': 0.05, 'silent': 0, 'objective': 'binary:logistic','booster': 'gbtree'}
num_round = 52
# 89
param['nthread'] = -1
param['eval_metric'] = "logloss"
evallist = [(dtest, 'test'), (dtrain, 'train')]
bst = xgb.train(params=param, dtrain=dtrain, num_boost_round=num_round, evals=evallist, early_stopping_rounds=10)

predict = bst.predict(dvalid)

for i in range(1,120):
    pred = test_x[predict>i*0.001].user_id
    list2 = pred.tolist()
    if len(list2)<=800:
	break
pre_5_15 = pd.DataFrame({"user_id": list2,"sku_id":list2})



###############
#sku_id训练模型
###############
deal_11_last = deal_1_last.copy()
deal_11_last= deal_11_last.fillna(0)
sku_train_all = deal_11_last.groupby(["user_id"]).apply(hanshusku_getsku_id)
deal_22_last = deal_2_last.copy()
deal_22_last= deal_22_last.fillna(0)
sku_test_all = deal_22_last.groupby(["user_id"]).apply(hanshusku_getsku_id)

X_train, X_test, y_train, y_test = train_test_split(sku_train_all1, sku_train_all1.label, test_size=0.2, random_state=1)
dtrain = xgb.DMatrix(X_train.drop([0,1, 'label'], axis=1), label=y_train)
dtest = xgb.DMatrix(X_test.drop([0,1, 'label'], axis=1), label=y_test)
dvalid = xgb.DMatrix(sku_test_all.drop([0,1], axis=1))

param = {'learning_rate' : 0.1, 'n_estimators': 200, 'max_depth': 2, 
        'min_child_weight': 5, 'gamma': 0, 'subsample': 1, 'colsample_bytree': 0.8,
        'scale_pos_weight': 1, 'eta': 0.05, 'silent': 1, 'objective': 'binary:logistic'}
num_round = 107
param['nthread'] = -1
param['eval_metric'] = "logloss"
evallist = [(dtest, 'test'), (dtrain, 'train')]
bst = xgb.train(params=param, dtrain=dtrain, num_boost_round=num_round, evals=evallist, early_stopping_rounds=50)
predict = bst.predict(dvalid)
sku_test_all["index_col"] =[x for x in range(len(sku_test_all))]
sku_test_all.drop_duplicates([0])
sku_test_all["pred"]=list(predict)



def hahahhaha(df):
    fgh = list(df.pred)
    return df.loc[df.pred==max(fgh)].loc[:,[0,1]]
    
tijiao = sku_test_all.groupby([0]).apply(hahahhaha)
tijiao.index =[x for x in range(len(tijiao))]
tijiao.columns=["user_id","sku_id"]
tijiao.user_id.value_counts()

t = pd.merge(pre_5_15,tijiao,how="left",on=["user_id"]).loc[:,["user_id","sku_id_y"]]
t.drop_duplicates(["user_id"],inplace=True)
t.columns =["user_id","sku_id"]

pre_5_15_1 = pd.concat([t.loc[:,["user_id"]].astype(int),t.loc[:,["sku_id"]].astype(int)],axis=1)
pre_5_15_1.to_csv("pre_online.csv",index=False)
#############pre_online.csv为最终的提交文档