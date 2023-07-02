
# Advent Of Code 2016 Solutions
Advent of Code 2016 solutions in Python. All the way from Day 1 - Day 25. Includes second parts.
Some include visual solutions and some don't. 


## Day 1
We have to navigate given only a direction and magnitude. Similar to polar coordinates.

 - We can solve this by using a **cartesian grid** and try to locate our current direction.
 - Then, we can use that information to multiply our distance by **-1** and **1** and move.
 - We also know that every other turn moves in the **same axis**. 
 - This can help us to know whether to move **up and down** or **left or right**. That's it!

## Day 2
We have to figure out the passcodes based off a direction manual. Simply manuevering around.

 - We can create a **vector class** to help us move around easily
 - If the movement goes **out of grid**, we don't **apply** it
 - Just do the same for other grid except for **5x5** and check if cell is **empty**


