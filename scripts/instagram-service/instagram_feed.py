
#!/usr/bin/env python3
import os
import time
import requests
import schedule
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Configuration
API_URL = os.getenv("API_URL", "http://api:8000/api")
REFRESH_INTERVAL = int(os.getenv("INSTAGRAM_REFRESH_INTERVAL", "3600"))  # Default: hourly

def fetch_instagram_feed():
    """
    Fetch the latest posts from Instagram for @proteus.lab
    This is a mock implementation for MVP - replace with actual Instagram API integration
    """
    logger.info("Fetching Instagram feed for @proteus.lab")
    
    try:
        # Mock data for MVP 
        # In a real implementation, this would use Instagram's API
        instagram_posts = [
            {
                "id": f"post_{int(datetime.now().timestamp())}",
                "image_url": "https://example.com/image1.jpg",
                "caption": "Latest 3D printing project completed! #3DPrinting #ProteusDev",
                "likes": 42,
                "timestamp": datetime.now().isoformat(),
            },
            {
                "id": f"post_{int(datetime.now().timestamp())-100}",
                "image_url": "https://example.com/image2.jpg",
                "caption": "Check out this amazing 3D model! #3DModel #ProteusDev",
                "likes": 38,
                "timestamp": datetime.now().isoformat(),
            }
        ]
        
        # Send the data to the API
        response = requests.post(
            f"{API_URL}/instagram/update",
            json={"posts": instagram_posts},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            logger.info("Successfully updated Instagram feed")
        else:
            logger.error(f"Failed to update Instagram feed: {response.status_code} - {response.text}")
            
    except Exception as e:
        logger.exception(f"Error fetching Instagram feed: {e}")

def main():
    logger.info("Starting Instagram feed service")
    
    # Fetch immediately on startup
    fetch_instagram_feed()
    
    # Schedule regular updates
    schedule.every(REFRESH_INTERVAL).seconds.do(fetch_instagram_feed)
    
    # Keep the service running
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
