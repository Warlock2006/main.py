from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous">
     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    <title>Отбор астронавтов</title>
</head>
<body>
<h1 align="center">Загрузка фотографии</h1>
<h2 align="center">для участия в миссии</h2>
<form method="post" class="login_form" enctype="multipart/form-data">
    <div class="form-group">
        <label for="photo">Приложите фотографию</label>
        <input type="file" class="form-control-file" id="photo" name="file">
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
</body>
</html>'''
    elif request.method == 'POST':
        file = request.files['file'].read()
        tail = request.files['file'].filename.split('.')[-1]

        with open(f'static/img/img.{tail}', 'wb') as f:
            f.write(file)
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous">
     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    <title>Отбор астронавтов</title>
</head>
<body>
<h1 align="center">Загрузка фотографии</h1>
<h2 align="center">для участия в миссии</h2>
<form method="post" class="login_form" enctype="multipart/form-data">
    <div class="form-group">
        <label for="photo">Приложите фотографию</label>
        <input type="file" class="form-control-file" id="photo" name="file">
    </div>
    <img src="{url_for('static', filename=f'img/img.{tail}')}" alt="Загрузите ваше фото">
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
