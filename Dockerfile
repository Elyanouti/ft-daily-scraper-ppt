FROM node:20-bullseye

# تثبيت Python و pip و الأدوات الأساسية
RUN apt-get update && \
    apt-get install -y python3 python3-pip git curl && \
    apt-get clean

# إعداد مجلد المشروع
WORKDIR /home/node/project

# نسخ سكريبتات المشروع
COPY . /home/node/project

# تثبيت مكتبات Python المطلوبة
RUN python3 -m pip install --no-cache-dir feedparser python-pptx ollama httpx

# تثبيت n8n عالميًا
RUN npm install -g n8n

# فتح بورت n8n
EXPOSE 5678

# تشغيل n8n بشكل افتراضي
CMD ["n8n"]
