# -*- coding: utf-8 -*-
import os

from app import MicroserviceMain

app = MicroserviceMain.create_app(os.getenv('PROFILE', 'prod'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
