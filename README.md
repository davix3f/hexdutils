# hexutils

**Hexutils** is a little (little little little) Python library to deal with hexadecimals.
Int to hex, hex to int, operations between hex.

The code is in **dev** branch.

## Usage

Function names are very clear by themselves, but here's a guide.

##### **intohex** (<int>number, [hex_prefix, uppercase])
  Returns a the hex value of a number as a string
  * Arguments:
    **Mandatory**:
    * [int] number: the integer to convert
  **Optional**:
    * [bool] hex_prefix: adds "0x" at the beginning of the output, like the native `hex` Python function. Set as *False* by default
    * [bool] uppercase: every letter in the output is uppercased. Set as *False* by default
##### **hextoint** (<str>target)
  Returns the value of an hex as an integer
  * Arguments:
  **Mandatory**:
    * [str] target: the hex value to convert. Accepts also "0x" values
##### **Operations**

|   Function	|  Operator 	|
|:-:	         |:-:	|
|**hex_add**     |  +   |
|**hex_subtract**|  -   |
|**hex_multiply**|  *   |
|**hex_divide**  |  //  |
|**hex_floor**   |  %   |
  
 The arguments for those functions are all the same:
  * **Mandatory**:
    * <str>value\_one
    * <str>value\_two
    * [bool] hex_output: if set as True, the operation result will be returned as an hex value. If set as False, an integer will be returned
  
  * **Optional**:
    * [bool] hex\_output\_prefix: If set as True, adds "0x" at the beginning of the output. Set as *False* by default
    * [bool] hex\_output\_upper: If set as True, every letter in the output is uppercased. Set as *False* by default
