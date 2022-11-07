# Get a list of running processes

# Get list of members
#Get-process | get-member

# Get a list of processes; name, id, and path
#Get-process | Select-object ProcessName, id, Path | Export-csv -Path "C:\Users\torfo\Documents\SYS-320\Week10\Classworkprocesses.csv"

$outputName = "C:\Users\torfo\Documents\SYS-320\Week10\Classwork\runningServices.csv"

# System Services & Properties
#Get-service | get-member
Get-service | Where-Object { $_.Status -eq "Running" } | Export-csv -Path $outputName

# Check to see if file exists
if ( Test-Path $outputName ) {

    write-host -backgroundcolor "Green" -foregroundcolor "white" "Services file was created!"

} else {

    write-host -backgroundcolor "red" -foregroundcolor "white" "Services file was not created!"

}
