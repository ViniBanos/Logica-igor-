Add=[[" "," "," "],[" "," "," "],[" "," "," "]]
vencedor=1
def tabuleiro(Add):
  for row in Add:
    print("|".join(row))
    print(".....")
jogador=0
while (jogador<9):
  tabuleiro(Add)
  row = int(input("Digite uma linha entre (0-2): "))
  col = int(input("Digite uma coluna entre (0-2): "))
  if row<3 and row>-1 and col<3 and col>-1:
    if Add[row][col] == " " and jogador%2==0:
      Add[row][col] = "X"
      jogador=jogador+1
    elif Add[row][col] == " " and jogador%2==1:
      Add[row][col] = "O"
      jogador=jogador+1
    else:
      print("Você precisa selecionar um espaço vazio")
    if Add[0][0] == "X" and Add[0][1] == "X" and Add[0][2]== "X":
      tabuleiro(Add)
      print("X wins")
      vencedor=0
      break
    if Add[0][0] == "X" and Add[1][1] == "X" and Add[2][2]== "X":
      tabuleiro(Add)
      print("X wins")
      vencedor=0
      break
    if Add[0][2] == "X" and Add[1][1] == "X" and Add[2][0]== "X":
      tabuleiro(Add)
      print("X wins")
      vencedor=0
      break
    if Add[1][1] == "X" and Add[0][1] == "X" and Add[1][2]== "X":
      tabuleiro(Add)
      print("X wins")
      vencedor=0
      break
    if Add[2][2] == "X" and Add[2][1] == "X" and Add[0][2]== "X":
      tabuleiro(Add)
      print("X wins")
      vencedor=0
      break
    if Add[0][0] == "O" and Add[0][1] == "O" and Add[0][2]== "O":
      tabuleiro(Add)
      print("O wins")
      vencedor=0
      break
    if Add[0][0] == "O" and Add[1][1] == "O" and Add[2][2]== "O":
      tabuleiro(Add)
      print("0 wins")
      vencedor=0
      break
    if Add[0][2] == "0" and Add[1][1] == "0" and Add[2][0]== "O":
      tabuleiro(Add)
      print("0 wins")
      vencedor=0
      break
    if Add[1][1] == "0" and Add[0][1] == "0" and Add[1][2]== "O":
      tabuleiro(Add)
      print("0 wins")
      vencedor=0
      break
    if Add[2][2] == "O" and Add[2][1] == "O" and Add[0][2]== "O":
      tabuleiro(Add)
      print("0 wins")
      vencedor=0
      break
  else:
    print("Você precisa selecionar um espaço válido")
if vencedor==0:
  vencedor=vencedor
else:
  tabuleiro(Add)
  print("Deu velha")
