import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "arb_app:app",
        host='0.0.0.0',
        port=8000,
        reload=True
    )



# http://94.103.94.219:8000

# cd /home/profit_finder/api/ProfitFinder/server/fast_api/
# uvicorn main:app --reload --host 0.0.0.0 
# OR
# python3 api/ProfitFinder/server/fast_api/server_fastapi.py 


# https://www.uvicorn.org/deployment/#gunicorn