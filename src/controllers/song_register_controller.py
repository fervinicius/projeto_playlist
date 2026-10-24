class SongRegisterController:

    def insert(self, new_song_informations: dict) -> dict:
        # Single Responsibility Principle
        try:
            self.__verify_songs_info(new_song_informations)
            self.__verify_if_song_already_registered(new_song_informations)
            self.__insert_song(new_song_informations)
            return self.__format_song(new_song_informations)
        except Exception as exception:
            return self.__format_error_response(exception)

    def __verify_songs_info(self, new_song_informations: dict) -> None:

        if len(new_song_informations["title"]) > 100:
            raise Exception("Título da música com mais de 100 caracteres")

        year = int(new_song_informations["year"])
        if year > 2026:
            raise Exception("Ano de música inválido!")        
    
    def __verify_if_song_already_registered(self, new_song_informations: dict) -> None:
        # Interaction with Models
        pass

    def __insert_song(self, new_song_informations: dict) -> None:
        # Interaction with Models
        pass

    def __format_song(self, new_song_informations: dict) -> dict:
        return {
            "success": True,
            "count": 1,
            "attributes": {
                "title": new_song_informations["title"]
            }
        }

    def __format_error_response(self, erro: Exception) -> dict:
        return {
            "success": False,
            "error": str(erro)
        }   