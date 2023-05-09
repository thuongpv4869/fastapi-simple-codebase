# FastAPI simple codebase

## Guide
prepare .env file like `.env_example, app/.env_example`  
1. Build image
```bash
docker-compose build
```
2. Run migrate db
```bash
docker-compose run api ./scripts/migrate.sh
```
3. Fake data
```bash
docker-compose run api ./scripts/fake_data.sh
```
4. Run server
```bash
docker-compose up
```
*api docs: http://localhost:8000/docs*

