VScodeでのモジュールエラー対応メモ
===
インポートされているモジュールを宣言しているがプログラムを実行後、モジュールエラーで仮想環境内のライブラリを参照していないためと思われる
### エラー内容

```
ImportError: cannot import name 'Translator' from partially initialized module 'googletrans' (most likely due to a circular import) (C:\Users\ahoo\Documents\python\translate\googletrans.py)
```
### 確認内容
1. インタープリターを仮想環境内のScripts\python.exeを選択する


VScodeの右下に実行するインタープリターの場所が表示されているので外部モジュールを参照していないか確認する
