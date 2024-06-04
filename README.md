# automatic_mail_sender

## Description
This tool allows you to **automatically send mails via gmail** when you provide it with a mailing list as a json file.  
Once a mail has been sent, it will be **deleted from the mailing list**, I suggest you to make a copy of it and use it instead of the official mailing list you provided.  
You can interrupt the script at any time, the mailing list will be **updated** each time a mail has been used.

## Tools needed

Python3.12  
A json file ordered like this :
```json
{
    "company_mail" : "company_name",
    }
```

## Installation

1. In your terminal :
```bash
python3 -m venv venv
source venv/bin/activate
pip freeze > requirements.txt
```
2. You will need to [Create a gmail password for an app](https://myaccount.google.com/apppasswords) so that your computer will be allowed to connect to the gmail server without other authorization but the one you provided. **KEEP THIS PASSWORD SECRET AT ALL COST.**

3. Create .env in the root folder and add :
```
APP_PASSWORD=your newly created password  
LOGIN=your mail address
```  

4. -In the body of the message in main.py:  
-Change all "XXXXXX" with your personal data.

5. -Insert in "Documents" the attachments you want to use and be sure to correctly insert their path at line 62 and 63. 
 
6. -Be sure to correctly insert the json path at line 18 and 103.

## How to use it

```bash
python3 main.py
```
## Contributing

Instructions for contributing to your project.

Fork the repository  
Create a new branch (git checkout -b feature-branch)  
Commit your changes (git commit -m 'Add some feature')  
Push to the branch (git push origin feature-branch)  
Open a pull request