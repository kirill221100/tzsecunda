создайте .env файл на подобии .env.example

запустить приложение: docker compose --env-file .env up --build -d

добавить тестовые данные в бд: docker exec -i db psql -d secunda3 -U postgres < tz-dump2.sql