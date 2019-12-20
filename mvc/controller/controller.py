import sys
sys.path.append('..')
from model import model

def register(name,email,password):
    return model.register(name,email,password)