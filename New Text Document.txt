# FocusXP.spec - PyInstaller build configuration
# Author: Charith (FocusXP Final Version)

block_cipher = None

a = Analysis(
    ['main.py'],                 # Entry point
    pathex=['.'],                # Base directory
    binaries=[],
    datas=[
        ('data/*', 'data'),      # include database folder
        ('config/*', 'config'),  # include config files
        ('exports/*', 'exports') # include exported CSVs
    ],
    hiddenimports=[
        'PyQt5', 'matplotlib', 'psutil', 'sqlite3'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=['tkinter', 'tests'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='FocusXP',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,             # GUI app, no terminal window
    icon='icon.ico'            # optional icon file
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='FocusXP'
)
