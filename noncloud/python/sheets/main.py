# Copyright 2022 Google LLC
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

from flask import Flask, render_template
import google.auth
from googleapiclient import discovery

app = Flask(__name__)

# Use service account; can switch to OAuth client ID if desired
CREDS, _PROJECT_ID = google.auth.default()
SHEETS = discovery.build('sheets', 'v4', credentials=CREDS)

# Quickstart Sheet: developers.google.com/sheets/api/quickstart/python
SHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'


@app.route('/')
def students(_req=None):
    """
    read spreadsheet data and render in template
    """

    # read data from Google Sheet
    rows = SHEETS.spreadsheets().values().get(
            spreadsheetId=SHEET_ID,
            range='Class Data',
            fields='values'
    ).execute().get('values', ['(no data)'])

    # create context & render template
    context = {'headers': rows[0], 'students': rows[1:]}
    return render_template('index.html', **context)


if __name__ == '__main__':
    import os
    app.run(debug=True, threaded=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
