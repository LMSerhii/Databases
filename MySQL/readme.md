# MySQL 

> Install MySQL on ubuntu / debian
---
#### Если sudo не установлено
```
apt install sudo 
```
#### Качаем ссылку на установочный файл deb и устанавливаем его
```commandline
sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.24-1_all.deb
```
```commandline
sudo dpkg -i mysql....deb
```
### Обновляем пакеты
```commandline
sudo apt update
```
### Устанавливаем mysql-server
```commandline
sudo apt install mysql-server
```
### Установка пакета безопасности
```commandline
sudo mysql_secure_installation
```
##### Заходим из под root
```commandline
sudo mysql 
```
#### Меняем пароль

```
ALTER USER `root`@`localhost` IDENTIFIED 
WITH mysql_native_password BY 'your_password';

```

### Заходим в файл конфига и меняем ip для входа из определенного или любого ip (0.0.0.0)
```
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```
### Системные команды

+ sudo systemctl status mysql

+ sudo systemctl start mysql

+ sudo systemctl enable mysql

+ sudo systemctl stop mysql 


### Удаление 

```
dpkg -l | grep -i mysql
```
```commandline
sudo systemctl stop mysql
```
```commandline
sudo apt purge mysql
```
``` commandline
sudo rm -Rf /var/lib/mysql/
sudo rm -Rf /var/log/mysql
sudo rm -Rf /etc/mysql
```

### Переустановка

```commandline
sudo apt update
sudo apt install -f
sudo apt install mysql-server
sudo apt dist-upgrade
```

### Вход 

```commandline

mysql -u root -p 

```
---
> Work in MySQL
#### Все базы данных
```
SHOW DATABASES;
```
#### Все таблицы
```
SHOW TABLES;
```
#### Создать базу данных

```
CREATE DATABASE db_name;
```
#### Использовать базу данных 

```
USE db_name;
```
#### Удалить базу данных

```
DROP DATABASE db_name;
```
#### Создать пользователя

```
CREATE USER `username`@`ip_address` 
IDENTIFIED BY 'your_password';
```
#### Права суперпользователя ко всем таблицам данной базы данных
 
```
GRANT ALL PRIVILEGES ON db_name.* TO
`username`@`ip_address`;
```
#### Показать всех пользователей

```
SELECT user, host FROM mysql.user;
```
---

> Work in Python: 
```
python3 -m pip install PyMySQL[rsa] 
```