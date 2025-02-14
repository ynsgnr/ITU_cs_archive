from bottle import request, route, run
from os import environ
from time import asctime, localtime


def htmlify(content):
    page = """
      <!DOCTYPE html>
      <html>
        <head>
          <title>Date and Time</title>
          <meta charset="utf-8" />
        </head>
        <body>
    """ + content + """
        </body>
      </html>
    """
    return page


def time_page():
    area = request.POST.get('area')
    city = request.POST.get('city')
    environ['TZ'] = area + '/' + city
    current_time = localtime()
    content = '<p>The current time in ' + city + ' is: ' + \
              asctime(current_time) + '</p>\n'
    content = content + '<hr />\n'
    content = content + '<p>Go to the <a href="/">home page</a>.</p>\n'
    return htmlify(content)


def home_page():
    content = """
      <p>Show me the time in:</p>
      <form action="/time" method="POST">
        Area:
          <input type="radio" name="area" value="Africa" /> Africa
          <input type="radio" name="area" value="America" /> America
          <input type="radio" name="area" value="Asia" /> Asia
          <input type="radio" name="area" value="Europe" /> Europe
          <input type="radio" name="area" value="Pacific" /> Pacific<br />
        City: <input type="text" name="city" /><br />
        <input type="submit" value="Show" />
      </form>
    """
    return htmlify(content)


route('/time', 'POST', time_page)
route('/', 'GET', home_page)

run()
