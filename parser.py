import urllib2
from datetime import date
from bs4 import BeautifulSoup

def earnings_reports_on_date(date_object=date.today()):

    date_string = str(date_object.year) + str(date_object.month).zfill(2) + str(date_object.day).zfill(2)
    url_sting = 'http://biz.yahoo.com/research/earncal/' + date_string + '.html'

    print '\n'
    print url_sting
    print '\n'

    try:
        page = urllib2.urlopen(url_sting)
        soup = BeautifulSoup(page, 'html.parser')
    except Exception:
        return []

    output_list = []

    rows = soup.find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 6:  # number of columns per row
            tmp_dict = {'name': cells[0].string,
                        'link': cells[1].find('a')['href'],
                        'ticker': cells[1].find('a').string,
                        'eps_estimate': cells[2].string,
                        'time_released': cells[3].string
                        }
            output_list.append(tmp_dict)
    return output_list

def earnings_report_date_for_symbol(symbol=""):
    return None
