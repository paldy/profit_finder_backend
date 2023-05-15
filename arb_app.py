from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Literal, List, Union

# http://94.103.94.219:8000/docs
# http://94.103.94.219:8000

# Import my modules for building requests to every trade place
import request_binance_p2p
import request_binance_main
import request_sbr

# Constants. Here you can add issue you need
PLACES = ('BncP2P', 'BncMain', 'CBRF')
FIATS = ('RUB', 'USD', 'EUR', 'CHF', 'TRY')
ASSETS = ('USDT', 'BTC', 'ETH', 'SHIB', 'USD')
PLACES_FOR_REQUESTS = {
        'BncP2P':  request_binance_p2p.bnb_request,
        'BncMain': request_binance_main.bnb_main_request,
        'CBRF':    request_sbr.sbr_request
     }

# Constant for building trade pair
PERMITS_for_PAIRS = (*ASSETS, *FIATS)


# For validation in POST
class ReqRates(BaseModel):
    place: Literal[PLACES]
    fiat: Literal[FIATS]
    asset: Literal[ASSETS]
    tradeType: Literal['SELL', 'BUY']


# Creates data for requests and execute them, returns response data
def controller(input_data):
    return PLACES_FOR_REQUESTS.get(input_data.place)(input_data)


# Routs
app = FastAPI(title="Profit Finder")

@app.get("/")
async def root():
    return {"Error": "Method Not Allowed. But take it easy man :) "}


@app.post("/")
async def create_item_post(asked_rates: ReqRates):
    input_data = ReqRates.parse_obj(asked_rates)
    req_body = controller(input_data)
    return {"At this stage": req_body}


@app.get("/rates")
async def read_user_item(
                            place: Literal[PLACES], 
                            pair: Union[List[Literal[PERMITS_for_PAIRS]], None] = Query(default=[])
                        ):

    if len(pair) != 2: 
        item = {'Error': f'I need 2 items for building trades pair. I have got {len(pair)} ones.'}
    else:
        item = {
            "place": place, 
            "pair": pair
        }
    return {"At this stage": item}











