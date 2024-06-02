## **Тестовое задание для Python-программиста: Разработка Telegram-клиента с использованием Telethon**

### _Цель задания: Разработать Telegram-клиент на Python с использованием библиотеки Telethon. Клиент должен иметь веб интерфейс и api с возможностью авторизации по QR-коду, получение и отправку текстовых сообщений._

### **Требования:**
 
1. #### Создайте новое приложение в https://my.telegram.org/ и получите API ID и API HASH.

1. #### Используя библиотеку python Telethon, разработайте web сервис, реализующий следующую функциональность:

   * #### Логин клиента по QR-коду.

   * #### Получение новых текстовых сообщений и их сохранение, разделенное по чатам.

   * #### Возможность отправки текстовых сообщений другим пользователям через клиента.

3. #### Реализуйте базовый веб-API интерфейс с использованием Flask (или любого другого фреймворка на ваш выбор) с методами, описанными ниже. Если будет покрыто тестами - большой плюс.

4. #### При запросе "wild: любой товар", должен запускаться парсинг wildberries с городом Москва и запросом "любой товар", бот должен отправлять 10 наименований товаров со ссылками на них.

5. #### Тестирование клиента можно выполнить с помощью утилиты curl или любого другого инструмент для отправки HTTP-запросов. 

####    _Например, для авторизации:_

`   curl -X POST -H "Content-Type: application/json" -d '{"code": "1234567890"}' http://localhost:5000/auth`

####    _Для отправки текстового сообщения:_

   `curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello, world!", "chat_id": 1234567890}' http://localhost:5000/send`

#### _Для получения новых текстовых сообщений:_

   `curl -X POST -H "Content-Type: application/json" -d '{"chat_id": 1234567890}' http://localhost:5000/get`
   
#### _Для запуска парсинга Wildberries:_

  `curl -X POST -H "Content-Type: application/json" -d '{"city": "Москва", "query": "любой товар"}' http://localhost:5000/wild `
  
#### 6. Запуск клиента

Запустите клиент с помощью команды:

`python app.py`

##### _Клиент будет работать на локальном сервере на порту 5000. Вы можете использовать утилиту curl или любое другое приложение для отправки HTTP-запросов и тестирования функциональности клиента._