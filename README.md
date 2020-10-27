# azcam-ds9

## Purpose

*azcam-ds9* is an *azcam extension* which supports SAO's ds9 display tool running under Windows. See https://sites.google.com/cfa.harvard.edu/saoimageds9.

## Installation

To display images on the ds9 image display tool from within AzCam, the xpans.exe program needs to be running See http://nssm.cc for details about how to install `xpans.exe` as a Windows service.

Use `install_xpans_nssm.bat` to install xpans as a service and `uninstall_xpans_nssm.bat` to uninstall the service.  You should expect to first edit `install_xpans_nssm.bat` to set the appropriate file paths. Note using `nssm.exe` modifies the Windows Registry.

To associate ds9 with FITS or MEF images:

- `set_ds9_default_fits.bat`
- `set_ds9_default_mef.bat`

To open a FITS or MEF file with ds9:

- `open_fits.ds9.bat`
- `open_mef.ds9.bat`

# ds9 and XPA installation
See http://ds9.si.edu/site/Home.html

## Notes
It may be helpful to remove all associations of .fits files in the registry and then only
execute the above batch files.  Do not directly associate .fits files with ds9.exe.