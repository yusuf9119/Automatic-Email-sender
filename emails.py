import os
import requests
from random import choice
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


rover_url = "#enter url here"
sg = SendGridAPIClient("#api client key here")

def send_mars_email(to_email,from_email,img_url):
    message = Mail(from_email = from_email,
                   to_email = to_email,
                   subject = "here is your mars rover photo",
                   html_content ='Thanks for joining this! any questions, email yusufa9119@gmail.com')

def get_mars_photo(sol):
    params = {'sol':sol,'api-key':"oRehpEBW0i0Qk0YKze3yZgDTMG3bWmPyfHCnowUF"}
    resp = requests.get(rover_url,params).json()
    #json converts the json to python

    img_url =choice( resp['photos'])['img_src']

    return img_url
