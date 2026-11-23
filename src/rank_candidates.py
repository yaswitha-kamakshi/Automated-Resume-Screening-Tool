def rank_candidates(candidates):

    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: candidate["match_percentage"],
        reverse=True
    )

    return ranked_candidates