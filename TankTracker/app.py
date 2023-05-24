from controllers.app_controller import prepare_app

if __name__ == "__main__":
    app = prepare_app()
    app.run("127.0.0.1", port=8000, debug=True)