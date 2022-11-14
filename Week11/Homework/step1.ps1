# Generate a random number 1000-9000
$getRand = Get-Random -Maximum 9000 -Minimum 1000

# Write Powershell code that copies the file 
# "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" 
# to your home directory using the "Copy-item" cmdlet.
Copy-Item -Path "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" `
-Destination "C:\Users\torfo\Documents\SYS-320\Week11\Homework\EnNoB-$getRand.exe"

# Rename the powershell.exe file based on the threat intell 
# report so it should be something like "C:\Users\dunston\EnNoB-1214.exe."
$randomFileName = "C:\Users\torfo\Documents\SYS-320\Week11\Homework\EnNoB-$getRand.exe"

# Check that the copied file exists.
# If so, then print it is found.  If not, then print an error.
if (Test-Path -Path $randomFileName){
    write-host "File found"
}
else{
    write-host "File not found"
}
