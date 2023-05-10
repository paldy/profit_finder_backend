# ProfitFinder
# profit_finder_backend
Back End for ProfitFinder project (FastAPI)


## API:

[http://<IP>:8000]

### /docs

All possible items:
```
PLACES = ('BncP2P', 'BncMain')
FIATS = ('RUB',)
ASSETS = ('USDT', 'BTC')
```

### /rates POST
request:
```[!javascript]
{
  place: 'BncP2P'
  pair: ['RUB', 'BTC']
}
```

response:
```[!javascript]
 {
   place: 'BncP2P',
   pair: ['RUB', 'BTC'],
   lastRate: [52.21, 53.16] 
 }
```

For testing:
```[!javascript]
getResource = async (path, body) => {
    const res = await fetch('http://185.209.29.18:8000',
                body ? {
                    method: 'POST',
                    body: JSON.stringify(body),
                    mode: 'no-cors'
                } : null
                );
    if (!res.ok) {
        throw new Error(`Could not fetch ${path}, received ${res.status}`)
    }
    return await res.json();
}

function test () {
  const body = {
    place: 'BncP2P',
    pair: ['RUB', 'BTC']
  };

  return getResource('/rates/', body);
}

test();
    
```

 ### /retro POST

 request:
 ```[!javascript]
 {
   place: 'BncP2P',
   pair: ['RUB', 'BTC'],
   startDate: '17/03/2022 00:00', // Date format
   endDate: '17/03/2022 01:00' // Date format
 }
 ```

 response:
  ```[!javascript]
 {
   place: 'BncP2P',
   pair: ['RUB', 'BTC'],
   startTimestamp: '14/02/2022 00:00' //Date
   endTimestamp: '14/02/2022 01:00' //Date
   rates_every_minute: [
         {
           rate: ['52.21', '52.78'],
           time: '14/02/2022 00:02' //Date
        },
        ... //objects
      ]
}
```

For testing:
```[!javascript]
getResource = async (path, body) => {
    const res = await fetch('http://185.209.29.18:8000',
                body ? {
                    method: 'POST',
                    body: JSON.stringify(body),
                    mode: 'no-cors'
                } : null
                );
    if (!res.ok) {
        throw new Error(`Could not fetch ${path}, received ${res.status}`)
    }
    return await res.json();
}
function test2 () {
  const body = {
    place: 'BncP2P',
    pair: ['RUB', 'BTC'],
    startDate: '17/03/2022 00:00', // Date format
    endDate: '17/03/2022 01:00' // Date format
  }

  return getResource('/retro/', body);
}
```
