from flask import Blueprint

test_page = Blueprint('test_page',__name__)
@test_page.route('/')

def show():
  return 'Hello'
