#set text(font: "Stix Two Text", size: 16pt, weight: "medium")

#let today = datetime.today()
#align(center)[Test-Driven Development Lab]
#set text( size: 14pt)
#grid(columns: (1fr, 1fr), [
    André Plancha \ #text(size:7pt)[#link("mailto:andre.plancha@hotmail.com")] \
    Yana Zlatanova \ #text(size:7pt)[#link("mailto:yana-zlatanova-gold@gmail.com")]
  ],align(right)[
      MALMÖ UNIVERTITY \ #align(bottom)[#today.display("[month repr:long] [day], [year]")]
]
)
#v(-6pt)
#line(length: 100%)
#set text(size: 12pt, weight: "regular")
#set par(justify: true)
#set table(stroke: none)
// #show table: set block(fill: none, width: auto)
#let question(it) = {
  show heading: itt => text(size: 12pt)[#itt.body]
  block(fill: luma(220), inset: 8pt, width: 100%, radius: 1pt, it)
}
#question[*
Answer the following questions for Task 1:
1. Please run the test coverage module, generate the HTML report, and attach the screenshot of test coverage (see the lecture for reference)
*]
#image("Task 1 Coverage.png")
#question[
*2. What types of coverage were measured?*
]
    Line Coverage: The percentage of code lines executed.
    
#question[*3. What is the code coverage you achieved with the test cases?*]
The coverage is 100 %.

#question[
*4. Please state and describe the defect found in the code. (There is a bug!).*
]
The defect in the code is an inconsistency in the CONSTANTS reference strings where 'g' is missing from _LOWER_CONSTANTS and 'D' is missing from _UPPER_CONSTANTS, causing these letters to be treated not as CONSTANTS but as vowels (or other character) and remain unchanged during encoding/decoding which is incorrect.

#question[*5. Which test case (s) found the defect (copy and paste the test case to answer the question)?*]

The defect was found in the test case for encoding and decoding of all CONSTANTS in lower and upper case in a string.


#image("Test Case Bug.png")
#image("Test Case Bug 2.png")


#question[*6. How did you fix the defect(s) found in the code?*]
The bug was mitigated by adding "g" and "D" to the string with reference constants.

/*
Running the tests in task 1
```bash
cd .\TDD_lab_student\
pixi run python Task1_Unittest_rover.py OR pixi run python task1
```
*/

#question[*
Answer the following ques6ons for Task 2: \
1. Please run the test coverage module, generate the HTML report, and attached the  screenshot of test coverage (see the lecture for reference)
*]
#image("screentask2.png")
#question[*2. What types of coverage were measured?*]
Line Coverage: The percentage of code lines executed
#question[*3. How many test cases were written to test the user stories mentioned in task 2?*]
A total of 16 tests we're written, some with a few subtests. Most of them we're one test (with subtests) per story.
#question[*4. What is the code coverage you achieved with the test cases?*]
We achieved 100% code coverage.