from sqlalchemy import create_engine, Column, Integer, String#, DateTime
from sqlalchemy.orm.session import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


def read_db(tickers: list):

    Base = declarative_base()

    class ApiUrls(Base):
        __tablename__ = "exchs"
        exchange = Column(String, primary_key=True)
        URIforAPI = Column(String)
        BTCUSD = Column(String)
        BTCEUR = Column(String)
        ETHUSD = Column(String)
        USDTRUB = Column(String)
        JSONforparsing = Column(String)

    engine = create_engine('sqlite:////home/profit_finder/api/ProfitFinder/server/fast_api/databases/data.db', 
                            connect_args={"check_same_thread": False}, 
                            echo=True)
    session = sessionmaker(bind=engine)()
    # s = session.execute("select URIforAPI, BTCEUR from 'exchs'")

    print(tickers)
    b = {}
    for tc in tickers:
        c = []
        for ex in session.query(ApiUrls):
            url = ex.URIforAPI.replace('{ticker}', ex.BTCEUR) if ex.BTCEUR else ''
            c.append(url)
        b[tc] = c

    # print(b)
    return b


# {
#     "tickers": ["BTCUSD", "BTCEUR", "ETHUSD", "USDTRUB"] 
# }



# {
#     "BTCUSD": [
#         "https://api.kraken.com/0/public/Ticker?pair=XBTEUR",
#         "https://api.binance.com/api/v3/ticker/price?symbol=BTCEUR",
#         ""
#     ],
#     "BTCEUR": [
#         "https://api.kraken.com/0/public/Ticker?pair=XBTEUR",
#         "https://api.binance.com/api/v3/ticker/price?symbol=BTCEUR",
#         ""
#     ],
#     "ETHUSD": [
#         "https://api.kraken.com/0/public/Ticker?pair=XBTEUR",
#         "https://api.binance.com/api/v3/ticker/price?symbol=BTCEUR",
#         ""
#     ],
#     "USDTRUB": [
#         "https://api.kraken.com/0/public/Ticker?pair=XBTEUR",
#         "https://api.binance.com/api/v3/ticker/price?symbol=BTCEUR",
#         ""
#     ]
# }