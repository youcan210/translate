import eel
import translate


@eel.expose
def view_set_lang(_set:int):
  lang = translate.set_lang(_set)
  return lang


@eel.expose
def send_text_to_python(text,set_lang):
  trans_text = translate.generate(text,set_lang)
  eel.send_text_to_javascript(trans_text)

