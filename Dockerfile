FROM python:3.7.2-alpine3.8
RUN apk add --no-cache tzdata \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone
ADD ./src /job
WORKDIR /job
RUN pip install -r requirements.txt
CMD ["python", "/job/weixin.py"]
