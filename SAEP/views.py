# Local packages
from core import app


from resources import index

app.route('/')(index.index)
