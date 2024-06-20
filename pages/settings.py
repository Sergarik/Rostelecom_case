"""Действующие данные для авторизации в системе"""
import os
from dotenv import load_dotenv
from faker import Faker
import string
load_dotenv()


"""Фейковые данные для авторизации в системе"""
fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
fake = Faker()
fake_password = fake.password()
fake_login = fake.user_name()
fake_email = fake.email()


valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')
valid_password = os.getenv('valid_password')
invalid_ls = '596017152855'

valid_email = os.getenv('valid_email')
valid_pass_reg = '#@&Subarik199'


def generate_string_rus(n):
    return 'б' * n


def generate_string_en(n):
    return 'x' * n


def english_chars():
    return 'abcdefghijklmnopqrstuvwxyz'


def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
    return '样你么会说人我在有个中他这为们大来以英语'
    # китайские иероглифы

def special_chars():
    return f'{string.punctuation}'