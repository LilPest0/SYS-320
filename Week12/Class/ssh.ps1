# Login to remote ssh server
#New-SSHSession -ComputerName '192.168.4.22' -Credential (Get-Credential sys320)

<#
while ($true) {
    # Add prompt to run commands
    $the_cmd = Read-Host -Prompt "Enter a command"

    # Run command on remote SSH Server
    (Invoke-SSHCommand -index 0 $the_cmd).Output
} 
#>

New-SSHSession -ComputerName '184.171.158.203' -Credential (Get-Credential sys320)
Set-SCPItem -ComputerName '184.171.158.203' -Credential (Get-Credential sys320) `
-Destination 'C:\Users\torfo\Documents\SYS-320\Week12\Class' -Path  'C:\Users\torfo\Desktop\gibbon.jpg'

