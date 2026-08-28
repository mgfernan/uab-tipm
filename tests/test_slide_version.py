from scripts.compute_slide_version import compute_version_from_messages, is_release_version


def test_release_version_counts_breaking_and_feat_fix_categories() -> None:
    messages = [
        "feat: add new section",
        "fix: repair typo",
        "docs: update notes",
        "feat!: redesign page",
        "refactor: simplify flow",
    ]

    assert compute_version_from_messages(messages) == "1.2.1-r2"
    assert is_release_version(messages) is True


def test_non_release_commits_keep_rn_without_tagging() -> None:
    messages = [
        "docs: update notes",
        "chore: tidy up formatting",
    ]

    assert compute_version_from_messages(messages) == "0.0.0-r2"
    assert is_release_version(messages) is False
