$ErrorActionPreference = "Stop"

$out = "C:\Users\芮\Documents\作品集合.html"
$html = @'
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>作品集合</title>
  <style>
    * {
      box-sizing: border-box;
    }

    html,
    body {
      margin: 0;
      min-height: 100%;
      background: #111;
    }

    .work {
      width: 100%;
      min-height: 100vh;
      border: 0;
      display: block;
      background: #111;
    }

    @media print {
      @page {
        size: A4 landscape;
        margin: 0;
      }

      .work {
        height: 210mm;
        min-height: 210mm;
        page-break-after: always;
      }

      .work:last-child {
        page-break-after: auto;
      }
    }
  </style>
</head>
<body>
  <iframe class="work" src="zuo1.html" title="作品一"></iframe>
  <iframe class="work" src="zuo2.html" title="作品二"></iframe>
</body>
</html>
'@

[System.IO.File]::WriteAllText($out, $html, [System.Text.Encoding]::UTF8)
Write-Output $out
