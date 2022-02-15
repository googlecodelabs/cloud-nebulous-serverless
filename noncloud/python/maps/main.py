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

from flask import Flask, render_template, request
import googlemaps
from settings import API_KEY

app = Flask(__name__)
GMAPS = googlemaps.Client(key=API_KEY)
ADDRESS = '1600 Amphitheatre Pkwy 94043'


@app.route('/', methods=['GET', 'POST'])
def mapsgeo(gcf_request=None):
    """
    main handler - show form and possibly previous translation
    """

    # Flask Request object passed in for Cloud Functions
    # (use gcf_request for GCF but flask.request otherwise)
    local_request = gcf_request if gcf_request else request

    # reset all variables (GET)
    address = ADDRESS
    results = []

    # form submission and if there is data to process (POST)
    if local_request.method == 'POST':
        address = local_request.form['address'].strip()
        if not address:
            address = ADDRESS
        rsp = GMAPS.geocode(address)
        if rsp:
            for data in rsp:
                if 'geometry' in data and 'location' in data['geometry']:
                    geocode = data['geometry']['location']
                    results.append({
                        'full_addr': data['formatted_address'],
                        'latlong': '%s, %s' % (geocode['lat'], geocode['lng']),
                    })

    # create context & render template
    context = {'address': address, 'results': results}
    return render_template('index.html', **context)


if __name__ == '__main__':
    import os
    app.run(debug=True, threaded=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
