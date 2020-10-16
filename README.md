# [hello.salamatov.org](https://hello.salamatov.org/)

Hello! Here we build small web-site based on Django telling about me, my profession and providing an opportunity for download my CV.

## Installation

You'll need [Python >3.8](https://www.python.org/downloads/) be installed.

1. Clone the repo

```bash
git clone https://github.com/s-salamatov/hello.git
```

2. Create new virtual environment and install required packages

```bash
cd hello
mkdir media
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Apply migrations and create superuser

```bash
python manage.py migrate
python manage.py creratesuperuser
```

4. Finally, run dev server

```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
