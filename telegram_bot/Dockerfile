FROM python:3.9.16

# Копируем файлы из текущего контекста сборки в контейнер
COPY . .

# Устанавливаем зависимости из файла requirements.txt
RUN pip install pyTelegramBotAPI==4.12.0

CMD python main.py

# 1. 

# Введите:
# docker run ID input.txt
# Чтобы передать список аргументов 