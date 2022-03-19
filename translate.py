from turtle import sety
from googletrans import Translator
import fire
import params


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
def init_trans(test="hello world"):
  """init googletrans
  
  """
  
  # オブジェクト生成
  translator = Translator()
  for i in lang_dict:
    # 原文データを取得する
    translator.translate(test,dest=i,src="ja").text
  return True


def set_lang(trans_lang):
  """
  翻訳する言語をセット


  """
  if trans_lang in lang_dict:
    return trans_lang
  else:
    return False
  
def check_lang(trans_lang):
  if trans_lang != None:
    return True
    

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
  
        
# if __name__ == "__main__":
#     fire.Fire(generate)