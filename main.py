# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, render_template, request
from google.cloud import translate
from settings import PROJECT_ID

app = Flask(__name__)
TRANSLATE = translate.TranslationServiceClient()
PARENT = 'projects/{}/locations/global'.format(PROJECT_ID)
SOURCE, TARGET = 'en', 'es'

@app.route('/', methods=['GET', 'POST'])
def translate(http_request=None):
    """
    main handler - show form and/or perform translation
    """

    # reset all variables (GET)
    orig = trans = {}
    text = translated = None

    # Flask Request object passed in for Cloud Functions
    if http_request:
        request = http_request

    # if there is data to process (POST)
    if request.method == 'POST':
        text = request.form['text']
        data = {
            'contents': [text],
            'parent': PARENT,
            'target_language_code': TARGET,
        }
        # handle older call for backwards-compatibility
        try:
            rsp = TRANSLATE.translate_text(request=data)
        except TypeError:
            rsp = TRANSLATE.translate_text(**data)
        translated = rsp.translations[0].translated_text

    # create context & render template
    context = {
        'orig':  {'text': text, 'lc': SOURCE},
        'trans': {'text': translated, 'lc': TARGET},
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    import os
    app.run(debug=True, threaded=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
