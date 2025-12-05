#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' 

echo -e "${GREEN}>>> Stopping old containers...${NC}"
docker compose down

echo -e "${GREEN}>>> Nuking database volume (Starting fresh)...${NC}"
docker volume rm ticketmaster_postgres_data || true  

echo -e "${GREEN}>>> Building and Starting...${NC}"
docker compose up --build -d

echo -e "${GREEN}>>> Waiting for Database to be ready...${NC}"
sleep 5  

echo -e "${GREEN}>>> Seeding Database (1 Venue (50 capacity), 1 Event, 100 Users)...${NC}"
docker exec -it ticketmaster-api-1 python -m app.seed

echo -e "${GREEN}>>> Running Load Test (K6) (booking 100 users on the same event)...${NC}"
docker run --rm -i \
  --network ticketmaster_default \
  grafana/k6 run - < tests/script.js

echo -e "${GREEN}>>> Verifying Booking Count...${NC}"
docker exec -it ticketmaster-db-1 psql -U admin -d ticketmaster -c "SELECT count(*) FROM bookings;"