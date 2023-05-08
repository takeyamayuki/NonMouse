# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['..\\nonmouse\\__main__.py'],
             pathex=['C:\\Users\\namik\\Documents\\NonMouse\\NonMouse'],    #それぞれの環境に応じて、変更してください
             binaries=[],
             datas=[('C:\\users\\namik\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\mediapipe\\modules', 'mediapipe\\modules'),],
             hiddenimports=[],
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
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='..\\images\\icon.ico')
