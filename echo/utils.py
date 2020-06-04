from random import choice

from telegram import ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize

from clarifai.rest import ClarifaiApp

from echo.config import EMOJI_LIST, CLARIFAI_API_KEY


def get_user_emoji(user_data):
    if 'smile' in user_data:
        return user_data['smile']
    else:
        user_data['smile'] = emojize(choice(EMOJI_LIST), use_aliases=True)
        return user_data['smile']

def get_keyboard():
    contact_button = KeyboardButton('Send contacts', request_contact=True)
    location_button = KeyboardButton('Send coordinates', request_location=True)
    test_keyboard = ReplyKeyboardMarkup([
        ['Random cat', 'Change avatar'],
        [contact_button, location_button]],
        resize_keyboard=True)
    return test_keyboard

def is_cat(file_name):
    image_has_cat = False
    app = ClarifaiApp(api_key=CLARIFAI_API_KEY)
    model = app.public_models.general_model
    response = model.predict_by_filename(file_name, max_concepts=5)
    if response['status'] == 10000:
        for concept in response['outputs'][0]['data']['concepts']:
            if concept['name'] == 'cat':
                image_has_cat = True
    return image_has_cat

if __name__ == '__main__':
    print(is_cat('cat1.jpg'))