"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    ans = int((width-GRAPH_MARGIN_SIZE*2)//len(YEARS)*year_index)+GRAPH_MARGIN_SIZE
    return ans


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, w-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, h-GRAPH_MARGIN_SIZE, w-GRAPH_MARGIN_SIZE, h-GRAPH_MARGIN_SIZE)
    t = 0
    for x in range(GRAPH_MARGIN_SIZE, w-GRAPH_MARGIN_SIZE, (w-GRAPH_MARGIN_SIZE*2)//len(YEARS)):
        canvas.create_line(x, 0, x, h)
        # 錯誤
        # if t < len(YEARS) 才對
        if t < 12:
            canvas.create_text(x+TEXT_DX, h-GRAPH_MARGIN_SIZE, text=YEARS[t], anchor=tkinter.NW)
        t += 1


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    c = 0
    for i in lookup_names:
        line_xcord = []
        line_ycord = []
        for year, rank in name_data[i].items():
            year_int = YEARS.index(int(year))
            x_cord = get_x_coordinate(CANVAS_WIDTH, year_int)
            if int(rank) < MAX_RANK:
                y_cord = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2)/MAX_RANK*int(rank) + GRAPH_MARGIN_SIZE
            else:
                y_cord = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                rank = "*"
            canvas.create_text(x_cord+TEXT_DX, y_cord, text=f"{i} {rank}", anchor=tkinter.NW)
            line_xcord.append(x_cord)
            line_ycord.append(y_cord)
        print(line_ycord)
        print(line_xcord)
        for x in range(len(line_xcord)):
            if x+1 < len(line_xcord):
                canvas.create_line(line_xcord[x], line_ycord[x],
                                   line_xcord[x+1], line_ycord[x+1],
                                   width=LINE_WIDTH, fill=COLORS[c])
        # changing colors for every lines
        c += 1
        if c >= len(COLORS):
            c = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
