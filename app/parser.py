# This whole parsing file is a MEGA HACK!

import urllib2
from magicdate import magicdate
from datetime import date
from bs4 import BeautifulSoup


def earnings_reports_on_date(date_object=date.today()):

    date_string = str(date_object.year) + str(date_object.month).zfill(2) + str(date_object.day).zfill(2)
    url_string = 'http://biz.yahoo.com/research/earncal/' + date_string + '.html'

    print url_string

    try:
        page = urllib2.urlopen(url_string)
        soup = BeautifulSoup(page, 'html.parser')
    except Exception, e:
        print e
        return []

    output_list = []

    rows = soup.find_all('tr')

    for row in rows:

        tmp_dict = {}
        cells = row.find_all('td')

        if len(cells) >= 4:  # number of columns per row
            try:
                tmp_dict['name'] = cells[0].string
                tmp_dict['link'] = cells[1].find('a')['href']
                tmp_dict['ticker'] = cells[1].find('a').string
                tmp_dict['eps_estimate'] = cells[2].string
                tmp_dict['time_released'] = cells[3].string

                # Check if it is a valid ticker
                if (len(tmp_dict['name']) == 0) or (len(tmp_dict['ticker']) == 0) or (' ' in tmp_dict['ticker']):
                    # Invalid record, skip it.
                    continue
                else:
                    output_list.append(tmp_dict)
            except Exception, e:
                continue
    return output_list


def earnings_report_date_for_symbol(symbol):

    url_string = 'http://biz.yahoo.com/rr/?s=' + symbol + '&d=research%2Fearncal'

    print url_string

    try:
        page = urllib2.urlopen(url_string)
        soup = BeautifulSoup(page, 'html.parser')
    except Exception, e:
        print e
        return None

    date_element = soup.find_all("font", attrs={'face': 'arial', 'size': '+1'})[0]
    date_text = date_element.find('b').string.replace('\n', ' ')

    sanitized_date_text = date_text.replace('US Earnings Calendar for ', '')

    output_date = str(magicdate(sanitized_date_text))

    return output_date
