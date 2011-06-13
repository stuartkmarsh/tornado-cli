tornado-boilerplate -- a standard layout for Tornado apps
===============================================================================

## Description

tornado-boilerplate is an attempt to set up an convention for
[Tornado](http://www.tornadoweb.org/) app layouts, to assist in writing
utilities to deploy such applications. A bit of convention can go a long way.

This app layout is the one assumed by [buedafab](https://github.com/bueda/ops). 

## Instructions

* Clone this repository
* cd into the repo directory
* At the command line type:
<pre><code>python ./app.py</code></pre>
* Visit http://localhost:8888 in your browser

### Related Projects

[buedafab](https://github.com/bueda/ops)
[django-boilerplate](https://github.com/bueda/django-boilerplate)
[python-webapp-etc](https://github.com/bueda/python-webapp-etc)
[comrade](https://github.com/bueda/django-comrade)

## Acknowledgements

The folks at Mozilla working on the [next version of AMO](https://github.com/jbalogh/zamboni)
were the primary inspiration for this layout.

## Directory Structure

    tornado-boilerplate/
        handlers/
            welcome.py
            base.py     
        logconfig/
        media/             
        templates/  
        environment.py  
        app.py
        settings.py

### handlers

All of your Tornado RequestHandlers go in this directory.

Everything in this directory is added to the `PYTHONPATH` when the
`environment.py` file is imported.        

### logconfig

An extended version of the
[log_settings](https://github.com/jbalogh/zamboni/blob/master/log_settings.py)
module from Mozilla's [zamboni](https://github.com/jbalogh/zamboni).

This package includes an `initialize_logging` method meant to be called from the
project's `settings.py` that sets Python's logging system. The default for
server deployments is to log to syslog, and the default for solo development is
simply to log to the console. 

All of your loggers should be children of your app's root logger (defined in
`settings.py`). This works well at the top of every file that needs logging:

    import logging
    logger = logging.getLogger('five.' + __name__)

### media

Sub directories for media (css, images etc) can be placed in here.            

### templates

Project-wide templates (i.e. those not belonging to any specific app in the
`handlers/` folder). The boilerplate includes a `welcome.html` template.  
    
#### environment.py

Modifies the `PYTHONPATH` to allow importing from the `apps/`, `lib/` and
`vendor/` directories. This module is imported at the top of `settings.py` to
make sure it runs for both local development (using Django's built-in server)
and in production (run through mod-wsgi, gunicorn, etc.).   

#### app.py

The main Tornado application, and also a runnable file that starts the Tornado 
server.

#### settings.py

A place to collect application settings ala Django. There's undoubtedly a better
way to do this, considering all of the flak Django is taking lately for this
global configuration. For now, it works.

## Contributing

If you have improvements or bug fixes:

* Fork the repository on GitHub
* File an issue for the bug fix/feature request in GitHub
* Create a topic branch
* Push your modifications to that branch
* Send a pull request

## Authors

* [Bueda Inc.](http://www.bueda.com)
* Christopher Peplin, peplin@bueda.com, @[peplin](http://twitter.com/peplin) 
* Modifications by Stuart Marsh, http://www.beardygeek.com
