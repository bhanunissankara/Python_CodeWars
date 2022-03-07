# Algorithm Basics - Python

## Overview

1. Ask questions
1. List inputs/outputs
1. Write code
    1. Define the function (including end curly brace)
    1. Define a result variable and return it
    1. Determine the output value in the empty case
    1. Write the for loop (including end curly brace)
    1. Assign the variable (if needed)
    1. Fill in the for loop - alter result in some way
1. Test the code

## Example

_Problem Statement:_ Write a function that takes an array of numbers, and returns the sum of its elements.

## Step 1: Ask Questions

Before coding, it's good to ask a few questions to make sure you understand the problem completely.

It's a good idea to consider the empty case, very large inputs, and unexpected inputs.

For example, some questions you might ask about the `sum` problem are:

- What should the function return when given an empty array?
- Should the code handle non-numbers in the array?
- Should the code handle the case where the array itself is null?

## Step 2: Write down some example inputs and outputs

Before writing code, it's good to have a sense of what success looks like by jotting down some inputs / outputs.

For example in this problem, some sample inputs / outputs might be:

```js
// [1,2,3] => 6
// [] => 0
// [-2, 0, 3] => 1
```

## Step 3: Write "Sandwich Code"

The final code will look like this:

```python
def sum(numbers):
    result = 0
    for number in numbers:
        result += number
    
    return result
```

But unlike English, it's generally not a good idea to write code from top to bottom. Instead, write it "outside in."

#### Applying the Process

1. Define a function

    How many inputs does it take? => 1 (an array of numbers)

    Define the function (and optionally add `pass` just to make it compile).

    ```python
    def sum(numbers):
        pass
    ```

    Run your program (or run the tests) to ensure that you have valid syntax.

2. Determine the output value in the empty case

    Questions to ask at this stage:

    What is the empty case? That is, what should the function return when passed an empty input?

    The empty case here is passing an empty array. When you sum an empty array, return `0`.

    Use `0` as the initial value of the result.

    Add `return result` at the bottom.

    ```python
    def sum(numbers):
        result = 0
        
        return result
    ```

    Run your program (or run the tests) to ensure that you have valid syntax.

3. Write the `for` loop

    Questions to ask at this stage:

    - Where should the loop start?
    - When should the loop exit?
    - How much should the counter change on each iteration?

    In this case, a simple `for in` loop will work.

    ```python
    def sum(numbers):
        result = 0
        for number in numbers:
            pass
        
        return result
    ```

    NOTE: sometimes you may need the index of the item in the list, in which case you can use `enumerate`:

    ```python
    def sum(numbers):
        result = 0
        for i, number in enumerate(numbers):
            result += number
        
        return result
    ```

    NOTE: if instead of hitting every element in the list, you want to skip some you can iterate over the range:

    ```python
    def sum(numbers):
        result = 0
        for i in range(0, len(numbers), 2) :
            number = numbers[i]
            reslt += number
        
        return result
    ```

    Run your program (or run the tests) to ensure that you have valid syntax.

4. Fill in the `for` loop

    Questions to ask at this stage:

    - What are all the variables I have available to me inside the loop?

    Inside the for loop for sum, you have several variables:

    ```python
    def sum(numbers):
        result = 0
        for number in numbers:
            # numbers    => [1,3,5,7,2]
            # result     => starts as 0
            # number     => the actual number in the array  

        return result        
    ```

    For problems like this, you have to modify the result somehow.  At this point, the function looks like this:

    ```python
    def sum(numbers):
        result = 0
        for number in numbers:
            result = ??
        
        return result
    ```

    For sum, we have:

    ```typescript
    def sum(numbers):
        result = 0
        for number in numbers:
            result += number
        
        return result
    ```

## Step 4: Test the code

Pick an input from Step 2 - for example `[1,2,3]`.

Build a table that contains your variables at the start of the loop, like so:

```python
def sum(numbers):
    result = 0
    for number in numbers:
        # ----- what are the variables right here?? -----
        result += number
    
    return result
```

|result|i|num|
|-|-|-|
|0|0|1|

Then run the code through your head and figure out how result will change, and add the next row.

This is what you'll end up with:

|result|i|num|
|-|-|-|
|0|0|1|
|1|1|2|
|3|2|3|
|3| | |


## Tips and Tricks

**When defining a function**

If you can, find a human-readable name for parameters. "start" is better than "x".

**When finding default values for the result variable**

Common values for default values are:

- `""` - empty string
- `[]` - empty list
- `{}` - empty dictionary
- `0` - zero
- `None` - zero

It won't always be one of these things, but this is a good place to start.

Sometimes figuring out the default value can be tricky.

If you are asked to find the smallest number in an array, what's the empty case there? Zero is a bad choice, because there could be numbers smaller than zero, so choose `None`.

#### Codewars Problems

Level 8:

- [Array plus array](https://www.codewars.com/kata/5a2be17aee1aaefe2a000151)
- [Alternating Case](https://www.codewars.com/kata/56efc695740d30f963000557)
- [Abbreviate a Two Word Name (split, join)](https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3)
- [Create phone number](https://www.codewars.com/kata/525f50e3b73515a6db000b83)
- [Check the exam](https://www.codewars.com/kata/5a3dd29055519e23ec000074)
- [CSV representation of array](https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036)
- [Convert number to reverse array of digits](https://www.codewars.com/kata/5583090cbe83f4fd8c000051)
- [Draw Stairs](https://www.codewars.com/kata/5b4e779c578c6a898e0005c5)
- [Find the Difference in Age between Oldest and Youngest Family Members](https://www.codewars.com/kata/5720a1cb65a504fdff0003e2)
- [Filling an array (part 1)](https://www.codewars.com/kata/571d42206414b103dc0006a1)
- [Find Multiples of a Number](https://www.codewars.com/kata/58ca658cc0d6401f2700045f)
- [Find first non-consecutive number](https://www.codewars.com/kata/58f8a3a27a5c28d92e000144)
- [Generate range of integers](https://www.codewars.com/kata/55eca815d0d20962e1000106)
- [Get the mean of an array](https://www.codewars.com/kata/563e320cee5dddcf77000158)
- [Grasshopper Summation](https://www.codewars.com/kata/55d24f55d7dd296eb9000030)
- [Invert values](https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad)
- [Lario and Muigi Pipe Problem ← array start/end](https://www.codewars.com/kata/56b29582461215098d00000f)
- [N-th Power](https://www.codewars.com/kata/57d814e4950d8489720008db)
- [Life Path Number](https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0)
- [Multiplication table for number](https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce)
- [Sum of positive](https://www.codewars.com/kata/5715eaedb436cf5606000381)
- [Removing Elements](https://www.codewars.com/kata/5769b3802ae6f8e4890009d2)
- [Reversed Words](https://www.codewars.com/kata/51c8991dee245d7ddf00000e)
- [Reversed Sequence](https://www.codewars.com/kata/5a00e05cc374cb34d100000d)
- [Reversed strings](https://www.codewars.com/kata/5168bb5dfe9a00b126000018)
- [Smallest unused ID](https://www.codewars.com/kata/55eea63119278d571d00006a)
- [Square(n) sum](https://www.codewars.com/kata/515e271a311df0350d00000f)
- [Speed Code #2 - Array Madness](https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1)
- [String Repeat](https://www.codewars.com/kata/57a0e5c372292dd76d000d7e)
- [Total amount of points](https://www.codewars.com/kata/5bb904724c47249b10000131)
- [Testing 1-2-3](https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9)
- [Remove First and Last Character](https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0)
- [Remove String Spaces](https://www.codewars.com/kata/57eae20f5500ad98e50002c5)
- [A Needle in the Haystack](https://www.codewars.com/kata/56676e8fabd2d1ff3000000c)
- [Count the Monkeys!](https://www.codewars.com/kata/56f69d9f9400f508fb000ba7)
- [How good are you really?](https://www.codewars.com/kata/5601409514fc93442500010b)
- [If you can't sleep, just count sheep!!](https://www.codewars.com/kata/5b077ebdaf15be5c7f000077)
- [Count by X](https://www.codewars.com/kata/5513795bd3fafb56c200049e)
- [The old switcheroo - hard](https://www.codewars.com/kata/55d410c492e6ed767000004f)
- [Elevator Distance - a little hard](https://www.codewars.com/kata/59f061773e532d0c87000d16)