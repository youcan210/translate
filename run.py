import eel
import view
import translate
if __name__ =="__main__":
  eel.init("view")
  eel.start("index.html",size=(500,400))
  translate.init_trans()

