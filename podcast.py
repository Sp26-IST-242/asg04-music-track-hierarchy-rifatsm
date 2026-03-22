"""
Concrete subclass of MusicTrack representing a podcast episode.

Podcast differs from Song in two ways:
  1. It has one extra field: is_explicit (bool), defaulting to False.
     The default value replaces Java-style constructor overloading — one
     __init__ handles both the explicit and non-explicit cases.
  2. play_time_formatted() returns 'HH:MM:SS' instead of 'MM:SS', because
     podcast episodes are typically longer than an hour.
"""

from music_track import MusicTrack
from artist import Artist
from album import Album


class Podcast(MusicTrack):
    """
    A podcast episode.

    Extends MusicTrack with:
        is_explicit : bool — whether the episode contains explicit content
                             (default False)
    """

    def __init__(
        self,
        artist: Artist,
        album: Album,
        duration_seconds: float,
        is_explicit: bool = False,   # default parameter replaces overloading
    ) -> None:
        """
        Parameters
        ----------
        artist           : Artist — the podcast creator / host
        album            : Album  — the podcast series
        duration_seconds : float  — episode length in seconds
        is_explicit      : bool   — True if the episode has explicit content
                                    (default: False)
        """
        # Pass the three common fields up to MusicTrack.__init__
        super().__init__(artist, album, duration_seconds)
        # Store the Podcast-specific field
        self._is_explicit = is_explicit

    # ------------------------------------------------------------------
    # Property for the Podcast-specific field
    # ------------------------------------------------------------------

    @property
    def is_explicit(self) -> bool:
        """Return True if the episode contains explicit content."""
        return self._is_explicit

    # ------------------------------------------------------------------
    # Concrete implementation of the abstract method
    # ------------------------------------------------------------------

    def play_time_formatted(self) -> str:
        """
        Return the duration as 'HH:MM:SS' (all parts zero-padded).

        Examples
        --------
        9000 seconds → '02:30:00'
        5400 seconds → '01:30:00'
        3661 seconds → '01:01:01'
        """
        total_seconds = int(self._duration_seconds)
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    # ------------------------------------------------------------------
    # String representation
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        Return '(<artist>) <album>, duration: <HH:MM:SS> is explicit: <bool>'.

        Example:
            (Joe Rogan, Comedy) The Joe Rogan Experience active = True,
             debut year: 2009, duration: 02:30:00 is explicit: True
        """
        return (
            f"({self._artist}) {self._album},"
            f" duration: {self.play_time_formatted()}"
            f" is explicit: {self._is_explicit}"
        )
