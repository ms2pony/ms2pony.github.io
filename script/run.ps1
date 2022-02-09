
$env:WORKPATH = "C:\Users\tam\OneDrive\Documents\GitHub\blog\source\_posts"
# $imgInfo = node.exe "C:\Users\tam\OneDrive\Documents\GitHub\blog\script\mdLinkExtract.js" | ConvertFrom-Json -AsHashtable

# Set-Location -Path $env:WORKPATH
# $imgInfo | ForEach-Object {
#     cp $_.href "C:\Users\tam\OneDrive\Documents\GitHub\blog\source\_posts\img"
# }
node.exe "C:\Users\tam\OneDrive\Documents\GitHub\blog\script\mdLinkExtract.js" | python.exe "C:\Users\tam\OneDrive\Documents\GitHub\blog\script\mdRefactor.py"


