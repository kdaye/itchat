FROM python:3.7.2-alpine3.8
RUN apk add --no-cache tzdata \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone
ADD ./src /job
WORKDIR /job
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev python-lxml py-pip build-base libxml2 \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies
CMD ["python", "/job/weixin.py"]
