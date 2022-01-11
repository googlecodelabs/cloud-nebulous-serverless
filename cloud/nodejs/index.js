// Copyright 2021 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

const express = require('express');
const nunjucks = require('nunjucks');
const {TranslationServiceClient} = require('@google-cloud/translate');

const app = express();
app.use(express.urlencoded({extended: true}));
nunjucks.configure('templates', {autoescape: true, express: app});
const TRANSLATE = new TranslationServiceClient();

const PORT = process.env.PORT || 8080;
const SOURCE = ['en', 'English'];
const TARGET = ['es', 'Spanish'];
let parent;
TRANSLATE.getProjectId().then(result => {
    parent = `projects/${result}`;
});


if (!process.env.FUNCTION_TARGET) {
    app.listen(PORT, () =>
        console.log(`Listening on port ${PORT}`)
    );
}

/**
 * main handler - show form and possibly previous translation
 */
async function translate(req, rsp) {
    // reset all variables (GET/POST)
    let text = null;
    let translated = null;

    // form submission and if there is data to process (POST)
    if (req.method === 'POST') {
        text = req.body.text.trim();
        if (text) {
            const data = {
                contents: [text],
                parent: parent,
                targetLanguageCode: TARGET[0]
            };
            const [response] = await TRANSLATE.translateText(data);
            translated = response.translations[0].translatedText;
        }
    }

    // create context & render template
    const context = {
        orig:  {text: text, lc: SOURCE},
        trans: {text: translated, lc: TARGET}
    };
    rsp.render('index.html', context);
}

app.all('/', translate);
module.exports = {
    app
};
