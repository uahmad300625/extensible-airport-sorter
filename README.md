# Airport Sorting Console Program
A console program that sorts a list of airports by a user-selected criterion — IATA code, name, city, state, delay status, temperature, or city-then-name — and prints the results to the console. Designed so new sorting criteria can be added without modifying any existing code.

## How It Works
Each airport has an IATA code, name, city, state, current temperature, and delay status. The program presents a menu of available sorting criteria, lets the user pick one, and prints the sorted list with the airport name in all caps.

```
Available sorting criteria:
1.)  City
2.)  Delay
...

Sort the airports by entering a criteria's respective number (or 'q' to quit):
```

## Design
The core design goal was: adding a new sorting criterion should require adding a new file, never editing existing ones.

- **`airport.py`** — the `Airport` data class.
- **`airport_data.py`** — the source data (a hardcoded list of airports).
- **`process_airports.py`** — sorts a list of airports given a sort-key function. Has no knowledge of what the available criteria are.
- **`sorting_criteria/`** — one small file per sorting criterion (e.g. `sorting_criteria_city.py`), each exposing a `criteria_to_sort_on` function used as the sort key.
- **`fetch_criteria.py`** — discovers available criteria by scanning the `sorting_criteria/` folder.
- **`fetch_a_criterion.py`** — dynamically imports the chosen criterion module using `importlib`.
- **`airport_sorting_console_program.py`** — the console entry point that ties everything together.

### Design principles applied

- **Open/Closed Principle** — new sorting criteria can be added by dropping a new file into `sorting_criteria/`, following the existing naming convention. No existing file needs to change.
- **Single Responsibility Principle** — `process_airports` only handles sorting; `fetch_a_criterion` is solely responsible for resolving a criterion name into a usable sort key.
- **Don't Repeat Yourself** — sorting logic lives in exactly one place (`process_airports`), rather than being duplicated across each criterion file.

## Tech Stack

- **Python**
- `dataclasses` — for the `Airport` model
- `importlib` — for dynamic module loading
- **unittest** — test suite, written using TDD

## Lessons Learned

### What design principles did you use in this project?

One of the design principles we used in this project was the Open-Close Principle.
OCP was a major aspect of this program since we had to ensure that new criteria could be added without modifying existing code.
We kept OCP in mind when designing and implementing various functions to allow for extension. 
Because of this, if anyone wants to add new criteria, they can do so by creating a new file that follows the formatting of the other sort_criteria files.
The existing files do not need to be modified in order for the new criteria to work with the application.

Another principle we used was the Single Responsiblity Principle.
This allowed for our functions to be more concise and cohesive.
For instance, process_airports requires a sort criteria, that will be used as a key for sorting, to be passed in. 
Instead of implementing that logic all in process_airports, fetch_a_criterion handles retrieving a criterion to then pass into process_airports.
process_airports now only has to handle the sorting, thus any changes to the function would be limited to the sorting.
This helped with making our code more maintainable and flexible for changes.

One other principle we used was Don't Repeat Yourself.
We tried to keep this in the back of our minds when working on the application. 
For instance, we originally designed process_airports where each sorting criteria housed a sorting function.
So when process_airports was called with a particular criterion, the criteria file would sort the airports and then return the sorted list.
This violated DRY since the sorting criteria would have repeat code of calling the sort function.
Through feedback, we designed process_airports to have the sort function while the criteria files would return the criterion the sort would use.
That way the sorting function code was only in one place instead of being repeated in multiple places.


### Any interesting lessons you learned in this project?

One lesson we learned is to request multiple reviews in a day in order to get more feedback.
In projects 1 and 2, we didn't take full advantage of the feedback opportunities as much as we could. We were aiming for 1 review a day.
However, we realized that was not enough to progress the projects effectively. 
For this project, we tried to shoot for as many reviews as we could achieve in a day.
It helped us move forward with the project much quicker and get the feedback faster so we could improve our design.

Another lesson we learned is to ask more questions and try to discuss solutions when we are stuck.
We didn't do that for the last two projects and it was detrimental to us.
This time around we put more effort into discussing solutions together and if we could not come to a good answer we would email you.
It showed that it is not wrong to ask questions that lead to discussions about better design decisions.

Another lesson is that following good design practices will lead to better applications.
It sounds obvious, but learning that many companies slack off in this regard is crazy to hear.
I couldn't imagine going to work every day knowing it was going to be a nightmare to deal with the code.
Although it was hard at times to follow good practices, it resulted in a significantly better application than if we hadn't.
If we want to add on to this application, it is in a good state to be extended and we don't have to worry about changing a ton of stuff first.


### Any surprises or things that you did not expect?

One thing that we did not expect was how much discipline is required to adhere to design principles.
So many times we felt it would be much simpler to allow OCP or DRY to be violated.
But looking back at the code now, it's amazing that the application is much more extensible than we could have imagined at the beginning of the project.

There were also a lot of techniques and tools that we did not know existed that we got exposed to.
For instance, we did not know there was a module that allowed for dynamic importing.
Additionally, using an empty tuple as a valid key for sorted() was something we never knew was possible if it wasn't for the professor's help.

Furthermore, there was one point where we were told to change all the sorting_criteria function names to criteria_to_sort_on.
This confused us because it seemed to contradict our learning that function/variable names should be clear and purposeful.
It wasn't until we started implementing fetch_a_criterion and discovered the importlib module that we realized why it needed to be changed.
It was mind-blowing, it showed that with proper knowledge and understanding of the tools you have, it gives you more flexibility to create better design.
