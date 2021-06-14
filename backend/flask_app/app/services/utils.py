import os
import base64
from flask import current_app
import flask_app.app.database.dao.imageDao as dao


def save_file(file_data, f_name, f_ext):
    file_fn = f_name + f_ext
    file_path = os.path.join(current_app.root_path, 'static/uploads', file_fn)

    with open(file_path, 'wb') as fd:
        fd.write(base64.b64decode(file_data))
    # if f_ext == '.pdf':
    #     print('pdf')
    #     buffer = file_data.stream._file
    #     buffer.seek(0,os.SEEK_END)
        
    #     with open(file_path, 'wb') as fd:
    #         fd.write(buffer.getvalue())
        
    # else:


    return file_path, file_fn

