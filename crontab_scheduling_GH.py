import crontab as CronTab

# Create a new cron job
cron = CronTab.CronTab(user=True)

# Define paths to python and script
path_to_python = "/path_to_python"
path_to_script = "/path_to_read_emails_GH.py"
command = f"{path_to_python} {path_to_script}"

# Create a new cron job to run the script at 3:30 PM every Monday through Thursday (since Friday is a podcast, and weekend is nothing)
job = cron.new(command=command, comment="Run script")
job.minute.on(30)
job.hour.on(15) # `15` is 3:00 PM
job.dow.on('1', '2', '3', '4') # Monday through Thursday

# Write the cron job to the crontab
cron.write()