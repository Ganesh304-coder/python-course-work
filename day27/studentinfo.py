import json

with open("data.json","r") as file:
    data =json.load(file)

data["Username"]= "Ganesh"
data["Skills"].append("python")

with open("data.json","w") as file:
    json.dump(data,file,indent=4)