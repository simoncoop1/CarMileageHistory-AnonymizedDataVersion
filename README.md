# CarMileageHistory-AnonymizedDataVersion
Chart Car Mileage History from Anonymized Data

The problem with my ukcarmileagehistory project is the mot data site does not play well with external scripts and is constantly changing. This project aims to recreate the project, but using anonymized MOT data.

## Data Required to run this project
You will need to obtain all the MOT results from https://data.gov.uk/dataset/e3939ef8-30c7-4ca8-9c7c-ad9475cc9b2f/anonymised-mot-tests-and-results  
Then you can run

```python3 data-extract.py```  

data-extract.py should be in the same folder as the data.

## Query MOT data

You need a MOT mileage from 2005-2019, the data of that MOT, and the date the vehicle was first registered. All available by entering a registration number on https://www.gov.uk/check-mot-history
```
python3 generator.py {regdate_motdate_motmileage} {regdate_motdate_motmileage} {regdate_motdate_motmileage}
```

## MOT Data Questions  
This script ask some set questions about the data and then proceeds to calculate an answer.
```
python3 dataQs.py -question1
```
calculated the answer to question1.  
```
python3 dataQs.py
```
For a list of questions.
