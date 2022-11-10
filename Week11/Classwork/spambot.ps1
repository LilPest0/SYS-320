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
