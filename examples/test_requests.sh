#!/bin/bash

# Base URL
BASE_URL="http://localhost:3000"

echo "Testing GET /api/users"
curl -X GET "http://localhost:3000/api/users"
echo -e "\n"

echo "Testing POST /api/users"
curl -X POST "$BASE_URL/api/users" \
  -H "Content-Type: application/json" \
  -d '{"name": "New User", "email": "user@example.com"}'
echo -e "\n"

echo "Testing GET /api/users/1"
curl -X GET "$BASE_URL/api/users/1"
echo -e "\n"

echo "Testing GET /not-captured"
curl -X GET "$BASE_URL/not-captured"
echo -e "\n"

# Test with query parameters
echo "Testing GET /api/users with query params"
curl -X GET "$BASE_URL/api/users?page=1&limit=10"
echo -e "\n"

# Test with headers
echo "Testing GET /api/users with custom headers"
curl -X GET "$BASE_URL/api/users" \
  -H "X-Custom-Header: test-value" \
  -H "Authorization: Bearer test-token"
echo -e "\n"