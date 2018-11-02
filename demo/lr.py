from LoginRadius import LoginRadius as LR

# *** FILL IN CREDENTIALS ***
API_KEY = ""
API_SECRET = ""
# ***************************

LR.API_KEY = API_KEY
LR.API_SECRET = API_SECRET
LR.LIBRARY = "requests"
# LR.CUSTOM_DOMAIN = "https://google.com/"
loginradius = LR()