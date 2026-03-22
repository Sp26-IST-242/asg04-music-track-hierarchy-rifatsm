"""
Concrete subclass of MusicTrack representing a standard music track.

Song adds no new fields beyond what MusicTrack already stores.  Its only
responsibility is to:
  1. Call super().__init__() to let MusicTrack do the storage work.
  2. Implement play_time_formatted() in MM:SS format.
  3. Override __str__ for a human-readable representation.
"""

from music_track import MusicTrack
from artist import Artist
from album import Album


class Song(MusicTrack):
    """
    A standard music song.

    Inherits artist, album, duration_seconds, release_year, and
    total_play_time() from MusicTrack.
    """

    def __init__(
        self, artist: Artist, album: Album, duration_seconds: float
    ) -> None:
        """
        Parameters
        ----------
        artist           : Artist — the performing artist
        album            : Album  — the album this song belongs to
        duration_seconds : float  — song length in seconds
        """
        # Delegate all field storage to the parent constructor.
        # Song has no extra fields to store.
        super().__init__(artist, album, duration_seconds)

    # ------------------------------------------------------------------
    # Concrete implementation of the abstract method
    # ------------------------------------------------------------------

    def play_time_formatted(self) -> str:
        """
        Return the duration as 'MM:SS' (both parts zero-padded).

        Examples
        --------
        220 seconds → '03:40'
        65  seconds → '01:05'
        """
        total_seconds = int(self._duration_seconds)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    # ------------------------------------------------------------------
    # String representation
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        Return '(<artist>) <album>, duration: <MM:SS>'.

        Example:
            (Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017,
            duration: 03:40

        Note: str(self._artist) calls Artist.__str__, and str(self._album)
        calls Album.__str__ — each object knows how to represent itself.
        """
        return (
            f"({self._artist}) {self._album},"
            f" duration: {self.play_time_formatted()}"
        )
