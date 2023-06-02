import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "13750040"))
    API_HASH = os.environ.get("API_HASH", "6553ea819bb17098b0e3c62530823328")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6201289396:AAHWjTcrly9Fl7AwpKn-zO6rsXCiHk1IDuc")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5842877813")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://spymusicbot:spymusicbot@cluster0.ulbp5cy.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQAKRhig3GJTT-Y4zRXR0LKjCM4GZ2fWJ5q4MHUuOTGi18_N6YW7Wr3KD2CPULXCxEDyVsXmI1zp2BNbDuvfGudnaU-5WksRriwsEHttY7kr8ua1fgFelNv-e_o6ut4mV1Aw__FQ3R__BOPrvwJX8leU7XmeUU5SactdMyG7-Y-EK89t3vUtjFYr3D8PFNqGOOl-LGhkBZuHJchHPsoQpz4XmbjiHUWUP9dH6YOsDrw109GtHUVo6HOSl-4hfhk6-dGzjqhFO53KaI78DGTTgmToRE3FnrinS2jw1F3zvJ6mJhvuxrveuJImcGokyefgYyHpShVwnawRgQNwGPcpWNC-AAAAAXUZulgA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001617102994"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "bulk_edit_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
