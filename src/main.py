"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
def print_recommendations(profile_name: str, recommendations: list) -> None:
    print(f"\n{'='*20} {profile_name} {'='*20}")
    for song, score, explanation in recommendations:
        print(f"🎵 {song['title']:<30} | Score: {score:.2f}")
        print(f"   Why: {explanation}")
        print("-" * 50)

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Profile for "intense rock"
    intense_rock_profile = {
        "favorite_genre": "rock", 
        "favorite_mood": "intense", 
        "target_energy": 0.9,
        "likes_acoustic": False
    }

    # Profile for "chill lofi"
    chill_lofi_profile = {
        "favorite_genre": "lofi", 
        "favorite_mood": "chill", 
        "target_energy": 0.4,
        "likes_acoustic": True
    }

    # Profile for "upbeat pop"
    upbeat_pop_profile = {
        "favorite_genre": "pop",
        "favorite_mood": "upbeat",
        "target_energy": 0.7,
        "likes_acoustic": False
    }

    # ADVERSARIAL PROFILE: Conflicting Preferences
    adversarial_profile = {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.9, # High energy but sad mood
        "likes_acoustic": False
    }

    # EDGE CASE PROFILE: Niche Preferences
    edge_case_profile = {
        "favorite_genre": "classical", # Potentially no classical songs in the dataset
        "favorite_mood": "contemplative",
        "target_energy": 0.2,
        "likes_acoustic": True
    }


    print("--- Intense Rock Recommendations ---")
    rock_recommendations = recommend_songs(intense_rock_profile, songs, k=3)
    for rec in rock_recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

    print("\n--- Chill Lofi Recommendations ---")
    lofi_recommendations = recommend_songs(chill_lofi_profile, songs, k=3)
    for rec in lofi_recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

    print("\n--- Upbeat Pop Recommendations ---")
    pop_recommendations = recommend_songs(upbeat_pop_profile, songs, k=3)
    for rec in pop_recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

    print("\n--- Adversarial Profile Recommendations ---")
    adversarial_recommendations = recommend_songs(adversarial_profile, songs, k=3)
    for rec in adversarial_recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

    print("\n--- Edge Case Profile Recommendations ---")
    edge_case_recommendations = recommend_songs(edge_case_profile, songs, k=3)
    for rec in edge_case_recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
