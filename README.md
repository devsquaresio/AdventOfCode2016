
# Advent Of Code 2016 Solutions
Advent of Code 2016 solutions in Python. All the way from Day 1 - Day 25. Includes second parts.
Some include visual solutions and some don't. You can check in the folders, or it says here.


## Day 1 *(Has visualized solution)*
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

## Day 3
Very easy day
 - We can easily just use **string functions** to get our values and **sort** them
 - If the highest value is **less** than the **sum of the two others**, they form a **triangle**
 - For the second part, we can use **enumerate** to help us look into the **two next rows**
   and fix from there

## Day 4 *(Has visualized solution)*
Finding if the rooms are true or not. Not that hard.
 - First, we create a **dictionary** to help us keep track of letter count
 - Then, we just do some list slicing and check if the room letters are true
 - Second part, we can create a decode function to shift the letters
 - I was checking, and if the room letters decode to "northpole object storage", return id

## Day 5
Hashing. No other way than to brute force.
 - We just check the hash to see if it has **five zeros** and keep on incrementing
 - For second part, we just do the same except grab **first and second nonzero** for
   the index and value, and make sure not to replace any spots

## Day 6
We can use some stuff from Day 4, like the dictionary
 - To get the columns, we make a **grid** and the **corresponding** index goes to the **list** in grid.
   (Ex: The **zeroth** index of an array goes in the **zero** index array)
 - Then, we just do the most popular letter thing like in **Day 4** and we **combine** all the letters
 - For second part, we **don't reverse** our sorted array and create another **variable** for the answer

## Day 7
Not a hard day, just don't misundertand the directions like I did.
 - We just check if the four letters we are on right now are equal to the first and second and second and first
 - For part two, we create a list for the hypernet
 - Then, we check if the three leters we are on are equal to the first, second, and first
 - And then in the hypernet, we check if the inverse is there, the BAB, and that is our answer

## Day 8
Just need a little bit of memory to do the problem.
 - The rect part is easy, just loop over ranges and make it '#'
 - For the rotate, I just create a temp array to store the row and column
 - Then with the help of mod, I loop through temp and move them all
 - For second part, I just print the pixel screen


