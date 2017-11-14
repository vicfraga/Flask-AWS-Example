from flask import Flask, render_template, flash
from flask_wtf import Form
from flask_wtf.file import FileField
from s3 import s3_upload
from dynamodb import dynamodb_scan, dynamodb_put_item

app = Flask(__name__)
app.config.from_object('config')


class UploadForm(Form):
    example = FileField('Example File')


@app.route('/', methods=['POST', 'GET'])
def upload_page():
    form = UploadForm()
    if form.validate_on_submit():
        item = s3_upload(form.example)
        dynamodb_put_item(item)
        flash('{src} uploaded to S3 as {dst}'.format(src=form.example.data.filename, dst=item["name"]))
    entries = dynamodb_scan()
    return render_template('example.html', form=form, entries=entries)


if __name__ == '__main__':
    app.run()
