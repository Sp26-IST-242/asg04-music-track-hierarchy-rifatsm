"""
Represents a music album or podcast series, including the years it was active.

Key concepts demonstrated here:
  • Input validation in __init__ (fail-fast with a clear ValueError).
  • Defensive copy on both input and output so external code cannot corrupt
    the internal years list.
  • A *derived* property (debut_year) that computes its value from stored data
    rather than keeping a second field in sync.
"""


class Album:
    """
    Stores metadata about an album or podcast series.

    Attributes
    ----------
    _title  : str        — album / show title
    _active : bool       — True if still releasing new content
    _years  : list[int]  — calendar years content was released (non-empty)
    """

    def __init__(self, title: str, active: bool, years: list[int]) -> None:
        """
        Parameters
        ----------
        title  : str       — album / show title
        active : bool      — whether still active
        years  : list[int] — non-empty list of release years

        Raises
        ------
        ValueError
            If *years* is empty, because debut_year would fail later
            with a confusing IndexError.  Fail early with a clear message.
        """
        if not years:
            # Fail immediately rather than letting an IndexError surface later
            raise ValueError(
                f"Album '{title}': the years list must contain at least one year."
            )

        self._title = title
        self._active = active
        # Defensive copy — mutations to the caller's list won't affect us
        self._years: list[int] = list(years)

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def title(self) -> str:
        """Return the album / show title."""
        return self._title

    @property
    def active(self) -> bool:
        """Return True if the album / show is still active."""
        return self._active

    @property
    def years(self) -> list[int]:
        """
        Return a *copy* of the internal years list.

        Returning a copy prevents external code from modifying the list
        without going through a controlled method.
        """
        return list(self._years)

    @property
    def debut_year(self) -> int:
        """
        Return the first year in the years list.

        This is a *derived* property — it does not have its own stored field.
        There is no risk of it drifting out of sync with _years.
        """
        return self._years[0]

    # ------------------------------------------------------------------
    # String representation
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        Return '<title> active = <active>,  debut year: <debut_year>'.

        Example: 'DAMN. active = True,  debut year: 2017'
        """
        return (
            f"{self._title} active = {self._active},"
            f"  debut year: {self._years[0]}"
        )
