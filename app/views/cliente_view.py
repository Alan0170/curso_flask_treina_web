class Cliente:
    def __init__(self, app):
        @app.route("/ola")
        def ola():
            return "Olá mundo em Flask!"

