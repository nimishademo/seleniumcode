import requests
import json # Import the json module
import pandas as pd

url = "https://api.hpxindia.com/api/getGDAMDataMarkSnap/w?deliveryperiod=Today&flag=web&fromdate=&frommonth=&fromweek=&interval=15-Minute+Block&todate=&tomonth=&toweek=&years="

payload = {}
headers = {
  'Cookie': 'AlteonP=AVcLIHq1qMA16e82dJnPYg$$'
}

response = requests.get(url, headers=headers, data=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response into a Python dictionary
    data = response.json() # Use .json() method directly

    # Now you can access the 'table' key
    if "table" in data:
        table_data = data["table"]
        # print(table_data)
    else:
        print("The 'table' key was not found in the response.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text) # Print the raw response text for debugging

df = pd.DataFrame(data = table_data)
df.to_excel('hpx.xlsx')
print(df)