# Run the Application

From the terminal, tell Flask where to find your application, then run it in development mode.

Development mode shows an interactive debugger whenever a page raises an exception, and restarts the server whenever you make changes to the code. You can leave it running and just reload the browser page.

## For Linux and Mac

```
$ export FLASK_APP=jogoteca
$ export FLASK_ENV=development
$ export DEBUG=True
$ flask run

```

## For Windows PowerShell, use `$env`: instead of `export`:

```
> $env:FLASK_APP = "jogoteca"
> $env:FLASK_ENV = "development"
> $env:FLASK_DEBUG = "True"
> flask run

```

You'll see output similar to this:

```
* Serving Flask app "jogoteca"
* Environment: development
* Debug mode: on
* Running on <http://127.0.0.1:5000/> (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761

```

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in a browser. Congratulations, you're now running your Flask web aplication!