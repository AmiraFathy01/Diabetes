# import libraries
import joblib
# load model:
filename = "Diabetes_model.joblib"
model = joblib.load(filename)
# create function 

def using_model():
    requirements=['age','hba1c','chol','bmi']
    dict_req={}
    predict_arry=[]
    for i in requirements :
        dict_req[i]=float(input(f"please enter your {i}"))
        predict_arry.append(dict_req[i])
    
    result=model.predict([predict_arry])
    
    answer=str(input("  please type \n 1- yes: to continue and get the result. \n 2- try: to try  correct your information again. \n 3- exit : to close the programe.  \n or enter the number of choices 1 or 2 or 3" ))
    print("*******************************************")
    if answer== "yes"or "Yes"or'1':
        if result==0:
            print("  it is good news for you, you don't have  diabetes  ^_^ ")
        elif result==1:
            print("  it is not good  news for you ,you  have  prediabetes .  you need to go to the doctor ")
        elif result==2:
            
            print(" I am sorry for you but  it is bad news  ,you  have the diabetes ,  you need to go to the doctor fastly  ")

    elif answer=="try"or "Try"or'2':
        using_model()
     
    elif answer=="exit"or "Exit"or'3':
        print("Thanks for used my programe ^_^  ")
    else :
        print(" you entered  the wrong answer ")
        answer=str(input("  please type \n 1- yes: to continue and get the result.   \n 2- try: to try  correct your information again. \n 3- exit : to close the programe.  \n or enter the number of choices 1 or 2 or 3" ))
        print("*******************************************")

    return   result 

using_model()
