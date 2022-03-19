# Google翻訳に文字列を渡して翻訳するアプリ

===
Google翻訳APIを使用して入力したテキストを英→日、日→英に翻訳、またEelライブラリを使用してGUIからの操作をします。
また、ほかの言語での翻訳にも対応できるように原文からの変換する言語を指定できるようにもします。
使用するAPI

- Googletrans

ライブラリ

- Eel

## googletransの基本

pipでgoogletransをインストールします。`pip install googletrans`でインストールした場合、正常に動かないバージョンがインストールされます。

```

pip install googletrans==4.0.0-rc1
```

バージョンを指定すると最新版がインストールされます。

以下が自動翻訳するための最小のコードです。

```

from googletrans import Translator

translator = Translator()
trans = translator.translate('veritas lux mea', dest="ja",src='la').text
print(trans)
```

Translatorオブジェクトをインスタンス化してtranslateメソッドに翻訳変換する文字列を入れます。第一引数に文字列、第二引数にdestとありますがこれは変換する言語を指定しています。何も指定しない場合、デフォルトで英訳(en)されます。

## Eelで画面を表示する

まずはEelで画面を表示します。最小の構成で画面を表示するには現在作業中のフォルダに表示する画面のHTMLを用意します。
Eelをインポートし、Eelで対象のフォルダを初期化します。その後、htmlファイルを起動させます。

```

import eel
if __name__ =="__main__":
  eel.init("view")
  eel.start("index.html")

```

## 翻訳を初期化する

アプリ起動時にまずデータの元となる言語設定が読み込まれているか初めにチェックしたいと思います。
今回翻訳するために使うgoogletransのオブジェクトを生成し無事データを取得することが出来たら真を返したいと思います。
```

def init_trans(test="hello world"):
  """init googletrans
  
  """
  
  # オブジェクト生成
  translator = Translator()
  for i in lang_dict:
    # 原文データを取得する
    translator.translate(test,dest=i,src="ja").text
```
デフォルト引数であらかじめテスト文を記述しています。このテスト文の処理を終了したなら真を返します。

## 翻訳言語をセットする

googletransで設定されている言語コードをセットします。

```
# 言語コード辞書をセット
lang_dict = {"en":"英語",
              "fr":"フランス語",
              "de":"ドイツ語",
              "es":"スペイン語",
              "nl":"オランダ語",
              "sv":"スウェーデン語",
              "he":"ヘブライ語",
              "ja":"日本語"
}

```

コードが多かったので今回は上記のコードのみです。
この言語辞書の中に翻訳する言語があればその設定を取得します。それ以外はFalseで返します。
```

def set_lang(trans_lang):
  """
  翻訳する言語をセット

  """
  if trans_lang in lang_dict:
    return trans_lang
  else:
    return False


```

## 言語を確認する

翻訳する言語でNoneオブジェクトを持っていないか確認します。持っていないのなら、真を返します。

```
def check_lang(trans_lang):
  if trans_lang != None:
    return True
    

```

ドロップダウンメニューで変更を検知します。

## 言語を生成する

ここまで、初期化の処理、原文データの取得、言語をセットを行いました。この流れを実際に処理し翻訳テキストを生成するのがこのgenerate関数です。
この関数で上記の関数を処理し逐次実行していきます。

```

def generate(test="世界は美しい",lang="en"):
  # 初期化処理
  init_trans()
  # 原文データ取得
  if check_lang(lang):
  # 言語をセット
    lang = set_lang(lang)
    trans = Translator()
    trans_text = trans.translate(test,dest=lang).text
    return trans_text
  
        
```

### JavaScriptから翻訳設定の値を取得

HTMLに翻訳言語を設定する。HTMLにselectタグのoptionタグに値を設定し、オプションタグに設定した値が選択されたらJavaScriptが値を取得、Pythonに値を渡します。
ですので、EelライブラリでPythonの処理の戻り値を取得してJavaScript側で受け取る処理を行います。

```
let element = document.getElementById("trans-select");
element.addEventListener("change", async function () {
  lang = this.value;

  let res = await eel.view_trans(lang)();
  console.log(res);
  if(res){
    alert("ok")
    console.log(res);
  }else {
    alert("No")
  }
```

JavaScriptでは、オプションタグで切り替えした値を取得するためにタグ要素を取得します。取得後、そのイベントハンドラーで切り替わったらイベントハンドラーで設定している要素を`this.value`で取得し、Eelで非同期処理を実行します。
ifによる処理はこの段階で値の確認をするための処理で取得を確認できたのらアラートとコンソールで値を表示するということをしています。

```
@eel.expose
def view_trans(set_lang:int):
  print(set_lang)
  return set_lang
```

上記のコードはPython側の処理です。EelではJavaScriptで実行する関数を探すのに@eel.exposeでデコレートします。デコレートした関数にはJavaScriptからの値を確認したいので戻り値で値の設定をします。これで値の取得をPython、JavaScriptから参照することができます。
参照することが出来たので次は作成した処理の関数を呼び出してセットした言語の設定が返ってくるかも見てみます。実行してみると`en
ja`のコマンドライン上に設定した言語設定が返ってきているのが確認できます。

### 設定した言語を翻訳する

上記の内容で設定した言語`ja en`どちらも返ってきているのが確認できました。ですので、次からは実際に設定した言語で翻訳し、その翻訳文が返ってくるか確認してみます。
テキストエリアに入力した文字列を取得し、EelでJavaScriptで取得した値をPythonで処理します。ここまでは先のロジックと同じです。イベントハンドラーを使い変更イベントが加わったとき記述した文字列をPythonへ送ります。

```

text.addEventListener("change",async function() {
  console.log(text.value);
  await eel.view_origin(text.value,set_lang)();

},false)

```
上記がJavaScriptでイベントハンドラーで変更イベントが起こったときにEelでテキストの値と、設定した言語が非同期処理で返ってきます。
```

@eel.expose
def view_origin(text,lang):
  return translate.generate(text,lang)
""""""
good morning
The program is the best
英語は最高の言語です
""""""""
```

JavaScriptから実行された関数はPythonのview.pyに記述したview_originです、これが処理`translate.generate()`で翻訳したテキストと言語設定を生成します。DOM上で文字列を入力するとコマンドラインから入力した文字列が設定した言語で返ってきているのが確認できます。
`return translate.generate()`で値を返すことをしています。ですがこの後でEelオブジェクトを使いJavaScriptへ値を渡します。このままではNoneで値が返ってきません。ですので処理側のgenerate関数をreturnに変更します。

### 翻訳文をテキストエリアに表示

ロジックの流れはJavaScriptで取得した値は、PythonへEelを通じて渡します。Pythonで翻訳処理を行いEelオブジェクトで翻訳テキストJavaScriptへ戻します。その後、JavaScriptで翻訳テキストをテキストエリアで表示するという流れです。
JavaScriptでイベントハンドラーでイベントを登録します。その後、Eelでテキストの値と言語設定を`send_text_to_python`関数で引数に渡しコールします。
```

text.addEventListener("change",function() {
      
      eel.send_text_to_python(text.value,set_lang)

    },false);
```
呼び出された関数`send_text_to_python`は翻訳を生成し変数に持たせます。翻訳処理を行い持たせた変数trans_textは再びJavaScriptへ`send_text_to_javascript`関数で引数に渡しコールします。
```

@eel.expose
def send_text_to_python(text,set_lang):
  trans_text = translate.generate(text,set_lang)
  eel.send_text_to_javascript(trans_text)

```

- Pythonにeelオブジェクトをコール
- Javascriptから呼び出された関数の処理を記述
- 翻訳処理を記述し変数を持たせる
- Eelオブジェクトで翻訳した変数で関数をコール
- JavaScriptで取得した関数はテキストエリアに表示

呼び出された`send_text_to_javascript`はテキストエリアに翻訳したテキストを表示します。
```
  eel.expose(send_text_to_javascript)
  function send_text_to_javascript(trans_text) {
    if(trans_text) {
      console.log(trans_text);
      textArea.innerHTML += trans_text + "\n";
    }
  }

```

以上でgoogletransを使って翻訳する処理を作成完了です。

以下に全コードを載せておきます。

html
javascript
python