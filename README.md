# cloud-computing-finale
Alexis, Nate, Suhas 


Games on April 7th

## Using Dagster

Gameplan

- Create example job
- Work through tutorial

## For setting up and connecting to front end EC2 

- port = 8050
- `chmod 600 /Users/alexiskaldany/school/cloud-dash.pem`
- ```
   ssh -i "/Users/alexiskaldany/school/cloud-dash.pem" ubuntu@54.208.41.106
   cd cloud-computing-finale
   source venv/bin/activate
   python3 Cloud_dash.py
   ```

- `sudo apt-get update`
- `sudo apt install python3-pip`
- `sudo apt install ruby`
- `sudo pip install virtualenv`
- `git clone https://github.com/alexiskaldany/cloud-computing-finale.git`
- `cd cloud-computing-finale`
- `sudo apt install python3.8-venv`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

### To run app
- `python3 app.py`

link will be the IP of the EC2 with :8050
- `http://54.208.41.106:8050`






- `pip install wget`
- `wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install`
- 'chmod +x ./install`
- `sudo ./install auto`
- `sudo service codedeploy-agent start `

### IAM user
`
### In local terminal
Copy github creds

- scp -i "/Users/alexiskaldany/school/cloud-dash.pem" "/Users/alexiskaldany/.ssh/id_ed25519" ubuntu@54.208.41.106:~/
- `scp -i "/Users/alexiskaldany/school/cloud-dash.pem" -r "/Users/alexiskaldany/school/cloud-computing-finale/" ubuntu@54.208.41.106:cloud-computing-finale/`

