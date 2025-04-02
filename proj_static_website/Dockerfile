FROM nginx:latest

# Set working directory
WORKDIR /usr/share/nginx/html

# Remove default index.html
RUN rm -rf /usr/share/nginx/html/*

# Copy project files
COPY . .

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
