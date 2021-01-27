from django.core.management import BaseCommand
from store.submodels import Genre, Language, Platform

class Command(BaseCommand):

    def injection(self, model, list):
        model.objects.all().delete()
        for item in list:
            model.objects.create(name=item)

    def handle(self, *args, **options):
        
        genres = ['Aksiyon', 'Macera', 'Dövüş', 'Simülasyon', 'Platform', 'Korku', 'Yarış', 
            'Rol Yapma', 'Spor', 'Strateji', 'Hayatta Kalma']

        languages = ['İngilizce', 'Türkçe', 'Almanca', 'Japonca']

        platform = ['PC', 'Playstation', 'XBox', 'Mobil']

        # refill data
        self.injection(Genre, genres)
        self.injection(Language, languages)
        self.injection(Platform, platform)