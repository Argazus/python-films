import file_manager
import unittest


class FileManagerTest(unittest.TestCase):
    """FileManagerTest: Test case sur le parcours du fichier JSON."""

    def setUp(self):
        """Initialisation des tests."""
        self.file = 'film.JSON'

    def test_total_number(self):
        """Ouvre le fichier JSON, et compte le nombre d'éléments présents dans la structure."""
        # TODO : Count the number of records available in the JSON file
        count = file_manager.count(self.file)
        self.assertEqual(count, 16, "Invalid count of records in file.JSON")

    def test_films_written_by(self):
        """Ouvre le fichier JSON, et cherche les enregistrements écrits par Vince Gilligan"""
        self.skipTest(
            "Skipping test, uncomment this line when previous step is commited")

        films = file_manager.written_by(self.file, "Vince Gilligan")
        self.assertEqual(len(films), 1, "Invalid number of records")
        self.assertEqual(films[0]['Writer'],
                         "Vince Gilligan", "Invalid record")

    def test_longest_title(self):
        """Ouvre le fichier JSON, et cherche le film avec le nom le plus long"""
        self.skipTest(
            "Skipping test, uncomment this line when previous step is commited")
        record = file_manager.longest_title(self.file)
        print(record['Title'])

        self.assertEqual(
            record['Title'], "Rogue One: A Star Wars Story", "Incorrect record returned")

    def test_best_rating(self):
        """Ouvre le fichier JSON, et cherche l'enregistrement avec le meilleur imdbRating """
        self.skipTest(
            "Skipping test, uncomment this line when previous step is commited")
        record = file_manager.best_rating(self.file)
        self.assertEqual(record['Title'], "Game of Thrones",
                         "There seems to be something even better")

    def test_latest_film(self):
        """Ouvre le fichier JSON, et cherche l'enregistrement avec le Year le plus récent, retourne le nom du film concerné """
        self.skipTest(
            "Skipping test, uncomment this line when previous step is commited")
        film_name = file_manager.latest_film(self.file)
        self.assertEqual(film_name, "Assassin's Creed",
                         "Invalid count of records in file.JSON")

    def test_films_per_genre(self):
        """Ouvre le fichier JSON, et cherche les enregistrements ayant le genre Fantasy"""
        self.skipTest(
            "Skipping test, uncomment this line when previous step is commited")
        films = file_manager.find_per_genre(self.file, "Fantasy")
        self.assertEqual(len(films), 5, "Invalid number of records")

    def test_bonus_release_after_Nov_2015(self):
        """Ouvre le fichier JSON, et compte le nombre d'éléments ayant une release date >= Nov 2015 """
        self.skipTest(
            "Skipping test, uncomment this line when previous step is commited")
        records = file_manager.released_after(self.file, "01/11/2015")
        self.assertEqual(
            len(records), 4, "Invalid count of records in file.JSON")
