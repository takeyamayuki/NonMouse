# -*- mode: python ; coding: utf-8 -*-
# https://github.com/google/mediapipe/issues/2162

block_cipher = None


a = Analysis(['app.py'],
            pathex=['/Users/yukitakeyama/Documents/Python/NonMouse2g'],
            binaries=[],
            datas=[('/usr/local/lib/python3.9/site-packages/mediapipe/modules', 'mediapipe/modules'),],
            hiddenimports=["pynput.keyboard._xorg", "pynput.mouse._xorg"],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)
exe = EXE(pyz,
            a.scripts,
            a.binaries,
            a.zipfiles,
            a.datas,
            [],
            name='app',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            upx_exclude=[],
            runtime_tmpdir=None,
            console=True )
