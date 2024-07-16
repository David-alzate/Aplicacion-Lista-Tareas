# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[r'C:\Users\alzat\Documents\Lista De Tareas'],  # Cambio de barras diagonales
    binaries=[],
    datas=[
        (r'C:\Users\alzat\Documents\Lista De Tareas\main.py', '.'), 
        (r'C:\Users\alzat\Documents\Lista De Tareas\interfaz.ui', '.'),
        (r'C:\Users\alzat\Documents\Lista De Tareas\dataBase.py', '.'),
        (r'C:\Users\alzat\Documents\Lista De Tareas\tablas.py', '.'),
        (r'C:\Users\alzat\Documents\Lista De Tareas\iconos\*', 'iconos'),
        (r'C:\Users\alzat\Documents\Lista De Tareas\\venv\\Lib\\site-packages\\PyQt5\\*', 'PyQt5'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Tareas',
    icon=r'C:\Users\alzat\Documents\Lista De Tareas\iconos\tar.ico',
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
)
