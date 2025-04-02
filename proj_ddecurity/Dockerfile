FROM node:14

RUN useradd -m appuser

WORKDIR /app

COPY ..

RUN chown -R appuser:appuser /app

USER appuser

CMD ["node", "app.js"]
