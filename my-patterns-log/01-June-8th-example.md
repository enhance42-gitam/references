### Problem

You are given a lowercase alphabet string text.  
Return a new string where every character in text  
is mapped to its reverse in the alphabet,  
so that a becomes z, b becomes y, c becomes x, and so on.

### Sample input and output

"a" => "z"  
"z" => "a"  
"abcdef" => "zyxwvu"  
"suraj" => "hfizq"  
"gitam" => "trgzn"

### Solution

#### Solution #1

```python
def map_a_to_z(ch):
    # get the ascii value
    ascii_value = ord(ch)

    # substract "a"'s ascii value
    ascii_value -= ord('a')

    # use this difference to remove from "z"'s ascii value
    ascii_result = ord('z') - ascii_value

    return chr(ascii_result)


def atbash_cipher_1(text):
    result = ""
    # for each character
    for ch in text:
        # convert this value into a char
        # add to result
        result = result + map_a_to_z(ch)

    return result
```

#### Solution #2

```python
def atbash_cipher(text):
    result_chars = list(map(map_a_to_z, text))
    # result = ""
    # for ch in result_chars:
    #     result = result + ch
    result = "".join(result_chars)
    return result
```

#### Solution #3

```python
def atbash_cipher_3(text):
    # string = take a..z
    a_to_z = "abcdefghijklmnopqrstuvwxyz"

    # rev_string = take z..a
    z_to_a = list(reversed(a_to_z))  # a_to_z[::-1]
    result = ""
    for ch in text:
        # find the index from string a_to_z
        pos = a_to_z.find(ch)

        # use the character in the same index from z_to_a string
        # add each character to result and return
        result += z_to_a[pos]
    return result
```

### Pattern for solutions

We enumerated each element.  
We have mapping function.  
We combined to return the solution.

### Create questions

#### Q #1

Given employee details.  
Return the employees joinned on same date.

#### Q #2

Given the passenger mobile numbers list on a bus.
And collection passenger records.  
Return all the passenger names on the bus.

#### Q #3

Return all the customers who don't have minimum balance of Rs 3000/-.
