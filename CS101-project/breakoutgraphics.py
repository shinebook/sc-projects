"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 100      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        self.pw = paddle_width
        self.__dy = 0
        self.__dx = 0
        self.xs = MAX_X_SPEED
        self.ys = INITIAL_Y_SPEED
        self.check = 0
        self.score = 0
        self.label = GLabel(f"Score: {self.score}")
        self.po = paddle_offset
        self.max_x_speed = MAX_X_SPEED
        self.max_y_speed = INITIAL_Y_SPEED
        self.bos = brick_offset
        self.bh = brick_height
        self.br = brick_rows
        self.bs = brick_spacing
        self.bw = brick_width
        self.final = False

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.ww = window_width
        self.window.add(self.label, x=0, y=self.label.height+1)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window.
        ball_width = ball_radius*2
        self.ball = GOval(ball_width, ball_width)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-ball_width)/2, y=(window_height-ball_width)/2)

        # Default initial velocity for the ball.
        self.ball.move(self.__dx, self.__dy)

        # Initialize our mouse listeners.
        onmouseclicked(self.ball_move)
        onmousemoved(self.control_paddle)
        # Draw bricks.
        color = ["red", "orange", "yellow", "green", "blue"]
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.fill_color = color[i // (brick_rows // 5)]
                self.window.add(brick, x=j*(brick_width+brick_spacing), y=brick_offset+i*(brick_height+brick_spacing))

    # method, paddle control
    def control_paddle(self, a):
        if self.pw/2 < a.x < self.ww - (self.pw/2+1):
            self.paddle.x = a.x-self.pw/2

    # method, ball movement
    def ball_move(self, a):
        if self.__dx == 0:
            self.__dx = random.randint(1, self.xs)
            self.__dy = self.ys
            self.check += 1
            if random.random() > 0.5:
                self.__dx = -self.__dx

    # method, check if object is paddle or not, if not remove. Also control grade
    def checking(self, tip, ycord):
        point = [10, 20, 30, 40, 50]
        h = (self.bs+self.bh)*self.br//5
        if tip is not self.paddle:
            self.window.remove(tip)
            if ycord <= self.bos + h:
                p = 4
            elif ycord <= self.bos + h * 2:
                p = 3
            elif ycord <= self.bos + h * 3:
                p = 2
            elif ycord <= self.bos + h * 4:
                p = 1
            else:
                p = 0
            self.score += point[p]
            self.label.text = f"Score: {self.score}"

    # method, reset ball speed after ball leave safe zone
    def reset(self):
        self.__dx = 0
        self.__dy = 0

    # method, ball speed after bounce on paddle
    def speed(self, i, ds=5):
        s = [self.max_x_speed+5, self.max_x_speed//2+3, -self.max_x_speed-5, -self.max_x_speed//2-3, ds/2]
        self.__dx = s[i]

    # method, end screen
    def end_screen(self):
        self.label.font = "-60"
        self.window.add(self.label,
                        x=(self.window.width-self.label.width)/2,
                        y=(self.window.height+self.label.height)/2)

    # method
    def is_it_over(self):
        self.final = True
        for i in range(0, self.window.width, self.bw+self.bs):
            for j in range(self.bos, self.br*(self.bh+self.bs), (self.bh+self.bs)):
                maybe = self.window.get_object_at(i, j)
                if maybe is not None:
                    self.final = False

    # getter
    def dx(self):
        return self.__dx

    def dy(self):
        return self.__dy
