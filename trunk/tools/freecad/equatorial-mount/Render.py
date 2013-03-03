import pivy.sogui
import pivy.coin

class Render:

    def __init__(self):
        self.defaultmaterial=pivy.coin.SoBaseColor()
        self.defaultmaterial.rgb=(1,1,1)
        self.defaulttextcolor=pivy.coin.SoBaseColor()
        self.defaulttextcolor.rgb=(1,1,1)
        
    @staticmethod
    def draw(shape, mat):
        input=pivy.coin.SoInput()
        input.setBuffer(shape.writeInventor())
        # SoNode is abstract, so what to use ?
        #rootnode=SoNode()
        #SoDB.read(input, rootnode)
        rootnode=pivy.coin.SoSeparator()
        objnode=pivy.coin.SoSeparator()
        objnode=pivy.coin.SoDB.readAll(input)
        rootnode.addChild(mat)
        rootnode.addChild(objnode)
        return rootnode

    @staticmethod
    def drawdefault(shape):
        return self.draw(obj, Render.defaultmaterial)

    @staticmethod
    def drawtext(self, text, posx, posy, posz, color):
        textnode=SoText2()
        textnode.string="Focus: 89.612 mm"
        texttr=SoTranslation()
        texttr.translation.setValue(posx, posy, posz)
        roottext=SoSeparator()
        roottext.addChild(color)
        roottext.addChild(texttr)
        roottext.addChild(textnode)
        return roottext

    @staticmethod
    def drawtextdefault(self, text, posx, posy, posz):
        return self.drawtext(text, posx, posy, posz, self.defaulttextcolor)
