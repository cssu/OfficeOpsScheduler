# Office Operations Scheduling

Scheduling script for CSSU lounge (BA2250) office operations, by solving a Constraint Satisfcation Problem (CSP). Yes, you should take [**CSC384**](https://fas.calendar.utoronto.ca/course/csc384h1).

## Usage

1. Prepare `<input.csv>` (with headers) where each cell is the list of people available to serve that time. Here is an example:

   ```csv
   Time/Day,Tue,Wed,Thu
   9:00 AM,A|B,,A|B
   10:00 AM,,,
   11:00 AM,,C,C
   12:00 PM,,,
   1:00 PM,A|B,A|B|C,
   ```

2. Check/edit hyperparameters.

   ```py
   ### USER HPARAMS

   # sort by least available first
   people_sorting = lambda p: (len(availability[p]), float("inf")
                              if p not in required else -required[p])

   # sort by latest times first
   time_sorting = lambda t: -t[1]

   # require two slots per person
   required = dict([(p, 2) for p in availability])

   # custom required slot for "A"
   required["A"] = 3

   # describe how many header rows/columns in the CSV
   header = (1, 1)

   ### END HPARAMS
   ```

3. Run the script to produce `<output>.md`.

   ```sh
   python scheduler.py <input.csv> <output.md>
   ```

   The resulting file looks like this.

   ```md
   | Time/Day | Tue | Wed | Thu |
   | -------- | --- | --- | --- |
   | 9:00 AM  | A   |     | A   |
   | 10:00 AM | A   |     |     |
   | 11:00 AM |     | C   | C   |
   | 12:00 PM |     |     |     |
   | 1:00 PM  | B   | B   |     |
   ```
