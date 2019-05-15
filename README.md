# stay-in-touch
Vilnius School of AI (Class D Project)

## About
App helps to Stay in touch with hundreds of people. To Have Great Relationships, Always Make the First Move. The meaning is simple: if you can help the relationship, then do it. This app just does that, helps you keep strong and healthy relations. 

### Usage: 

Simply add people you want to keep in touch into the following lists, and system will remind you to contact them on the right dates by sending email.

**A list**: Very important people. Contact every three weeks (21 days).

**B list**: Important people. Contact every two months (60 days). 

**C list**: Most people. Contact every six months (180 days). 

**D list**: Demoted people. Contact once a year, to make sure you still have their correct info. (365 days)


### Installation: 

Do following before runinig, the system:

1. Open run.py file in your code editor, set your email where you will receive notifications to: 

`receiver_email = 'your_email@domain.com'`

2. Register on https://sendgrid.com/ & create receive SECRET API KEY

3. Setup Environment Variables for Sendgrid. 

**MAC**

```
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

**Windows**

`setx SENDGRID_API_KEY "YOUR_API_KEY"`

### Dependencies
* [sendgrid](https://github.com/sendgrid/sendgrid-python)

