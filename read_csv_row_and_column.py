import csv


with open("/home/ajay/Documents/Oodles_projects/Hey_kaido/kaido-web-app/kaido/gift_data.csv","r") as f:
    csvobject=csv.reader(f)
    # data=csvobject.readlines()
    row=0
    listcsvData=list(csvobject)
    # print(listcsvData)
    column=len(listcsvData[0])

    print("column",column)
    for i in listcsvData:
        # print(i)
        row+=1
    print("row",row)
   
