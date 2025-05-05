# Reflection

Student Name:  name
Sudent Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
At first I honestly didn’t understand what this assignment was asking for. I thought it would just be some basic pandas, but then I saw that it involved building a whole ETL pipeline with real data and pushing to S3. I’ve never done anything like that before, so it took me a while to get into it. Once I broke it into steps (extract, transform, load), it made more sense.

I learned how to use `pandas.read_csv()` from Google Sheets, how to use `read_html()` to get tables from websites (even though I had to install lxml which confused me at first), and how to normalize columns like salary using cost of living data. I also practiced writing helper functions like `clean_currency` and `extract_year_mdy` which we used to clean data consistently.

The part that confused me most was the transformation step. There were so many columns with long names that had to match exactly, and I kept getting KeyErrors. Eventually I printed out the column names to fix them, which was helpful. I also didn’t realize at first that merging data by city would be hard since the formats were slightly different. Creating that `_full_city` column helped a lot.

Another challenge was figuring out how to upload to MinIO since I’ve never used boto3 before. But once I ran the script and saw the files show up in the S3 bucket, I was okay.

If I were to do this again, I’d want to get better at writing cleaner pivot tables and maybe handling errors better when merging data. Overall, this assignment helped me understand what an actual data pipeline looks like, and it made me feel more confident working with real-world data.

