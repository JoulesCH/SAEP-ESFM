# Installed packages
from flask import render_template, request, redirect, make_response

# Local packages
from utils import debug
import models as m


def index(): return render_template('index.html')
