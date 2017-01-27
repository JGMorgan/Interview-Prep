Technical Interview Prep
========================

Having just graduated with my Computer Science degree I spent a lot of time this
last semester practicing for interviews and interviewing with various companies.
I've interviewed with startups you've probably never heard about that have
single digit employees and tech giants like Amazon, Google and Facebook.

This is a collection of interview problems I've received in the past as well as
some other common interview problems all solved as efficiently as possible. Feel
free to submit pull requests with problems you've been asked in the past.

Some Tips and Things to Study
-----------------------------

### Be Honest
While interviewing if you've seen a problem before just be honest about it.
Don't act like you've never seen this problem before and then pretend to
struggle. Your interviewer has probably asked this question before to many other
candidates and they know what real struggling looks like, they can spot your
(bad) acting from a mile away. Keep in mind your interviewer is trying to figure
if you'd make a good coworker and nobody wants to work with a liar.

### Act Natural
Chances are you've probably spent a good amount of time with fellow engineers so
you know what they're like. If you're doing a technical interview then your
interviewer is going to be an engineer. Don't forget they're judging how good of
a coworker you would make.Just act like you would around other engineers even if
non engineers wouldn't consider your behavior to be normal.

### Big Oh
**This is extremely important.** You should be able to tell someone the time and
space complexity of your algorithm without having to think about it. Often times
you will be told to write and algorithm and you will be given a target time and
space complexity or you will be told to write an algorithm and be asked about the
time and space complexity after you implement it.

If you can't figure out the time and space complexity of most of the algorithms
implemented here in less than a minute you **NEED** to study up on Big Oh.

### String Manipulation
While manipulating strings might be easy make sure you know how to efficiently
mutate strings in your language of choice.

For example, if you're using Java and you use a String instead of StringBuilder
you're going to get laughed at.

### Hash Tables
**This is the most important Data Structure.**

They are O(1) to insert, delete, and get. To quote my data structures professor
"Hash Tables are the blue dream of data structures"

Every language has it's own implementation and you better know how to use it in
the language you're interviewing with. Many of the problems you receive in an
interview can be easily and efficiently solved using hash tables.

For every single problem you get during an interview your first thought should
be "can I solve this using a hash table?", I can tell you from experience that
there is a pretty good chance you can.

### Bit Manipulation
For most people these seem to be the hardest problems. Typically if you solved
a problem with a hash table and your interviewer says the dreaded words "Good,
now do it without extra space" this means its time to whip out your knowledge
of boolean algebra.

Try to translate binary operations into normal terms. If you are trying to see
what bits are different in two binary strings then XOR will do the trick but if
you want to see what is identical in two binary strings then AND will do it.

### Language Choice
Unless you're interviewing for a start up typically you are free to choose any 
programmer language. Always choose a language that is very readable and one 
that the interviewer is likely to know. That being said do not use a purely 
functional programming language. Some interviewers probably won't be able to 
understand your code and you don't want that. If they don't understand it means 
you have to do a really good job of explaining even if your code does work. 

Make sure you are extremely comfortable with atleast one Object Oriented 
language. Some good choices are Python, Ruby, Java, C# and C++. Those languages 
are very commonly used by candidates so your interviewer should be able to 
understand and if they don't know one of them the syntax should be familiar 
enough that they will understand. 

I highly recommend Python or some other very high level language since you can 
implement more with less lines of code and time is limited during the interview.

### How to Answer an Algorithm Question
Now that you know what kind of questions you might get and what Big Oh is you
actually have to come up with solutions to algorithm questions. **Don't be
afraid to give a solution that isn't optimal.** You might think that it is
obvious but your interviewer doesn't know what you're thinking. So if you come
up with an obvious solution just say it and then try to improve.

Think about what the optimal time complexity could be.
If our problem involves searching through an entire list of elements then our
lower bound is probably O(n) but if that list has some special properties we
might be able to solve it with some variation on binary search.
If the problem involves finding multiple elements then maybe a hash table can
help.
If you know when to use certain data structure and some of the graph algorithms
optimizing your solution shouldn't be too difficult.
While you're trying to improve your solution you should be thinking out loud.
Don't let there be any silence through out the interview, talk to them about the
optimizations you have in mind and their pros and cons.

Now that you have an algorithm, writing the code should be pretty easy. Just
make sure you keep your code clean and very readable. Like I mentioned earlier,
silence is bad so feel free to talk to your interviewer while you're writing
code. 

Now on to testing. Way too many people come up with a solution, write the code
to their solution and then say "here you go". **Always test your solution.**
Create a few test inputs, don't forget to include a few edge cases and walk your
interviewer through the code and explain what happens at every step with those
inputs. If you have the option to run the code you should still walk your
interviewer through your code but you should run it just to confirm.

### Design Questions
These typically do not involve coding but at times will involve coding. When
these questions do require coding it usually does not involve any complex
algorithms so do not worry.

Make sure you know good Object Oriented practices and how to scale your
application. For these questions there are no right answers but plenty of wrong
answers.

**Be prepared to answer the question "Why?".** Regardless of how good of a
certain design decision is there is a good chance they are going to tell you
something that you could've done instead. **This doesn't mean that what you said
is wrong or that you should back down.** Argue your point and if you know what
you're talking about then this interview should be a breeze.
