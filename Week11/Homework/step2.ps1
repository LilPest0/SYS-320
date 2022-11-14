# The malware performs the following action: "The « step1.ps1 » script creates a
# ransom demand file named « Readme.READ ». Albeit very short, this message
# contains the same PROTONMAIL e-mail addresses as above" (Page 5)
$msg = "If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you."

# "Readme.READ."
$readMe = "C:\Users\torfo\Documents\SYS-320\Week11\Homework\Readme.READ"

# $msg added to $Readme.READ
Write-Output $msg > $readME

# Check that the Readme.READ file exists.
if (Test-Path -Path $readMe){
    # If so, then print it is found.  If not, then print an error
    write-host "File found"
} 
else{
    write-host "File not found"
}
