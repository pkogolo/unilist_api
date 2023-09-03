#This program grabs data from an api website that publishes
#the list of all universities in a every country then 
#accummulate the number of universities in a country e.g Nigeria
#then publishes the names of the universities in a seperate array
#used the len() to get the cummulative number of published university
#used the enumerate() to iterate over tyhe university list tracking the 
#their index(numbers) and the element(university name)
#Then print the universities serially in alphabetic order
from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def unilist():
    uni_url = "http://universities.hipolabs.com/search?country=Nigeria"

        #Also define a file path to write the output
        #path = "c:\\Users\\kogos\\OneDrive\\Desktop\\Python\\NGN_Universities.txt"

    data = requests.get(uni_url)
    uni_data = data.content

        #use jason.loads() to parse the JSON and store in uni_list
    uni_list = json.loads(uni_data)

    uni_accumulator = len(uni_list) #populate the counter
    print("The Number Of Universities Published in Nigeria is:", uni_accumulator)

        # Create an empty array to store university names
    uni_names = []

        #This loops generate serial numbers and append tem to the
        #corresponding univeristy names on the list
    for uni_num, uni in enumerate(uni_list, start=1):
            names = uni["name"] #the variable "name" is used in each uni dictionary
            numbered_names = f"{uni_num}.{names}"
            uni_names.append(numbered_names)
            for serial_names in uni_names:
                print(serial_names)
    return json.dumps(uni_names)

        # with open(path, "w") as file: #open file outside the loop prevents overwrite  
        #     for serial_names in uni_names:
        #         print(serial_names)
        #         file.write(serial_names + "\n")

if __name__ == "__main__":
# 	#app.run()
   app.run(host="0.0.0", port=7000)



