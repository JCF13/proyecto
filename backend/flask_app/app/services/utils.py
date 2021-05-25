

def save_file(file_data,f_name,f_ext):
    ultima_id = daoFichero.find_last_file()
    print(ultima_id)
    file_fn = f_name + f_ext
    file_path = os.path.join(current_app.root_path, 'static/uploads', file_fn)
    output_size = (125, 125)
    
    print(file_fn)
    print(file_path)
    if f_ext == '.pdf':
        print('pdf')
        buffer = file_data.stream._file
        buffer.seek(0,os.SEEK_END)
        
        with open(file_path, 'wb') as fd:
            fd.write(buffer.getvalue())
        
    else:
        with open(file_path, 'wb') as fd:
            fd.write(base64.b64decode(file_data))


    return file_path, file_fn
