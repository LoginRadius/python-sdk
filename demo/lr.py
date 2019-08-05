from LoginRadius import LoginRadius as LR

# *** FILL IN CREDENTIALS ***
API_KEY = ""
API_SECRET = ""
# ***************************

LR.API_KEY = API_KEY
LR.API_SECRET = API_SECRET
LR.LIBRARY = "requests"
# LR.CUSTOM_DOMAIN = "https://example.com/"
# LR.SERVER_REGION = ""
LR.API_REQUEST_SIGNING = False
loginradius = LR()
