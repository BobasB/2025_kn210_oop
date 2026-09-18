# Віртуальні середовища
# Мета робота: гавчитись створювати та працювати з віртуальними середовищами Python.

## Віртуальні середовища
- потрібні для швидкого створення проекту, без відволікань на налаштування середовища та його оновлення
- працюючи в віртуальному середовищі, ви можете встановлювати пакети, які потрібні лише для цього проекту, для цього користуючись менеджером пакетів pip, який втановлює пакети з репозиторію PyPI (Python Package Index)
- якщо ми перестворюємо віртуальне середовище, то всі пакети, які були встановлені в попередньому середовищі, будуть недоступні, тому що вони встановлені в іншому місці і миможемо використати requirements.txt для швидкого встановлення всіх необхідних пакетів
```bash
pip freeze > requirements.txt

##  в новому середовищі
python -m venv ./my_env && source my_env/bin/activate && pip install -r requirements.txt

python anime.py
deactivate 
```
- попросили АІ дописати роботу з Базою даних, реззультат можна побачити запустивши код
```bash
python anime.py
```
## Віртуальні середовища з Pipenv
```
python -m venv ./my_env
source ./my_env/bin/activate
```
- встановлюємо пакети для розробки та тестування
```bash
pip install flake8
pip install mypy
pip list
pip freeze > requirements-dev.txt
pip install -r requirements.txt
pip list
deactivate
```
- створюємо віртуальне середовище з Pipenv, який автоматично створює та керує віртуальними середовищами для ваших проектів, а також додає та видаляє пакети з файлу Pipfile як ви їх встановлюєте або видаляєте

```bash
cd ../
cd 2_pipenv
pipenv -h
python -V
pipenv --python 3.13
pipenv install jikanpy-v4 Flask
pipenv install flake8 mypy --dev
pipenv graph
```

---
