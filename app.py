from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def uni_lister():
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

    return json.dumps(uni_names)


if __name__ == "__main__":
	app.run()

