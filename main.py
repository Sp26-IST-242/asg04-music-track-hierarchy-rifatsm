"""
Driver script demonstrating the complete Music Track hierarchy.

Run:
    python main.py

Expected output
---------------
Before sorting:
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False

After sorting:
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
"""

from artist import Artist
from album import Album
from song import Song
from podcast import Podcast
from playlist import Playlist


def main() -> None:
    # ------------------------------------------------------------------
    # 1. Create Artist objects
    # ------------------------------------------------------------------
    kendrick = Artist("Kendrick Lamar", "Hip-Hop")
    alanis   = Artist("Alanis Morissette", "Alternative")
    rogan    = Artist("Joe Rogan", "Comedy")
    koenig   = Artist("Sarah Koenig", "Journalism")

    # ------------------------------------------------------------------
    # 2. Create Album objects
    #    list(range(start, stop)) builds [start, start+1, ..., stop-1]
    # ------------------------------------------------------------------
    damn_album   = Album("DAMN.",                        True,  list(range(2017, 2019)))
    jlp_album    = Album("Jagged Little Pill",           False, list(range(1995, 1997)))
    jre_album    = Album("The Joe Rogan Experience",     True,  list(range(2009, 2011)))
    serial_album = Album("Serial",                       False, list(range(2014, 2016)))

    # ------------------------------------------------------------------
    # 3. Create MusicTrack objects (Song and Podcast)
    #    Note: Podcast.is_explicit defaults to False — no need to pass it
    #    for serial_ep.
    # ------------------------------------------------------------------
    humble         = Song(kendrick, damn_album,   220)          # 03:40
    you_oughta_know= Song(alanis,   jlp_album,    245)          # 04:05
    jre_ep         = Podcast(rogan,  jre_album,   9000,
                             is_explicit=True)                  # 02:30:00
    serial_ep      = Podcast(koenig, serial_album, 5400)        # 01:30:00, not explicit

    # ------------------------------------------------------------------
    # 4. Build the playlist and add tracks in insertion order
    # ------------------------------------------------------------------
    p = Playlist()
    p.add_track(humble)
    p.add_track(you_oughta_know)
    p.add_track(jre_ep)
    p.add_track(serial_ep)

    # ------------------------------------------------------------------
    # 5. Print before sorting
    # ------------------------------------------------------------------
    print("Before sorting:")
    print(p)
    print()   # blank line for readability

    # ------------------------------------------------------------------
    # 6. Sort by release year (ascending) and print again
    # ------------------------------------------------------------------
    p.sort_by_release_year()

    print("After sorting:")
    print(p)


if __name__ == "__main__":
    main()

