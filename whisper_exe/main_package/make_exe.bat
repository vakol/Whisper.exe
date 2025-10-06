set PYTHONUTF8=1
pyinstaller --onefile __init__.py --add-data "C:\Users\vacla\AppData\Roaming\Python\Python311\site-packages\whisper\assets;whisper\assets"
echo ALL DONE
pause