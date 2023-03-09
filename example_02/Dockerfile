FROM python

ADD . /python

WORKDIR /python

ENTRYPOINT ["python", "main.py", "t_input.txt", "t_output"]


# 1. 

# Проверка
# docker build -t test 

# 2.

# docker run -it -v /tmp/python/:/python/data test t_input.txt data/t_output.txt
# Твой main.py будет принимать входные данные от /python/data.txt и записать выходные данные в /python/data/output.txt
# Поскольку /python/data смонтирован в /tmp/python/, вы получите output.txt в /tmp/python/ в вашем локальном