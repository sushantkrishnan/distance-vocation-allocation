import pandas as pd
import random
import numpy
import datetime

populate = {
    #Category: Broad Domains, Weight
    'Category1': ['Technical', 54],
    'Category2': ['Medical', 13],
    'Category3': ['SocialScience', 13],
    'Category4': ['Management', 10],
    'Category5': ['Language', 6],
    'Category6': ['AgroLive', 4]
}
populate1 = {
    #Broad Domains: Prefrences,Weight
    'Technical1': ['Computer',26],
    'Technical2': ['Mechanical',23],
    'Technical3': ['Electronics',18],
    'Technical4': ['Civil',16],
    'Technical5': ['Electrical',12],
    'Technical6': ['InfoTech',5]
}

populate2 = {
    'Medical1': ['Nursing',34],
    'Medical2': ['Pharmacy',31],
    'Medical3': ['Dentistry',11],
    'Medical4': ['Ayurveda',9],
    'Medical5': ['Homeopathy',6],
    'Medical6': ['Physiotherapy',8],
    'Medical7': ['Unani',1]
}

populate3 = {
    'SocialScience1': ['PoliticalScience',24],
    'SocialScience2': ['Sociology',23],
    'SocialScience3': ['History',21],
    'SocialScience4': ['Economics',15],
    'SocialScience5': ['Geography',8],
    'SocialScience6': ['Psychology',6],
    'SocialScience7': ['PublicAdmin',3]
}

populate4 = {
    'Management1': ['BusinessAdmin',94],
    'Management2': ['BusinessMgmt',3],
    'Management3': ['MarketingMgmt',1],
    'Management4': ['Technology',1],
    'Management5': ['FinancialMgmt',1],
    'Management6': ['HRMgmt',1]
}

populate5 = {
    'Language1': ['Hindi',29],
    'Language2': ['Bengali',7],
    'Language3': ['Urdu',5],
    'Language4': ['Sanskrit',5],
    'Language5': ['Tamil',3],
    'Language6': ['Telugu',3],
    'Language7': ['Punjabi',1],
    'Language8': ['Kannada',1],
    'Language9': ['Odiya',1],
    'Language10': ['Malayalam',1],
    'Language11': ['English',44],
    'Language12': ['French',1],
    'Language13': ['German',1],
    'Language14': ['Spanish',1]
}

populate6 = {
    'AgroLive1': ['Agriculture',74],
    'AgroLive2': ['Horticulture',11],
    'AgroLive3': ['Forestry',3],
    'AgroLive4': ['Sericulture',1],
    'AgroLive5': ['Veterinary',10],
    'AgroLive6': ['DairyScience',1],
}

columns = ['Stud_ID','Category','Pref1','Pref2','Pref3','PIN']

df = pd.DataFrame(columns=columns)

#Populating Broad categories
for i in range(100):
    cat_list = [cat for cat in populate]
    weights = [populate[cat][1] for cat in populate]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate[cat][0]
    df.loc[i] = [i,broad_cat,"NA","NA","NA","NA"]
#------------------------Populating Technical----------------------
#Populating Pref 1
for i in range(100):
    cat_list = [cat for cat in populate1]
    weights = [populate1[cat][1] for cat in populate1]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate1[cat][0]

    
    if (df['Category'][i]=='Technical'):
        df['Pref1'].loc[i] = broad_cat


#Populating Pref 2
for i in range(100):
    cat_list = [cat for cat in populate1]
    weights = [populate1[cat][1] for cat in populate1]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate1[cat][0]

    
    if (df['Category'][i]=='Technical'):
        if(broad_cat != df['Pref1'][i]):
           df['Pref2'].loc[i] = broad_cat
        elif(broad_cat == df['Pref1'][i]):
            broad_cat1 = broad_cat
            while(broad_cat1==df['Pref1'][i]):
                cat_list1 = [cat1 for cat1 in populate1]
                weights1 = [populate1[cat1][1] for cat1 in populate1]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate1[cat1][0]
            df['Pref2'].loc[i] = broad_cat1 
        
#Populating Pref 3
for i in range(100):
    cat_list = [cat for cat in populate1]
    weights = [populate1[cat][1] for cat in populate1]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate1[cat][0]

    
    if (df['Category'][i]=='Technical'):
        if((broad_cat != df['Pref1'][i]) and (broad_cat != df['Pref2'][i])):
           df['Pref3'].loc[i] = broad_cat
        elif((broad_cat == df['Pref1'][i])or(broad_cat == df['Pref2'][i])):
            broad_cat1 = broad_cat
            while((broad_cat1==df['Pref1'][i])or(broad_cat1 == df['Pref2'][i])):
                cat_list1 = [cat1 for cat1 in populate1]
                weights1 = [populate1[cat1][1] for cat1 in populate1]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate1[cat1][0]
            df['Pref3'].loc[i] = broad_cat1 


#-------------------------Populating Medical----------------------

#Populating Pref 1
for i in range(100):
    cat_list = [cat for cat in populate2]
    weights = [populate2[cat][1] for cat in populate2]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate2[cat][0]

    
    if (df['Category'][i]=='Medical'):
        df['Pref1'].loc[i] = broad_cat


#Populating Pref 2
for i in range(100):
    cat_list = [cat for cat in populate2]
    weights = [populate2[cat][1] for cat in populate2]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate2[cat][0]

    
    if (df['Category'][i]=='Medical'):
        if(broad_cat != df['Pref1'][i]):
           df['Pref2'].loc[i] = broad_cat
        elif(broad_cat == df['Pref1'][i]):
            broad_cat1 = broad_cat
            while(broad_cat1==df['Pref1'][i]):
                cat_list1 = [cat1 for cat1 in populate2]
                weights1 = [populate2[cat1][1] for cat1 in populate2]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate2[cat1][0]
            df['Pref2'].loc[i] = broad_cat1 
        
#Populating Pref 3
for i in range(100):
    cat_list = [cat for cat in populate2]
    weights = [populate2[cat][1] for cat in populate2]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate2[cat][0]

    
    if (df['Category'][i]=='Medical'):
        if((broad_cat != df['Pref1'][i]) and (broad_cat != df['Pref2'][i])):
           df['Pref3'].loc[i] = broad_cat
        elif((broad_cat == df['Pref1'][i])or(broad_cat == df['Pref2'][i])):
            broad_cat1 = broad_cat
            while((broad_cat1==df['Pref1'][i])or(broad_cat1 == df['Pref2'][i])):
                cat_list1 = [cat1 for cat1 in populate2]
                weights1 = [populate2[cat1][1] for cat1 in populate2]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate2[cat1][0]
            df['Pref3'].loc[i] = broad_cat1 



#-------------------------Populating SSC----------------------

#Populating Pref 1
for i in range(100):
    cat_list = [cat for cat in populate3]
    weights = [populate3[cat][1] for cat in populate3]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate3[cat][0]

    
    if (df['Category'][i]=='SocialScience'):
        df['Pref1'].loc[i] = broad_cat


#Populating Pref 2
for i in range(100):
    cat_list = [cat for cat in populate3]
    weights = [populate3[cat][1] for cat in populate3]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate3[cat][0]

    
    if (df['Category'][i]=='SocialScience'):
        if(broad_cat != df['Pref1'][i]):
           df['Pref2'].loc[i] = broad_cat
        elif(broad_cat == df['Pref1'][i]):
            broad_cat1 = broad_cat
            while(broad_cat1==df['Pref1'][i]):
                cat_list1 = [cat1 for cat1 in populate3]
                weights1 = [populate3[cat1][1] for cat1 in populate3]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate3[cat1][0]
            df['Pref2'].loc[i] = broad_cat1 
        
#Populating Pref 3
for i in range(100):
    cat_list = [cat for cat in populate3]
    weights = [populate3[cat][1] for cat in populate3]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate3[cat][0]

    
    if (df['Category'][i]=='SocialScience'):
        if((broad_cat != df['Pref1'][i]) and (broad_cat != df['Pref2'][i])):
           df['Pref3'].loc[i] = broad_cat
        elif((broad_cat == df['Pref1'][i])or(broad_cat == df['Pref2'][i])):
            broad_cat1 = broad_cat
            while((broad_cat1==df['Pref1'][i])or(broad_cat1 == df['Pref2'][i])):
                cat_list1 = [cat1 for cat1 in populate3]
                weights1 = [populate3[cat1][1] for cat1 in populate3]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate3[cat1][0]
            df['Pref3'].loc[i] = broad_cat1 



#-------------------------Populating Management----------------------


#Populating Pref 1
for i in range(100):
    cat_list = [cat for cat in populate4]
    weights = [populate4[cat][1] for cat in populate4]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate4[cat][0]

    
    if (df['Category'][i]=='Management'):
        df['Pref1'].loc[i] = broad_cat


#Populating Pref 2
for i in range(100):
    cat_list = [cat for cat in populate4]
    weights = [populate4[cat][1] for cat in populate4]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate4[cat][0]

    
    if (df['Category'][i]=='Management'):
        if(broad_cat != df['Pref1'][i]):
           df['Pref2'].loc[i] = broad_cat
        elif(broad_cat == df['Pref1'][i]):
            broad_cat1 = broad_cat
            while(broad_cat1==df['Pref1'][i]):
                cat_list1 = [cat1 for cat1 in populate4]
                weights1 = [populate4[cat1][1] for cat1 in populate4]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate4[cat1][0]
            df['Pref2'].loc[i] = broad_cat1 
        
#Populating Pref 3
for i in range(100):
    cat_list = [cat for cat in populate4]
    weights = [populate4[cat][1] for cat in populate4]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate4[cat][0]

    
    if (df['Category'][i]=='Management'):
        if((broad_cat != df['Pref1'][i]) and (broad_cat != df['Pref2'][i])):
           df['Pref3'].loc[i] = broad_cat
        elif((broad_cat == df['Pref1'][i])or(broad_cat == df['Pref2'][i])):
            broad_cat1 = broad_cat
            while((broad_cat1==df['Pref1'][i])or(broad_cat1 == df['Pref2'][i])):
                cat_list1 = [cat1 for cat1 in populate4]
                weights1 = [populate4[cat1][1] for cat1 in populate4]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate4[cat1][0]
            df['Pref3'].loc[i] = broad_cat1 



#-------------------------Populating Language----------------------


#Populating Pref 1
for i in range(100):
    cat_list = [cat for cat in populate5]
    weights = [populate5[cat][1] for cat in populate5]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate5[cat][0]

    
    if (df['Category'][i]=='Language'):
        df['Pref1'].loc[i] = broad_cat


#Populating Pref 2
for i in range(100):
    cat_list = [cat for cat in populate5]
    weights = [populate5[cat][1] for cat in populate5]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate5[cat][0]

    
    if (df['Category'][i]=='Language'):
        if(broad_cat != df['Pref1'][i]):
           df['Pref2'].loc[i] = broad_cat
        elif(broad_cat == df['Pref1'][i]):
            broad_cat1 = broad_cat
            while(broad_cat1==df['Pref1'][i]):
                cat_list1 = [cat1 for cat1 in populate5]
                weights1 = [populate5[cat1][1] for cat1 in populate5]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate5[cat1][0]
            df['Pref2'].loc[i] = broad_cat1 
        
#Populating Pref 3
for i in range(100):
    cat_list = [cat for cat in populate5]
    weights = [populate5[cat][1] for cat in populate5]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate5[cat][0]

    
    if (df['Category'][i]=='Language'):
        if((broad_cat != df['Pref1'][i]) and (broad_cat != df['Pref2'][i])):
           df['Pref3'].loc[i] = broad_cat
        elif((broad_cat == df['Pref1'][i])or(broad_cat == df['Pref2'][i])):
            broad_cat1 = broad_cat
            while((broad_cat1==df['Pref1'][i])or(broad_cat1 == df['Pref2'][i])):
                cat_list1 = [cat1 for cat1 in populate5]
                weights1 = [populate5[cat1][1] for cat1 in populate5]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate5[cat1][0]
            df['Pref3'].loc[i] = broad_cat1 



#-------------------------Populating Agriculture----------------------


#Populating Pref 1
for i in range(100):
    cat_list = [cat for cat in populate6]
    weights = [populate6[cat][1] for cat in populate6]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate6[cat][0]

    
    if (df['Category'][i]=='AgroLive'):
        df['Pref1'].loc[i] = broad_cat


#Populating Pref 2
for i in range(100):
    cat_list = [cat for cat in populate6]
    weights = [populate6[cat][1] for cat in populate6]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate6[cat][0]

    
    if (df['Category'][i]=='AgroLive'):
        if(broad_cat != df['Pref1'][i]):
           df['Pref2'].loc[i] = broad_cat
        elif(broad_cat == df['Pref1'][i]):
            broad_cat1 = broad_cat
            while(broad_cat1==df['Pref1'][i]):
                cat_list1 = [cat1 for cat1 in populate6]
                weights1 = [populate6[cat1][1] for cat1 in populate6]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate6[cat1][0]
            df['Pref2'].loc[i] = broad_cat1 
        
#Populating Pref 3
for i in range(100):
    cat_list = [cat for cat in populate6]
    weights = [populate6[cat][1] for cat in populate6]

    cat = random.choices(cat_list, weights=weights)[0]
    broad_cat = populate6[cat][0]

    
    if (df['Category'][i]=='AgroLive'):
        if((broad_cat != df['Pref1'][i]) and (broad_cat != df['Pref2'][i])):
           df['Pref3'].loc[i] = broad_cat
        elif((broad_cat == df['Pref1'][i])or(broad_cat == df['Pref2'][i])):
            broad_cat1 = broad_cat
            while((broad_cat1==df['Pref1'][i])or(broad_cat1 == df['Pref2'][i])):
                cat_list1 = [cat1 for cat1 in populate6]
                weights1 = [populate6[cat1][1] for cat1 in populate6]

                cat1 = random.choices(cat_list1, weights=weights1)[0]
                broad_cat1 = populate6[cat1][0]
            df['Pref3'].loc[i] = broad_cat1 


pinc = [400049,440021,400027,400070,400036,400065,400001,444601,414301,400065,400065,400062,400065,400065,415519,400010,400027,400003,400003,400066,423502,400033,415726,400069,400051,400060,400093,400028,400058,400039,444806,400018,400037,400015,400018,400070,400012,400008,400001,400002,400028,400064,400025,400066,400001,400012,400070,400019,400007,442705,422108,444126,425127,400013,400078,400049,400037,400022,400065,416707,416320,415705,425303,400021,441903,400005,400070,400010,400008,400060,413409,400028,400028,400088,400068,400057,401301,400060]
for i in range(100):
    res = random.choice(pinc)
    df['PIN'].loc[i] = res

df.to_csv('test_data9.csv')
#print (df['Category'][0])

#for j in range(10):
#    df['PIN'].loc[j] = 1

print (df)