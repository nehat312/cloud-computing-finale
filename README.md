# cloud-computing-finale
Alexis, Nate, Suhas 


Games on April 7th


## For setting up and connecting to front end EC2 

- port = 8050
- `chmod 600 /Users/alexiskaldany/school/cloud-dash.pem`
- `ssh -i "/Users/alexiskaldany/school/cloud-dash.pem" ubuntu@54.208.41.106`

- `sudo apt-get update`

`sudo add-apt-repository universe`

- `sudo apt install python3-pip`
- ` sudo apt install ruby`
- `sudo pip install virtualenv`
- `pip install wget`
- `wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install`
- 'chmod +x ./install`
- `sudo ./install auto`
- `sudo service codedeploy-agent start `



- `mkdir cloud-computing-finale`

`
### In local terminal
Copy github creds

- scp -i "/Users/alexiskaldany/school/cloud-dash.pem" "/Users/alexiskaldany/.ssh/id_ed25519" ubuntu@54.208.41.106:~/
- `scp -i "/Users/alexiskaldany/school/cloud-dash.pem" -r "/Users/alexiskaldany/school/cloud-computing-finale/" ubuntu@54.208.41.106:cloud-computing-finale/`

