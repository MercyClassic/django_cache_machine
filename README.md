**<h2> Startup </h2>**
- **<h3> `git clone https://github.com/MercyClassic/django_cache_machine.git` </h2>**
- **<h3> `cp .env.example .env` </h3>**
- **<h3> `docker compose up --build` </h3>**

**<h2> Usage: </h2>**
- **<h3> Login in admin panel with default credentials (`username=root`, `password=root`) </h3>**
- **<h3> Create several items </h3>**
- **<h3> Send POST request to the /cache_machine endpoint with json data: `{"items":[1, 1, 1, 2, 2]}` to create pdf receipt </h3>**
- - **<h3> You can do it via `postman` or `http://127.0.0.1:8000/swagger` </h3>**
- **<h3> Send GET request to the url in qr_code, you will receive a pdf receipt </h3>**

**<h3> `Note:` If you want to get receipt on your phone,
then send POST request local domain e.g `http://192.168.0.1:8000/cache_machine` to get right link in the qrcode </h3>**

**<h2> Stack </h2>**
- **<h3> Python 3.11 </h3>**
- **<h3> Django, Django rest </h3>**
- **<h3> PostgreSQL </h3>**
- **<h3> reportlab, qrcode </h3>**
- **<h3> Docker </h3>**
