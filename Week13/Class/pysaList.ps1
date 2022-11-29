# List the files in a direcotry &
#Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path .\Documents |get-member

Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path .\Documents |export-csv `
-Path files.csv

# import CSV file
$fileList = import-csv -Path .\files.csv -header FullName 

$fileList 
# loop through the results
foreach ($f in $fileList) {

    Get-ChildItem -Path $f.FullName
    
}
