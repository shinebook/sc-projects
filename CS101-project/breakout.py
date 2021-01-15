"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1500 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    g = BreakoutGraphics()
    dx = 0
    dy = 0
    corner = [2, 3, 6, 7]
    stay = [g.window, g.label]
    interact = [g.paddle]
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        if lives > 0 and g.final is False:
            # check if there's brick left
            g.is_it_over()
            # disable bouncing after ball pass paddle height
            if g.ball.y+g.ball.height/2 < g.window.height - g.po:
                # after click, ball will gain speed
                if dx == 0 and dy == 0:
                    dx = g.dx()
                    dy = g.dy()
                # ball speed
                g.ball.move(dx, dy)
                if g.ball.x <= 0:
                    dx = -dx
                    g.window.add(g.ball, x=0, y=g.ball.y)
                if g.ball.x + g.ball.width >= g.window.width:
                    dx = -dx
                    g.window.add(g.ball, x=g.window.width-g.ball.width, y=g.ball.y)
                if g.ball.y <= 0:
                    dy = -dy
                    g.window.add(g.ball, x= g.ball.x, y=0)
                # value for which side ball bounce on
                value = 0
                # four check point on ball
                x1 = g.ball.x
                y1 = g.ball.y
                x2 = g.ball.x + g.ball.width
                y2 = g.ball.y + g.ball.height
                x_cord = [x1, x2]
                y_cord = [y1, y2]
                tip = g.window.get_object_at(g.label.width+1, 0)
                for i in range(2):
                    for j in range(2):
                        x = x_cord[i]
                        y = y_cord[j]
                        tip = g.window.get_object_at(x, y)
                        if tip is not None and tip not in stay:
                            value += i+j*4+2
                            g.checking(tip, y)
                # top, bottom
                if value == 5 or value == 13:
                    dy = -dy
                # right, left
                if value == 8 or value == 10:
                    dx = -dx
                # corner
                if value in corner:
                    dx = dx
                    dy = -dy
                if value != 0 and tip in interact:
                    # ball on right 1/5 of paddle
                    if g.ball.x+g.ball.width/2 > g.paddle.x + g.paddle.width*4/5:
                        g.speed(0)
                    # ball on right 2/5 of paddle
                    elif g.ball.x+g.ball.width/2 > g.paddle.x + g.paddle.width*3/5:
                        g.speed(1)
                    # ball on left 1/5 of paddle
                    elif g.ball.x+g.ball.width/2 < g.paddle.x + g.paddle.width*1/5:
                        g.speed(2)
                    # ball on left 2/5 of paddle
                    elif g.ball.x+g.ball.width/2 < g.paddle.x + g.paddle.width*2/5:
                        g.speed(3)
                    # ball on middle of paddle
                    else:
                        g.speed(4, ds=dx)
                    dx = g.dx()
            # try to fix the ball stick on the paddle by disable bounce back after ball pass paddle(fail)
            else:
                while g.ball.y < g.window.height:
                    g.ball.move(dx, dy)
                    pause(FRAME_RATE)
                # reset speed for next loop(loop "have" to start with 0 speed)
                dx = 0
                dy = 0
                lives -= 1
                g.reset()
                g.window.add(g.ball, x=(g.window.width - g.ball.width) / 2, y=(g.window.height - g.ball.width) / 2)
        else:
            g.window.remove(g.ball)
            g.end_screen()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()