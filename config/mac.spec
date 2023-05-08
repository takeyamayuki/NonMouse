# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['../nonmouse/__main__.py'],
             pathex=['/Users/yukitakeyama/Documents/Python/NonMouse2g'],    # 各々の環境に合わせてPATHを変更してください
             binaries=[],
             datas=[('../venv/lib/python3.9/site-packages/mediapipe/modules', 'mediapipe/modules'),], 
            #  hiddenimports=['pynput', 'pywinauto', 'tkinter', 'tkinter.filedialog prog', 'pkg_resources.py2_warn', 'pkg_resources.markers'],
             hookspath=[],
             hooksconfig={},
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
          name='NonMouse',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='../images/icon.ico')
