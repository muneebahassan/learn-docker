# stage 1: build the site
FROM nginx:alpine AS builder
COPY index.html /usr/share/nginx/html/

# stage 2: final image
FROM alpine:3.15
RUN apk add --no-cache nginx
COPY --from=builder /usr/share/nginx/html/ /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
