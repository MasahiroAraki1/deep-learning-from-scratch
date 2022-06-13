# coding: utf-8


class MulLayer: #乗算レイヤ
    def __init__(self): #インスタンス変数であるxとyの初期化を行う(順伝播時の入力値を保持するため)
        self.x = None
        self.y = None

    def forward(self, x, y): #2つの引数を受け取る
        self.x = x
        self.y = y                
        out = x * y

        return out

    def backward(self, dout): #上流から流れてきた微分(dout)に対し，順伝播の”ひっくり返した値”を乗算して下流に流す
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy


class AddLayer: #加算レイヤ
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y

        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1

        return dx, dy
