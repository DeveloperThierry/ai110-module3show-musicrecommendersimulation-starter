import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initializes the Recommender with a list of songs."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Recommends a list of songs to a user based on their profile."""
        # This is the OOP part, we will focus on the functional implementation first
        # as per the user's request on the recipe.
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explains why a song is recommended to a user."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric strings to actual numbers
            for key in ['energy', 'tempo_bpm', 'valence', 'danceability', 'acousticness']:
                if key in row and row[key]:
                    try:
                        row[key] = float(row[key])
                    except (ValueError, TypeError):
                        row[key] = 0.0 # or some other default value
            row['id'] = int(row['id'])
            songs.append(row)
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Genre Match: +2.0 points
    if song.get("genre") == user_prefs.get("favorite_genre"):
        score += 2.0
        reasons.append("+2.0 for Genre match")

    # Mood Match: +1.5 points
    if song.get("mood") == user_prefs.get("favorite_mood"):
        score += 1.5
        reasons.append("+1.5 for Mood match")

    # Energy Similarity: Up to +1.0 point
    if "target_energy" in user_prefs and "energy" in song:
        energy_diff = abs(user_prefs["target_energy"] - song["energy"])
        # Award points only if the energy is reasonably close (e.g., diff < 0.5)
        if energy_diff < 0.5:
            energy_score = 1.0 * (1 - (energy_diff / 0.5)) # Scale to 0-1
            score += energy_score
            reasons.append(f"+{energy_score:.2f} for Energy similarity")

    # Acoustic Bonus: +1.0 point
    if user_prefs.get("likes_acoustic") and song.get("acousticness", 0) > 0.6:
        score += 1.0
        reasons.append("+1.0 for Acoustic bonus")

    return (score, reasons)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        if score > 0:
            explanation = f"This song is a good match because of: {', '.join(reasons)}."
            scored_songs.append((song, score, explanation))

    # Sort songs by score in descending order
    scored_songs.sort(key=lambda x: x[1], reverse=True)

    return scored_songs[:k]