# BrowserGabriel
ChatGPT на любом кирпиче

![Screenshot 2023-04-10 at 18 14 53](https://user-images.githubusercontent.com/90187830/230930495-2f86037b-9eac-4586-a18c-937e9452eec4.png)

## Установка:
```
pip3 install revChatGPT==4.0.3
git clone https://github.com/egor835/BrowserGabriel
cd BrowserGabriel
sudo chmod 777 start.sh
sudo chmod 777 cgi-bin/chat.py
nano token
```
Прописываем свой openAI токен, сохраняем ctrl+x y.

## Запуск:
```
./start.sh
```
Вводим в браузере http://localhost:8000/cgi-bin/chat.py и радуемся.
