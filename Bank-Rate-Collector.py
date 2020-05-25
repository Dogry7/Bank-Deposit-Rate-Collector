############################################################################
#   AUTHOR: RYAN CLEMINSON
#   PROJECT: 
#   DATE OF CREATION: 27/02/2020
############################################################################

# https://www.westpac.com.au/personal-banking/bank-accounts/term-deposit/rates/?fid=iwg:act_drop2_nav:per:tdr
# https://www.westpac.com.au/business-banking/savings-accounts/term-deposits/business-term-deposit-rates/?fid=iwg:act_drop2_nav:bus:tdr
# https://www.commbank.com.au/banking/term-deposits/rates-and-fees.html
# https://www.anz.com.au/personal/bank-accounts/term-deposits/anz-term-deposit/
# https://www.nab.com.au/personal/interest-rates-fees-and-charges/indicator-rates-selected-term-deposit-products
# https://docs.python.org/3/library/html.parser.html
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/


import webbrowser, sys
import requests
import pandas as pd

############################################################################
#   FUNCTION: SECONDARY MAIN LINE
############################################################################
def main():

    WESTPAC_DOMAIN = "https://www.westpac.com.au/personal-banking/bank-accounts/term-deposit/rates/?fid=iwg:act_drop2_nav:per:tdr"
    COMMONWEALTH_DOMAIN = "https://www.commbank.com.au/banking/term-deposits/rates-and-fees.html"
    ANZ_DOMAIN = "https://www.anz.com.au/personal/bank-accounts/term-deposits/anz-term-deposit/"
    NAB_DOMAIN = "https://www.nab.com.au/personal/interest-rates-fees-and-charges/indicator-rates-selected-term-deposit-products"

    webbrowser.open(WESTPAC_DOMAIN)
    res = requests.get(WESTPAC_DOMAIN)



    term=[] #List to store name of the product
    interest_p_a=[] #List to store price of the product
    interest_p_m=[] #List to store rating of the product
    

    driver.get(WESTPAC_DOMAIN)
    content = driver.page_source
    soup = BeautifulSoup(content)
    print('HI')
    for index in soup.findAll('a',href=True, attrs={'class':'tabcordion-body'}):
        name=a.find('div', attrs={'class':'[[Rates#TD|Term Deposit - 5000~1.5000~1.dispclass{none}]]'})
        # price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        # rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
        term.append(name.text)
        # prices.append(price.text)
        # ratings.append(rating.text) 
        print(term)
        print("hi")
    return

def collect_westpac():
    pass

    return

def collect_commonwealth():
    
    pass
    return

def collect_ANZ():
    
    pass
    return

def collect_NAB():


    pass
    return



############################################################################
#   FUNCTION: MAIN LINE
############################################################################
main()