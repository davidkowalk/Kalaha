# Kalaha

> Kalah, also called Kalaha, is a copy of the ancient game mancala trademarked in the United States by William Julius Champion, Jr. in 1940. This game is sometimes also called "Kalahari", possibly by false etymology from the Kalahari desert in Namibia.
>
> As the most popular and commercially available variant of mancala in the West, Kalah is also sometimes referred to as Warri or Awari, although those names more properly refer to the game Oware.

\- Wikipedia

## How to play

> This section does not explain the rules, but how to start the game. For rules please look under "Rules".

This is a console implementation of Mancala.
To start the game go into the src-folder and open the console/terminal and start the game with python3:

```
Linux/Mac:
$ python3 ./app.py

Windows:
> python app.py

From now on I will use "python3".
If you are on windows only use "python"
```

You can also provide a game-code which will start the game in a certain configuration:

```
$ python3 app.py "0b06070103000611010503040107"
Layout
╔══╦══╦══╦══╦══╦══╦══╦══╗
║  ║ 6║ 5║ 4║ 3║ 2║ 1║  ║ <- Player 2
║  ╠══╬══╬══╬══╬══╬══╣  ║
║  ║ 1║ 2║ 3║ 4║ 5║ 6║  ║ <- Player 1
╚══╩══╩══╩══╩══╩══╩══╩══╝

GAME

    ╔══╦══╦══╦══╦══╦══╦══╦══╗
    ║  ║ 7║ 1║ 4║ 3║ 5║ 1║  ║
    ║11╠══╬══╬══╬══╬══╬══╣17║
    ║  ║ 6║ 7║ 1║ 3║ 0║ 6║  ║
    ╚══╩══╩══╩══╩══╩══╩══╩══╝

Player 1:
```

The players then take turns choosing a position to play the stones from by providing a number from 1 to 6. The positions are numbered as follows:

```
╔══╦══╦══╦══╦══╦══╦══╦══╗
║  ║ 6║ 5║ 4║ 3║ 2║ 1║  ║ <- Player 2
║  ╠══╬══╬══╬══╬══╬══╣  ║
║  ║ 1║ 2║ 3║ 4║ 5║ 6║  ║ <- Player 1
╚══╩══╩══╩══╩══╩══╩══╩══╝
```

The players can also exit the game by typing "exit". This will provide a game-code.

## Rules
The board is divided into two sets of 6 positions each filled with 6 stones and one House (Mancala) for each player.

```
╔══╦══╦══╦══╦══╦══╦══╦══╗
║  ║ 6║ 6║ 6║ 6║ 6║ 6║  ║
║0 ╠══╬══╬══╬══╬══╬══╣ 0║
║  ║ 6║ 6║ 6║ 6║ 6║ 6║  ║
╚══╩══╩══╩══╩══╩══╩══╩══╝
```

Player one starts by choosing a position and spreading the stones in their position counter-clockwise, putting one in their own Mancala (the first to encounter) if passed, but not in the opponents.

```
Example:
╔══╦══╦══╦══╦══╦══╦══╦══╗
║  ║10║ 3║ 9║10║ 0║ 9║  ║
║ 2╠══╬══╬══╬══╬══╬══╣ 5║
║  ║ 3║ 2║10║ 9║ 0║ 0║  ║
╚══╩══╩══╩══╩══╩══╩══╩══╝
     ^
     |
     Player 1 plays position 1

Result:
╔══╦══╦══╦══╦══╦══╦══╦══╗
║  ║10║ 3║ 9║10║ 0║ 9║  ║
║ 2╠══╬══╬══╬══╬══╬══╣ 5║
║  ║ 0║ 3║11║10║ 0║ 0║  ║
╚══╩══╩══╩══╩══╩══╩══╩══╝

Try it with the code: 0203020a0900000509000a09030a
```

If a player ends their turn on an empty position of their own and the opponents position opposite to the empty one has any stones in it the last stone played and the opponents stones in that opposing position are put into the players Manala.

```
Example:
╔══╦══╦══╦══╦══╦══╦══╦══╗
║  ║ 7║ 7║ 7║ 7║ 8║ 0║  ║
║ 1╠══╬══╬══╬══╬══╬══╣ 2║
║  ║ 1║ 0║ 8║ 8║ 8║ 8║  ║
╚══╩══╩══╩══╩══╩══╩══╩══╝
     ^
     |
     Player 1 plays position 1

Result:
╔══╦══╦══╦══╦══╦══╦══╦══╗
║  ║ 7║ 0║ 7║ 7║ 8║ 0║  ║
║ 1╠══╬══╬══╬══╬══╬══╣10║
║  ║ 0║ 0║ 8║ 8║ 8║ 8║  ║
╚══╩══╩══╩══╩══╩══╩══╩══╝

Try it with the code: 0101000808080802000807070707
```

If a player ends their turn in their own Mancala they may play again.

If a player has no more possible moves all the stones on each side get counted up. The player with more stones wins.
