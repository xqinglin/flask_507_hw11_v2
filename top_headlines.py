import datetime
from flask import Flask, render_template, url_for
import  requests

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'


@app.route('/user/<nm>')
def hello_name(nm):
    section = 'technology'
    current = datetime.datetime.now().hour
    if current < 12:
        str_greet = 'Good morning'
    elif current<16:
        str_greet = 'Good afternoon'
    elif current <20:
        str_greet ='Good evening'
    else:
        str_greet= 'Good night'
    list_res = find_top_article(section)
    return render_template('user.html', name=nm, list_res=list_res,str_greet=str_greet)

@app.route('/user/<nm>/<section>')
def hello_name_section(nm, section):
    current = datetime.datetime.now().hour
    # print('time', current.hour, type(current.hour))
    str_greet = ''
    if current < 12:
        str_greet = 'Good morning'
    elif current<16:
        str_greet = 'Good afternoon'
    elif current <20:
        str_greet ='Good evening'
    else:
        str_greet= 'Good night'
    list_res = find_top_article(section)
    return render_template('user.html', name=nm, list_res=list_res,section=section ,str_greet=str_greet)

def find_top_article(section):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/{}.json'.format(section)
    print(base_url)
    params = { 'api-key': "dffca63f6deb4c019567247bbd8c1b41",
               'section': section
               }
    results = requests.get(base_url, params).json()['results']
    # print(results)
    res = []
    count = 0
    print('='*10)
    for i in results:
        # if i['section'] == "Technology":
        #     print(i)
        title = i['title']
        url_cur = i['url']
        tech = i['section']
        if tech.lower() == section.lower() and count<5:
            # res_cur = title+' ({})'.format(url_cur)+'---{}'.format(tech)
            res_cur = title + ' ({})'.format(url_cur)
            res.append(res_cur)
            count += 1
    count = 0
    if len(res) == 0:
        for i in results:
            title = i['title']
            url_cur = i['url']
            if count<5:
                res_cur = title + ' ({})'.format(url_cur)
                res.append(res_cur)
                count += 1
    return res
    # rhy_words = []
    # for r in results:
    #     rhy_words.append(r['word'])
    # return render_template('list.html')
if __name__ == '__main__':
    print('start the app', app.name)
    app.run(debug = True)




