How to install PostgreSQL on Ubuntu

sudo apt update
sudo apt install postgresql
sudo apt install postgresql-contrib
sudo apt install pgadmin4

команды сервиса: 
service postgresql 

вход: 
sudo -i -u postgres

консоль: 
psql

\l список баз данных 
\q выход из консоли
\du список пользователей 

Создание базы данных: 
createdb db_name

Удаление базы данных: 
dropdb db_name

Изменение пароля пользователя в консоли:
ALTER USER postgres WITH PASSWORD 'qwerty';

Создание пользователя: 
CREATE USER username WITH PASSWORD 'password';

Права супер пользователя: 
ALTER USER username WITH SUPERUSER;

Удаление пользователя:
DROP USER username;
