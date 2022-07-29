from flask import Flask, render_template, request
from solver import Suduko,puzzle

def input_grid(data):
    print(data)
    grid = [[0 for i in range(9)] for j in range(9)]
    for row in range(9):
        for col in range(9):
            ind_name=str(row)+"_"+str(col)
            if(data[ind_name] != None and data[ind_name].isnumeric() ):
                x=data[ind_name]
                grid[row][col]=int(x)
    # print(grid)
    # grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
    #         [0, 1, 0, 0, 0, 4, 0, 0, 0],
    #     [4, 0, 7, 0, 0, 0, 2, 0, 8],
    #     [0, 0, 5, 2, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 9, 8, 1, 0, 0],
    #     [0, 4, 0, 0, 0, 3, 0, 0, 0],
    #     [0, 0, 0, 3, 6, 0, 0, 7, 2],
    #     [0, 7, 0, 0, 0, 0, 0, 0, 3],
    #     [9, 0, 3, 0, 0, 0, 6, 0, 4]]
    return grid



app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template("empty_sudoko.html")

@app.route('/solved' , methods=['POST'])
def solved():
    print(request.method)
    
    
    data=request.form
    grid = input_grid(data)

    print("***************")

    if (Suduko(grid, 0, 0)):
        puzzle(grid)
    
    # print(data)
    return render_template("solved_sudoko.html", result=grid)
@app.route("/sk")
def salvador():
    return "Hello, SK"

app.run(host='0.0.0.0', port=81, use_reloader=True)