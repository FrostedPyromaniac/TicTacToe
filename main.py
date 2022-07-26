from processing import *

WIDTH = 510
HEIGHT = 525


BACKGROUND_COLOR = (32, 176, 174)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (66, 233, 245)

class Mouse:
  
  def __init__(self):
    self.clicked = False
    self.canClick = True

mouse = Mouse()

class Game:
  
  def __init__(self):
    self.board = [
      ["", "", ""],
      ["", "", ""],
      ["", "", ""]
    ]
    self.turn = 0
    self.markers = ["X", "O"]
    self.padding = 15
    self.yOffset = 15
    self.boxSize = (WIDTH - 2 * self.padding) // 3
  
  def draw_board(self):
    textAlign(LEFT, TOP)
    fill(*WHITE)
    noFill()
    stroke(*WHITE)
    strokeWeight(1)
    rect(
      self.padding, self.padding + self.yOffset,
      WIDTH - 2 * self.padding,
      HEIGHT - (2 * self.padding + self.yOffset)
    )
    something = self.padding + self.boxSize
    line(self.padding, something + self.yOffset, WIDTH - self.padding, something + self.yOffset)
    line(self.padding, something + self.yOffset + self.boxSize, WIDTH - self.padding, something + self.yOffset + self.boxSize)
    line(something, self.padding + self.yOffset, something, HEIGHT - self.padding)
    line(something+self.boxSize, self.padding + self.yOffset, something+self.boxSize, HEIGHT - self.padding)
    mouseCol = (mouseX - self.padding) // self.boxSize
    mouseRow = (mouseY - (self.padding + self.yOffset)) // self.boxSize
    if mouseCol >= 0 and mouseCol <= 2 and mouseRow >= 0 and mouseRow <= 2 and self.board[mouseCol][mouseRow] == "":
      fill(*HIGHLIGHT_COLOR)
      rect(
        self.padding + mouseCol * self.boxSize,
        self.padding + self.yOffset + mouseRow * self.boxSize,
        self.boxSize, self.boxSize
      )
    for row in xrange(3):
      for col in xrange(3):
        if self.board[row][col] == "X":
          self.drawX(row, col)
        elif self.board[row][col] == "O":
          self.drawO(row, col)
    
  def drawX(self, row, col):
    stroke(*WHITE)
    strokeWeight(2)
    top = 3*self.padding+self.yOffset+(row*self.boxSize)
    bottom = top + self.boxSize - 4*self.padding
    left = 3*self.padding + (col*self.boxSize)
    right = left + self.boxSize - 4*self.padding
    line(left, top, right, bottom)
    line(left, bottom, right, top)
  
  def drawO(self, row, col):
    noFill()
    stroke(*WHITE)
    strokeWeight(2)
    top = 3*self.padding+self.yOffset+(row*self.boxSize)
    left = 3*self.padding + (col*self.boxSize)
    ellipse(left, top, self.boxSize - 4*self.padding, self.boxSize - 4*self.padding)

def setup():
  global game
  game = Game()
  ellipseMode(CORNER)
  size(WIDTH, HEIGHT)

def draw():
  background(*BACKGROUND_COLOR)
  game.draw_board()

def mousePressed():
  game.clicked = True

def mouseReleased():
  game.clicked = False

run()
