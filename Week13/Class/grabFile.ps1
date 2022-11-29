# create commandline parameters to copy file and place it into an evidence directory
param (

 [parameter(Mandatory = $true)]
 [int]$reportNo,

 [parameter(Mandatory = $true)]
 [int]$filePath

)

# Create a directory with the report number
$reportDir = "rpt$reportNo"

# Create new directory
mkdir $reportDir

# Copy file
Copy-Item $filePath $reportDir
