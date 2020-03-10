#!/usr/bin/python3
from lxml import html
import requests

page = requests.get('https://www.tff.org/Default.aspx?pageId=30&kisiId=1330123')
#print(page.content)
tree = html.fromstring(page.content)


"""dene =
//*[@id="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_grdTakimlar_ctl01"]/tbody/tr[1]/td[2]
print (tree)"""
sozlesme_bitis = tree.xpath('//*[@id="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_grdTakimlar_ctl01"]/tbody/tr[1]/td[3]/text()')
sozlesme_baslangic = tree.xpath('//*[@id="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_grdTakimlar_ctl01"]/tbody/tr[1]/td[2]/text()')
lisans_turu = tree.xpath('//*[@id="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_grdTakimlar_ctl01"]/tbody/tr[1]/td[4]/text()')

print ('SÖZLEŞME BAŞLANGIÇ: ', sozlesme_baslangic, 'SÖZLEŞME BİTİŞ:', sozlesme_bitis, 'LİSANS TÜRÜ:', lisans_turu)