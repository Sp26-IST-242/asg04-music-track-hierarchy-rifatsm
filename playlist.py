"""
A collection class that holds MusicTrack objects (Songs and Podcasts).

Design notes:
  • _tracks is kept private (single underscore) and exposed as a *copy*
    through the `tracks` property to protect encapsulation.
  • clear_playlist() uses list.clear() rather than rebinding to None or a new
    list, so the internal object reference stays valid.
  • sort_by_release_year() delegates to list.sort(), which in turn calls
    MusicTrack.__lt__ — the comparison logic defined in Part 3 pays off here.
  • __str__ uses a generator expression with str.join() for a concise
    multi-line string without building an intermediate list manually.
"""

from music_track import MusicTrack


class Playlist:
    """
    An ordered collection of MusicTrack objects.

    Methods
    -------
    add_track(track)        — append a track to the playlist
    clear_playlist()        — remove all tracks (list stays non-None)
    sort_by_release_year()  — sort tracks in place by debut year
    tracks                  — property returning a copy of the internal list
    __str__                 — one track per line
    """

    def __init__(self) -> None:
        """Create an empty playlist."""
        # Type hint documents intent; Python does not enforce it at runtime.
        self._tracks: list[MusicTrack] = []

    # ------------------------------------------------------------------
    # Property — read-only access to a defensive copy
    # ------------------------------------------------------------------

    @property
    def tracks(self) -> list[MusicTrack]:
        """
        Return a copy of the internal track list.

        Callers may mutate the returned list freely without affecting the
        Playlist's internal state.
        """
        return list(self._tracks)

    # ------------------------------------------------------------------
    # Mutating methods
    # ------------------------------------------------------------------

    def add_track(self, track: MusicTrack) -> None:
        """
        Append *track* to the end of the playlist.

        Parameters
        ----------
        track : MusicTrack — any Song or Podcast instance
        """
        self._tracks.append(track)

    def clear_playlist(self) -> None:
        """
        Remove all tracks from the playlist.

        Uses list.clear() deliberately — assigning None or a new list would
        break subsequent add_track() calls if any code held a reference to
        the original list.
        """
        self._tracks.clear()

    def sort_by_release_year(self) -> None:
        """
        Sort the playlist in place from earliest to most recent release year.

        list.sort() calls MusicTrack.__lt__ for comparisons, which was
        implemented in Part 3 to compare by release_year.
        """
        self._tracks.sort()

    # ------------------------------------------------------------------
    # String representation
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """Return all tracks joined by newlines, one track per line."""
        return "\n".join(str(track) for track in self._tracks)
