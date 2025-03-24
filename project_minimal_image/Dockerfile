FROM alpine

# Set working directory
WORKDIR /

# Copy the shell script into the container
COPY counter.sh /counter.sh

# Make sure the script is executable
RUN chmod +x /counter.sh

# Run the script
CMD ["/bin/sh", "/counter.sh"]
