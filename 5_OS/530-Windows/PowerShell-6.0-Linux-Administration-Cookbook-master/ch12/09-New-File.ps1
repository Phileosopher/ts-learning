function New-File {
    [CmdletBinding(
        ConfirmImpact='High',
        SupportsShouldProcess=$true
    )]
    param (
        # The path to the file (or the name)
        [Parameter(Mandatory=$true, Position=0, ValueFromPipeline)]
        [string[]]
        $Path
    )
    begin {
        Write-Host "$(Get-Date)"
    }
    process {
        foreach ($Item in $Path) {
            if ($PSCmdlet.ShouldProcess("$PsScriptRoot", "Create $Item")) {
                New-Item -Path $Item -ItemType File
            }
        }
    }
    end {}
}