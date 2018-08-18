# hexdutils
[![PyPI version](https://img.shields.io/pypi/v/hexdutils.svg)](https://pypi.python.org/pypi/hexdutils/)
[![GitHub license](https://img.shields.io/github/license/davix3f/hexdutils.svg)](https://github.com/davix3f/hexdutils/blob/master/README.md)

**hexdutils** is a little (little little little) Python library to deal with hexadecimals.
Int to hex, hex to int, text-to-hex, operations between hex.

The code is in **dev** branch.

## Usage

Function names are very clear by themselves, but here's a guide.

### intohex (`int` number, [`bool` hex_prefix, `bool`uppercase])
  Returns a the hex value of a number as a string.
  * **Arguments**:
    * **Mandatory**:
      * `int` number: the integer to convert;
    * **Optional**:
      * `bool` hex_prefix: adds "0x" at the beginning of the output, like the native `hex` Python function. Set as *False* by default;
      * `bool` uppercase: every letter in the output is uppercased. Set as *False* by default;

### hextoint (`str` target)
  Returns the value of an hex as an integer.
  * **Arguments**:
    * **Mandatory**:
      * `str` target: the hex value to convert. Accepts also "0x" values;

### abctohex (`str` target, `str` conversion, [`bool` verbose, `bool`|`str` prefix, `bool`|`str` individual_prefix])
  Returns text converted in hex. Randomization available.
  * **Arguments**
    * **Mandatory**:
      * `str` target: text to convert;
    * **Optional**:
      * `str` conversion: the letter values to be used. "alphabet" uses the position of each letter in the alphabet to assign an integer value (e.g a=1, b=2, etc.). "ord" uses the result of `ord(letter)` (e.g `ord("a") = 97`). Set as *"ord"* by default:
      * `bool` verbose: if *True*, some additional logs will
      be printed. Set as *False* by default
      * `bool`|`str` prefix: if set as *True*, the "0x" prefix
      will be added to the output. Also, you can type a custom
      prefix and it will be added. Set as *False* by default.
      * `bool`|`str` individual_prefix: if set only as True,
      each hex value in the output will have the "0x" prefix.
      Like `prefix`, you can set this value to a custom prefix string, and use it instead of "0x". **Requires `prefix=True` to work**.
      Set as *False* by default

### hextoabc (`str` target)
  * **Arguments**:
   * **Mandatory**:
      * `str` target: hex value to convert to text.

### Operations

|   Function	|  Operator 	|
|:-:	         |:-:	|
|**hex_add**     |  +   |
|**hex_subtract**|  -   |
|**hex_multiply**|  *   |
|**hex_divide**  |  //  |
|**hex_floor**   |  %   |

 Usage: `operation(<str>value_one, <str>value_two, [<bool>hex_output, <bool>hex_output_prefix. <bool>hex_output_upper])`

 The arguments for those functions are all the same:
  * **Mandatory**:
    - `str`  value\_one;
    - `str`  value\_two;
    - `bool` hex_output: if set as True, the operation result will be returned as an hex value. If set as False, an integer will be returned;

  * **Optional**:
    - `bool` hex\_output\_prefix: If set as True, adds "0x" at the beginning of the output. Set as *False* by default;
    - `bool` hex\_output\_upper: If set as True, every letter in the output is uppercased. Set as *False* by default;
