# Tomi - Google App Engine - Python Boilerplate

## Setup (Linux (Debian))

* Download the Google App Engine SDK for Python

    * Downloads page:

      https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python

    * Linux download link (version: 1.9.38)

      https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.38.zip

* Install the Google App Engine SDK

  * Unzip SDK

        unzip google_appengine_1.9.38.zip

  * Add SDK to path

        export PATH=$PATH:/path/to/google_appengine/

      OR (to make it permanent)

        echo 'export PATH=$PATH:/path/to/google_appengine/' >> ~/.profile

        source ~/.profile

  * Check for Python installation

        /usr/bin/env python -V

      * If not installed, intstall Python 2.7.X

### Get Project Source code

* Clone the git repository

      git clone <repo url>

## Run local development environment

    dev_appserver.py gae_python_boilerplate

## Deploy to App Engine

    appcfg.py -A [YOUR_PROJECT_ID] -V v1 update ./gae_python_boilerplate

  * Visit http://[YOUR_PROJECT_ID].appspot.com/

  * Add custom domain in google app engine console