# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
The recommender generates recommendations from music in the csv file based on energy, mood, etc. match of a user preference.
- What assumptions does it make about the user
It assumes the wil  provide preferences for genre, mood, and energy  
- Is this for real users or classroom exploration  
For now, its using classroom exploration as the user profiles are hardcoded.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
The song's genre, mood, and energy level are the main factors.
- What user preferences are considered  
We consider the user preference for genre, mood, and energy level.
- How does the model turn those into a score  
Each song gets assigned points based on matching the user's preferences. The final score is the total of the points.
- What changes did you make from the starter logic  
The recommemder uses weights in the scoring system. The most important or weighted factor is genre. 

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
There are 40 songs in the catalog
- What genres or moods are represented 
Rock, pop, Electronic, lofi, etc. 
- Did you add or remove data  
No, I neither added or removed songs
- Are there parts of musical taste missing in the dataset  
Yes, classical, rap, country and other emerging musical tastes are not represented in the dataset

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
Users that have a clear understanding of musical preferences are at an advantage. For example, there is more data for lofi and pop genres.
- Any patterns you think your scoring captures correctly  
Assigning added weight and points for artist preference represents real life.
- Cases where the recommendations matched your intuition  
People who like a certain genere like lofi will see those songs more likely to be recommended

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
It does not consider bpm (beats per minute), danceability, and more.
- Genres or moods that are underrepresented  
Lofi and pop are overrepresented and other generes like ambient, jazz, etc. are underrepresented appearning only once.
- Cases where the system overfits to one preference  
Yes, the system overfits on genre matches with +2.0
- Ways the scoring might unintentionally favor some users  
The Lofi users may recevie the best recommendations as that is what most of the dataset is made of.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
I tested user profile for upbeat_pop, intense_rock, chill_lofi, and a few other adversarial profiles.
- What you looked for in the recommendations  
In the recommendation, I looked for songs which match the user preferences.
- What surprised you  
I was suprised that AI suggested dislike system, which mimics real life, where users may not enjoy a certain genre.
- Any simple tests or comparisons you ran  
Yes, I ran adversarial tests and edge cases.

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
In the future, the model can be improved by adding tempo and release_year into the preference system.
- Better ways to explain recommendations
  We explained why the song was recommended, but we could explain how it compares to others 
- Improving diversity among the top results  
Introduce more variety in dataset or penalty for frequently seen songs.
- Handling more complex user tastes  
An idea we considered was activity based recommendations for example rock and pop may be best for exercise while slower lofi beats maybe more optimal for study.
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
I learned recommender systems use a scoring system to match user preferences
- Something unexpected or interesting you discovered
The edge and adverserial case proved how no one system is perfect and should always be improved.
- How this changed the way you think about music recommendation apps  
I have more appreciation for recommendation apps that can adjust and be dynamic.