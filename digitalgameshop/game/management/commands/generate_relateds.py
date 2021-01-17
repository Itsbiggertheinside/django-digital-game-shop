from django.core.management import BaseCommand
from game.models.game_dependencies import Genre, Language, Platform

class Command(BaseCommand):

    def dependencyInjection(self, model, list):
        for item in list:
            model.objects.create(name=item)

    def handle(self, *args, **options):
        
        genres = ['Aksiyon', 'Macera', 'Dövüş', 'Simülasyon', 'Platform', 'Korku', 'Yarış', 
            'Rol Yapma', 'Spor', 'Strateji', 'Hayatta Kalma']

        languages = ['İngilizce', 'Türkçe', 'Almanca', 'Japonca']

        platform = ['PC', 'Playstation', 'XBox', 'Mobil']


        self.dependencyInjection(Genre, genres)
        self.dependencyInjection(Language, languages)
        self.dependencyInjection(Platform, genres)


    