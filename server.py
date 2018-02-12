from app.app import create_app
import os 

if __name__ == "__main__":
	DEFAULT_PORT = 8000
	PORT = int(os.environ.get("PORT", DEFAULT_PORT))
	env = os.environ.get("ENVIRONMENT", "DEV")
	app = create_app()
	print("Environment: " + env)
	app.run(host="0.0.0.0", port=PORT)
