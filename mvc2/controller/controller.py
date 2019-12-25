import sys
sys.path.append('..')
from model import model

def register(name,email,password):
    return model.register(name,email,password)

def login(email,password):
    return model.login(email,password) 