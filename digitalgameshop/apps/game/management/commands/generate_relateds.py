from django.core.management import BaseCommand
from game.models.game_dependencies import Genre, Language, Platform

class Command(BaseCommand):

    def injection(self, model, list):
        for item in list:
            model.objects.create(name=item)

    def itemRemover(self, model):
        model.objects.all().delete()

    def handle(self, *args, **options):
        
        genres = ['Aksiyon', 'Macera', 'Dövüş', 'Simülasyon', 'Platform', 'Korku', 'Yarış', 
            'Rol Yapma', 'Spor', 'Strateji', 'Hayatta Kalma']

        languages = ['İngilizce', 'Türkçe', 'Almanca', 'Japonca']

        platform = ['PC', 'Playstation', 'XBox', 'Mobil']


        # delete data
        self.itemRemover(Genre)
        self.itemRemover(Language)
        self.itemRemover(Platform)

        # refill data
        self.injection(Genre, genres)
        self.injection(Language, languages)
        self.injection(Platform, platform)


    