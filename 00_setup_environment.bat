pip install virtualenv
python -m venv venv

:: АКТИВАЦИЯ ВИРТУАЛЬНОГО ОКРУЖЕНИЯ

cd %~dp0venv\Scripts
echo [INFO] let's activate.bat VIRTUAL ENVIRONMENT "selenium_env"
call activate

:: УСТАНОВКА БИБЛИОТЕК В ВИРТУАЛЬНОЕ ОКРУЖЕНИЕ
cd ../..
echo [INFO] let's install requirements.txt
pip install -r requirements.txt

:: ДЕАКТИВАЦИЯ ВИРТУАЛЬНОГО ОКРУЖЕНИЯ
echo [INFO] let's deactivate.bat VIRTUAL ENVIRONMENT "selenium_env"
cd %~dp0venv\Scripts
call deactivate

pause