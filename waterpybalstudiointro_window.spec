# -*- mode: python ; coding: utf-8 -*-

import pkgutil
import numpy, pandas, xarray, matplotlib, cftime, netCDF4, osgeo, rasterio, richdem, rioxarray,pyet, PyQt6, ctypes


pack_list=[numpy, pandas, xarray, matplotlib, cftime, netCDF4, osgeo, rasterio, richdem, rioxarray, pyet, PyQt6, ctypes]

additional_packages = list()

for package in pack_list:

	prefix = package.__name__ + "."

	# list all submodules, to include them in the package
	for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
							prefix=prefix,
							onerror=lambda x:None):

		print (modname)
		#module = __import__(modname, fromlist="dummy")
		additional_packages.append(modname)



#package=rasterio

#for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
#                                                      prefix=package.__name__+'.',
#                                                      onerror=lambda x: None):
#    print(modname)

#additional_packages = list()
#for package in pkgutil.iter_modules(rasterio.__path__, prefix="rasterio."):
#    additional_packages.append(package.name)


block_cipher = None


a = Analysis(
    ['waterpybal_gui_main.py'],
    pathex=[],
    binaries=[],
    datas=[('curve_number_standard_table.xls','.'),('8.ico','.'),('7_resized.png','.')],
    hiddenimports=additional_packages,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='WaterpyBal Studio',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='8.ico'
)
