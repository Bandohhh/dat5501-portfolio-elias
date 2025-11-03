# us_election/src/plot_bar_by_state.py
# Reads a semicolon-delimited US primary results CSV and plots a BLUE bar chart
# of a chosen candidate's vote fraction by state (within their party).

from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = Path("us_election/data/US-2016-primary.csv")  # adjust if needed
SAVE_PATH = Path("us_election/output/bar_chart.png")

def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)
    # IMPORTANT: semicolon-delimited
    df = pd.read_csv(path, sep=";")
    # normalise column names to lowercase
    df.columns = [c.strip().lower() for c in df.columns]
    required = {"state", "party", "candidate", "votes"}
    if not required.issubset(df.columns):
        raise ValueError(f"CSV must include columns {sorted(required)}; found {df.columns.tolist()}")
    # tidy types
    df["state"] = df["state"].astype(str).str.strip()
    df["party"] = df["party"].astype(str).str.strip()
    df["candidate"] = df["candidate"].astype(str).str.strip()
    df["votes"] = pd.to_numeric(df["votes"], errors="coerce")
    df = df.dropna(subset=["votes"])
    return df

def compute_state_fractions(df: pd.DataFrame, candidate_name: str) -> pd.DataFrame:
    # locate candidate rows (case-insensitive)
    cand_mask = df["candidate"].str.lower() == candidate_name.lower()
    cand_rows = df[cand_mask]
    if cand_rows.empty:
        examples = sorted(df["candidate"].unique().tolist())
        raise ValueError(
            f"No rows for candidate '{candidate_name}'. "
            f"Try one of: {examples[:20]}{' ...' if len(examples)>20 else ''}"
        )
    # infer candidate's party from the data
    cand_party = cand_rows["party"].mode().iloc[0]
    # denominator: total party votes per state
    denom = (df[df["party"] == cand_party]
             .groupby("state", as_index=False)["votes"].sum()
             .rename(columns={"votes": "total_party_votes"}))
    # numerator: candidate votes per state
    num = (cand_rows
           .groupby("state", as_index=False)["votes"].sum()
           .rename(columns={"votes": "candidate_votes"}))
    merged = num.merge(denom, on="state", how="left")
    merged["fraction"] = (merged["candidate_votes"] / merged["total_party_votes"]).clip(0, 1)
    merged["party"] = cand_party
    return merged.sort_values("fraction", ascending=False).reset_index(drop=True)

def plot_blue_bar(frac_df: pd.DataFrame, candidate_name: str, save_path: Path | None = None):
    states = frac_df["state"].tolist()
    fractions = frac_df["fraction"].tolist()
    party = frac_df["party"].iloc[0] if not frac_df.empty else "Primary"

    plt.figure(figsize=(12, 6))
    plt.bar(states, fractions, color="blue", edgecolor="black")
    plt.title(f"Vote fraction by state – {candidate_name} ({party} primary)")
    plt.ylabel("Vote fraction (0–1)")
    plt.xticks(rotation=60, ha="right")
    plt.ylim(0, 1)
    plt.tight_layout()
    if save_path:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight")
        print(f"Saved chart to: {save_path}")
    plt.show()

def main():
    df = load_data(DATA_PATH)
    candidate = input("Enter candidate name (e.g., Donald Trump, Hillary Clinton, Bernie Sanders): ").strip()
    frac = compute_state_fractions(df, candidate)
    print(frac[["state", "fraction"]])
    plot_blue_bar(frac, candidate, SAVE_PATH)

if __name__ == "__main__":
    main()
