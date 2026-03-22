"""
Abstract base class for all music tracks (Songs and Podcasts).

Design decisions explained:
  • ABC makes it impossible to instantiate MusicTrack directly — you can only
    create concrete subclasses that implement every @abstractmethod.
  • Common fields (artist, album, duration_seconds) live here so that Song and
    Podcast do not each need to repeat them.
  • release_year is a *derived* property delegating to Album.debut_year; the
    year is not stored a second time.
  • play_time_formatted() is abstract because Song and Podcast format time
    differently (MM:SS vs HH:MM:SS).
  • total_play_time() is concrete because the calculation is identical for all
    track types: duration × number of plays.
  • @functools.total_ordering generates <=, >, >= automatically from __eq__ and
    __lt__, giving us full comparison support with minimal code.
  • __hash__ is defined to stay consistent with __eq__ (Python sets __hash__ to
    None when you define __eq__, making objects unhashable unless you fix it).
"""

from abc import ABC, abstractmethod
from functools import total_ordering

from artist import Artist
from album import Album


@total_ordering
class MusicTrack(ABC):
    """
    Abstract representation of any playable music track.

    Subclasses MUST implement:
        play_time_formatted(self) -> str
    """

    def __init__(
        self, artist: Artist, album: Album, duration_seconds: float
    ) -> None:
        """
        Parameters
        ----------
        artist           : Artist — who created this track
        album            : Album  — the album or series it belongs to
        duration_seconds : float  — length of the track in seconds
        """
        self._artist = artist
        self._album = album
        self._duration_seconds = duration_seconds

    # ------------------------------------------------------------------
    # Properties — common to ALL subclasses
    # ------------------------------------------------------------------

    @property
    def artist(self) -> Artist:
        """Return the Artist associated with this track."""
        return self._artist

    @property
    def album(self) -> Album:
        """Return the Album this track belongs to."""
        return self._album

    @property
    def duration_seconds(self) -> float:
        """Return the raw duration of this track in seconds."""
        return self._duration_seconds

    @property
    def release_year(self) -> int:
        """
        Return the debut year derived from the Album.

        This is computed, not stored, so it always reflects the Album's data.
        """
        return self._album.debut_year

    # ------------------------------------------------------------------
    # Abstract method — subclasses MUST provide their own implementation
    # ------------------------------------------------------------------

    @abstractmethod
    def play_time_formatted(self) -> str:
        """
        Return a human-readable duration string.

        Song    → "MM:SS"    (e.g. "03:40")
        Podcast → "HH:MM:SS" (e.g. "02:30:00")
        """
        ...

    # ------------------------------------------------------------------
    # Concrete method — shared logic; subclasses inherit it for free
    # ------------------------------------------------------------------

    def total_play_time(self, num_plays: int) -> float:
        """
        Return total play time in seconds if this track is played *num_plays*
        times in a row.

        Parameters
        ----------
        num_plays : int — how many times to play the track

        Returns
        -------
        float — total seconds
        """
        return self._duration_seconds * num_plays

    # ------------------------------------------------------------------
    # Comparison methods — enable sorted() and list.sort()
    # ------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Two tracks are equal when they share the same release year."""
        if not isinstance(other, MusicTrack):
            return NotImplemented
        return self.release_year == other.release_year

    def __lt__(self, other: object) -> bool:
        """A track is 'less than' another when its release year is earlier."""
        if not isinstance(other, MusicTrack):
            return NotImplemented
        return self.release_year < other.release_year

    def __hash__(self) -> int:
        """
        Must be defined whenever __eq__ is overridden.

        Python sets __hash__ = None by default when you define __eq__,
        which would make MusicTrack objects unhashable (cannot be put in a
        set or used as a dict key).  We hash by release year to stay
        consistent with our equality definition.
        """
        return hash(self.release_year)
