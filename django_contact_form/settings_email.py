"""
Using settings inheritance to separate the Email Configurations from the basic Django settings
It's not necessary to have the settings in a separate file
"""

from .settings import *

"""
This configuration is for using Google's mail server.
If you are using other mail server, change the corresponding values
"""

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "gmail@email.com"
EMAIL_HOST_PASSWORD = "gmail password"
EMAIL_PORT = 587
EMAIL_RECEIVER = "mail@receiver"
