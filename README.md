# Tic-Tac-Toe with Minmax

## Problem:
Consider a modification of the classic old game, where:
- The first player plays with – and the second plays with |.
- Each box can have one of these symbols, none or both (in which case it forms a +).
- On each turn, the player cannot play on the same square as the previous player.
- The player who manages to form three + in the same row, column or diagonal wins.<br>
  
For example, the following is a winning setup (where the last move was |):<br>
```+ | + | +<br>
----------
| | – | +<br>
----------
– |   | |```<br>

Say if there is a winning strategy for any of the players involved.
To solve this problem, use the minmax method.
