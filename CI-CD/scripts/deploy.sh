# CI-CD/scripts/deploy.sh
#!/bin/bash

echo "Starting deployment..."

# Pull latest code
git pull origin main

# Restart application
docker-compose up --build -d

echo "Deployment complete!"
