import os
import sys
if sys.platform == 'wn64':
    pybabel = 'D:\\blog\\pybabel'
else:
    pybabel = 'flask/bin/pybabel'
os.system(pybabel + ' compile -d app/translations')