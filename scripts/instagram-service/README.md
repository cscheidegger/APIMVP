
# Proteus.lab Instagram Integration Service

This service connects to Instagram's API to fetch and process posts from the @proteus.lab account for display in the main application.

## Overview

The Instagram Integration Service runs as a standalone microservice that:

1. Periodically fetches recent posts from the @proteus.lab Instagram account
2. Processes images and metadata (captions, hashtags, etc.)
3. Categorizes content based on hashtags or predefined rules
4. Stores processed data in the main application database via API calls
5. Uses caching to reduce API calls and improve performance

## Features

- **Scheduled Fetching**: Automatically refreshes content at configurable intervals
- **Error Handling**: Handles API limitations and errors gracefully
- **Caching**: Uses Redis to cache responses and avoid rate limiting
- **Metadata Processing**: Extracts useful information from posts (hashtags, project types)
- **API Integration**: Communicates with the main backend via REST API

## Configuration

The service is configured via environment variables:

```
INSTAGRAM_REFRESH_INTERVAL=3600  # Time in seconds between updates
API_URL=http://api:8000/api      # URL of the main API
REDIS_URL=redis://redis:6379/0   # Redis connection string for caching
```

## Installation

### Prerequisites
- Python 3.10+
- Redis (for caching)
- Network access to Instagram API
- Network access to the main Proteus.lab API

### Using Docker

The service is containerized for easy deployment:

```bash
docker build -t proteuslab-instagram-service .
docker run -d --name instagram-service \
  -e INSTAGRAM_REFRESH_INTERVAL=3600 \
  -e API_URL=http://api:8000/api \
  proteuslab-instagram-service
```

## Technical Implementation

The service is built on Python and uses:

1. **Requests**: For API calls to Instagram and the main backend
2. **Redis**: For caching Instagram responses
3. **Scheduled tasks**: For regular updates without manual intervention

### API Endpoints (Internal)

- `GET /feed`: Fetches the latest processed Instagram posts
- `GET /refresh`: Manually triggers a refresh of Instagram data

## Integration Flow

```
┌─────────────────┐     ┌───────────────┐     ┌────────────────┐
│                 │     │               │     │                │
│  Instagram API  │────▶│ This Service  │────▶│  Main Backend  │
│                 │     │               │     │                │
└─────────────────┘     └───────────────┘     └────────────────┘
```

1. Service requests posts from Instagram API
2. Instagram returns post data
3. Service processes and categorizes data
4. Service sends processed data to main backend API
5. Frontend displays posts from the main backend

## Development

To run the service locally for development:

```bash
# Set up Python environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the service
python instagram_feed.py
```
