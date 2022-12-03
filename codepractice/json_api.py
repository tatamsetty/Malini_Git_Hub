import json
from urllib.request import urlopen

with urlopen("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json") as response:
    source = response.read()
data = json.loads(source)
#print(json.dumps(data, indent=2))

dataseries=list()
temp=dict()

for item in data['dataseries']:  
    
    temp['timepoint']=item['timepoint']
    temp['Cloudcover']= item['cloudcover'],
    temp['Seeing']= item['seeing'],
    temp['transparency']= item['transparency'],
    temp['rh2m']= item['rh2m'],
    temp['lifted_index']= item['lifted_index']
    
    dataseries.append({
        'timepoint':item['timepoint'],
        'Cloudcover': item['cloudcover'],
        'Seeing': item['seeing'],
        'transparency': item['transparency'],
        'rh2m': item['rh2m'],
        'lifted_index': item['lifted_index']
    })     
    
with open('C:/Malini/Precision/codepractice/Weather_forecasts.json', 'w') as f:
  json.dump(dataseries, f, indent=2)



