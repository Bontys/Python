from flask import Flask, render_template, request

app = Flask(__name__)

# Состояние игры (доска)
board = [' ' for _ in range(9)]
current_player = 'X'

# Функция для проверки победителя
# def check_winner():
#     # Все возможные выигрышные комбинации
#     winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
#                             (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                             (0, 4, 8), (2, 4, 6)]
    
#     for combo in winning_combinations:
#         if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
#             return board[combo[0]]
    
#     return None

# 0 1 2
# 3 4 5
# 6 7 8

def check_winner(): 
    global current_player     
    # for i in range(3): 
    if board[0] == board[1] == board[2] == current_player: 
        return True 
    if board[3] == board[4] == board[5] == current_player: 
        return True 
    if board[6] == board[7] == board[8] == current_player: 
        return True         
    
    if board[0] == board[3] == board[6] == current_player: 
        return True     
    if board[1] == board[4] == board[7] == current_player: 
        return True 
    if board[2] == board[5] == board[8] == current_player: 
        return True         



    if board[0] == board[4] == board[8] == current_player: 
        return True 
    if board[2] == board[4] == board[6] == current_player: 
        return True 
    return False

def check_draw():
    return not ' ' in board
        

@app.route('/')
def index():
    return render_template('index.html', board=board)

@app.route('/make_move', methods=['POST'])
def make_move():
    global current_player
    global board
    position = int(request.form['position'])
    
    if board[position] == ' ':
        board[position] = current_player
        winner = check_winner()
        draw = check_draw()
        if winner:
            winner_sym = current_player
            board = [' ' for _ in range(9)]
            current_player = 'X'
            return render_template('winner.html', winner=winner_sym)
        if draw:
            board = [' ' for _ in range(9)]
            current_player = 'X'
            return render_template('draw.html')

        
        current_player = 'X' if current_player == 'O' else 'O'
        return render_template('index.html', board=board)


if __name__ == '__main__':
    app.run(debug=True)