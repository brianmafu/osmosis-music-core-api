from django.db import models

LANGUAGE_CHOICES = (
    ("English", "English"),
    ("Nepali", "Nepali"),
    ("Hindi", "Hindi"),
    ("Dzongkha", "Dzongkha")
)

GENRE_CHOICES = (
    ("Unknown", "Unknown"),
    ("Movie", "Movie"),
    ("Pop", "Pop"),
    ("Rock", "Rock"),
    ("Alternative/Indie", "Alternative/Indie"),
    ("Remix", "Remix"),
    ("Instrumental", "Instrumental"),
    ("Folk", "Folk"),
    ("Electronic", "Electronic")
)


class Playlist(models.Model):
    name = models.CharField(max_length=1000)
    cover_art = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    title = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000, blank=True)
    name = models.CharField(max_length=1000, blank=True)
    profileImageURL = models.CharField(max_length=2000, blank=True)
    thumbnailProfileImageURL = models.CharField(max_length=2000, blank=True)
    about = models.CharField(max_length=3000)
    stars = models.IntegerField(default=0)
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    title = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, blank=True, on_delete=models.PROTECT)
    thumbnail = models.CharField(max_length=10000)
    stars = models.IntegerField(default=0)
    genre = models.CharField(max_length=50,
                             choices=GENRE_CHOICES,
                             default=GENRE_CHOICES[0][0])
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])
    duration = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, blank=True, on_delete=models.PROTECT)
    fileName = models.CharField(max_length=1000)
    stars = models.IntegerField(default=0)
    imageURL = models.CharField(max_length=10000)
    thumbnailImageURL = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)
    genre = models.CharField(max_length=50,
                             choices=GENRE_CHOICES,
                             default=GENRE_CHOICES[0][0])
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])

    album = models.ForeignKey(Album, blank=True, on_delete=models.PROTECT)
    duration = models.CharField(max_length=10000)
    durationInSeconds = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title




class Video(models.Model):
    title = models.CharField(max_length=1000)
    lyrics = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, blank=True, on_delete=models.PROTECT)
    url = models.CharField(max_length=1000)
    genre = models.CharField(max_length=50,
                             choices=GENRE_CHOICES,
                             default=GENRE_CHOICES[0][0])
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.title


