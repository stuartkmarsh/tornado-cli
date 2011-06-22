tornado-cli -- a command line helper for Tornado apps
===============================================================================

## Description

Tornado-cli is a command line tool for Tornado.    

## Dependancies

[Tornado](http://www.tornadoweb.org)

Although it's required for the cli, you need it to run the resulting Tornado application

## Instructions

There is currently only a single command:

startproject

Usage:

<pre><code>tcli startproject project_name</code></pre>

or

<pre><code>tornado-cli startproject project_name</code></pre>

This creates a project directory called project_name, and creates a file
structure for the project.  The output is from [tornado-boilerplate](https://github.com/beardygeek/tornado-boilerplate).

Then cd into the project directory and run:

<pre><code>python ./app.py</code></pre>