import pandas as pd
import matplotlib.pyplot as plt
from fuzzywuzzy import process  # For fuzzy name matching [web:4]


DATA_PATH = "week_5/us_election/US-2016-primary.csv"
DELIMITER = ";"  # CSV uses semicolon as separator for columns


def load_election_data(path: str, delimiter: str = ";") -> pd.DataFrame:
    """
    Load the election data CSV and clean data.

    - Reads the CSV file with the given delimiter.
    - Fills missing values with 0 to avoid errors when summing.
    """
    df = pd.read_csv(path, delimiter=delimiter)  # [web:18]
    df.fillna(0, inplace=True)
    return df


def ask_candidate_name(candidates) -> str:
    """
    Interactively ask the user for a candidate name.

    Uses fuzzy match to suggest the closest known candidate name.
    - Exact match (score 100): accepts the typed name.
    - High match (score >= 80) then it will suggest the closest name and asks for confirmation.
    - Otherwise it will asks again.

    Returns:
        The confirmed candidate name.
    """
    while True:
        user_input = input("Please enter the candidate's name (e.g. John Kasich): ")

        # process.extractOne returns (best_match, score) for the given list of choices [web:1][web:5]
        matched_candidate, score = process.extractOne(user_input, candidates)

        if score == 100:
            # Exact match: use what the user typed
            print(f"Exact match found for '{user_input}'.")
            return user_input

        if score >= 80:
            # High confidence suggestion
            print(f"Did you mean: '{matched_candidate}'? (match score: {score})")
            confirm = input("Type 'y' to confirm, or any other key to try again: ")
            if confirm.lower() == "y":
                return matched_candidate
            # Otherwise loop again

        else:
            # Low score: ask again
            print("Candidate not found with enough confidence. Please try again.")


def compute_candidate_stats(election_df: pd.DataFrame, candidate: str) -> dict:
    
    #outputs  core statistics for a given candidate.

  
    # Filter rows for this candidate
    candidate_df = election_df[election_df["candidate"] == candidate]

    # Total votes for the candidate (all states)
    total_candidate_votes = candidate_df["votes"].sum()

    # Total votes in each state
    state_total_votes = election_df.groupby("state")["votes"].sum()  

    # Candidate's total votes in each state
    state_candidate_votes = candidate_df.groupby("state")["votes"].sum()

    # Avoid division by zero by replacing 0 totals with NaN
    safe_state_totals = state_total_votes.replace(0, pd.NA)

    # Fraction of votes in each state that went to the candidate
    state_fraction_of_state = state_candidate_votes / safe_state_totals

    # Fraction of candidate's total votes that came from each state
    # (sum should be 1, ignore all missing values)
    state_fraction_of_candidate = state_candidate_votes / total_candidate_votes

    return {
        "candidate_df": candidate_df,
        "total_candidate_votes": total_candidate_votes,
        "state_total_votes": state_total_votes,
        "state_candidate_votes": state_candidate_votes,
        "state_fraction_of_state": state_fraction_of_state,
        "state_fraction_of_candidate": state_fraction_of_candidate,
    }


def plot_state_fraction_of_state(state_fraction_of_state: pd.Series, candidate: str) -> None:
    """
    Plot a bar chart showing, for each state, what fraction of that state's votes
    went to the chosen candidate.
    """
    state_fractions_sorted = state_fraction_of_state.sort_values(ascending=False)
    ax = state_fractions_sorted.plot(
        kind="bar",
        title=f"Fraction of state votes for {candidate}",
        edgecolor="black",
        color="skyblue",  # Slight customisation for clarity
    )
    ax.set_xlabel("State")
    ax.set_ylabel("Fraction of State Votes")
    plt.grid(True, axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_state_fraction_of_candidate(state_fraction_of_candidate: pd.Series, candidate: str) -> None:
    """
    Plot a bar chart showing, for each state, what fraction of the candidate's
    total votes came from that state.
    """
    candidate_fractions_sorted = state_fraction_of_candidate.sort_values(ascending=False)
    ax = candidate_fractions_sorted.plot(
        kind="bar",
        title=f"Fraction of {candidate} votes by state",
        edgecolor="black",
        color="orange",
    )
    ax.set_xlabel("State")
    ax.set_ylabel("Fraction of Candidate's Total Votes")
    plt.grid(True, axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def print_text_summary(candidate: str, stats: dict) -> None:
    """
    Print a short text summary of the candidate's performance.
     The code shows 

    - Total votes for the candidate.
    - State with the highest fraction of state votes for this candidate.
    - State that contributed the largest share of the candidate's total votes.
    """
    total_votes = stats["total_candidate_votes"]

    # Drop missing values so idxmax works safely
    frac_state = stats["state_fraction_of_state"].dropna()
    frac_candidate = stats["state_fraction_of_candidate"].dropna()

    top_state_by_share = frac_state.idxmax() if not frac_state.empty else "N/A"
    top_state_share_value = frac_state.max() if not frac_state.empty else 0

    top_state_by_origin = frac_candidate.idxmax() if not frac_candidate.empty else "N/A"
    top_state_origin_value = frac_candidate.max() if not frac_candidate.empty else 0

    print("\n=== Candidate summary ===")
    print(f"Candidate: {candidate}")
    print(f"Total votes (all states): {int(total_votes)}")
    print(
        f"Highest in-state support: {top_state_by_share} "
        f"with about {top_state_share_value:.2%} of that state's votes."
    )
    print(
        f"Largest source of votes: {top_state_by_origin} "
        f"with about {top_state_origin_value:.2%} of the candidate's total votes."
    )


def main() -> None: #1. Load data. Ask the user to choose a candidate (with fuzzy matching). Compute statistics. Show a text summary. Plot two bar charts.

    # Step 1: Load and prepare data
    election_data_df = load_election_data(DATA_PATH, DELIMITER)

    # Step 2: Ask for a candidate name
    candidates = election_data_df["candidate"].unique()
    candidate = ask_candidate_name(candidates)

    # Step 3: Compute statistics for this candidate
    stats = compute_candidate_stats(election_data_df, candidate)

    # Step 4: Print a small text summary
    print_text_summary(candidate, stats)

    # Step 5: Plot charts
    plot_state_fraction_of_state(stats["state_fraction_of_state"], candidate)
    plot_state_fraction_of_candidate(stats["state_fraction_of_candidate"], candidate)


if __name__ == "__main__":
    main()
