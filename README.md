# How much the coin
-------------------
Get cryptocurrencies exchange rates from https://ru.cryptonator.com/api/ 
and update rates each 10 seconds.


## Requirements
- Docker
- Docker Compose
- Fabric3 for development (see fabfile.py)


## Development
- Clone project
- Run `docker-compose up` or use fabric command `fab start`
- Run `docker-compose exec web python3 manage.py runserver 0.0.0.0:8000` or `fab runserver`
- To shutdown docker run `docker-compose down` or `fab stop`


## Production
- Follow the first step outlined above
- Run `docker-compose -f docker-compose.prod.yml up --build -d`
- Run `docker-compose -f docker-compose.prod.yml exec web python3 manage.py migrate`
- Run `docker-compose -f docker-compose.prod.yml exec web python3 manage.py collectstatic`
- Visit website


## TO-DO:
- Move to Bootstrap4
