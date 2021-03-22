import requests
import json
dataSet = []

url = 'https://universities.hipolabs.com/search?name='

def readUrl(search):
    results = requests.get(url+search)
    print("Status Code: ", results.status_code)
    print("Headers: Content-Type: ", results.headers['Content-Type'])
    # print("Headers: ", results.headers)
    return results.json()

if __name__=="__main__":
    jsonResult = readUrl('Wales')
    # print(jsonResult)
    for university in jsonResult:
        name = university['name']
        url = university['web_pages'][0]
        dataSet.append([name,url])

    print("Total Universities Found: ",len(dataSet))
    print(dataSet)

'''
Status Code:  200
Headers: Content-Type:  application/json
Total Universities Found:  10
[['University of Wales', 'https://www.wales.ac.uk/'],
 ['University of Wales Institute, Cardiff', 'https://www.uwic.ac.uk/'], 
 ['University of Wales College of Medicine', 'https://www.uwcm.ac.uk/'], 
 ['Johnson & Wales University', 'https://www.jwu.edu/'], 
 ['University of New South Wales', 'https://www.unsw.edu.au/'], 
 ['University of Wales, Newport', 'https://www.newport.ac.uk/'], 
 ['University of Wales, Swansea', 'https://www.swan.ac.uk/'], 
 ['University of Wales, Aberystwyth', 'https://www.aber.ac.uk/'], 
 ['University of Wales, Lampeter', 'https://www.lamp.ac.uk/'],
  ['University of Wales, Bangor', 'https://www.bangor.ac.uk/']]
'''
