"""
Represents a musical artist or podcast creator.

This is the simplest class in the hierarchy — no dependencies, no validation.
It introduces two core Python OOP conventions:
  1. The single leading-underscore (_name) signals a non-public attribute.
  2. @property exposes a clean public getter without allowing direct mutation.
"""


class Artist:
    """
    Stores the name and genre of a musical artist or podcast creator.

    Attributes
    ----------
    _name  : str  — the artist / show name
    _genre : str  — the primary genre (e.g. "Hip-Hop", "Journalism")
    """

    def __init__(self, name: str, genre: str) -> None:
        """
        Parameters
        ----------
        name  : str — artist name
        genre : str — primary genre
        """
        self._name = name
        self._genre = genre

    # ------------------------------------------------------------------
    # Properties — read-only getters following the _underscore convention
    # ------------------------------------------------------------------

    @property
    def name(self) -> str:
        """Return the artist's name."""
        return self._name

    @property
    def genre(self) -> str:
        """Return the artist's primary genre."""
        return self._genre

    # ------------------------------------------------------------------
    # String representation
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """Return '<name>, <genre>' — e.g. 'Kendrick Lamar, Hip-Hop'."""
        return f"{self._name}, {self._genre}"
