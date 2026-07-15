$ErrorActionPreference = "Stop"

$portfolio = "C:\Users\芮\Documents\portfolio_altea.html"
$html = [System.IO.File]::ReadAllText($portfolio, [System.Text.Encoding]::UTF8)

$css = @'

    .page-gallery-frame {
      display: block;
      padding: 0;
      background: #070b11;
      page-break-before: always;
    }

    .page-gallery-frame iframe {
      width: 100%;
      height: 100%;
      min-height: 720px;
      border: 0;
      display: block;
      background: #070b11;
    }

    @media print {
      .page-gallery-frame iframe {
        min-height: 210mm;
      }
    }
'@

$page = @'

  <main class="page page-gallery-frame" aria-label="生命印象作品展示">
    <iframe src="gallery_assets/gallery.html" title="生命印象作品展示"></iframe>
  </main>
'@

if ($html -notmatch 'page-gallery-frame') {
  $html = $html -replace '</style>', ($css + "`r`n  </style>")
  $html = $html -replace '</body>', ($page + "`r`n</body>")
} else {
  $html = $html -replace '(?s)\s*<main class="page page-gallery-frame".*?</main>\s*</body>', ($page + "`r`n</body>")
}

[System.IO.File]::WriteAllText($portfolio, $html, [System.Text.Encoding]::UTF8)
Write-Output "appended gallery page"
