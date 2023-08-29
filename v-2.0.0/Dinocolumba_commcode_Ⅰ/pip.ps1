# Flask
if (-not (Test-Path (Join-Path $env:PYTHONPATH "Lib\site-packages\flask"))){
    Write-Host "安装 Flask..."
    pip install Flask
} else {
    Write-Host "Flask 已安装."
}

# nltk
if (-not (Test-Path (Join-Path $env:PYTHONPATH "Lib\site-packages\nltk"))){
    Write-Host "安装 nltk..."
    pip install nltk
} else {
    Write-Host "nltk 已安装."
}

# cryptography
if (-not (Test-Path (Join-Path $env:PYTHONPATH "Lib\site-packages\cryptography"))){
    Write-Host "安装 cryptography..."
    pip install cryptography
} else {
    Write-Host "cryptography 已安装."
}

Write-Host "完成."
