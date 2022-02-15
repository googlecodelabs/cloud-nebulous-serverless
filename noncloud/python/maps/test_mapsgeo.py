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

from contextlib import contextmanager

from flask import template_rendered
import pytest

from main import ADDRESS, app as flask_app
BAD_ADDR = '1 ave 90000'
MLT_ADDR = 'york'  # (1-10), 'springfield' (1-10), 'dakota' (1-2)


@pytest.fixture
def app():
    """
    fixture connecting Flask app
    """
    yield flask_app


@contextmanager
def captured_templates(app):
    """
    capture template render requests
    """
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_mapsgeo_get(app):
    """
    test GET request to main application
    """
    with captured_templates(app) as templates:
        rv = app.test_client().get('/')
        assert rv.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'index.html'
        assert len(context['address']) > 1 and len(context['results']) == 0


def test_mapsgeo_post(app):
    """
    test POST request to main application
    """
    with captured_templates(app) as templates:
        rv = app.test_client().post('/', data={'address': ADDRESS})
        assert rv.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert 'address' in context and 'results' in context
        assert '37.422388, -122.0841883' == context['results'][0]['latlong']


def test_mapsgeo_post_fail(app):
    """
    test POST request to main application
    """
    with captured_templates(app) as templates:
        rv = app.test_client().post('/', data={'address': BAD_ADDR})
        assert rv.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'index.html'
        assert 'address' in context and 'results' in context
        assert len(context['results']) == 0


def test_mapsgeo_post_sometimes_multi(app):
    """
    test POST request to main application
    """
    with captured_templates(app) as templates:
        rv = app.test_client().post('/', data={'address': MLT_ADDR})
        assert rv.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert 'address' in context and 'results' in context
        assert len(context['results']) >= 1
