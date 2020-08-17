# Financial_Data_Extraction
extracting Data from a messed financial data sheet
# Problem Statement Focus: To check for NLP and Python capability to extract data elements from the financial statement documents.

## Data to be provided – 
•	Training & Development Set - 500 Text files (OCR output of images)
	
### Sample Data to be Extracted
Highlighted text on the image is required to be extracted
                 FLEXI BUSINESS SOLUTIONS LIMITED   
                 
                 Registered number:                                                      06101470
                 Balance Sheet
                 as at 28 February 2019
                                                                                                                         2019                                            2018
                                                                                                                               £                                               £
                 Current assets                                                                 51,700                                          31,061
                 Creditors: amounts falling due within
                 one year                                                                     (55,505)                                        (46,039)
                 Net current liabilities                                                                             (3,805)                                        (14,978)
                 Total assets less current liabilities                                                               (3,805)                                        (14,978)
                 Accruals and deferred income                                                                           (500)                                            (500)
                 Net liabilities                                                                                     (4,305)                                        (15,478)
                 Capital and reserves                                                                                (4,305)                                        (15,478)


                 The company is a private company limited by shares and incorporated in England. Its registered
                 office is Pentax House South Hill Avenue, South Harrow, Harrow, England, HAZ 0DU.
                 The directors are satisfied that the company is entitled to exemption from the requirement to obtain
                 an audit under section 477 of the Companies Act 2006.
                 The members have not required the company to obtain an audit in accordance with section 476 of
                 
                 the Act.
                 
                 The      directors       acknowledge             their    responsibilities          for complying             with    the     requirements           of the
                 
                 Companies Act 2006 with respect to accounting                                records and the preparation of accounts.                                                                                                                           
                 The accounts           have been prepared in accordance with the micro entity provisions of the Companies                                                                                                                          
                 Act 2006 and FRS 105, The Financial Reporting Standard applicable to the Micro-entities Regime.                                                                                                                        
                 The accounts             have been delivered in accordance with the provisions applicable to companies                                                                                                                             
                 subject to the small companies regime. The profit and loss account                                              has not been delivered to the                                                                                                                          
                 Registrar of Companies.                                                                                                                                         
                 Mr Arulkumaran Kandasamy                                                                                                                                         
                 Director                                                                                                                                                                                                                                                                                                         
                 Approved by the board on 30 November 2019                                                                                                                       
                 This document was delivered using electronic communications and authenticated in accordance with the                                                                                                      
                registrar's rules relating to electronic form, authentication and manner of delivery under section 1072 of                                                                                                   
                the Companies Act 2006.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
## Fields to be extracted are:

•	Current Assets : 51,700 -> 51700

•	Creditors: amounts falling due within one year : 55,505 -> 55505

•	Net current liabilities : (3,805) -> 3805

•	Total assets less current liabilities : (3,805) -> 3805

•	Accruals and deferred income : (500) -> -500

•	Net liabilities : (4,305) -> -4305

•	Capital and reserves : (4,305) -> -4305

## Results file entry:
{“Current assets":"51700","Creditors:amounts falling due within one year":"-55505","Net current liabilities":"-3805","Total assets less current liabilities":"-3805","Accurals and deferred income":"-500","Net liabilities":"-4305","Capital and reserves":"-4305"}


# Another Example


                               EARLY MORNING MEDIA LIMITED
                               REGISTERED NUMBER:06719248
                              G -

                               BALANCE SHEET
                               AS AT 31 MARCH 2019                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                          2019                                          2018                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                       Note                                                 £                                            £                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                              Fixed assets
                               Intangible assets                                                        5                                            9,423                                       14,354
                              Tangible assets                                                           6                                            6,414                                         4,948
                                                                                                                                                   15,837                                        19,302
                              Current assets

                              Debtors: amounts falling due within one year                             7                  113,831                                       130,880
                              Cash at bank and in hand                                                 8                  122,352                                         99,193
                                                                                                                          236,183                                       230,073
                              Creditors: amounts falling due within one                                                                                                                     -
                                 year                                                                  9                 {110,924)                                       (82,414)
                              Net current assets                                                                                                 125,259                                       147,659

                              Net assets                                                                                                         141,096                                       166,961
                              Capital and reserves
                              Called up share capital                                                                                              70,587                                        70,587
                              Profit and loss account                                                                                              70,509                                       96,374
                              Shareholders funds                                                                                                 141,096                                       166,961
                                                                                                                                                                                        = =
                              The directors consider that the Company is entitled to exemption from audit under section 477 of the Companies
                              Act 2006 and members have not required the Company to abtain an audit for the year in question in accordance
                              with section 476 of Companies Act 2006,
                              The directors acknowledge their responsibilities for complying with the requirements of the Companies Act 2006
                              with respect to accounting                records and the preparation of financial statements.
                              The financial statements have been prepared in accordance with the provisions applicable to companies subject
                              to the small companies regime and in accordance with the provisions of FRS 102 Section 1A -                                                        small entities.

                              The financial statements have been delivered in accordance with the provisions applicable to companies subject
                              to the small companies regime.

                             The Company has opted not to file the statement of comprehensive income in accordance with provisions
                              applicable to companies subject to the small companies’ regime.
                             
## Fields to be extracted are: 
•	Fixed asset :  15837

•	Intangible assets : 9423

•	Tangible assets : 6414

•	“nan” : 15,837 -> 15837

•	Current Assets : 236,183 -> 236183

•	Debtors: amounts falling due within one year : 113,831 -> 113831

•	Cash at bank and in hand : 122,352 -> 122352

•	Creditors: amounts falling due within one year : (110,924) ->  -110924

•	Net current assets : 125,259 → 125259

•	Net assets : 141,096 → 141096

•	Capital and reserves: -

•	Called up share capital : 70,587 -> 70587

•	Profit and loss accounts 70,509 -> 70509

•	Shareholders funds : 141,096 -> 141096

## Results file entry:

{"nan": "236183", "Current assets": "nan", "Creditors: amounts falling due within one year": "{110924)", "Shareholders funds": "141096", "Intangible assets": "9423", "Fixed assets": "nan", "Net assets": "141096", "Tangible assets": "6414", "Called up share capital": "70587", "Capital and reserves": "nan", "Net current assets": "125259", "Profit and loss account": "70509", "Cash at bank and in hand": "122352", "Debtors: amounts falling due within one year": "113831"}


## Please note, data only for year 2019 is to be extracted.

# How to use this repo?

	1. clone download the repo.
	2. extract it.
	3. install all the dependencies if programm not run.
	4. run the file finalSOLUTION.py 
	other .ipynb files are given for developement purpose
