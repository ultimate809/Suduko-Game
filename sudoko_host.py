from flask import *
from solver import Suduko,input_validator

def input_grid(data):
    initial=[[' ' for i in range(9)] for j in range(9)]
    grid = [[0 for i in range(9)] for j in range(9)]
    for row in range(9):
        for col in range(9):
            ind_name=str(row)+"_"+str(col)
            if(data[ind_name] != None and data[ind_name].isnumeric() and data[ind_name].isnumeric() in range(1,10)):
                x=data[ind_name]
                grid[row][col]=int(x)
                initial[row][col]=x
    # grid = [[2, 2, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    return initial,grid



app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template("empty_sudoko.html")

@app.route('/invalid')
def invalid():
    return render_template("invalid.html")

@app.route('/solved' , methods=['POST'])
def solved():    
    
    data=request.form
    initial,grid = input_grid(data)

    if(input_validator(grid)):
        Suduko(grid, 0, 0)
    else:
        print("Invalid Input") 
        return redirect(url_for('invalid'))  
    
    return render_template("solved_sudoko.html", initial=initial ,result=grid)


app.run(host='0.0.0.0', port=80, use_reloader=True)