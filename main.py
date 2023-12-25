# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from WebScraper import WebScraper  # Ensure this points to your WebScraper class

class Config(BaseModel):
    url: str
    match: str
    selector: str
    maxPagesToCrawl: int
    outputFileName: str

app = FastAPI()

@app.post("/start_scraping/")
async def start_scraping(config: Config):
    try:
        # Initialize the scraper with the provided configuration
        scraper = WebScraper(config.dict())
        # Start the scraping process
        await scraper.scrape()
        return {"message": "Scraping started successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)