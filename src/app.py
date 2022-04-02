
# import json
import json
# import csv
import csv
# import flask library
from flask import Flask

# Python program to calculate BMI


#BMI category class for Table 1
class BMI:
    bmi_categoty ={ 'UW' :'Underweight',
                    'NW': 'Normal Weight',
                    'OW': 'Over Weight',
                    'MO': 'Moderately obese',
                    'SO': 'Severly obese',
                    'VSO': 'Very Severly obese',
                   }

    health_risk = {
                    'MR':'Malnutrition Risk',
                    'LR': 'Low Risk',
                    'ER': 'Enhanced Risk',
                    'MRS': 'Medium Risk',
                    'HR': 'High Risk',
                    'VHR': 'Very High Risk',
    }

#Read input json file
def read_json():
    list_of_row = []
    with open('src/input.json') as file:
        alllines = json.load(file)
        for row in alllines:
            list_of_row.append(row)
            #print(row)
        return list_of_row    

def resultdata_with_bmi(alldata):
    line_count = 0
    notValidData = []
    validData = []    
    for row in alldata:
        if line_count == 0:
            line_count = 1
        elif row["Gender"].isalpha() == True and str(row["HeightCm"]).isnumeric() == True and str(row["WeightKg"]).isnumeric() == True :
            bmi = calculate_bmi(row)
            validData.append(list(row.values())+bmi)
            line_count +=1
        else:
            notValidData.append(list(row.values()))
            line_count +=1
    #print('this data is not valid-->',notValidData)
    #print('total_rows-->',line_count)
    return validData

#Calculate BMI
def calculate_bmi(data):
    BMI_categoty= None
    Health_risk= None
    BMI_range = None
    x =int(data["HeightCm"])
    y = int(data["WeightKg"])
    bmi = y/((x/100)**2)
    if bmi <= 18.4 :
        BMI_categoty = BMI.bmi_categoty.get('UW')
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('MR')
    elif bmi >=18.5 and bmi <= 24.9:
        BMI_categoty = BMI.bmi_categoty.get('NW')
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('LR')
    elif bmi >=25 and bmi <= 29.9:
        BMI_categoty = BMI.bmi_categoty.get("OW")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('ER')
    elif bmi >=30 and bmi <= 34.9:
        BMI_categoty = BMI.bmi_categoty.get("MO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('MRS')
    elif bmi >= 35 and bmi <= 39.9:
        BMI_categoty = BMI.bmi_categoty.get("SO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('HR')
    elif bmi > 40:
        BMI_categoty = BMI.bmi_categoty.get("VSO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('VHR')
    bmi_list =[BMI_categoty,BMI_range,Health_risk]
    return bmi_list


def write_csv(data):
    with open('output_for_BMI_Calculator_Height_Weight.csv', 'w',newline='') as file:
        csv_data = csv.writer(file, delimiter=',')
        csv_data.writerow(['Gender', 'Height', 'Weight', 'BMI_categoty', 'BMI_range', 'Health_risk'])
        for row in data:
            # print(row)
            csv_data.writerows([row])
    return 'csv file added successfully..'

app = Flask(__name__)

@app.route("/")
def index():
    contents = read_json()
    #print(contents)
    finaldata = resultdata_with_bmi(contents)
    #print('final data with BMI-->',finaldata)
    #result = write_csv(finaldata)
    #print(result)
    return json.dumps(finaldata)

if __name__ == "__main__":
     app.run()

