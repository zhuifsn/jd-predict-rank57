#-*- coding=utf-8 -*-
import pandas as pd
import numpy as np
import datetime


def hanshu_index_col(df):
    t1 = list(df.index_col)[0]
    t2 = list(df.index_col)[-1]
    if ((t2-t1+1)/len(df))<= 1.1:
        return 10
    else:
        return 0
# 读取注册天数######
def hanshu_user_reg_tm(df):
    t = list(df.zhucedays)[0]
    return t

# 年龄分化########
def hanshu_age1(df):
    tt =list(df["age"])
    if len(tt)==0:
        return 0
    if tt[0] =="15岁以下":
        return 10
    else:
        return 0 
def hanshu_age2(df):
    tt =list(df["age"])
    if len(tt)==0:
        return 0
    if tt[0] =="16-25岁":
        return 10
    else:
        return 0 
def hanshu_age3(df):
    tt =list(df["age"])
    if len(tt)==0:
        return 0
    if tt[0] =="26-35岁":
        return 10
    else:
        return 0 
def hanshu_age4(df):
    tt =list(df["age"])
    if len(tt)==0:
        return 0
    if tt[0] =="36-45岁":
        return 10
    else:
        return 0 
def hanshu_age5(df):
    tt =list(df["age"])
    if len(tt)==0:
        return 0
    if tt[0] =="46-55岁":
        return 10
    else:
        return 0 
def hanshu_age6(df):
    tt =list(df["age"])
    if len(tt)==0:
        return 0
    if tt[0] =="55岁以上":
        return 10
    else:
        return 0 

def hanshu_age0(df):
    tt =list(df["age"])
    if len(tt)==0:
        return 0
    elif tt[0] ==0:
        return 10
    else:
        return 0

#  根据性别分类#######
def hanshu_sex(df):
    tt =list(df["sex"])
    if len(tt)==0:
        return 0
    elif tt[0] == 0:
        return 1
    elif tt[0] == 1:
        return 2
    elif tt[0] == 2:
        return 3
    
def hanshu_user_lv_cd(df):
    tt =list(df["user_lv_cd"])[0]
    if tt == 3:
        return 3
    elif tt==4:
        return 4
    elif tt ==5:
        return 5
    else:
        return 3

#      求出浏览的时间之和##########
def hanshu_time_time(df):            # 求出浏览的时间之和
    df_list = list(df.time_sum)
    number=1
    time_time=1
    for j in range(len(df_list)-1):
        if abs(df_list[j]-df_list[j+1])>10:
            number = number + 1
            time_time= time_time +1
        else:
            time_time = abs(df_list[j]-df_list[j+1]) + time_time
    return time_time

# 分割开来  只有1/6  和2/3/5。
def hanshu_type_car_con_6(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=3]
    click = list(df.type_x).count(6)
    if click==0:
        return 0#look/(look+click)
    else:
        return 10
def hanshu_type_car_con_1(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=3]
    look = list(df.type_x).count(1)
    if look == 0 :
        return 0#look/(look+click)
    else:
        return 10
def hanshu_type_car_con_2(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=3]
    car = list(df.type_x).count(2)

    if car==0 :
        return 0#look/(look+click)
    else:
        return 10
def hanshu_type_car_con_3(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=3]
    nocar = list(df.type_x).count(3)
    if nocar==0 :
        return 0#look/(look+click)
    else:
        return 10
def hanshu_type_car_con_5(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=3]
    con = list(df.type_x).count(5)
    if con ==0 :
        return 0#look/(look+click)
    else:
        return 10
#####################################
# 分割开来  只有1/6  和2/3/5。
def hanshu_type_car_con_6_all(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=7]
    click = list(df.type_x).count(6)
    if click==0:
        return 0#look/(look+click)
    else:
        return 10
def hanshu_type_car_con_1_all(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=7]
    look = list(df.type_x).count(1)
    if look == 0 :
        return 0#look/(look+click)
    else:
        return 10
def hanshu_type_car_con_2_all(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=7]
    car = list(df.type_x).count(2)

    if car==0 :
        return 0#look/(look+click)
    else:
        return 10
def hanshu_type_car_con_3_all(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=7]
    nocar = list(df.type_x).count(3)
    if nocar==0 :
        return 0#look/(look+click)
    else:
        return 10
def hanshu_type_car_con_5_all(df):           # 分割开来  只有1/6  和2/3/5。
    df = df.loc[df.days<=7]
    con = list(df.type_x).count(5)
    if con ==0 :
        return 0#look/(look+click)
    else:
        return 10
    
######################

#  看了多少次
def hanshu_time_ci(df):         #  看了多少次
    df_list = list(df.time_sum)
    number=1
    for j in range(len(df_list)-1):
        if abs(df_list[j]-df_list[j+1])>10:
            number = number + 1
    return number
# 看了多少个种类
def hanshu_sku_number(df):    # 看了多少个种类
    return len(set(list(df.sku_id_x)))

## 看了多少天####
def hanshu_days_number(df):
    return len(set(list(df.days)))
##是否该买    
def hanshu_if_buy(df):
    if len(df.loc[df.type_y>0])==0:
        return 0
    else :
        return 1
    
# 判断天数登陆
def hanshu_day_1(df):
    if len(df.loc[df.days==1])==0:
        return 0
    else:
        return 10
def hanshu_day_2(df):
    if len(df.loc[df.days==2])==0:
        return 0
    else:
        return 10 
def hanshu_day_3(df):
    if len(df.loc[df.days==3])==0:
        return 0
    else:
        return 10
def hanshu_day_4(df):
    if len(df.loc[df.days==4])==0:
        return 0
    else:
        return 10 
def hanshu_day_5(df):
    if len(df.loc[df.days==5])==0:
        return 0
    else:
        return 10 
def hanshu_day_6(df):
    if len(df.loc[df.days==6])==0:
        return 0
    else:
        return 10
def hanshu_day_7(df):
    if len(df.loc[df.days==7])==0:
        return 0
    else:
        return 10
##求的a的属性
def hanshu_qiua1(df):
    df1 = df.loc[df.a1>0].a1
    
    if len(df1)>0:
        return df1.value_counts().index[0]
    elif len(df.loc[df.a1>-2].a1):
        return df.a1.value_counts().index[0]
    else:
        return 0
def hanshu_qiua2(df):
    df1 = df.loc[df.a2>0].a2
    
    if len(df1)>0:
        return df1.value_counts().index[0]
    elif len(df.loc[df.a2>-2].a2):
        return df.a2.value_counts().index[0]
    else:
        return 0
def hanshu_qiua3(df):
    df1 = df.loc[df.a3>0].a3
    
    if len(df1)>0:
        return df1.value_counts().index[0]
    elif len(df.loc[df.a3>-2].a3):
        return df.a3.value_counts().index[0]
    else:
        return 0
    
#求的4小时登陆
def hanshu_time2_1(df):
    if len(df.loc[(df.time2>=0)&(df.time2<=3)])==0:
        return 0
    else:
        return 10
def hanshu_time2_2(df):
    if len(df.loc[(df.time2>=4)&(df.time2<=7)])==0:
        return 0
    else:
        return 10 
def hanshu_time2_3(df):
    if len(df.loc[(df.time2>=8)&(df.time2<=11)])==0:
        return 0
    else:
        return 10 
def hanshu_time2_4(df):
    if len(df.loc[(df.time2>=12)&(df.time2<=15)])==0:
        return 0
    else:
        return 10 
def hanshu_time2_5(df):
    if len(df.loc[(df.time2>=16)&(df.time2<=19)])==0:
        return 0
    else:
        return 10 
def hanshu_time2_6(df):
    if len(df.loc[(df.time2>=20)&(df.time2<=23)])==0:
        return 0
    else:
        return 10
###############################
def hanshu_sku_only_one(df):
    if len(set(list(df.sku_id_x)))==1:
        return 10
    else:
        return 0
def hanshu_brand_number(df):
    return len(set(list(df.brand)))
def hanshu_brand_only_one(df):
    if len(set(list(df.brand)))==1:
        return 10
    else:
        return 0
def hanshu_brand_top_545(df):
    brand_list = list(df.brand)
    brand_set = list(set(list(df.brand)))
    kong=[]
    for i in range(len(brand_set)):
        kong.append(brand_list.count(brand_set[i]))
    brand_top = brand_set[kong.index(max(kong))]
    if brand_top == 545:
        return 10
    elif brand_top == 214:
        return 9
    elif brand_top == 489:
        return 8
    elif brand_top == 800:
        return 7
    elif brand_top == 30:
        return 6
    elif brand_top == 403:
        return 5
    elif brand_top == 306:
        return 4
    elif brand_top == 658:
        return 3
    elif brand_top == 885:
        return 2
    elif brand_top == 677:
        return 1
    elif brand_top not in [545,214,489,800,30,403,306,693,658,885 ]:
        return 0

    
def hanshu_model_number(df):
    df1=df.loc[df["model_id"]>0]
    return len(set(list(df1.model_id)))
    
def hanshu_model_216(df):
    df1 = df.loc[df["model_id"]>0]
    model_list = list(set(list(df1.model_id)))
    if 216 in model_list:
        return 10
    else:
        return 0
    
def hanshu_model_217(df):
    df1 = df.loc[df["model_id"]>0]
    model_list = list(set(list(df1.model_id)))
    if 217 in model_list:
        return 10
    else:
        return 0   
def hanshu_model_27(df):
    df1 = df.loc[df["model_id"]>0]
    model_list = list(set(list(df1.model_id)))
    if 27 in model_list:
        return 10
    else:
        return 0
def hanshu_model_26(df):
    df1 = df.loc[df["model_id"]>0]
    model_list = list(set(list(df1.model_id)))
    if 26 in model_list:
        return 10
    else:
        return 0

def hanshusku_getsku_id(df):

    df_sum_col = len(df.sku_id_x )

    df_sum_kind = len(set(list(df.sku_id_x )))

    sku_id_list = list(set(list(df.sku_id_x)))
    sku_id_listall = list(df.sku_id_x)
    kong=[]
    for g in range(len(sku_id_list)):
        kong.append(sku_id_listall.count(sku_id_list[g]))
    max_len = sku_id_list[kong.index(max(kong))]
    
    if len(sku_id_list )==1:
        only_one =1
    else:
        only_one =0

    df_brand_kind = len(set(list(df.brand)))
    df_a1_kind = len(set(list(df.a1)))
    df_a2_kind = len(set(list(df.a2)))
    df_a3_kind = len(set(list(df.a3)))

    dfa1_list = list(df.a1)
    dfa1_list1 = list(set(list(df.a1)))
    a1_max_list=[]
    for i in range(len(dfa1_list1)):
        a1_max_list.append(dfa1_list.count(dfa1_list1[i]))
    a1_max = a1_max_list[a1_max_list.index(max(a1_max_list))]

    dfa2_list = list(df.a2)
    dfa2_list1 = list(set(list(df.a2)))
    a2_max_list=[]
    for i in range(len(dfa2_list1)):
        a2_max_list.append(dfa2_list.count(dfa2_list1[i]))
    a2_max = a2_max_list[a2_max_list.index(max(a2_max_list))]

    dfa3_list = list(df.a3)
    dfa3_list1 = list(set(list(df.a3)))
    a3_max_list=[]
    for i in range(len(dfa3_list1)):
        a3_max_list.append(dfa3_list.count(dfa3_list1[i]))
    a3_max = a3_max_list[a3_max_list.index(max(a3_max_list))]

    age_fl = list(df.age)[0]
    sex_fl = list(df.sex)[0]
    user_lv_cd_fl = list(df.user_lv_cd)[0]

    sex_1 =0
    sex_2 =0
    sex_0 =0
    if sex_fl== 1:
        sex_1 = 1
    elif sex_fl ==2:
        sex_2 = 1 
    elif sex_fl ==0 :
        sex_0 = 1

    lv_cd_3 =0
    lv_cd_4 =0
    lv_cd_5 =0
    if user_lv_cd_fl== 3:
        lv_cd_3 = 1
    elif sex_fl ==4:
        lv_cd_4 = 1 
    elif sex_fl ==5 :
        lv_cd_5 = 1    
    
    age_1 = 0
    age_2 = 0
    age_3 = 0
    age_4 = 0
    age_5 = 0
    age_6 = 0
    if age_fl =="15岁以下":
        age_1 = 1
    elif age_fl =="16-25岁":
        age_2 = 1
    elif age_fl =="26-35岁":
        age_3 = 1
    elif age_fl =="36-45岁":
        age_4 = 1
    elif age_fl =="46-55岁":
        age_5 = 1
    elif age_fl =="56岁以上":
        age_6 = 1
    
    
    df_days_1 =0
    df_days_2 =0
    df_days_3 =0
    df_days_4 =0
    df_days_5 =0
    df_days_6 =0
    df_days_7 =0
    df_days_list = list(df.days)
    if 1 in df_days_list:
        df_days_1 = 1 
    elif 2 in df_days_list:
        df_days_2 = 1 
    elif 3 in df_days_list:
        df_days_3 = 1 
    elif 4 in df_days_list:
        df_days_4 = 1 
    elif 5 in df_days_list:
        df_days_5 = 1 
    elif 6 in df_days_list:
        df_days_6 = 1 
    elif 7 in df_days_list:
        df_days_7 = 1
    
    

    df_time_sum_list = list(df.time_sum)
    number=1
    for j in range(len(df_time_sum_list)-1):
        if abs(df_time_sum_list[j]-df_time_sum_list[j+1])>10:
            number = number + 1
    time_ci = number
##########################################   
##############################################
##################################################
#####################################################
#     this_df1_sum_col = 1
#     df1_a1 = 0 
#     df1_a2 = 0 
#     df1_a3 = 0 
#     df1_brand = 0 
    #print(len(sku_id_list),sku_id_list)
    for j in range(1):#,len(sku_id_list)):
        ###########
        if max_len ==sku_id_list[j]:
            max_number =1
        else:
            max_number =0 
        
        this_df1_sum_col = 1
        df1_a1 = 0 
        df1_a2 = 0 
        df1_a3 = 0 
        df1_brand = 0 
        df1 = df.loc[df.sku_id_x == sku_id_list[j]]
        
        this_df1_sum_col = len(df1)
        this_df1_sum_col_rate = this_df1_sum_col/df_sum_col
        df1_a1 = list(df1.a1)[0]
        df1_a2 = list(df1.a2)[0]
        df1_a3 = list(df1.a3)[0]
        
        df2_type_car =0
        df2_type_nocar =0
        df2_type_con =0
        df2 = df1.loc[df1.days<=3]
        if 2 in list(df2.type_x):
            df2_type_car = 1
        elif 3 in list(df2.type_x):
            df2_type_nocar = 1
        elif 5 in list(df2.type_x):
            df2_type_con =1
        
        
        df3_type_car = 0
        df3_type_nocar = 0
        df3_type_con = 0
        df3 = df1.loc[(df1.days<=7)&(df1.days>=4)]
        if 2 in list(df3.type_x):
            df3_type_car = 1
        elif 3 in list(df3.type_x):
            df3_type_nocar = 1
        elif 5 in list(df3.type_x):
            df3_type_con =1
                        
        
        
        df1_brand_list = list(df1.brand)
        df1_brand_545 = 0
        df1_brand_214 = 0
        df1_brand_489 = 0
        df1_brand_800 = 0
        df1_brand_30 = 0
        df1_brand_403 = 0
        df1_brand_306 = 0
        df1_brand_693 = 0
        df1_brand_658 = 0
        df1_brand_885 = 0
        df1_brand_677 = 0
        df1_brand_812 = 0
        df1_brand_427 = 0
        df1_brand_244 = 0
        df1_brand_less = 0
        
        if df1_brand_list[0]==545:
            df1_brand_545 = 1
        elif df1_brand_list[0]==214:
            df1_brand_214 = 1
        elif df1_brand_list[0]==489:
            df1_brand_489 = 1
        elif df1_brand_list[0]==800:
            df1_brand_800 = 1
        elif df1_brand_list[0]==30:
            df1_brand_30 = 1
        elif df1_brand_list[0]==403:
            df1_brand_403 = 1
        elif df1_brand_list[0]==306:
            df1_brand_306 = 1
        elif df1_brand_list[0]==693:
            df1_brand_693 = 1
        elif df1_brand_list[0]==658:
            df1_brand_658 = 1
        elif df1_brand_list[0]==885:
            df1_brand_885 = 1
        elif df1_brand_list[0]==677:
            df1_brand_677 = 1
        elif df1_brand_list[0]==812:
            df1_brand_812 = 1
        elif df1_brand_list[0]==427:
            df1_brand_427 = 1
        elif df1_brand_list[0]==244:
            df1_brand_244 = 1
        else:
            df1_brand_less = 1
        
        #############################
        
        df1_days_1 =0
        df1_days_2 =0
        df1_days_3 =0
        df1_days_4 =0
        df1_days_5 =0
        df1_days_6 =0
        df1_days_7 =0
        df1_days_list = list(df1.days)
        if 1 in df1_days_list:
            df1_days_1 = 1 
        elif 2 in df1_days_list:
            df1_days_2 = 1 
        elif 3 in df1_days_list:
            df1_days_3 = 1 
        elif 4 in df1_days_list:
            df1_days_4 = 1 
        elif 5 in df1_days_list:
            df1_days_5 = 1 
        elif 6 in df1_days_list:
            df1_days_6 = 1 
        elif 7 in df1_days_list:
            df1_days_7 = 1
            
        df1_time_sum_list = list(df1.time_sum)
        number1=1
        for jj in range(len(df1_time_sum_list)-1):
            if abs(df1_time_sum_list[jj]-df1_time_sum_list[jj+1])>10:
                number1 = number1 + 1
        time_ci1 = number1 
        
        ########################
        time_shijian1 = 0
        time_shijian2 = 0
        time_shijian3 = 0
        time_shijian4 = 0
        time_shijian5 = 0
        time_shijian6 = 0
        if len(df1.loc[(df1.time2>=0)&(df1.time2<=3)])> 0:
            time_shijian1 = 1
        elif len(df1.loc[(df1.time2>=4)&(df1.time2<=7)])> 0:
            time_shijian2 = 1
        elif len(df1.loc[(df1.time2>=8)&(df1.time2<=11)])> 0:
            time_shijian3 = 1
        elif len(df1.loc[(df1.time2>=12)&(df1.time2<=15)])> 0:
            time_shijian4 = 1
        elif len(df1.loc[(df1.time2>=16)&(df1.time2<=19)])> 0:
            time_shijian5 = 1
        elif len(df1.loc[(df1.time2>=20)&(df1.time2<=23)])> 0:
            time_shijian6 = 1
            
        bad_com_rate = list(df1.bad_comment_rate)[0]
        
       
            
        all_list =[]
        all_list.append(list(df1.user_id)[0])
        all_list.append(sku_id_list[0])
        all_list.append(df_sum_col)
        all_list.append(df_sum_kind)
        all_list.append(df_brand_kind)
        all_list.append(df_a1_kind)
        all_list.append(df_a2_kind)
        all_list.append(df_a3_kind)
        all_list.append(df_days_1)
        all_list.append(df_days_2)
        all_list.append(df_days_3)
        all_list.append(df_days_4)
        all_list.append(df_days_5)
        all_list.append(df_days_6)
        all_list.append(df_days_7)
        all_list.append(time_ci)
        all_list.append(age_1)
        all_list.append(age_2)
        all_list.append(age_3)
        all_list.append(age_4)
        all_list.append(age_5)
        all_list.append(age_6)
        all_list.append(sex_0)
        all_list.append(sex_1)
        all_list.append(sex_2)
        all_list.append(lv_cd_3)
        all_list.append(lv_cd_4)
        all_list.append(lv_cd_5)
        all_list.append(this_df1_sum_col)
        all_list.append(this_df1_sum_col_rate)
        all_list.append(df1_a1)
        all_list.append(df1_a2)
        all_list.append(df1_a3)
        all_list.append(df1_brand_545)
        all_list.append(df1_brand_214)
        all_list.append(df1_brand_489)
        all_list.append(df1_brand_800)
        all_list.append(df1_brand_30)
        all_list.append(df1_brand_403)
        all_list.append(df1_brand_306)
        all_list.append(df1_brand_693)
        all_list.append(df1_brand_658)
        all_list.append(df1_brand_885)
        all_list.append(df1_brand_677)
        all_list.append(df1_brand_812)
        all_list.append(df1_brand_427)
        all_list.append(df1_brand_244)
        all_list.append(df1_brand_less)
        all_list.append(df1_days_1)
        all_list.append(df1_days_2)
        all_list.append(df1_days_3)
        all_list.append(df1_days_4)
        all_list.append(df1_days_5)
        all_list.append(df1_days_6)
        all_list.append(df1_days_7)
        all_list.append(time_ci1)
        all_list.append(time_shijian1)
        all_list.append(time_shijian2)
        all_list.append(time_shijian3)
        all_list.append(time_shijian4)
        all_list.append(time_shijian5)
        all_list.append(time_shijian6)
        all_list.append(max_number)
        all_list.append(only_one)
        all_list.append(bad_com_rate)
        all_list.append(df2_type_car)
        all_list.append(df2_type_nocar)
        all_list.append(df2_type_con)
        all_list.append(df3_type_car)
        all_list.append(df3_type_nocar)
        all_list.append(df3_type_con)
        #all_list.append(list(df1.user_id)[0])
        now1  = pd.DataFrame({"index": all_list})
#####################################################
############################################################
#######################################################
################################################################
    for j in range(1,len(sku_id_list)):
        ###########
        #print(sku_id_list[j])
        if max_len ==sku_id_list[j]:
            max_number =1
        else:
            max_number =0 
            
        this_df1_sum_col = 1
        df1_a1 = 0 
        df1_a2 = 0 
        df1_a3 = 0 
        df1_brand = 0 
        df1 = df.loc[df.sku_id_x == sku_id_list[j] ]
        
        this_df1_sum_col = len(df1)
        this_df1_sum_col_rate = this_df1_sum_col/df_sum_col
        df1_a1 = list(df1.a1)[0]
        df1_a2 = list(df1.a2)[0]
        df1_a3 = list(df1.a3)[0]
        
        df1_brand_list = list(df1.brand)
        df1_brand_545 = 0
        df1_brand_214 = 0
        df1_brand_489 = 0
        df1_brand_800 = 0
        df1_brand_30 = 0
        df1_brand_403 = 0
        df1_brand_306 = 0
        df1_brand_693 = 0
        df1_brand_658 = 0
        df1_brand_885 = 0
        df1_brand_677 = 0
        df1_brand_812 = 0
        df1_brand_427 = 0
        df1_brand_244 = 0
        df1_brand_less = 0
        
        if df1_brand_list[0]==545:
            df1_brand_545 = 1
        elif df1_brand_list[0]==214:
            df1_brand_214 = 1
        elif df1_brand_list[0]==489:
            df1_brand_489 = 1
        elif df1_brand_list[0]==800:
            df1_brand_800 = 1
        elif df1_brand_list[0]==30:
            df1_brand_30 = 1
        elif df1_brand_list[0]==403:
            df1_brand_403 = 1
        elif df1_brand_list[0]==306:
            df1_brand_306 = 1
        elif df1_brand_list[0]==693:
            df1_brand_693 = 1
        elif df1_brand_list[0]==658:
            df1_brand_658 = 1
        elif df1_brand_list[0]==885:
            df1_brand_885 = 1
        elif df1_brand_list[0]==677:
            df1_brand_677 = 1
        elif df1_brand_list[0]==812:
            df1_brand_812 = 1
        elif df1_brand_list[0]==427:
            df1_brand_427 = 1
        elif df1_brand_list[0]==244:
            df1_brand_244 = 1
        else:
            df1_brand_less = 1
        
        #############################
        
        df1_days_1 =0
        df1_days_2 =0
        df1_days_3 =0
        df1_days_4 =0
        df1_days_5 =0
        df1_days_6 =0
        df1_days_7 =0
        df1_days_list = list(df1.days)
        if 1 in df1_days_list:
            df1_days_1 = 1 
        elif 2 in df1_days_list:
            df1_days_2 = 1 
        elif 3 in df1_days_list:
            df1_days_3 = 1 
        elif 4 in df1_days_list:
            df1_days_4 = 1 
        elif 5 in df1_days_list:
            df1_days_5 = 1 
        elif 6 in df1_days_list:
            df1_days_6 = 1 
        elif 7 in df1_days_list:
            df1_days_7 = 1
            
        df1_time_sum_list = list(df1.time_sum)
        number1=1
        for jj in range(len(df1_time_sum_list)-1):
            if abs(df1_time_sum_list[jj]-df1_time_sum_list[jj+1])>10:
                number1 = number1 + 1
        time_ci1 = number1 
        
        ########################
        time_shijian1 = 0
        time_shijian2 = 0
        time_shijian3 = 0
        time_shijian4 = 0
        time_shijian5 = 0
        time_shijian6 = 0
        if len(df1.loc[(df1.time2>=0)&(df1.time2<=3)])> 0:
            time_shijian1 = 1
        elif len(df1.loc[(df1.time2>=4)&(df1.time2<=7)])> 0:
            time_shijian2 = 1
        elif len(df1.loc[(df1.time2>=8)&(df1.time2<=11)])> 0:
            time_shijian3 = 1
        elif len(df1.loc[(df1.time2>=12)&(df1.time2<=15)])> 0:
            time_shijian4 = 1
        elif len(df1.loc[(df1.time2>=16)&(df1.time2<=19)])> 0:
            time_shijian5 = 1
        elif len(df1.loc[(df1.time2>=20)&(df1.time2<=23)])> 0:
            time_shijian6 = 1
            
        bad_com_rate = list(df1.bad_comment_rate)[0]
            
        df2_type_car =0
        df2_type_nocar =0
        df2_type_con =0
        df2 = df1.loc[df1.days<=3]
        if 2 in list(df2.type_x):
            df2_type_car = 1
        elif 3 in list(df2.type_x):
            df2_type_nocar = 1
        elif 5 in list(df2.type_x):
            df2_type_con =1
        
        
        df3_type_car = 0
        df3_type_nocar = 0
        df3_type_con = 0
        df3 = df1.loc[(df1.days<=7)&(df1.days>=4)]
        if 2 in list(df3.type_x):
            df3_type_car = 1
        elif 3 in list(df3.type_x):
            df3_type_nocar = 1
        elif 5 in list(df3.type_x):
            df3_type_con =1
        
        
        
            
        all_list =[]
        
        all_list.append(list(df1.user_id)[0])
        all_list.append(sku_id_list[j])
        all_list.append(df_sum_col)
        all_list.append(df_sum_kind)
        all_list.append(df_brand_kind)
        #5
        all_list.append(df_a1_kind)
        all_list.append(df_a2_kind)
        all_list.append(df_a3_kind)
        all_list.append(df_days_1)
        all_list.append(df_days_2)
        #10
        all_list.append(df_days_3)
        all_list.append(df_days_4)
        all_list.append(df_days_5)
        all_list.append(df_days_6)
        all_list.append(df_days_7)
        #15
        all_list.append(time_ci)
        all_list.append(age_1)
        all_list.append(age_2)
        all_list.append(age_3)
        all_list.append(age_4)
        #20
        all_list.append(age_5)
        all_list.append(age_6)
        all_list.append(sex_0)
        all_list.append(sex_1)
        all_list.append(sex_2)
        #25
        all_list.append(lv_cd_3)
        all_list.append(lv_cd_4)
        all_list.append(lv_cd_5)
        all_list.append(this_df1_sum_col)
        all_list.append(this_df1_sum_col_rate)
        #30
        all_list.append(df1_a1)
        all_list.append(df1_a2)
        all_list.append(df1_a3)
        all_list.append(df1_brand_545)
        all_list.append(df1_brand_214)
        all_list.append(df1_brand_489)
        all_list.append(df1_brand_800)
        all_list.append(df1_brand_30)
        all_list.append(df1_brand_403)
        all_list.append(df1_brand_306)
        all_list.append(df1_brand_693)
        all_list.append(df1_brand_658)
        all_list.append(df1_brand_885)
        all_list.append(df1_brand_677)
        all_list.append(df1_brand_812)
        all_list.append(df1_brand_427)
        all_list.append(df1_brand_244)
        all_list.append(df1_brand_less)
        all_list.append(df1_days_1)
        all_list.append(df1_days_2)
        all_list.append(df1_days_3)
        all_list.append(df1_days_4)
        all_list.append(df1_days_5)
        all_list.append(df1_days_6)
        all_list.append(df1_days_7)
        all_list.append(time_ci1)
        all_list.append(time_shijian1)
        all_list.append(time_shijian2)
        all_list.append(time_shijian3)
        all_list.append(time_shijian4)
        all_list.append(time_shijian5)
        all_list.append(time_shijian6)
        all_list.append(max_number)
        all_list.append(only_one)
        all_list.append(bad_com_rate)
        all_list.append(df2_type_car)
        all_list.append(df2_type_nocar)
        all_list.append(df2_type_con)
        all_list.append(df3_type_car)
        all_list.append(df3_type_nocar)
        all_list.append(df3_type_con)
        now2 = pd.DataFrame({"index": all_list})             
        now1 = pd.concat([now1,now2],axis=1 )  
    return now1.T
            
       
    # 特征有：总行数：，年龄段：，性别：，用户等级：，a1最多：，a2最多： ，a3最多：,牌子种类数量,浏览天数，浏览次数 ||| 1+6+3+3+3+1
    # 是否处于第一类别:，该类行数 ，该类占比 ，a1 ,a2  ,a3, brand ,浏览天数,浏览次数 ，浏览时间段  ,购物车||| 1+1+1+3+15+7+7+7+7++6
    
#deal_1_last.groupby(["user_id"]).apply(hanshusku_getsku_id)