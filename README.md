# Position Generator

Randomly generates positions for the non-GDS members of the trumpet section for Purdue's "All-American" Marching Band.

## Usage

<pre><code>./generate.py &ltfile with formatted list of names></pre></code>

## Input File Format

The file you pass to the script should be in the format of:
<pre><code>&ltassignment code>|&ltfirst last>|&lt*optional number*></pre></code>
The possible assignment codes are:

| Assignment Code | Meaning |
| --------------- |:-------:|
| m               | Signifies a marcher who will be randomly switched around |
| c               | Signifies a constant marcher |
| g               | Signifies a member of GDS for the week |

Constant in this instance refers to a 1, 10, 5, or 6, or people whose spots you wouldn't want to change. GDS are not included in the assignment process and marchers are people who will be randomly switched around.

## Example

Here's an example of what an input file would look like:
<pre><code>
c|Alex A.|10
m|Bobby B.
c|Colin C.|11
m|David D.
m|Ethan E.
g|Faith F.
</pre></code>

In this example, Alex and Colin would keep their original spots of 10 and 11 respectively, Bobby, David, and Ethan would be randomly switched around, and Faith wouldn't be included in the final list.
