import crontab as CronTab

# Create a new cron job
cron = CronTab.CronTab(user='ec2-user') # I'm running this on an AWS EC2 instance, so the user is 'ec2-user'

# Define paths to python and script
path_to_python = "/path_to_python" # can be found by executing 'which python3' in the terminal
path_to_script = "/path_to_read_emails_GH.py" # path to the script you want to run
command = f"{path_to_python} {path_to_script}"

# Create a new cron job to run the script at 3:30 PM every Monday through Thursday (since Friday is a podcast, and weekend is nothing)
job = cron.new(command=command, comment="Run script")
job.minute.on(30) # `30` is :30 PM EST
job.hour.on(1) # `1` is 3:00 PM EST
job.dow.on(1,2,3,4) # Monday through Thursday

# Write the cron job to the crontab
cron.write()