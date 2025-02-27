import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores_descending = scores["score"].sort_values(ascending = False)
    rank = []
    r = 0
    prev = float("inf")
    for sc in scores_descending:
        if prev==sc:
            rank.append(r)
        else:
            r += 1
            rank.append(r)
            prev = sc
    return pd.DataFrame({
        "score":scores_descending,
        "rank":rank
    })

